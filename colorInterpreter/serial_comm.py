import serial
import time

class SerialComm:
    def __init__(self, porta="COM3", baudrate=9600):
        self.ser = serial.Serial(porta, baudrate, timeout=1)
        time.sleep(1.5)

    def mover(self, nome, angulo):
        comando = f"{nome}:{angulo}"
        self.ser.write((comando + "\n").encode())
        print("Enviado:", comando)

    def fechar(self):
        self.ser.close()