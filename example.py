#Write your own code with pluto, use the my_pluto object to give commmands to your pluto drone

from Pluto import pluto
import time

my_pluto = pluto()

my_pluto.arm()
time.sleep(5)
my_pluto.disarm()
exit()