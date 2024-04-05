import cv2
import numpy as np
import os

def histogram_enhancement_ppm(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    b, g, r = cv2.split(image)
    b_enhanced = cv2.equalizeHist(b)
    g_enhanced = cv2.equalizeHist(g)
    r_enhanced = cv2.equalizeHist(r)
    enhanced_image = cv2.merge((b_enhanced, g_enhanced, r_enhanced))

    return image, enhanced_image

rgb_image_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) + "/images/histogram/EntradaRGB.ppm"
original_image, enhanced_image = histogram_enhancement_ppm(rgb_image_path)

cv2.imshow('Original Image', original_image)
cv2.imshow('Enhanced Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
