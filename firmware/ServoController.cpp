#include "ServoController.h"
#include "Config.h"

void ServoController::begin() {
  ombroDireito.attach(PIN_OMBRO_DIREITO);
  cotoveloDireito.attach(PIN_COTOVELO_DIREITO);
  ombroEsquerdo.attach(PIN_OMBRO_ESQUERDO);
  cotoveloEsquerdo.attach(PIN_COTOVELO_ESQUERDO);
  tronco.attach(PIN_TRONCO);
  pescoco.attach(PIN_PESCOCO);
}

void ServoController::mover(String nome, int angulo) {

  if (nome == "OD") ombroDireito.write(angulo);
  if (nome == "CD") cotoveloDireito.write(angulo);
  if (nome == "OE") ombroEsquerdo.write(angulo);
  if (nome == "CE") cotoveloEsquerdo.write(angulo);
  if (nome == "TR") tronco.write(angulo);
  if (nome == "PE") pescoco.write(angulo);
}