import os
import image_manipulator as im
import file_manipulator as fp

file_name = "/images/process/EntradaEscalaCinzaReduzidaBW.pgm"
new_file_name = "/images/process/EntradaEscalaCinzaReduzidaBWNegativo.pgm"

old_image = im.ImageManipulator(file_name)

image = old_image.read_image()

new_image = old_image.reduce_bw_intensity_with_invertion(image.get_content())

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + new_file_name
file = fp.FileManipulator(file_path)

file.open_file()
file.write_to_file(f"{image.get_type()}")
file.write_to_file(f"{image.get_size()}\n")
file.write_to_file(f"1\n")

for line in new_image:
    for pixel in line:
        file.write_to_file(f'{pixel} ')
    file.write_to_file('\n')

file.close_file()

