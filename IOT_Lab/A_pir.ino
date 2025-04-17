int sensor = 4;
void setup(){
 pinMode(sensor, INPUT);
 Serial.begin(9600);
}
void loop(){
 int state = digitalRead(sensor);
 if (state == HIGH){
 Serial.println("Motion detected");
 delay(1000);
 }
 else{
 Serial.println("Motion absent");
 delay(1000);
 }
}
