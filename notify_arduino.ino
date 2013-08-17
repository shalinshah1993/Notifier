int pinA = 4;
int pinB = 3;
int pinC = 5;
int pinD = 8;
int pinE = 9;
int pinF = 7;
int pinG = 10;
int Gnd1 = 6;
int Gnd2 = 2;

int who = 0, num1 = 0, num2 = 0,i,j;

void setup(){
  Serial.begin(9600);
  pinMode(pinA,OUTPUT);
  pinMode(pinB,OUTPUT);
  pinMode(pinC,OUTPUT);
  pinMode(pinD,OUTPUT);
  pinMode(pinE,OUTPUT);
  pinMode(pinF,OUTPUT);
  pinMode(pinG,OUTPUT);
  pinMode(Gnd1,OUTPUT);
  pinMode(Gnd2,OUTPUT);
}

void loop(){
  if(Serial.available()>0){
    who = (int)Serial.read()-48;
    num1 = (int)Serial.read()-48;
    num2 = (int)Serial.read()-48;

    //int who = atoi(input1);
    //int num1 = atoi(input2);
    //int num2 = atoi(input3);

    Serial.println(who);
    Serial.println(num1);
    Serial.println(num2);

    if(who==0){
      for(j=0;j<250;j++){
        Gmail();
        //delay(1500);
      }
      for(i=0;i<250;i++){
        numbers(num1);
        digitalWrite(Gnd1,B0);
        digitalWrite(Gnd2,B1);
        delay(10);
        numbers(num2);
        digitalWrite(Gnd1,B1);
        digitalWrite(Gnd2,B0);
        delay(10);
      }
    }
    else if(who==1){
      for(j=0;j<250;j++){
        FB();
        //delay(1500);
      }
      for(i=0;i<250;i++){
        numbers(num1);
        digitalWrite(Gnd1,B0);
        digitalWrite(Gnd2,B1);
        delay(10);
        numbers(num2);
        digitalWrite(Gnd1,B1);
        digitalWrite(Gnd2,B0);
        delay(10);
      }
    }
    else
      error();

  }

  idle();


}

void idle(){
  int x = 100;
  digitalWrite(pinG,B0);
  digitalWrite(Gnd1,B0);
  digitalWrite(Gnd2,B0);
  digitalWrite(pinA,B1);
  delay(x);
  digitalWrite(pinA,B0);
  digitalWrite(pinB,B1);
  delay(x);
  digitalWrite(pinB,B0);
  digitalWrite(pinC,B1);
  delay(x);
  digitalWrite(pinC,B0);
  digitalWrite(pinD,B1);
  delay(x);
  digitalWrite(pinD,B0);
  digitalWrite(pinE,B1);
  delay(x);
  digitalWrite(pinE,B0);
  digitalWrite(pinF,B1);
  delay(x);
  digitalWrite(pinF,B0);

}

void FB(){
  digitalWrite(pinA,B1);
  digitalWrite(pinB,B0);
  digitalWrite(pinC,B0);
  digitalWrite(pinD,B0);
  digitalWrite(pinE,B1);
  digitalWrite(pinF,B1);
  digitalWrite(pinG,B1);
  digitalWrite(Gnd1,B0);
  digitalWrite(Gnd2,B1);
  delay(10);
  digitalWrite(pinA,B1);
  digitalWrite(pinB,B1);
  digitalWrite(pinC,B1);
  digitalWrite(pinD,B1);
  digitalWrite(pinE,B1);
  digitalWrite(pinF,B1);
  digitalWrite(pinG,B1);
  digitalWrite(Gnd1,B1);
  digitalWrite(Gnd2,B0);
  delay(10);
}

void Gmail(){
  digitalWrite(pinA,B1);
  digitalWrite(pinB,B0);
  digitalWrite(pinC,B1);
  digitalWrite(pinD,B1);
  digitalWrite(pinE,B1);
  digitalWrite(pinF,B1);
  digitalWrite(pinG,B0);
  digitalWrite(Gnd1,B0);
  digitalWrite(Gnd2,B1);
  delay(10);
  digitalWrite(pinA,B0);
  digitalWrite(pinB,B0);
  digitalWrite(pinC,B0);
  digitalWrite(pinD,B1);
  digitalWrite(pinE,B1);
  digitalWrite(pinF,B1);
  digitalWrite(pinG,B0);
  digitalWrite(Gnd1,B1);
  digitalWrite(Gnd2,B0);
  delay(10);
}

void numbers(int num){
  switch(num){
  case 0:
    digitalWrite(pinA,B1);
    digitalWrite(pinB,B1);
    digitalWrite(pinC,B1);
    digitalWrite(pinD,B1);
    digitalWrite(pinE,B1);
    digitalWrite(pinF,B1);
    digitalWrite(pinG,B0);
    break;
  case 1:
    digitalWrite(pinA,B0);
    digitalWrite(pinB,B1);
    digitalWrite(pinC,B1);
    digitalWrite(pinD,B0);
    digitalWrite(pinE,B0);
    digitalWrite(pinF,B0);
    digitalWrite(pinG,B0);
    break;
  case 2:
    digitalWrite(pinA,B1);
    digitalWrite(pinB,B1);
    digitalWrite(pinC,B0);
    digitalWrite(pinD,B1);
    digitalWrite(pinE,B1);
    digitalWrite(pinF,B0);
    digitalWrite(pinG,B1);
    break;
  case 3:
    digitalWrite(pinA,B1);
    digitalWrite(pinB,B1);
    digitalWrite(pinC,B1);
    digitalWrite(pinD,B1);
    digitalWrite(pinE,B0);
    digitalWrite(pinF,B0);
    digitalWrite(pinG,B1);
    break;
  case 4:
    digitalWrite(pinA,B0);
    digitalWrite(pinB,B1);
    digitalWrite(pinC,B1);
    digitalWrite(pinD,B0);
    digitalWrite(pinE,B0);
    digitalWrite(pinF,B1);
    digitalWrite(pinG,B1);
    break;
  case 5:
    digitalWrite(pinA,B1);
    digitalWrite(pinB,B0);
    digitalWrite(pinC,B1);
    digitalWrite(pinD,B1);
    digitalWrite(pinE,B0);
    digitalWrite(pinF,B1);
    digitalWrite(pinG,B1);
    break;
  case 6:
    digitalWrite(pinA,B1);
    digitalWrite(pinB,B0);
    digitalWrite(pinC,B1);
    digitalWrite(pinD,B1);
    digitalWrite(pinE,B1);
    digitalWrite(pinF,B1);
    digitalWrite(pinG,B1);
    break;
  case 7:
    digitalWrite(pinA,B1);
    digitalWrite(pinB,B1);
    digitalWrite(pinC,B1);
    digitalWrite(pinD,B0);
    digitalWrite(pinE,B0);
    digitalWrite(pinF,B0);
    digitalWrite(pinG,B0);
    break;
  case 8:
    digitalWrite(pinA,B1);
    digitalWrite(pinB,B1);
    digitalWrite(pinC,B1);
    digitalWrite(pinD,B1);
    digitalWrite(pinE,B1);
    digitalWrite(pinF,B1);
    digitalWrite(pinG,B1);
    break;
  case 9:
    digitalWrite(pinA,B1);
    digitalWrite(pinB,B1);
    digitalWrite(pinC,B1);
    digitalWrite(pinD,B1);
    digitalWrite(pinE,B0);
    digitalWrite(pinF,B1);
    digitalWrite(pinG,B1);
    break;
  }
}

void error(){
  int i;
  for(i=0; i<200;i++){
    digitalWrite(pinA,B1);
    digitalWrite(pinB,B0);
    digitalWrite(pinC,B0);
    digitalWrite(pinD,B1);
    digitalWrite(pinE,B1);
    digitalWrite(pinF,B1);
    digitalWrite(pinG,B1);
    digitalWrite(Gnd1,B0);
    digitalWrite(Gnd2,B1);
    delay(10);
    digitalWrite(pinA,B0);
    digitalWrite(pinB,B0);
    digitalWrite(pinC,B1);
    digitalWrite(pinD,B0);
    digitalWrite(pinE,B1);
    digitalWrite(pinF,B0);
    digitalWrite(pinG,B1);
    digitalWrite(Gnd1,B1);
    digitalWrite(Gnd2,B0);
    delay(10);
  }
}

