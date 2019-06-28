import paho.mqtt.client as mqtt
from flask import Flask, render_template, request
import json
import sqlite3

app = Flask(__name__)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# The callback for when the client receives a 'CONNECT' response from the server.
def on_connect(client, userdata, flags, rc):
    #print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("dht")

# The callback for when a PUBLISH message is received from the ESP8266.

def on_message(client, userdata, message):

    if message.topic == "dht":
        print "DHT readings update:", message.payload

        dhtreadings_json = json.loads(message.payload)

	#print "Temperature:",dhtreadings_json['temperature'];
        #print "Humidity",dhtreadings_json['humidity']

        # connects to SQLite database. File is named "sensordata.db" without the quotes
        # WARNING: your database file should be in the same directory of the app.py file or have the correct path
        conn=sqlite3.connect('sensordata.db')
        c=conn.cursor()
        c.execute("""INSERT INTO dhtreadings (temperature,
            humidity, currentdate, currenttime, device) VALUES((?), (?), date('now'),
            time('now'), (?))""", (dhtreadings_json['temperature'],
            dhtreadings_json['humidity'], 'ESP32') )
	conn.commit()
        conn.close()

mqttc=mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect("localhost",1883,60)
mqttc.loop_start()

@app.route("/")
def main():
   # connects to SQLite database. File is named "sensordata.db" without the quotes
   # WARNING: your database file should be in the same directory of the app.py file or have the correct path
   conn=sqlite3.connect('sensordata.db')
   conn.row_factory = dict_factory
   print "Level-01"
   c=conn.cursor()
   c.execute("SELECT * FROM dhtreadings ORDER BY id DESC LIMIT 20")
   readings = c.fetchall()
   print(readings)
   print "Hello"
   return render_template('main.html', readings=readings)

if __name__ == "__main__":
   app.run(host='localhost', port=6500, debug=True)
