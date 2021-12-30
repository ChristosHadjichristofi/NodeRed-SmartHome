CREATE TABLE IF NOT EXISTS smoke_sensor(
	id int not null auto_increment primary key,
	name varchar(255) not null,
	status boolean not null,
	date_time varchar(100) 
);

CREATE TABLE IF NOT EXISTS light_sensor(
	id int not null auto_increment primary key,
	name varchar(255) not null,
	lm int not null,
	date_time varchar(100) 
);

CREATE TABLE IF NOT EXISTS motion_sensor(
	id int not null auto_increment primary key,
	name varchar(255) not null,
	status boolean not null,
	date_time varchar(100) 
);

CREATE TABLE IF NOT EXISTS temp_sensor(
	id int not null auto_increment primary key,
	name varchar(255) not null,
	temp int not null,
	temp_dif int not null,
	date_time varchar(100) 
);

CREATE TABLE IF NOT EXISTS magnet_sensor(
	id int not null auto_increment primary key,
	name varchar(255) not null,
	status boolean not null,
	date_time varchar(100) 
);

CREATE TABLE IF NOT EXISTS alarm(
	id int not null auto_increment primary key,
	name varchar(255) not null,
	status boolean not null,
	date_time varchar(100) 
);

CREATE TABLE IF NOT EXISTS siren(
	id int not null auto_increment primary key,
	name varchar(255) not null,
	status boolean not null,
	date_time varchar(100) 
);

CREATE TABLE IF NOT EXISTS thermostat(
	id int not null auto_increment primary key,
	name varchar(255) not null,
	status boolean not null,
	temp int not null,
	date_time varchar(100) 
);

CREATE TABLE IF NOT EXISTS lamp(
	id int not null auto_increment primary key,
	name varchar(255) not null,
	status boolean not null,
	date_time varchar(100) 
);


CREATE TABLE IF NOT EXISTS vacuum(
	id int not null auto_increment primary key,
	name varchar(255) not null,
	status boolean not null,
	date_time varchar(100) 
);

CREATE TABLE IF NOT EXISTS air_condition(
	id int not null auto_increment primary key,
	name varchar(255) not null,
	status boolean not null,
	temp int not null,
	date_time varchar(100) 
);

CREATE TABLE IF NOT EXISTS water_heater(
	id int not null auto_increment primary key,
	name varchar(255) not null,
	status boolean not null,
	date_time varchar(100) 
);

CREATE TABLE IF NOT EXISTS switch(
	id int not null auto_increment primary key,
	name varchar(255) not null,
	status boolean not null,
	date_time varchar(100) 
);

