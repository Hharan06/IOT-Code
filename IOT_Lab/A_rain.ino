#define POWER_PIN D7
#define AO_PIN A0
void setup() {
    Serial.begin(9600);
    pinMode(POWER_PIN, OUTPUT); 
}
void loop() {
    digitalWrite(POWER_PIN, HIGH);
    delay(10);
    int rainValue = analogRead(AO_PIN);
    digitalWrite(POWER_PIN, LOW);
    Serial.println(rainValue);
    delay(1000); 
}