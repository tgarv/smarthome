from flask import Flask
import os
import time
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