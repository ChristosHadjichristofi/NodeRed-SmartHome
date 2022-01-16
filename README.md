# SmartHome System

## Technology Stack
* [Apache Kafka](https://kafka.apache.org/) as message broker
* [Node-Red](https://nodered.org/) to handle the logic of our smart home
* [NodeJS](https://nodejs.org/en/) and [ExpressJS](https://expressjs.com/) to create a server and specifically a route to handle all incoming requests from the smart home's devices
* [NVM](https://github.com/nvm-sh/nvm) as the Node Version Manager (so as we can have different versions of node in our pc)
* [Python3](https://www.python.org/downloads/) to create dummy data that represent the data from the smart home sensors and to create a simulation script which makes many api calls to the express server
* [MySQL](https://www.mysql.com/) as the database
* [Docker](https://www.docker.com/) to create a container for the database (here we could even create container for everything, but this would require a connection bridge)
* [Grafana](https://grafana.com/) as a simple user dashboard where the user (smart home owner) can see many details and monitor the IOT devices
* [Telegram](https://telegram.org/) where we created a bot that will notify us (more info in upcoming sections)
* [FlyWay](https://flywaydb.org/) as a database version control. Used for matters of ease when developing the system

## Installation
1. Download NVM ```curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash```
2. Install NodeJS ```nvm install 16```
3. Download Apache Kafka ```https://dlcdn.apache.org/kafka/3.0.0/kafka_2.13-3.0.0.tgz``` and then unzip it to the desired folder i.e Home (cd ~/Kafka)
4. Navigate to ```cd ~/Kafka``` and create 2 folders, ```data``` and ```logs```
5. Open ```vim ~/Kafka/kafka_2.13-3.0.0/config/zookeeper.properties```, and change ```dataDir``` to the directory where ```data``` folder is. In our case ```dataDir=~/Kafka/data```
6. Open ```vim ~/Kafka/kafka_2.13-3.0.0/config/server.properties```, and change ```log.dirs``` to the directory where ```logs``` folder is. In our case ```log.dirs=~/Kafka/logs```
7. Create aliases to use kafka easier. Navigate to ```cd ~``` and ```vim .bashrc```. Find the ```#some more aliases``` comment and below add
```
#kafka-aliases
#start zookeeper
alias zookeeper="bin/zookeeper-server-start.sh config/zookeeper.properties"
#start kafka
alias kafka="bin/kafka-server-start.sh config/server.properties"
#topics commands
alias list-topics="bin/kafka-topics.sh --bootstrap-server localhost:9092 --list"
alias describe-topic="bin/kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic"
alias consume-topic="bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic"
alias create-topic="bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --topic"
alias delete-topic="bin/kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic"

#grafana
alias grafana="sudo systemctl start grafana-server"
```
8. Open a terminal and navigate to ```cd ~/Kafka/kafka_2.13-3.0.0```. Execute the command ```zookeeper```
9. Open a new terminal and navigate again to ```cd ~/Kafka/kafka_2.13-3.0.0```. Execute the command ```kafka``` as soon as ```zookeeper``` is finished
10. Open a new terminal and navigate again to ```cd ~/Kafka/kafka_2.13-3.0.0```. Execute the command ```create-topic [name] --partitions [number] --replication-factor 1```. In our case the ```name``` is `smart-home` and `number` is `6`
11. Git clone this repository
12. Navigate to `kafka-api` open a terminal and execute the command `npm install`
13. Install docker with `sudo snap install docker`
14. Open a new terminal and execute the command `docker run -p 3311:3306 --name smart-home-db -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7`. This will create a container for our database which will be created in the following steps
15. Use a database management tool (in our case we used dbeaver which you can install by executing `sudo snap install dbeaver-ce`) in order to create a new database. The name of the database for this project is `smart_home`
16. In the database management tool open an SQL Script and paste inside the content of `sql/V1__initial.sql` which is again located in the project folder
17. After the above step you should have several tables in your database
18. Install Node-Red. Open a new terminal and execute the command `sudo snap install node-red`
19. In the previous terminal execute the command `node-red.desktop-launch`. This will start the node-red
20. Open a browser and navigate to `http://localhost:1880/`. Here you should see node-red running
21. From the top right corner press the hamburger menu and choose `import`. Choose `select a file to import` and locate `node-red-flow.json` which is in the folder which you git cloned in step 11
22. 

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
|5      |Alarm      |

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
|Switch - Phone charger |switch0         |`bool` state             |binary                                                                        |
|Switch - Coffee machine|switch1         |`bool` state             |"                                                                             |

## Scenario
Because this is a simulation, we had to create a scenario based on the life of an imaginary person, John. <br>
John works on weekdays. More specifically:
* He wakes up at 07:30
* Eats breakfast at 08:00
* Works from 09:00 to 17:00
* He arms the alarm before leaving the house and disarms the alarm when he returns
* Takes a shower at 17:30
* Eats dinner at 20:00
* Sleeps at 24:00

On the weekends he has a more relaxed schedule.
* He wakes up at 09:00
* He sleeps at 02:00

John, on a daily basis has some demands for this smart home system. More specifically:
* He wants the Water heater to start boiling water at 17:00
* He wants the vacuum to work Monday - Wednesday - Friday from 10:00 to 12:00
* He wants his phone to get charged from 03:30 to 06:30
* He wants to have his coffee ready by 07:45
* He wants the living room lights to be turned on when its getting dark and he enters the appartment
* He wants the balcony room lights to be turned on when its getting dark and motion is detected on the balcony 
* He wants the lights in the bedroom, bathroom and kitchen to be switched off when he arms the alarm
* He wants the thermostat to be set on when the temperature drops below 22 degrees
* He wants the a/c in the bedroom to be turned on when the temperature rises above 29 degrees
* He wants the a/c in the living room to be turned on when the temperature rises above 29 degrees
* He wants door/window openings to be logged to the database

Also in case of an emegerncy, he wants to be notified from a bot.
* Fire
* Burglary
* Possible malfunction of any temperature sensor in the smart system

Unexpected events throughout the week
* On Tuesday at 13:00 burglars broke into John's house using the door in the living room
* On Friday at 20:00 there was a fire in John's kitchen
* On Sunday at 16:00 the temperature sensor malfunctioned

Based on the above a script was created, that simulates John's life for a period of a week. 
