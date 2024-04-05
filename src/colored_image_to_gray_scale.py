import os
import image_manipulator as im
import file_manipulator as fp

def convert_rgb_to_gray_scale(file_name, new_file_name):
    old_image = im.ImageManipulator(file_name)

    image = old_image.read_image()

    new_image = old_image.image_to_gray_scale(image.get_content())

    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + new_file_name
    file = fp.FileManipulator(file_path)

    file.open_file()
    file.write_to_file(f"{image.get_type()}")
    file.write_to_file(f"{image.get_size()}\n")
    file.write_to_file(f"255\n")

    for line in new_image:
        for pixel in line:
            file.write_to_file(f'{pixel} ')
        file.write_to_file('\n')

    file.close_file()

# convert Fig1
file_name = "/images/colored_process/Fig1.ppm"
new_file_name = "/images/colored_process/Fig1GrayScale.ppm"
convert_rgb_to_gray_scale(file_name, new_file_name)

# convert Fig4
file_name1 = "/images/colored_process/Fig4.ppm"
new_file_name1 = "/images/colored_process/Fig4GrayScale.ppm"
convert_rgb_to_gray_scale(file_name1, new_file_name1)


