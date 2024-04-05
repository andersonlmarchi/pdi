import os
import utils as util
import image_manipulator as im
import file_manipulator as fp

file_name = "/images/process/EntradaEscalaCinza.pgm"
new_file_name = "/images/process/EntradaEscalaCinzaReduzidaBrilhante.pgm"

old_image = im.ImageManipulator(file_name)

image = old_image.read_image()

new_image_bits = 5
old_image_bits = util.get_intensity_from_value(image.get_intencity())

new_image = old_image.reduce_intensity_with_brightness(image.get_content(), new_image_bits, 1.2)

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + new_file_name
file = fp.FileManipulator(file_path)

file.open_file()
file.write_to_file(f"{image.get_type()}\n")
file.write_to_file(f"{image.get_size()}\n")
file.write_to_file(f"{2 ** new_image_bits}\n")

for line in new_image:
    for pixel in line:
        file.write_to_file(f'{pixel} ')
    file.write_to_file('\n')

file.close_file()
