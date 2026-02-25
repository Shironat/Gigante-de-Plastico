#include "Config.h"
#include "ServoController.h"
#include "SerialControl.h"

ServoController servoController;
SerialControl serialControl;

void setup() {
  serialControl.begin(BAUD_RATE);
  servoController.begin();
}

void loop() {
  if (serialControl.available()) {
    String cmd = serialControl.readCommand();

    // Exemplo: "OD:120"
    int separator = cmd.indexOf(':');

    if (separator > 0) {
      String nome = cmd.substring(0, separator);
      int angulo = cmd.substring(separator + 1).toInt();

      servoController.mover(nome, angulo);
    }
  }
}