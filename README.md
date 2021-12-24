# SmartHome System

## Devices
Because this project will eventually be a simulation of a smart home system, we had to think of some devices that exist in a smart home system. After the placement in the house, we came up with different scenarios that trigger some specific flows in NodeRed.

The simulation consists of:

|Room ID|Room       |
|-------|-----------|
|0      |Bedroom    |
|1      |Living Room|
|2      |Kitchen    |
|3      |Bathroom   |
|4      |Balcony    |

Each device that appears in the following table consists of its name plus a number. The number is in which room this device belongs. If no number exists, there's only one device of that kind in the house.

|Device                 |Name            |Value                    |Value Range                                                                   |
|-----------------------|----------------|-------------------------|------------------------------------------------------------------------------|
|Smoke sensor           |sensorSmoke     |`bool` state             |binary                                                                        |
|Light sensor           |sensorLight0    |`int` lm                 |range `0...1000` (sunshine: `>500`, evening: `0 ~ 100`, lighting: `100...500`)|
|Light sensor           |sensorLight1    |`int` lm                 |"                                                                             |
|Light sensor           |sensorLight4    |`int` lm                 |"                                                                             |
|Motion sensor          |sensorMotion1   |`bool` state             |binary                                                                        |
|Motion sensor          |sensorMotion4   |`bool` state             |binary                                                                        |
|Temperature sensor     |sensorTemp0     |`int` temp, `int` tempDif|temp: range `10...35`, tempDif example: `+/- 4`                               |
|Temperature sensor     |sensorTemp1     |`int` temp, `int` tempDif|"                                                                             |
|Window/Door magnet     |sensorMagnet0   |`bool` state             |binary                                                                        |
|Window/Door magnet     |sensorMagnet1   |`bool` state             |"                                                                             |
|Window/Door magnet     |sensorMagnet2   |`bool` state             |"                                                                             |
|Window/Door magnet     |sensorMagnet3   |`bool` state             |"                                                                             |
|Alarm                  |alarm           |`bool` state             |binary                                                                        |
|Siren                  |siren           |`bool` state             |binary                                                                        |
|Thermostat             |thermostat      |`bool` state, `int` temp |state: binary, temp: range `10...35`                                          |
|Lamp                   |lamp0           |`bool` state             |binary                                                                        |
|Lamp                   |lamp1           |`bool` state             |"                                                                             |
|Lamp                   |lamp2           |`bool` state             |"                                                                             |
|Lamp                   |lamp3           |`bool` state             |"                                                                             |
|Lamp                   |lamp4           |`bool` state             |"                                                                             |
|Vacuum                 |vacuum          |`bool` state             |binary                                                                        |
|Air-Conditioner        |ac0             |`bool` state, `int` temp |state: binary, temp: range `18...30`                                          |
|Air-Conditioner        |ac1             |`bool` state, `int` temp |"                                                                             |
|Water Heater           |waterHeater     |`bool` state             |binary                                                                        |
|Switch                 |switch0         |`bool` state             |binary                                                                        |
|Switch                 |switch1         |`bool` state             |"                                                                             |
