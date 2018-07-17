from tkinter import *
from tkinter import colorchooser
import serial
import os 
import time
auto = False

bluetoothSerial = serial.Serial( "/dev/rfcomm1", baudrate=9600 )

def switch_light(event=None):
  if lightstat.get():
	bluetoothSerial.write('g')
  else :
	bluetoothSerial.write('f')

def switch_fan(event=None):
  if fanstat.get():
	bluetoothSerial.write('i')
  else :
	bluetoothSerial.write('h')
	
def switch_humid(event=None):
  if humidstat.get():
	 bluetoothSerial.write('k')
  else :
	 bluetoothSerial.write('j')
	 
def perf(choice):
	if choice == 'a':
		bluetoothSerial.write('l')
	if choice == 'b':
		bluetoothSerial.write('m')



def yeeenable(event=None):
	if yee.get():
		os.system('./light.sh on')
		yeecontrol()
		os.system('./yeelight-rgb.sh 0 xFF,FF,FF')
	else :
		os.system('./light.sh off')
		yeedestroy()
		
def yeecontrol():
	yeecol.grid()
	yeebright.grid()
	yeebright.set(25)
	
def yeedestroy():
	yeecol.grid_remove()
	yeebright.grid_remove()

def setbright(val):
	os.system('./yeelight-brightness.sh 0 %s' % val)
	
	
def colorpick(even=None):
	color = colorchooser.askcolor()
	s = color[1]
	a,b,c,d,e,f,g = s
	red = ['x',b,c]
	green = [d,e]
	blue = [f,g]
	RED=''.join(red)
	GREEN=''.join(green)
	BLUE=''.join(blue)
	os.system('./yeelight-rgb.sh 0 %s,%s,%s'%(RED,GREEN,BLUE))


def mandisable():
  lightstat.set(1)
  fanstat.set(1)
  humidstat.set(1)
  yee.set(1)
  light.grid_remove()
  fan.grid_remove()
  humid.grid_remove()
  roomf.grid_remove()
  perf1.grid_remove()
  perf2.grid_remove()
  mood.grid_remove()
  yeelight.grid_remove()
  yeecol.grid_remove()
  yeebright.grid_remove()
  os.system('./light.sh off')
  global auto
  auto = True
  
def manenable():
  light.grid()
  fan.grid()
  humid.grid()
  roomf.grid()
  perf1.grid()
  perf2.grid()
  mood.grid()
  yeelight.grid()
  bluetoothSerial.write('e')
  global auto
  auto = False
 
def automode():
  if auto:
		bluetoothSerial.write('a')
		os.system ('python capture.py')
  app.after(2000, automode)


def tempmandisable():
  lightstat.set(1)
  fanstat.set(1)
  humidstat.set(1)
  yee.set(1)
  light.grid_remove()
  fan.grid_remove()
  humid.grid_remove()
  roomf.grid_remove()
  perf1.grid_remove()
  perf2.grid_remove()
  mood.grid_remove()
  yeelight.grid_remove()
  yeecol.grid_remove()
  yeebright.grid_remove()
  os.system('./light.sh off')

app = Tk()

lightstat = BooleanVar()
fanstat = BooleanVar()
humidstat = BooleanVar()
yee = BooleanVar()
scentchoice = IntVar()

lightstat.set(1)
fanstat.set(1)
humidstat.set(1)
yee.set(1)

app.title("AAPSAD")
app.geometry("+320+240")

Label(app, text="Please choose Mode").grid(row=0, columnspan=3)

#Radio Buttons
autorad = Radiobutton(app,text="Auto Mode",value=1,command = mandisable).grid(row=1, column = 0, padx=10, pady=10)
manrad = Radiobutton(app,text="Manual Mode", value=2,command = manenable).grid(row=1, column = 2, padx=10, pady=10)

#Manual Controls
light = Checkbutton(app, text="Light", variable=lightstat,onvalue=0,offvalue=1)
light.bind("<Button-1>",switch_light)
light.grid(row=2)

fan = Checkbutton(app, text="Fan", variable=fanstat,onvalue=0,offvalue=1)
fan.bind("<Button-1>",switch_fan)
fan.grid(row=2, column=1)

humid = Checkbutton(app, text="Humidifier", variable=humidstat,onvalue=0,offvalue=1)
humid.bind("<Button-1>",switch_humid)
humid.grid(row=2, column=2)

#Room Freshner
roomf=Label(app, text="Room Freshner", pady=20)
roomf.grid(row=3, columnspan=3)

perf1 = Button(app, text= "Summer Delights", command=lambda *args: perf('a'))
perf1.grid(row=4, column=0,padx=10)

perf2 = Button(app, text= "Citrus", command=lambda *args: perf('b'))
perf2.grid(row=4, column=2, padx=10)

#Yeelight
mood=Label(app, text="Mood Lamp")
mood.grid(row=5, columnspan=3)

yeelight=Checkbutton(app, text="ON/OFF", variable=yee,onvalue=0,offvalue=1)
yeelight.bind("<Button-1>",yeeenable)
yeelight.grid(row=6, columnspan=3)
global color
yeecol=Button(app, text = "Pick Color")
yeecol.bind("<Button-1>",colorpick)
yeecol.grid(row=7, pady=10)

yeebright=Scale(app, from_=1, to=100, orient=HORIZONTAL,command=setbright)
yeebright.grid(row=7,column=1, columnspan=2,pady=5)

tempmandisable()

app.after(500, automode) #Looping for Emotion detection
app.mainloop()
