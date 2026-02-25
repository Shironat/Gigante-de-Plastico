import cv2
from vision import detectar_pontos
from angle import calcular
from serial_comm import SerialComm
from movement.servo_mapper import ServoMapper

url = "http://10.0.0.36:7556/video"
cap = cv2.VideoCapture(url)

arduino = SerialComm("COM3", 9600)
mapper = ServoMapper(arduino)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    pontos = detectar_pontos(frame)

    if len(pontos) >= 7:

        pontos = sorted(pontos, key=lambda p: p[0])

        tronco = pontos[len(pontos)//2]

        esquerda = sorted(pontos[:3], key=lambda p: p[1])
        ombro_e, cotovelo_e, pulso_e = esquerda

        direita = sorted(pontos[-3:], key=lambda p: p[1])
        ombro_d, cotovelo_d, pulso_d = direita

        angulo_cotovelo_e = calcular(ombro_e, cotovelo_e, pulso_e)
        angulo_ombro_e = calcular(tronco, ombro_e, cotovelo_e)

        angulo_cotovelo_d = calcular(ombro_d, cotovelo_d, pulso_d)
        angulo_ombro_d = calcular(tronco, ombro_d, cotovelo_d)


        print(
            "CE:", round(angulo_cotovelo_e, 1),
            "OE:", round(angulo_ombro_e, 1),
            "CD:", round(angulo_cotovelo_d, 1),
            "OD:", round(angulo_ombro_d, 1)
        )


        mapper.atualizar_esquerdo(angulo_cotovelo_e, angulo_ombro_e)
        mapper.atualizar_direito(angulo_cotovelo_d, angulo_ombro_d)

cap.release()
arduino.fechar()