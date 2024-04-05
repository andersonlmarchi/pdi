import os
import cv2
import sys
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import functions as fn

def convert_image_grayscale(caminho):
    imagem = cv2.imread(caminho, cv2.IMREAD_UNCHANGED)
    
    if len(imagem.shape) == 3 and imagem.shape[2] == 3:
        imagem = cv2.cvtColor(imagem, cv2.COLOR_BGRA2RGBA)
    
    return imagem

image_a = fn.get_image_path('/addition/bird_add_in_journal.png')
image_b = fn.get_image_path("/addition/birds.png")

img_a = convert_image_grayscale(image_a)
img_b = convert_image_grayscale(image_b)

img_a = cv2.resize(img_a, (500, 500))

img_a_normalized = img_a.astype(float) / 255.0
img_b_normalized = img_b.astype(float) / 255.0

# Calcular a diferença entre as imagens
img_difference = img_a_normalized - img_b_normalized

# Converter de volta para o intervalo [0, 255]
img_difference = (img_difference * 255).astype('uint8')

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Adicionar cada imagem a um dos subplots
axs[0].set_title("Image A")
axs[0].imshow(img_a)
axs[1].set_title("Imagem B")
axs[1].imshow(img_b)
axs[2].set_title("Imagem Gerada")
axs[2].imshow(img_difference)

new_image = fn.get_image_path('/addition/bird_substract_in_journal.png')

if os.path.exists(new_image):
    os.remove(new_image)

cv2.imwrite(new_image, img_difference)

for ax in axs:
    ax.axis('off')

plt.show()
