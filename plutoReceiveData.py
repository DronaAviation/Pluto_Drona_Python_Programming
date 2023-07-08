import socket
import threading 
import struct

TRIM_MAX = 1000
TRIM_MIN = -1000

isAutoPilotOn = 0
    
MSP_HEADER_IN = "244d3c"# "$M<" "MSP packet header"

TCP_IP = '192.168.4.1' #Ip Addr
TCP_PORT = 23 #Port

#MSP(MultiWii Serial Protocols)
MSP_FC_VERSION = 3
MSP_RAW_IMU = 102
MSP_RC = 105
MSP_ATTITUDE = 108
MSP_ALTITUDE = 109
MSP_ANALOG = 110
MSP_SET_RAW_RC = 200
MSP_ACC_CALIBRATION = 205
MSP_MAG_CALIBRATION = 206
MSP_SET_MOTOR = 214
MSP_SET_ACC_TRIM = 239
MSP_ACC_TRIM = 240
MSP_EEPROM_WRITE = 250
MSP_SET_POS = 216
MSP_SET_COMMAND = 217
MSP_STATUS = 101		
MSP_BOXNAMES = 116
MSP_BOX = 113

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) # Creates a TCP connection

client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 9)
client.connect((TCP_IP, TCP_PORT))

print("Connected")
# Now you can use the 'client' socket for sending/receiving data

inputBuffer = bytearray(1024) # used to store data from packets
bufferIndex = 0

roll = 0
pitch = 0
yaw = 0
battery = 0.0
rssi = 0
accX = 0.0
accY = 0.0
accZ = 0.0
gyroX = 0.0
gyroY = 0.0
gyroZ = 0.0
magX = 0.0
magY = 0.0
magZ = 0.0
alt = 0.0

FC_versionMajor = 0
FC_versionMinor = 0
FC_versionPatchLevel = 0

trim_roll = 0
trim_pitch = 0

rcThrottle = 1500
rcRoll = 1500
rcPitch = 1500
rcYaw = 1500
rcAUX1 = 1500
rcAUX2 = 1500
rcAUX3 = 1500
rcAUX4 = 1500

raw_rcThrottle = 1500
raw_rcRoll = 1500
raw_rcPitch = 1500
raw_rcYaw = 1500
raw_rcAUX1 = 1500
raw_rcAUX2 = 1500
raw_rcAUX3 = 1500
raw_rcAUX4 = 1500

IDLE = 0
HEADER_START = 1
HEADER_M = 2
HEADER_ARROW = 3
HEADER_SIZE = 4
HEADER_CMD = 5
HEADER_ERR = 6
indx = 0
# len = 0
checksum = None
command = 0
payload_size = 0
optval = 0
optlen = 0
socketSyckLock = 0
socketOpStarted = 0
checksumIndex = 0
recbuf = bytearray(1024)
c_state = 0
c = 0
err_rcvd = False
offset = None
dataSize = 0
cmd = 0
i = 0

#Helper functions to read data according the byte size
def read8():
    global bufferIndex
    value = inputBuffer[bufferIndex] & 0xFF
    bufferIndex += 1
    return value

def read16():
    global bufferIndex
    value_1 = inputBuffer[bufferIndex] & 0xFF
    value_2 = inputBuffer[bufferIndex + 1] & 0xFF
    bufferIndex += 2
    return value_1 + (value_2 << 8)

def read32():
    global bufferIndex
    value_1 = inputBuffer[bufferIndex] & 0xFF
    value_2 = inputBuffer[bufferIndex + 1] & 0xFF
    value_3 = inputBuffer[bufferIndex + 2] & 0xFF
    value_4 = inputBuffer[bufferIndex + 3] & 0xFF
    bufferIndex += 4
    return value_1 + (value_2 << 8) + (value_3 << 16) + (value_4 << 24)

#Get the numerical value of data from bytes received
def evaluateCommand(command):
    global roll, pitch, yaw, battery, rssi, accX, accY, accZ, gyroX, gyroY, gyroZ, magX, magY, magZ, alt, rcAUX1, rcAUX2, rcAUX3, rcAUX4, rcThrottle, rcPitch, rcYaw, rcRoll, raw_rcThrottle, raw_rcPitch, raw_rcRoll, raw_rcYaw, raw_rcAUX1, raw_rcAUX2, raw_rcAUX3, raw_rcAUX4
    global FC_versionMajor, FC_versionMinor, FC_versionPatchLevel, trim_roll, trim_pitch
    print(command)
    if command == MSP_FC_VERSION:
        FC_versionMajor = read8()
        FC_versionMinor = read8()
        FC_versionPatchLevel = read8()

    elif command == MSP_RAW_IMU:
        accX = read16()
        accY = read16()
        accZ = read16()

        gyroX = read16() / 8
        gyroY = read16() / 8
        gyroZ = read16() / 8

        magX = read16() / 3
        magY = read16() / 3
        magZ = read16() / 3

    elif command == MSP_ATTITUDE:
        roll = read16() / 10
        pitch = read16() / 10
        yaw = read16()

    elif command == MSP_ALTITUDE:
        alt = (read32() / 10) - 0
       

    elif command == MSP_ANALOG:
        battery = read8() / 10.0
        rssi = read16()

    elif command == MSP_ACC_TRIM:
        trim_pitch = read16()
        trim_roll = read16()

    elif command == MSP_RC or command == MSP_SET_RAW_RC:
        rcThrottle = read16()
        rcRoll = read16()
        rcPitch = read16()
        rcYaw = read16()
        rcAUX1 = read16()
        rcAUX2 = read16()
        rcAUX3 = read16()
        rcAUX4 = read16()


def readSock(sock, buffer, count):
    
    k = sock.recv_into(buffer, 1)
    if k == b'':
        raise RuntimeError("Connection broken")
    if k:
        return struct.pack('B', recbuf[0])
    else:
        return k


#Reading the decoding the MSP packets received            
def readFrame():
    global c_state, recbuf, client, checksum, offset, dataSize, err_rcvd, cmd, bufferIndex
    c = readSock(client, recbuf, 1)
    if c_state == IDLE:
        c_state = HEADER_START if c == b'$' else IDLE
    elif c_state == HEADER_START:
        c_state = HEADER_M if c == b'M' else IDLE
    elif c_state == HEADER_M:
        if c == b'>':
            c_state = HEADER_ARROW
        elif c == b'!':
            c_state = HEADER_ERR
        else:
            c_state = IDLE
    elif c_state == HEADER_ARROW or c_state == HEADER_ERR:
        err_rcvd = (c_state == HEADER_ERR)
        dataSize = (ord(c) & 0xFF)
        offset = 0
        if checksum is None:
            checksum = 0
        checksum = 0
        checksum ^= (ord(c) & 0xFF)
        c_state = HEADER_SIZE
    elif c_state == HEADER_SIZE:
        if checksum is None:
            checksum=0
        cmd = (ord(c) & 0xFF)
        checksum ^= (ord(c) & 0xFF)
        c_state = HEADER_CMD
    elif c_state == HEADER_CMD and offset < dataSize:
        checksum ^= (ord(c) & 0xFF)
        if offset is None:
            offset = 0
        inputBuffer[offset] = (ord(c) & 0xFF)
        offset+=1
    elif c_state == HEADER_CMD and offset >= dataSize:
        if (checksum & 0xFF) == (ord(c) & 0xFF):
            if err_rcvd:
                pass
            else:
                bufferIndex = 0
                evaluateCommand(cmd)
        else:
            pass
        c_state = IDLE


def readFunction():
    while True:
        readFrame()
        print(f'GyroX={gyroX} GyroY={gyroY} GyroZ={gyroZ}')
        print(f'AccX={accX} AccY={accY} AccZ={accZ}')
        print(f'MagX={magX} MagY={magY} MagZ={magZ}')
        print(f'Roll={roll} Pitch={pitch} Yaw={yaw}')
        print(f'Altitude={alt}')
        print(f'Battery={battery} Signal Strength={rssi}')
        print(f'Raw Throttle={rcThrottle} Pitch={rcPitch} Roll={rcRoll} Yaw={rcYaw}')
        print(f'Raw RCAux1={rcAUX1} RCAux2={rcAUX2} RCAux3={rcAUX3} RCAux4={rcAUX4}')


def main():
   
    readThread = threading.Thread(target=readFunction)
    readThread.start()

if __name__ == "__main__":
    main()