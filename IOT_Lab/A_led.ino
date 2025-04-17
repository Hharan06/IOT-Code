// Define the pin where the LED is connected
int ledPin = 12; // Most Arduino boards have a built-in LED on pin 12

void setup() {
  pinMode(ledPin, OUTPUT); // Set the LED pin as output
}

void loop() {
  digitalWrite(ledPin, HIGH); // Turn the LED on
  delay(1000);                // Wait for 1 second (1000 milliseconds)
  digitalWrite(ledPin, LOW);  // Turn the LED off
  delay(1000);                // Wait for 1 second
}