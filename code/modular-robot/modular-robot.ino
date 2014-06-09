#define laserPin 7 // laser pin or laser relay - 5v pin may be needed for current


void setup() {
	delay(500); // give code time to finish uploading
	Serial.begin(9600); // connect at 9600 baud
	Serial.println("Ready");
	pinMode(laserPin, OUTPUT);
}
void loop() {
	char inByte = ' ';
	if(Serial.available()) { // only send data back if data has been sent
		char inByte = Serial.read(); // read the incoming data
		Serial.println(inByte); // send the data back in a new line so that it is not all one long line
		if(inByte=='a') {
			digitalWrite(7, HIGH);
		} else if(inByte=='s') {
			digitalWrite(7, LOW);
		}
	}
	delay(100); // delay for 1/10 of a second
}