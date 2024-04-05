import os
import cv2
import sys
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import functions as fn

image_a = fn.get_image_path("/addition/paper.tif")
image_b = fn.get_image_path("/addition/birds.png")

img_a = cv2.imread(image_a, cv2.COLOR_BGRA2RGBA)
img_b = cv2.imread(image_b, cv2.IMREAD_UNCHANGED)

img_a = cv2.resize(img_a, (700, 700))

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Adicionar cada imagem a um dos subplots
axs[0].set_title("Image A")
axs[0].imshow(img_a)
axs[1].set_title("Imagem B")
axs[1].imshow(img_b)

x, y = 100, 100

# Crie uma máscara para a região que será inserida
mask = img_b[:, :, 3] / 255.0  # Normalize os valores de 0 a 255 para 0 a 1

# Inverta a máscara para a operação de combinação
inv_mask = 1 - mask[:, :, None]

# Combine as imagens usando a máscara
for i in range(img_b.shape[0]):
    for j in range(img_b.shape[1]):
        # Obtém as contribuições de A e B usando as máscaras
        a = (1 - mask[i, j]) * img_a[y + i, x + j, :3]
        b = mask[i, j] * img_b[i, j, :3]
        
        # Soma as contribuições e atualiza a imagem A
        img_a[y + i, x + j, :3] = a + b

axs[2].set_title("Imagem Gerada")
axs[2].imshow(img_a)

new_image = fn.get_image_path('/addition/bird_insert_in_journal.png')

if os.path.exists(new_image):
    os.remove(new_image)

cv2.imwrite(new_image, img_a)

for ax in axs:
    ax.axis('off')

plt.show()
