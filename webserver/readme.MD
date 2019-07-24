# Study of flask and Grafana using MQTT protocol
This code contains support for SQLite as well as MYSQL

For visualisation using grafana the SQLite database is not supported, so we need to use 'MYSQL' database.

The code for node js is added in 'Grafana' directory.

Before running the code in grafana directory, make sure of the following:
	
	-You have installed grafana locally, if not the enter the following command in terminal  and hit enter:
		wget https://dl.grafana.com/oss/release/grafana_5.4.2_amd64.deb
	
	-To include the node modules using:
		-npm install dependencies

# Prerequisites:
  Devices:
  
  	Hardware requirements:
    
	▪ RaspberryPi – Acts as a broker
    	▪ DHT11 – Sensing Temperature and Humidity
    	▪ ESP32 – Acts as a publisher

	Software requirements:
	
	▪ Arduino IDE
    	▪ Flask
    	▪ Python
    	▪ SQLite

# Installation:

	• Flask:

	Flask is an open source micro-framework for python based on Werkzeug, Jinja 2 and good intentions and supports
	"Web Server Gateway Interface (WSGI)"
	‘WSGI is adopted as standard for python web application development’
  		- sudo apt-get update
   		- sudo apt-get upgrade
   		- sudo apt-get install python-pip python-flask git-core
   		- sudo pip install flask
   		- sudo pip install paho-mqtt
   		- sudo pip install flask

	• SQLite:

	SQLite is an embedded SQL database engine.
	SQLite is serverless – access disk directly
	Supports cross platform architecture
	Also, Python supports an in-built support for sqlite
		- sudo apt-get install sqlite3
		- sqlite3 sensordata.db

Lets create a table before running the program:

sqlite> BEGIN;

sqlite> CREATE TABLE dhtreadings(id INTEGER PRIMARY KEY AUTOINCREMENT, temperature  NUMERIC, humidity NUMERIC, 

currentdate DATE, currentime TIME, device TEXT);

sqlite> COMMIT;

To list all the avilable tables, type:

sqlite> .tables

dhtreadings

It returns the newly created table named ‘dhtreadings’. You can see the fullschema of the tables when you enter:

sqlite> .fullschema

• MYSQL:

	MySQL Community Edition is a freely downloadable version of the world's most popular open source database that is supported by an active community of open source developers and enthusiasts.
	Follow this link to install MYSQL successfully:
	https://dev.mysql.com/downloads/mysql/5.5.html

	Before running program make sure to run this table creation command in mysql:
	mysql>
	CREATE DATABASE mydb;
	USE mydb;
	CREATE TABLE tbl_messages ( 
	messageID INT NOT NULL AUTO_INCREMENT, 
	clientID VARCHAR(20) NOT NULL, 
	topic VARCHAR(50) NOT NULL, 
	message VARCHAR(100) NOT NULL, 
	Enable BOOLEAN DEFAULT 1, 
	DateTime_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
	PRIMARY KEY (messageID)
	);


• Grafana:

	Installation: wget https://dl.grafana.com/oss/release/grafana_5.4.2_amd64.deb

	Grafana is an open source software for time series analytics which has advanced and rich metrics dashboard than chronograf
	Features of grafana:
		Better visualization
		Alert notification feature
		Runs on port 3000


# Procedure
	Run the esp32_DHT11.ino on arduino by interfacing esp32 and dht11 with system
	Follow the installation step of 'Flask' and 'SQLite' and then on client side copy the client folder.
	Run the code.py file using 'python code.py' 
	-For getting output on flask run the 'code.py' and check the flask output on specified port.
	-To check on SQLite database enter the following commands:
		sqlite3 sensordata.db
		SELECT * FROM dhtreadings;

	To check on Grafana visualisation you need to run the MYSQL folder on client system.
	Run the index.js file from Grafana folder and check on the sql database as well as grafana visualisation.
	-To check on MYSQL database enter the following commands:
		select * from mydb;
	-To check Grafana output open browser and enter 'localhost:3000'	(3000 is default grafana port)

#Outputs:
	
	The output of this project can be seen on 'Flask' as well as on 'Grafana'
	
Modified by: 
	
	Saurabh Patil (er.saurabhpatil@gmail.com)
	Lomesh Mahajan
	Sanket Desai
