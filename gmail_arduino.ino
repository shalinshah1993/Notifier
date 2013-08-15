int incomingByte = 0;   // for incoming serial data
int led = 13;

void setup() {
        pinMode(led, OUTPUT);
        Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
}

void loop() {

        // send data only when you receive data:
        if (Serial.available() > 0) {
                // read the incoming byte:
                incomingByte = Serial.read();
                // say what you got:
                Serial.print("I received ");
                Serial.print(incomingByte-48, DEC);
                Serial.println(" mail/mails");
        }
}
