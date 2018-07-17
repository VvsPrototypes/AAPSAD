#include <TroykaDHT.h>
#include <SoftwareSerial.h>

#define ROOM_SUM 11
#define ROOM_CIT 12
#define HUMIDIFIER 2
#define FAN 4
#define LIGHT 5
#define BRX 9
#define BTX 10
#define LIGHT_SENSE A0

void off_all()
{
  digitalWrite(HUMIDIFIER,LOW);
  digitalWrite(FAN,HIGH);
  digitalWrite(LIGHT,HIGH);
}

void freshner (int fresh)
  { 
    digitalWrite(fresh,HIGH);
    delay(750);
    digitalWrite(fresh,LOW); 
  }

DHT dht(8, DHT11);
SoftwareSerial btserial(BRX, BTX);
int hum;
float temperature;
char bdata;

void setup()
 {
   pinMode(HUMIDIFIER, OUTPUT);
   pinMode(ROOM_SUM, OUTPUT);
   pinMode(ROOM_CIT, OUTPUT);
   pinMode(FAN, OUTPUT);
   pinMode(LIGHT, OUTPUT);
   digitalWrite(FAN,HIGH);
   digitalWrite(LIGHT,HIGH);
   btserial.begin(9600);
   dht.begin();
 }

void loop()
{ 
  dht.read();
  delay(100);
  hum = dht.getHumidity();
  temperature = dht.getTemperatureC();
  int lux;
  if (btserial.available()){
   bdata=btserial.read();
   Serial.println(bdata);
  
   switch(bdata){
    case 'a' : //Auto
      off_all();
      lux = analogRead(LIGHT_SENSE);
      if (lux < 100)
         {
          digitalWrite(LIGHT,LOW);
         }
      break;

     case 'b': //ANGER
         digitalWrite(LIGHT,HIGH);
         if (hum<80)
            {
              digitalWrite(HUMIDIFIER,HIGH);
            }
         if (temperature>26)
            {
              digitalWrite(FAN,LOW);
            }
         freshner(ROOM_CIT);
         //delay(480000);
         break;
       
     
      case 'c':             //SAD
        digitalWrite(LIGHT,HIGH);
        if (hum<60)
          {
              digitalWrite(HUMIDIFIER,HIGH); 
          }
        if (temperature>26)
            {
              digitalWrite(FAN,LOW);
            }
        freshner(ROOM_SUM);
        //delay(480000);
        break;

       case 'd':             //JOY
         digitalWrite(LIGHT,HIGH);
         if (hum<60)
          {
              digitalWrite(HUMIDIFIER,HIGH); 
          }
         if (temperature>26)
            {
              digitalWrite(FAN,LOW);
            }
         freshner(ROOM_CIT);
         //delay(480000);
         break;

       case 'e': //MANUAL
          off_all();
          break;
       case 'f':
          digitalWrite(LIGHT,HIGH);
          break;
       case 'g':
          digitalWrite(LIGHT,LOW);
          break;
       case 'h':
          digitalWrite(FAN,HIGH);
          break;
       case 'i':
          digitalWrite(FAN,LOW);
          break;
       case 'j':
          digitalWrite(HUMIDIFIER,LOW);
          break;
       case 'k':
          digitalWrite(HUMIDIFIER,HIGH);
          break;
       case 'l':
          freshner(ROOM_SUM);
          break;
       case 'm':
          freshner(ROOM_CIT);
          break;
       default:
          break;
  }
 }
}
