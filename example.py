#Write your own code with pluto, use the my_pluto object to give commmands to your pluto drone

from Pluto import pluto
import time

my_pluto = pluto()

print("Caution! Arming Motors...")
my_pluto.arm()
time.sleep(5)
print("Disarming Motors...")
my_pluto.disarm()
exit()