  /* Robot_script  criado em maio de 2020. 

  Algoritmo para controle de braço robótico 6 eixos + garra;
  Funciona apenas com script Python;
  Comunicação Serial com PC necessária;
  */

  /* Parametros das funçoes:
  
  GRIPPER(estado, limite);
    estado: if true: fecha a garra até o valor limite
            if false: abre a garra, NÃO USA LIMITE
    limite: valor opcional(caso não inserido é igual a 0)
            indica o ângulo máximo de fechamento.

  MOVE( J1, J2, J3, J4, J5, J6);
    J1: ângulo -90 a 90 para servo1
    J2: ângulo -90 a 90 para servo2
    J3: ângulo -90 a 90 para servo3
    J4: ângulo -90 a 90 para servo4
    J5: ângulo -90 a 90 para servo5
    J6: ângulo -90 a 90 para servo6
  */

#include <VarSpeedServo.h>

#define pinJ1 2    // orange
#define pinJ2 3    // orange(black)   
#define pinJ3 4    // yellow
#define pinJ4 5    // green
#define pinJ5 6    // blue
#define pinJ6 7    // white
#define pinJ7 8    // purple


void MotionControls(int servoPsition, char rotation)
void MOVE(int J1, int J2, int J3, int J4, int J5, int J6);
void GRIPPER(bool Open, int Degree = 0);
char rx;
int SPEED;

VarSpeedServo servo1;
VarSpeedServo servo2;
VarSpeedServo servo3;
VarSpeedServo servo4;
VarSpeedServo servo5;
VarSpeedServo servo6;
VarSpeedServo servo7;


void setup() {

  servo1.attach(pinJ1);
  servo2.attach(pinJ2);
  servo3.attach(pinJ3);
  servo4.attach(pinJ4);
  servo5.attach(pinJ5);
  servo6.attach(pinJ6);
  servo7.attach(pinJ7);

  SPEED = 30;
  
  MOVE(0, 0, 0, 0, 0, 0);
  GRIPPER(true, 5);

  Serial.begin(9600);
  Serial.write('available')
}

void loop() {

  while (Serial.available() <= 0) {;} // O while é que espera ter informaçoes para ler.
 
  if (Serial.available() > 0) rx = Serial.read();

  if (rx == 'a') MOVE(0, 0, 0, 0, 0, 0);
  if (rx == 'b') MOVE(0, 2, 16, 0, 70, 0);
  if (rx == 'c') MOVE(-34, 24, -10, 2, 74, -36);
  if (rx == 'd') MOVE(32, 20, -4, -2, 72, 32);
  if (rx == 'e') MOVE(20, -6, -10, -14, 66, 20);
  if (rx == 'f') MOVE(90, -6, 10, -14, 66, 20);
  
  // Servo 1 =========================
  if (rx == 'g') {
    servo1.write(MotionControls(servo1.read(), '+'), SPEED);
    Serial.println("available");
  }
  if (rx == 'h') {
    servo1.write(MotionControls(servo1.read(), '-'), SPEED);
    Serial.println("available");
  }

  // Servo 2 =========================
  if (rx == 'i') {
    servo2.write(MotionControls(servo2.read(), '+'), SPEED);
    Serial.println("available");
  }
  if (rx == 'j') {
    servo2.write(MotionControls(servo2.read(), '-'), SPEED);
    Serial.println("available");
  }
 
  // Servo 3 =========================
  if (rx == 'k'){
    servo3.write(MotionControls(servo3.read(), '+'), SPEED);
    Serial.println("available");
  }
  if (rx == 'l') {
    servo3.write(MotionControls(servo3.read(), '-'), SPEED);
    Serial.println("available");
  }

  // Servo 4 =========================
  if (rx == 'm') {
    servo4.write(MotionControls(servo4.read(), '+'), SPEED);
    Serial.println("available");
  }
  if (rx == 'n') {
    servo4.write(MotionControls(servo4.read(), '-'), SPEED);
    Serial.println("available");
  }

  // Servo 5 =========================
  if (rx == 'o') {
    servo5.write(MotionControls(servo5.read(), '+'), SPEED);
    Serial.println("available");
  }
  if (rx == 'p') {
    servo5.write(MotionControls(servo5.read(), '-'), SPEED);
    Serial.println("available");
  }

  // Servo 6 =========================
  if (rx == 'q') {
    servo6.write(MotionControls(servo6.read(), '+'), SPEED);
    Serial.println("available");
  }
  if (rx == 'r') {
    servo6.write(MotionControls(servo6.read(), '-'), SPEED);
    Serial.println("available");
  }

  // Servo 7 =========================
  if (rx == 's') {
    GRIPPER(true, 5);
    Serial.println("available");
  }
  if (rx == 't') {
    GRIPPER(false);
    Serial.println("available");
  }
}

int MotionControls(int servoPsition, char rotation) {
  if (rotation == '+' && 0 <= servoPsition && servoPsition < 180) {servoPsition += 2; return servoPsition;}
  if (rotation == '-' && 0 < servoPsition && servoPsition <= 180) {servoPsition -= 2; return servoPsition;}
}

void MOVE(int J1, int J2, int J3, int J4, int J5, int J6) {
    
    int a1 = map(J1, -90, 90, 0, 180);
    int a2 = map(J2, -40, 50, 0, 180);
    int a3 = map(J3, -95, 85, 0, 180);
    int a4 = map(J4, -90, 90, 0, 180);
    int a5 = map(J5, -90, 90, 180, 0);
    int a6 = map(J6, -90, 90, 0, 180);
    
    servo1.write(a1, SPEED);    
    servo2.write(a2, SPEED);
    servo3.write(a3, SPEED);
    servo4.write(a4, SPEED);
    servo5.write(a5, SPEED);
    servo6.write(a6, SPEED);

    servo1.wait();    
    servo2.wait();
    servo3.wait();
    servo4.wait();
    servo5.wait();
    servo6.wait();

    delay(1000);
    Serial.println("available");
}

void GRIPPER(bool Close, int Degree) { 
  if (Close) {
    servo7.write(Degree + 100, SPEED);
  }
  else {
    servo7.write(50 + 100, SPEED); // Soma 100 por conta de defeito mecânico em servo7.
  }
}
