# DEVICES
#
# Input Devices:
#   sensorSmoke
#   sensorLight1, sensorLight0, sensorLight4
#   sensorMotion1, sensorMotion4
#   sensorTemp0, sensorTemp1
#   sensorMagnet0, sensorMagnet1, sensorMagnet2, sensorMagnet3
#   alarm
#
# Output devices:
#   siren
#   lamp0, lamp1, lamp2, lamp3, lamp4
#   thermostat
#   ac0, ac1
#   waterHeater 
#   vacuum 
#   switch0, switch1 

import sys
import json
import random

f = open("events.json", "w")
sys.stdout = f


days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

state = {"sensorSmoke" : {"status" : 0 }, 
         "sensorLight0" : { "lm" : 0 }, 
         "sensorLight1" : { "lm" : 0 }, 
         "sensorLight4" : { "lm" : 0 }, 
         "sensorMotion1" : { "status" : 0 }, 
         "sensorMotion4" : { "status" : 0 }, 
         "sensorTemp0" : { "temp" : 0, "tempDif" : 0 }, 
         "sensorTemp1" : { "temp" : 0, "tempDif" : 0 }, 
         "sensorMagnet0" : { "status" : 0 }, 
         "sensorMagnet1" : { "status" : 0 }, 
         "sensorMagnet2" : { "status" : 0 },
         "sensorMagnet3" : { "status" : 0 },
         "alarm" : { "status" : 0 }} 


def print_state(state):
    print('{',end=' ')
    for k,v in state.items():
        print(json.dumps(k),' : ',sep='', end='')
        print(json.dumps(v), end='')
        if(k!='alarm'):
            print(', ',end='')
    if (days.index(day) == 6 and hour==23 and mins==45):
        print('}')
    else:
        print('},')
    return


def sensorLights(state): # light from 6:00 until 20:45 everyday
    if(hour <= 5 or hour >= 21):
        state["sensorLight0"]["lm"] = 0
        state["sensorLight1"]["lm"] = 0
        state["sensorLight4"]["lm"] = 0
    else:
        state["sensorLight0"]["lm"] = 1000 - 130*( abs(hour - 13.5 + mins/60) )
        state["sensorLight1"]["lm"] = 1000 - 130*( abs(hour - 13.5 + mins/60) )
        state["sensorLight4"]["lm"] = 1000 - 130*( abs(hour - 13.5 + mins/60) )
    return


def sensorMotion1(state): # Motion sensor in the living room can be triggered by John between 8:00 -8:30 and 17:30-00:00 on weekdays and between 9:00-24:00 on weekends
    state["sensorMotion1"]["status"] = 0
    if days.index(day) <= 4: 
        if ((hour + mins/60) >= 8 and (hour + mins/60) < 8.5 ):
            state["sensorMotion1"]["status"] = int((random.randint(0, 100) > 50 ))
        elif ((hour + mins/60) >= 17.5):
            state["sensorMotion1"]["status"] = int((random.randint(0, 100) > 75 ))
    else:
        if ((hour + mins/60) >= 9):
            state["sensorMotion1"]["status"] = int((random.randint(0, 100) > 65 ))


def sensorMotion4(state): # Motion sensor in the balcony can be triggered by John between 7:30-8:30 and 17:30-00:00 on weekdays and between 9:00-24:00 on weekends
    state["sensorMotion4"]["status"] = 0
    if days.index(day) <= 4: 
        if ((hour + mins/60) >= 7.5 and (hour + mins/60) < 8.5 ):
            state["sensorMotion4"]["status"] = int((random.randint(0, 100) > 95 ))
        elif ((hour + mins/60) >= 17.5):
            state["sensorMotion4"]["status"] = int((random.randint(0, 100) > 85 ))
    else:
        if ((hour + mins/60) >= 9):
            state["sensorMotion4"]["status"] = int((random.randint(0, 100) > 75 ))


def sensorTemp(state): # temperature changes and the warmest time of the day is 13:30, Monday is on average the coldest day and Sunday is on average the warmest day
    prev_temp_0 = state["sensorTemp0"]["temp"]
    prev_temp_1 = state["sensorTemp1"]["temp"]

    state["sensorTemp0"]["temp"] = int(20 - 0.75*( abs(hour - 13.5 + mins/60))) + days.index(day) 
    if ((days.index(day) == 6) and (hour + mins/60) >= 16 and (hour + mins/60) <= 16.5): # On Sunday at 16:00 the temperature sensor malfunctioned
        state["sensorTemp1"]["temp"] = 35
    else:
        state["sensorTemp1"]["temp"] = int(20 - 0.75*( abs(hour - 13.5 + mins/60))) + days.index(day) 
    state["sensorTemp0"]["tempDif"] = state["sensorTemp0"]["temp"] - prev_temp_0
    state["sensorTemp1"]["tempDif"] = state["sensorTemp1"]["temp"] - prev_temp_1
    if((days.index(day) == 0) and hour==0 and mins==0):
        state["sensorTemp0"]["tempDif"] = 0
        state["sensorTemp1"]["tempDif"] = 0


def sensorMagnet0(state): # Bedroom door opens when John wakes up or goes to bed
    state["sensorMagnet0"]["status"] = 0
    if days.index(day) <= 4: 
        if ((hour + mins/60) >= 7.5 and (hour + mins/60) < 8.5 ):
            state["sensorMagnet0"]["status"] = int((random.randint(0, 100) > 50 ))
    else:
        if ((hour + mins/60) >= 9 and (hour + mins/60) <= 10 ):
            state["sensorMagnet0"]["status"] = int((random.randint(0, 100) > 50 ))
    if days.index(day) <= 3 or days.index(day) == 6:
        if ((hour + mins/60) >= 23):
            state["sensorMagnet0"]["status"] = int((random.randint(0, 100) > 40 ))          
    else:
        if ((hour + mins/60) <= 2 ):
            state["sensorMagnet0"]["status"] = int((random.randint(0, 100) > 40 ))


def sensorMagnet1(state): # Living room door opens when John leaves and returns from job
    state["sensorMagnet1"]["status"] = 0
    if(((hour + mins/60) == 8.5 or (hour + mins/60) == 17.5) and days.index(day) <= 4):
        state["sensorMagnet1"]["status"] = 1
    else:
        state["sensorMagnet1"]["status"] = 0


def sensorMagnet2(state): # Kitchen door opens when John is eating
    state["sensorMagnet2"]["status"] = 0
    if days.index(day) <= 4: 
        if ((hour + mins/60) >= 7.5 and (hour + mins/60) < 8.5 ):
            state["sensorMagnet2"]["status"] = int((random.randint(0, 100) > 50 ))
        elif ((hour + mins/60) >= 17.5):
            state["sensorMagnet2"]["status"] = int((random.randint(0, 100) > 85 ))
    else:
        if ((hour + mins/60) >= 9):
            state["sensorMagnet2"]["status"] = int((random.randint(0, 100) > 90 ))



def sensorMagnet3(state): # Bathroom door opens when John is at home
    state["sensorMagnet3"]["status"] = 0
    if days.index(day) <= 4: 
        if ((hour + mins/60) >= 7.5 and (hour + mins/60) < 8.5 ):
            state["sensorMagnet3"]["status"] = int((random.randint(0, 100) > 50 ))
        elif ((hour + mins/60) >= 17.5):
            state["sensorMagnet3"]["status"] = int((random.randint(0, 100) > 90 ))
    else:
        if ((hour + mins/60) >= 9):
            state["sensorMagnet3"]["status"] = int((random.randint(0, 100) > 95 ))



def armAlarm(state): # Alarm is armed when John is at work from 8:30 to 17:30 on weekdays
    if(((hour + mins/60) >=8.5) and ((hour + mins/60) <= 17.5) and days.index(day) <= 4):
        state["alarm"]["status"] = 1
    else:
        state["alarm"]["status"] = 0

def burglary(state): # On Tuesday at 13:00 burglars broke into John's house using the door in the living room
    state["sensorMagnet1"]["status"] = 0
    state["sensorMotion1"]["status"] = 0
    state["sensorMagnet0"]["status"] = 0
    state["sensorMagnet2"]["status"] = 0
    state["sensorMagnet3"]["status"] = 0
    if days.index(day) == 1:
        if ((hour + mins/60) == 13):
            state["sensorMagnet1"]["status"] = 1
            state["sensorMotion1"]["status"] = 1
        elif ((hour + mins/60) == 13.25):
            state["sensorMagnet1"]["status"] = 1
            state["sensorMotion1"]["status"] = 1
            state["sensorMagnet0"]["status"] = 1
            state["sensorMagnet2"]["status"] = 1
            state["sensorMagnet3"]["status"] = 1

def fire(state): # On Friday at 20:00 there was a fire in John's kitchen
    state["sensorSmoke"]["status"] = 0
    if days.index(day) == 4:
        if ((hour + mins/60) == 20 or (hour + mins/60) == 20.25):
            state["sensorSmoke"]["status"] = 1

        
prev_state = state.copy()
print('{')
for day in days:
    for hour in range(24):
        for mins in range(0,60,15):
            if(hour<10):
                print('"2022-01-',days.index(day)+17, ' 0', hour,':', sep='', end='')
            else:
                print('"2022-01-',days.index(day)+17, ' ', hour,':', sep='', end='')
            if(mins==0):
                print('0',mins,':00":',sep='',end='')
            else:
                print(mins,':00":',sep='',end='')

            sensorLights(state)
            sensorMotion1(state)
            sensorMotion4(state)
            sensorTemp(state)
            sensorMagnet0(state)
            sensorMagnet1(state)
            sensorMagnet2(state)
            sensorMagnet3(state)
            armAlarm(state)
            burglary(state)
            fire(state)
            print_state(state)
            prev_state = state.copy()
print('}')
f.close()
