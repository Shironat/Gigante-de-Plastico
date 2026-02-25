#include "SerialControl.h"

void SerialControl::begin(long baud) {
  Serial.begin(baud);
}

bool SerialControl::available() {
  return Serial.available();
}

String SerialControl::readCommand() {
  if (Serial.available()) {
    buffer = Serial.readStringUntil('\n');
    buffer.trim();
    return buffer;
  }
  return "";
}
