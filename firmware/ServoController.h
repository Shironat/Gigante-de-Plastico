#ifndef SERVO_CONTROLLER_H
#define SERVO_CONTROLLER_H

#include <Arduino.h>
#include <Servo.h>

class ServoController {
  private:
    Servo ombroDireito;
    Servo cotoveloDireito;
    Servo ombroEsquerdo;
    Servo cotoveloEsquerdo;
    Servo tronco;
    Servo pescoco;

  public:
    void begin();
    void mover(String nome, int angulo);
};

#endif