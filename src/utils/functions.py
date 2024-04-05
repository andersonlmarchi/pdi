
import random
import math
import os

def generate_random(minNumber, maxNumber):
    return random.randint(minNumber, maxNumber)
    
def create_empty_square_matrix(size):
    return create_empty_matrix(size, size)

def create_empty_matrix(lines, columns):
    x = []
    y = []
    for j in range(0, lines):
        y.append(0)
    for i in range(0, columns):
        x.append(y)
    return x

def remove_eol(strings):
    return [string.rstrip('\n') for string in strings]

def get_intensity_from_value(value):
    return int(math.log2(int(value))) + 1

def get_image_path(image_name):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) + "/images/" + image_name
