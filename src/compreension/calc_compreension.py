
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import functions as fn

def compress_rle(line):
    compressed_line = []
    count = 1

    for i in range(3, len(line), 3):
        if line[i-3:i] == line[i:i+3]:
            count += 1
        else:
            compressed_line.extend([count, line[i-3], line[i-2], line[i-1]])
            count = 1

    # if len(line) > 0:
    #     compressed_line.extend([count, line[-3], line[-2], line[-1]])

    return compressed_line

# def compress_rle(line):
#     compressed_line = []
#     count = 1

#     # Ajuste o intervalo para pular a cada 3 valores
#     for i in range(3, len(line), 3):
#         # Compare o pixel atual (i-3, i-2, i-1) com o próximo pixel (i, i+1, i+2)
#         if line[i-3:i] == line[i:i+3]:
#             count += 1
#         else:
#             compressed_line.extend([count] + line[i-3:i])
#             count = 1

#     # Adicione o último pixel
#     if len(line) > 0:
#         compressed_line.extend([count] + line[-3:])

#     return compressed_line

def compress_image(filename):
    with open(filename, 'r') as ppm_file:
        compressed_lines = []

        # Lê o cabeçalho e extrai largura (l) e altura (a)
        header = read_non_empty_line(ppm_file)
        l, a = map(int, read_non_empty_line(ppm_file).split())
        _ = read_non_empty_line(ppm_file).split()

        # Lê o pixmap e divide em linhas para R, G e B
        pixmap = []

        for _ in range(a*3):
            line = list(map(int, read_non_empty_line(ppm_file).strip().split()))
            pixmap.append(line)

        # Comprime as linhas R, G e B
        for i in range(a*3):
            compressed_line = compress_rle(pixmap[i])
            compressed_lines.extend(compressed_line)
            print(*compressed_line)

        return header, l, a, compressed_lines

def save_compressed_data(filename, header, l, a, compressed_data):
    with open(filename, 'w') as compressed_file:

        # Escreve a largura e altura
        compressed_file.write(f"{header}\n")
        compressed_file.write(f"{l} {a}\n")
        compressed_file.write("255\n")

        # Escreve os dados comprimidos
        for i in range(0, len(compressed_data), 4):
            count = compressed_data[i]
            r_value = compressed_data[i+1]
            g_value = compressed_data[i+2]
            b_value = compressed_data[i+3]
            compressed_file.write(f"{count} {r_value} {g_value} {b_value}\n")

def save_compressed_data_bmp(filename, l, a, compressed_data):

    # Cria o cabeçalho do arquivo BMP
    header = bytearray([66, 77, 134, 0, 0, 0, 0, 0, 0, 0, 54, 0, 0, 0, 40, 0, 0, 0, l & 0xFF, (l >> 8) & 0xFF, (l >> 16) & 0xFF, (l >> 24) & 0xFF, a & 0xFF, (a >> 8) & 0xFF, (a >> 16) & 0xFF, (a >> 24) & 0xFF, 1, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    with open(filename, 'wb') as compressed_file:

        # Escreve o cabeçalho
        compressed_file.write(header)
        compressed_file.write("".encode("utf-8"))

        # Escreve os dados comprimidos
        for i in range(0, len(compressed_data), 4):
            count = compressed_data[i]
            r_value = compressed_data[i+1]
            g_value = compressed_data[i+2]
            b_value = compressed_data[i+3]

            # Escreve os valores R, G e B no arquivo
            for _ in range(count):
                compressed_file.write(bytearray([r_value, g_value, b_value]))

def read_non_empty_line(file):
    line = file.readline().strip()
    while not line:
        line = file.readline().strip()
    return line

# Faz a compressão da imagem e retorna os dados comprimidos
header, l, a, compressed_data = compress_image(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) + "/images/colored_process/Fig4.ppm")

# Salva os dados comprimidos em um arquivo do tipo Anderson Luis Marchi (alm)
save_compressed_data(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) + "/images/compressed/compressed_data.alm", header, l, a, compressed_data)

# Salva os dados comprimidos em um arquivo do tipo Bitmap (bmp)
save_compressed_data_bmp(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) + "/images/compressed/compressed_data.bmp", l, a, compressed_data)
