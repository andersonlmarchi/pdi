
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def decompress_rle(compressed_line):
    decompressed_line = []

    for i in range(0, len(compressed_line)):
        count = compressed_line[i][0]
        r_value = compressed_line[i][1]
        g_value = compressed_line[i][2]
        b_value = compressed_line[i][3]

        decompressed_line.extend([r_value, g_value, b_value] * count)

    return decompressed_line

def save_ppm_from_data(filename, header, l, a, pixmap):
    with open(filename, 'w') as ppm_file:
        
        ppm_file.write(f"{header}\n")
        ppm_file.write(f"{l} {a}\n")
        ppm_file.write("255\n")

        for i in range(0, len(pixmap), l * 3):
            line = pixmap[i:i + l * 3]
            ppm_file.write(" ".join(map(str, line)) + '\n')

def load_compressed_ppm(filename):
    with open(filename, 'r') as ppm_file:
        header = read_non_empty_line(ppm_file)

        l, a = map(int, read_non_empty_line(ppm_file).split())
        _ = read_non_empty_line(ppm_file).split()

        pixmap = []

        for _ in range(a):
            line = list(map(int, read_non_empty_line(ppm_file).strip().split()))            
            pixmap.append(line)

        return header, l, a, pixmap

def read_non_empty_line(file):
    line = file.readline().strip()
    while not line:
        line = file.readline().strip()
    return line

header, l, h, compressed_data = load_compressed_ppm(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) + "/images/compressed/compressed_data.alm")
decompressed_data = decompress_rle(compressed_data)
save_ppm_from_data(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) + "/images/compressed/decompressed_data.ppm", header, l, h, decompressed_data)
