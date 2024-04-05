# Descrição da atividade: Crie um arquivo PBM P1 com dimensões 400x400 e com valores binários aleatórios.

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import file_manipulator as fp
from utils import functions as fn

size = 400
file_name = fn.get_image_path("/generated/random_p1.pbm")

matrix = fn.create_empty_square_matrix(size)

file = fp.FileManipulator(file_name)
file.open_file()
file.write_to_file("P1\n")
file.write_to_file("#random_p1.pbm\n")
file.write_to_file("400 400\n")

matrix = [[fn.generate_random(0, 1) for _ in range(size)] for _ in range(size)]

for i in range(size):
    for j in range(size):
        file.write_to_file(str(matrix[i][j]) + " ")
    file.write_to_file("\n")

file.close_file()
