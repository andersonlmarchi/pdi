import cv2
import numpy as np
import os

def histogram_enhancement_pgm(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    enhanced_image = cv2.equalizeHist(image)

    return image, enhanced_image

gray_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) + "/images/histogram/EntradaEscalaCinza.pgm"
original_image, enhanced_image = histogram_enhancement_pgm(gray_image_path)

cv2.imshow('Original Image', original_image)
cv2.imshow('Enhanced Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
