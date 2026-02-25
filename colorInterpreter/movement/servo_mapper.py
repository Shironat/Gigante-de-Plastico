class ServoMapper:
    def __init__(self, serial):
        self.serial = serial

        self.last_angles = {}
        self.threshold = 15

        self.limites = {
            "CE": (10, 170),
            "OE": (20, 160),
            "CD": (10, 170),
            "OD": (20, 160),
        }

    def _mapear(self, nome, angulo):
        min_s, max_s = self.limites[nome]
        return max(min_s, min(max_s, angulo))

    def _send_new(self, nome, angulo):
        angulo = self._mapear(nome, angulo)
        ultimo = self.last_angles.get(nome)

        if ultimo is None or abs(angulo - ultimo) > self.threshold:
            self.serial.mover(nome, int(angulo))
            self.last_angles[nome] = angulo

    def atualizar_esquerdo(self, cotovelo, ombro):
        self._send_new("CE", cotovelo)
        self._send_new("OE", ombro)

    def atualizar_direito(self, cotovelo, ombro):
        self._send_new("CD", cotovelo)
        self._send_new("OD", ombro)