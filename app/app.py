from flask import Flask, jsonify, request
import os
import time
import Adafruit_DHT
import json
import datetime
import sqlite3
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/tv_on")
def tv_on():
    os.system("/usr/bin/irsend SEND_ONCE RMT-TX102U KEY_POWER")
    return "TV ON"

@app.route("/tv_off")
def tv_off():
    os.system("/usr/bin/irsend SEND_ONCE RMT-TX102U KEY_POWER")
    return "TV OFF"

@app.route("/stereo_on")
def stereo_on():
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_POWER")
    return "STEREO ON"

@app.route("/stereo_off")
def stereo_off():
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_POWER")
    return "STEREO OFF"

@app.route("/stereo_mute")
def stereo_mute():
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_MUTE")
    return "STEREO MUTE"

@app.route("/volume_up")
def volume_up():
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_VOLUMEUP")
    time.sleep(0.2)
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_VOLUMEUP")
    time.sleep(0.2)
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_VOLUMEUP")
    time.sleep(0.2)
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_VOLUMEUP")
    time.sleep(0.2)
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_VOLUMEUP")
    time.sleep(0.2)
    return "VOLUME UP"

@app.route("/volume_down")
def volume_down():
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_VOLUMEDOWN")
    time.sleep(0.2)
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_VOLUMEDOWN")
    time.sleep(0.2)
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_VOLUMEDOWN")
    time.sleep(0.2)
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_VOLUMEDOWN")
    time.sleep(0.2)
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_VOLUMEDOWN")
    time.sleep(0.2)
    return "VOLUME UP"

@app.route("/HDMI1")
def stereo_hdmi1():
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_1")
    return "HDMI1"

@app.route("/HDMI2")
def stereo_hdmi2():
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_2")
    return "HDMI2"

@app.route("/HDMI3")
def stereo_hdmi3():
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_3")
    return "HDMI3"

@app.route("/HDMI4")
def stereo_hdmi4():
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_4")
    return "HDMI4"

@app.route("/bluetooth_audio")
def bluetooth_audio():
    os.system("/usr/bin/irsend SEND_ONCE YAMAHA_RAV463 KEY_5")
    return "HDMI5"

@app.route("/read_temperature_humidity")
def read_temperature_humidity():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 24)
    return jsonify({"temperature": temperature, "humidity": humidity})

@app.route("/log_temperature_humidity", methods=["GET", "POST"])
def log_temperature_humidity():
    connection = get_sql_connection()
    cursor = connection.cursor()
    humidity = request.args.get("humidity")
    temperature = request.args.get("temperature")
    room = request.args.get("room")
    time = datetime.datetime.now()
    cursor.execute('INSERT INTO temperature_humidity_log (temperature, humidity, currentdate, room) VALUES (?, ?, ?, ?)', (temperature, humidity, time.isoformat(), room))
    connection.commit()
    return str(cursor.lastrowid)

@app.route("/get_temperature_humidity")
def get_temperature_humidity():
    room = request.args.get("room")
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    connection = get_sql_connection()
    cursor = connection.cursor()
    if start_date is not None and end_date is not None:
        sql = 'SELECT room, temperature, humidity, currentdate FROM temperature_humidity_log WHERE (currentdate BETWEEN ? AND ?)'
        parameters = [start_date, end_date]
        if room is not None:
            sql = sql + ' AND room=?'
            parameters.append(room)
        sql = sql + ' ORDER BY currentdate ASC'
        cursor.execute(sql, parameters)
    else:
        cursor.execute('SELECT temperature, humidity, currentdate FROM temperature_humidity_log WHERE room=? ORDER BY ID DESC LIMIT 1', (room,))
    return jsonify(cursor.fetchall())

def get_sql_connection():
    return sqlite3.connect('/home/pi/projects/smart_home/sensordata.db')
