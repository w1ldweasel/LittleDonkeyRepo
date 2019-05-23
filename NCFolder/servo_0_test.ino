#include <Servo.h>
#include <Wire.h>
#include <TimeLib.h>
#include <DS3232RTC.h>
Servo servo_1;
Servo servo_2;
int Hrs = 0;
int Min = 0;
int lastmin = 0;

void setup()
{
  Serial.begin(9600);
  servo_1.attach(2);
  servo_2.attach(3);
  delay(500);
  servo_1.write(0);
  servo_2.write(0);
  delay(500);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{


}
