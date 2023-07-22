import RPi.GPIO as GPIO
from flask import Flask,render_template,request
app=Flask(__name__,template_folder='/home/pi/RPI/templates')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
bulb=11
bulbstatus=0
GPIO.setup(bulb,GPIO.OUT)
GPIO.output(bulb,GPIO.HIGH)
@app.route("/")
def index():
	bulbstatus=GPIO.input(bulb)
	templateData={
		'bulb': bulbstatus,
	}
	return render_template('index.html',**templateData)
@app.route("/<devicename>/<action>")
def action(devicename,action):
	if devicename=='bulb':
		actuator=bulb
	if action=="off":
		GPIO.output(actuator,GPIO.HIGH)
	if action=="on":
		GPIO.output(actuator,GPIO.LOW)
	bulbstatus=GPIO.input(bulb)
	templateData={
		'bulb': bulbstatus,
	}
	return render_template('index.html',**templateData)
if __name__=="__main__":
	app.run(host='192.168.43.83',port=80,debug=True)
