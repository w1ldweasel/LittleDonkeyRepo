
#include <DS3232RTC.h>      // https://github.com/JChristensen/DS3232RTC
#include <Wire.h>
#include <Adafruit_NeoPixel.h>

#define NEOPIN 6          // Neopixel strip control to Pin 6.
#define N_LEDS 59
#define BRIGHTNESS 70     // Maximum LED brightness definition.

Adafruit_NeoPixel strip(N_LEDS, NEOPIN, NEO_GRB + NEO_KHZ800); // Neopixel strip definitiol.

DS3232RTC myRTC();           // Real Time Clock (RTC) used.

byte h, m, s;  // Time managing variables.

void setup () {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT); //set onboard LED to flash
  Wire.begin();        // Activate I2C.
  setSyncProvider(RTC.get);   // the function to get the time from the RTC

  if (timeStatus() != timeSet)
    Serial.println("Unable to sync with the RTC");
  else
    Serial.println("RTC has set the Arduino time");

  strip.begin();       // Activate Neopixel.
  strip.show();
  strip.setBrightness(64);
}

//------- LOOP--------------
void loop () {

  time_t t = now();
  h = hour(t);       // Obtain Hour.
  m = minute(t);    // Obtain Minutes.
  s = second(t);    // Obtain Seconds.

  print_h(h);
  print_m(m);
  print_s(s);

  digitalClockDisplay(); //for testing to output to serial port
  // Make the Onboard LED Tick on seconds
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on
  delay(100);                       // wait for half a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off
  delay(900);                       // wait for half a second
  
  leds_off();
}

//----------------- print_h Per encendre LEDs corresponents a l'hora.
void print_h(int h) {
  if (h >= 12)              // Hour from 0 to 12.
    h = h - 12;

  switch (h) {
    case 0:
      prints_leds_h(0);    // 0 hour is showed at the extreme of the strip.
      break;
    case 1:
      prints_leds_h(55);     // Hour 1 is showed at the other extreme of the strip.
      break;
    case 2:
      prints_leds_h(50);
      break;
    case 3:
      prints_leds_h(45);
      break;
    case 4:
      prints_leds_h(40);
      break;
    case 5:
      prints_leds_h(35);
      break;
    case 6:
      prints_leds_h(30);
      break;
    case 7:
      prints_leds_h(25);
      break;
    case 8:
      prints_leds_h(20);
      break;
    case 9:
      prints_leds_h(15);
      break;
    case 10:
      prints_leds_h(10);
      break;
    case 11:
      prints_leds_h(5);
      break;
    default:
      break;
  }
}

//------------------ TURNS ON THE HOUR LEDS
// Play with the Brightness parameter.
void prints_leds_h(int primer_led) {
  //Check time for night dimmed night mode

  strip.setPixelColor(primer_led, 5, 0, 0);
  strip.setPixelColor(primer_led + 1, 25, 0, 0);
  strip.setPixelColor(primer_led + 2, 80, 0, 0);
  strip.setPixelColor(primer_led + 3, 25, 0, 0);
  strip.setPixelColor(primer_led + 4, 5, 0, 0);
  strip.show();
}

//------------------ TURNS ON THE MINUTE LEDS
void print_m(int m) {
  if (m == 0)          // Paint the complete minute at the "end" of the strip.
    m = 60;
  strip.setPixelColor(60 - m - 1, 0, 10, 0);
  strip.setPixelColor(60 - m, 0, 80, 0);
  strip.setPixelColor(60 - m + 1, 0, 10, 0);
  strip.show();
}

//------------------ TURNS ON THE SECOND LED
void print_s(int s) {
  if (s == 0)        // Paint the complete second at the "end" of the strip.
    s = 59;

  strip.setPixelColor(60 - s, 0, 0, 80);
  strip.show();
}

//------------------ TURNS OFF ALL THE LEDs.
void leds_off() {
  for (int i = 0; i < 60; i++) {
    strip.setPixelColor(i, 0, 0, 0);
  }
  strip.show();
}

void digitalClockDisplay() //for testing to output to serial port
{
  // digital clock display of the time
  Serial.print(hour());
  printDigits(minute());
  printDigits(second());
  Serial.print(' ');
  Serial.print(day());
  Serial.print(' ');
  Serial.print(month());
  Serial.print(' ');
  Serial.print(year());
  Serial.println();
}

void printDigits(int digits) //for testing to output to serial port
{
  // utility function for digital clock display: prints preceding colon and leading 0
  Serial.print(':');
  if (digits < 10)
    Serial.print('0');
  Serial.print(digits);
}
