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

image_a = fn.get_image_path("/addition/paper.tif")
image_b = fn.get_image_path("/addition/birds.tif")

img_a = convert_image_grayscale(image_a)
img_b = convert_image_grayscale(image_b)

img_a = cv2.resize(img_a, (612, 612))

# Normalizar as imagens para o intervalo [0, 1]
img_a_normalized = img_a.astype(float) / 255.0
img_b_normalized = img_b.astype(float) / 255.0

# Definir o fator de blending - fator de "mistura", sendo 0.5 a junção das imagens é uniforme
alpha = 0.5

# Aplicar o blending - 
blended_img = cv2.addWeighted(img_a_normalized, alpha, img_b_normalized, 1 - alpha, 0)

# Converter de volta para o intervalo [0, 255]
img_addition = (blended_img * 255).astype('uint8')

new_image = fn.get_image_path('/addition/bird_add_in_journal.png')

if os.path.exists(new_image):
    os.remove(new_image)

cv2.imwrite(new_image, img_addition)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].set_title("Image A")
axs[0].imshow(img_a)
axs[1].set_title("Imagem B")
axs[1].imshow(img_b)
axs[2].set_title("Nova imagem")
axs[2].imshow(img_addition)

for ax in axs:
    ax.axis('off')

plt.show()
