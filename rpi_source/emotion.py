import io
import os
import serial
bluetoothSerial = serial.Serial( "/dev/rfcomm1", baudrate=9600 )

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = 'emo.jpg'

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.face_detection(image=image)
faces = response.face_annotations
# 0-'UNKNOWN',1-'VERY_UNLIKELY',2-'UNLIKELY',3-'POSSIBLE',4-'LIKELY',5- 'VERY_LIKELY')
for face in faces:
    anger = face.anger_likelihood
    joy = face.joy_likelihood
    sorrow = face.sorrow_likelihood
#print(anger) print(joy) print(sorrow)
if (anger >= joy) and (anger >= sorrow):
   emo = 'a'
elif (joy >= anger) and (joy >= sorrow):
   emo = 'j'
else :
   emo = 's'

if emo == 'a' :
  bluetoothSerial.write('d')
  os.system('./light.sh on')
  os.system('./light.sh color Teal')
  os.system('./light.sh brightness 20')
  os.system('omxplayer Anger.mp4')
  os.system('killall omxplayer.bin')
if emo == 'j' :
  bluetoothSerial.write('d')
  os.system('./light.sh on')
  os.system('./light.sh color Yellow')
  os.system('./light.sh brightness 20')
  os.system('omxplayer Joy.mp4')
  os.system('killall omxplayer.bin')
if emo == 's' :
  bluetoothSerial.write('c')
  os.system('./light.sh on')
  os.system('./light.sh color Lime')
  os.system('./light.sh brightness 20')
  os.system('omxplayer Sorrow.mp4')
  os.system('killall omxplayer.bin')
