#ifndef SERIAL_CONTROL_H
#define SERIAL_CONTROL_H

#include <Arduino.h>

class SerialControl {
  private:
    String buffer;

  public:
    void begin(long baud);
    bool available();
    String readCommand();
};

#endif
