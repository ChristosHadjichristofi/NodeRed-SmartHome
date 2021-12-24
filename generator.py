lista = ["sensorSmoke", "sensorLight0", "sensorLight1", "sensorLight4", "sensorMotion1", "sensorMotion4",
        "sensorTemp0", "sensorTemp1", "sensorMagnet0", "sensorMagnet1", "sensorMagnet2", "sensorMagnet3",
        "siren", "alarm", "thermostat",	"lamp0", "lamp1", "lamp2", "lamp3", "lamp4", "vacuum", 
        "ac0", "ac1", "waterHeater", "switch0", "switch2"
]

print('{')
for element in lista:
    print('"',element,'" : {',sep='')
    print('"','status','" : ',sep='')
    print('}')
print('}')