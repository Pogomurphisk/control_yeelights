import yeelight
import datetime
import time

bulbs = yeelight.discover_bulbs()
a = yeelight.Bulb("192.168.1.2")

bulb_on = datetime.time(6, 0)
bulb_off = datetime.time(22, 30)

def bulb_refresh(a, bulb_on, bulb_off):
    current_time = datetime.datetime.now().time()
    toggle_bulb(a, current_time, bulb_on, bulb_off)
    
def toggle_bulb(a, current_time, bulb_on, bulb_off):
    power = a.get_properties()['power']
    if (bulb_on < current_time < bulb_off and power == "off"):
        a.turn_on()
    elif (bulb_off < current_time and power == "on"):
        a.turn_off()
    time.sleep(60)
        
while True:
    bulb_refresh(a, bulb_on, bulb_off)