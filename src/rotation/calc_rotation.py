import os
import cv2
import sys
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import functions as fn

file_name = fn.get_image_path("/histogram/EntradaRGB.ppm")

img = cv2.imread(file_name)

rotated_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotated_180 = cv2.rotate(img, cv2.ROTATE_180)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

axs[0].set_title("Image Original")
axs[0].imshow(img)
axs[1].set_title("Imagem Rotacionado em 90º")
axs[1].imshow(rotated_90)
axs[2].set_title("Imagem Rotacionado em 180º")
axs[2].imshow(rotated_180)

for ax in axs:
    ax.axis('off')

plt.show()
