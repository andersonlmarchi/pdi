import os
import image_manipulator as im
import file_manipulator as fp

def convert_rgb_with_channel(file_name, new_file_name, channel, isMax):
    old_image = im.ImageManipulator(file_name)

    image = old_image.read_image()

    new_image = old_image.rgb_image_with_channel(image.get_content(), channel, isMax)

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


# convert test created images
# white image
file_name = "/images/colored_process/White.ppm"
new_file_name = "/images/colored_process/WhiteR.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'R', False)

new_file_name = "/images/colored_process/WhiteG.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'G', False)

new_file_name = "/images/colored_process/WhiteB.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'B', False)

#black image
file_name = "/images/colored_process/Black.ppm"
new_file_name = "/images/colored_process/BlackR.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'R', True)

new_file_name = "/images/colored_process/BlackG.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'G', True)

new_file_name = "/images/colored_process/BlackB.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'B', True)


# convert Fig1
file_name = "/images/colored_process/Fig1.ppm"
new_file_name = "/images/colored_process/Fig1RT.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'R', True)
new_file_name = "/images/colored_process/Fig1RF.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'R', False)
new_file_name = "/images/colored_process/Fig1GT.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'G', True)
new_file_name = "/images/colored_process/Fig1GF.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'G', False)
new_file_name = "/images/colored_process/Fig1BT.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'B', True)
new_file_name = "/images/colored_process/Fig1BF.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'B', False)

# convert Fig4
file_name = "/images/colored_process/Fig4.ppm"
new_file_name = "/images/colored_process/Fig4RT.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'R', True)
new_file_name = "/images/colored_process/Fig4RF.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'R', False)
new_file_name = "/images/colored_process/Fig4GT.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'G', True)
new_file_name = "/images/colored_process/Fig4GF.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'G', False)
new_file_name = "/images/colored_process/Fig4BT.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'B', True)
new_file_name = "/images/colored_process/Fig4BF.ppm"
convert_rgb_with_channel(file_name, new_file_name, 'B', False)


