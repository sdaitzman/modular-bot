// This work by Sam Daitzman et al. is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
// To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/.

#define initMessage "dogeArm Initialized"
#define laserPin 12

void setup() {
  Serial.begin(9600);
  Serial.println(initMessage);
  
  pinMode(laserPin, OUTPUT);
}

void loop() {
  digitalWrite(laserPin, HIGH);
}
