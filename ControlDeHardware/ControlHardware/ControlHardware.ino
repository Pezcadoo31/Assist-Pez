#include <Servo.h>

Servo myservo;  // crea el objeto Servo
int servoPin = 9; // pin al que está conectado el servo

int speedPin = 11;
int dirPin1 = 12;
int dirPin2 = 13;
int speedMotor = 130;

int redPin = 7;
int greenPin = 6;
int bluePin = 5;

void setup() {
  Serial.begin(9600);  // inicia la comunicación serial
  pinMode(speedPin, OUTPUT);
  pinMode(dirPin1, OUTPUT);
  pinMode(dirPin2, OUTPUT);

  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);

  myservo.attach(servoPin);  // adjunta el servo al pin PWM
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');  // lee el comando de la serial
    command.trim();  // elimina los espacios en blanco adicionales
    
    if (command == "ENCENDER AIRE") {
      digitalWrite(dirPin1, LOW);
      digitalWrite(dirPin2, HIGH);
      analogWrite(speedPin, 255);
      delay(100);
      analogWrite(speedPin, speedMotor);
      Serial.println("Motor Encendido");
    } else if (command == "APAGAR AIRE") {
      analogWrite(speedPin, 0);
      Serial.println("Motor Apagado");
    } 
    else if (command == "ABRIR PUERTA") {
      myservo.write(50);  // mueve el servo a 90 grados
      Serial.println("La puerta se ha abierto");
    } else if (command == "CERRAR PUERTA") {
      myservo.write(170);  // mueve el servo a 0 grados
      Serial.println("La puerta se ha cerrado");
    }
    else if (command == "ENCENDER LUZ") {
      analogWrite(redPin, 255);
      analogWrite(greenPin, 0);
      analogWrite(bluePin, 255);
      Serial.println("Luz Morada Encendida");
    } else if (command == "ENCENDER LUZ VERDE") {
      analogWrite(redPin, 0);
      analogWrite(greenPin, 255);
      analogWrite(bluePin, 0);
      Serial.println("Luz Verde Encendida");
    } else if (command == "ENCENDER LUZ ROJA") {
      analogWrite(redPin, 255);
      analogWrite(greenPin, 0);
      analogWrite(bluePin, 0);
      Serial.println("Luz Roja Encendida");
    } else if (command == "ENCENDER LUZ AZUL") {
      analogWrite(redPin, 0);
      analogWrite(greenPin, 0);
      analogWrite(bluePin, 255);
      Serial.println("Luz Azul Encendida");
    } else if (command == "APAGAR LUZ") {
      analogWrite(redPin, 0);
      analogWrite(greenPin, 0);
      analogWrite(bluePin, 0);
      Serial.println("Luz Apagada");
    }
  }
}

