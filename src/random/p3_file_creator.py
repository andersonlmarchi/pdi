# Descrição da atividade: Crie dois arquivos PPM P3 com dimensões 400x400 e 1000x1000 e com valores aleatórios entre 0 e 15.

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import file_manipulator as fp
from utils import functions as fn
size = 400
rgbsize = size * 3

file_name = fn.get_image_path("/generated/random_p3.ppm")

# create file 1
file = fp.FileManipulator(file_name)
file.open_file()
file.write_to_file("P3\n")
file.write_to_file("#random_p3.ppm\n")
file.write_to_file("400 400\n")
file.write_to_file("15\n")

matrix = [[fn.generate_random(0, 15) for _ in range(rgbsize)] for _ in range(size)]

for i in range(rgbsize):
    for j in range(size):
        file.write_to_file(str(matrix[j][i]) + " ")
    file.write_to_file("\n")

file.close_file()

#create file 2
size = 1000
rgbsize = size * 3
file_name = fn.get_image_path("/generated/random_p3_1.ppm")

file = fp.FileManipulator(file_name)
file.open_file()
file.write_to_file("P3\n")
file.write_to_file("#random_p3_1.ppm\n")
file.write_to_file("1000 1000\n")
file.write_to_file("15\n")

matrix = [[fn.generate_random(0, 15) for _ in range(rgbsize)] for _ in range(size)]

for i in range(rgbsize):
    for j in range(size):
        file.write_to_file(str(matrix[j][i]) + " ")
    file.write_to_file("\n")

file.close_file()
