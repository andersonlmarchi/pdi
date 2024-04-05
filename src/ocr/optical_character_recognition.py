import cv2
import pytesseract
import matplotlib.pyplot as plt

def exibir_imagem(titulo, imagem):
    plt.imshow(imagem, cmap='gray')
    plt.title(titulo)
    plt.show()

def reconhecer_placa(img_path):
    # Carrega a imagem
    img = cv2.imread(img_path)

    # Exibe a imagem original
    exibir_imagem('Imagem Original', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Exibe a imagem em escala de cinza
    exibir_imagem('Escala de Cinza', gray)

    # Aplica um desfoque para melhorar a qualidade do OCR
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Exibe a imagem desfocada
    exibir_imagem('Imagem Desfocada', blurred)

    # Aplica a detecção de bordas usando o Canny
    edges = cv2.Canny(blurred, 50, 150)

    # Exibe a imagem com bordas detectadas
    exibir_imagem('Bordas Detectadas', edges)

    # Encontra os contornos na imagem
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Ordena os contornos pelo tamanho
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    # Loop pelos contornos encontrados
    for contour in contours:
        # Aproxima um polígono ao contorno
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Se o contorno aproximado tem quatro vértices, é provavelmente um retângulo (assumindo ser uma placa)
        if len(approx) == 4:
            # Obtém as coordenadas do retângulo
            (x, y, w, h) = cv2.boundingRect(approx)

            # Recorta a região da placa
            roi = img[y:y + h, x:x + w]

            # Normaliza a intensidade dos pixels na região da placa
            roi_normalized = cv2.normalize(roi, None, 0, 255, cv2.NORM_MINMAX)

            # Exibe a região da placa
            exibir_imagem('Região da Placa', cv2.cvtColor(roi_normalized, cv2.COLOR_BGR2RGB))

            # Converte a região da placa para escala de cinza
            roi_gray = cv2.cvtColor(roi_normalized, cv2.COLOR_BGR2GRAY)

            # Exibe a região da placa em escala de cinza
            exibir_imagem('Região da Placa em Escala de Cinza', roi_gray)

            # Usa o pytesseract para realizar o OCR na região da placa
            texto_placa = pytesseract.image_to_string(roi_gray, config='--psm 10')

            # Imprime o texto reconhecido
            return remove_special_characters(texto_placa)

def remove_special_characters(text):
    return ''.join(filter(str.isalnum, text))

# Exemplo de uso:
# caminho_imagem = 'placa1.jpeg'
# caminho_imagem = 'placa2.jpeg'
# caminho_imagem = 'placa3.png'
caminho_imagem = 'placa4.png'
texto_placa = reconhecer_placa(caminho_imagem)
print('Texto da Placa:', texto_placa)
