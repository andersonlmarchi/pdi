import cv2
import os

diretorio = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) + "/images/equalize/"
arquivos = os.listdir(diretorio)

for arquivo in arquivos:
    if arquivo.endswith('.tif'):
        imagem = cv2.imread(os.path.join(diretorio, arquivo))
        imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        imagem_equalizada = cv2.equalizeHist(imagem_gray)

        cv2.imshow('Imagem Original', imagem_gray)
        cv2.imshow('Imagem Equalizada', imagem_equalizada)

        cv2.waitKey(0)

cv2.destroyAllWindows()
