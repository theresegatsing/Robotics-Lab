

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int potpin = A0;
int val; 

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
    // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// The serve changes position accroding to the temperature.
void loop() {
  val = analogRead(potpin); 
  Serial.println(val);           // reads the value of the potentiometer (value between 0 and 1023)
  val = map(val, 20, 150, 0, 180);     // scale it to use it with the servo (value between 0 and 180)
  myservo.write(val);                  // sets the servo position according to the scaled value
  delay(15);                     // waits 15ms for the servo to reach the position
  } 
