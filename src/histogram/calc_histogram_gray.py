import os
import cv2
import matplotlib.pyplot as plt

def calcular_histograma_ge_opencv(imagem_path):
    imagem = cv2.imread(imagem_path, cv2.IMREAD_GRAYSCALE)
    histograma = cv2.calcHist([imagem], [0], None, [256], [0,256])
    return histograma

def plotar_histograma_ge_opencv(histograma):
    plt.plot(histograma)
    plt.title('Histograma')
    plt.xlabel('Intencidade')
    plt.ylabel('Frequência')
    plt.show()

gray_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) + "/images/histogram/EntradaEscalaCinza.pgm"

histograma = calcular_histograma_ge_opencv(gray_image_path)
plotar_histograma_ge_opencv(histograma)
