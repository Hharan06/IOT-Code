float temp;
int temppin = 0;
void setup() {
  Serial.begin(9600);
}
void loop() {
  int sensorvalue = analogRead(temppin);
  float voltage = sensorvalue * (5.0 / 1023.0);
  temp = voltage / 0.1;
  Serial.print(“TEMPERATURE = ”);
  Serial.print(temp);
  Serial.print(“oC”);
  Serial.println();
  delay(1000);
}
