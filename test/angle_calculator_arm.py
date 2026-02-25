import cv2
import numpy as np
import math

url = "http://IP:port/video"
cap = cv2.VideoCapture(url)

def calcular_angulo(A, B, C):
    BA = np.array(A) - np.array(B)
    BC = np.array(C) - np.array(B)

    produto = np.dot(BA, BC)
    norma_BA = np.linalg.norm(BA)
    norma_BC = np.linalg.norm(BC)

    if norma_BA == 0 or norma_BC == 0:
        return 0

    cos_angulo = produto / (norma_BA * norma_BC)
    cos_angulo = np.clip(cos_angulo, -1.0, 1.0)

    angulo = math.degrees(math.acos(cos_angulo))
    return angulo

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([20, 100, 100])
    upper = np.array([35, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    pontos = []

    for c in contours:
        area = cv2.contourArea(c)
        if area > 500:
            x, y, w, h = cv2.boundingRect(c)
            cx = x + w // 2
            cy = y + h // 2
            pontos.append((cx, cy))

    if len(pontos) >= 3:
        pontos = sorted(pontos, key=lambda p: p[1])  # ordena por altura (y)

        A = pontos[0]
        B = pontos[1]
        C = pontos[2]

        angulo = calcular_angulo(A, B, C)

        print("Ângulo do cotovelo:", round(angulo, 2))

cap.release()