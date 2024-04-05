import os
import cv2
import matplotlib.pyplot as plt

def calcular_histograma_rgb_opencv(imagem_path):
    imagem = cv2.imread(imagem_path, cv2.IMREAD_COLOR)
    b_hist = cv2.calcHist([imagem], [0], None, [256], [0, 256])
    g_hist = cv2.calcHist([imagem], [1], None, [256], [0, 256])
    r_hist = cv2.calcHist([imagem], [2], None, [256], [0, 256])
    return b_hist, g_hist, r_hist

def plotar_histograma_rgb_opencv(b_hist, g_hist, r_hist):
    plt.plot(b_hist, color='b', label='Blue')
    plt.plot(g_hist, color='g', label='Green')
    plt.plot(r_hist, color='r', label='Red')
    plt.title('RGB Histograma')
    plt.xlabel('Intencidade')
    plt.ylabel('Frequência')
    plt.legend()
    plt.show()

rgb_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) + "/images/histogram/EntradaRGB.ppm"

b_hist, g_hist, r_hist = calcular_histograma_rgb_opencv(rgb_image_path)
plotar_histograma_rgb_opencv(b_hist, g_hist, r_hist)
