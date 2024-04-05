import os
import math
import image_type as img
import file_manipulator as fp

class ImageManipulator:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_image(self):
        file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + self.file_path
        file = fp.FileManipulator(file_name)

        type = file.read_file(1)
        size = file.read_file(2).split()
        intencity = file.read_file(3)

        content = file.read_file_content(4)

        return img.ImageType(type, size[0], size[1], 1 if type == "P1" else intencity, content)

    def redimensionar(self, image, new_width, new_height):
        original_width = int(image.width)
        original_height = int(image.height)
        content = image.content

        new_image = bytearray(new_width * new_height)

        for y in range(new_height):
            for x in range(new_width):
                pixel_original_x = (x * original_width) // new_width
                pixel_original_y = (y * original_height) // new_height

                old_idx = (pixel_original_y * original_width) + pixel_original_x
                new_idx = (y * new_width) + x

                new_image[new_idx] = content[old_idx]

        return new_image
        
    def write_new_image(self, image, new_file_name, new_width, new_height):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + new_file_name
        file = fp.FileManipulator(file_path)

        file.open_file()
        file.write_to_file("P2\n")
        file.write_to_file(f"{new_width} {new_height}\n")
        file.write_to_file("255\n")

        new_image = self.redimensionar(image, new_width, new_height)

        for y in range(new_height):
            linha = " ".join(map(str, new_image[y * new_width : (y + 1) * new_width]))
            file.write_to_file(f"{linha}\n")

        file.close_file()
        print(f"Image '{new_file_name}' has been created.")

    def reduce_intensity(self, image, num_bits):

        if isinstance(image, int):
            image = [image]

        new_image = []
        div_value = 2 ** (8 - num_bits)
        for row in image:
            if isinstance(row, int):
                row = [row]
            new_row = [int(int(pixel) // div_value) for pixel in row]
            new_image.append(new_row)
        return new_image
    
    def reduce_intensity_with_brightness(self, image, num_bits, brightness):

        if isinstance(image, int):
            image = [image]

        new_image = []
        div_value = 2 ** (8 - num_bits)
        for row in image:
            if isinstance(row, int):
                row = [row]
            new_row = [self.round_value(pixel / div_value, brightness) for pixel in row]
            new_image.append(new_row)
        return new_image
    
    def reduce_intensity_with_negative(self, image):

        if isinstance(image, int):
            image = [image]

        new_image = []
        for row in image:
            if isinstance(row, int):
                row = [row]
            new_row = [self.negative(pixel) for pixel in row]
            new_image.append(new_row)
        return new_image
    
    def reduce_intensity_with_bw(self, image):

        if isinstance(image, int):
            image = [image]

        new_image = []
        for row in image:
            if isinstance(row, int):
                row = [row]
            new_row = [self.to_bw_convert(pixel) for pixel in row]
            new_image.append(new_row)
        return new_image
    
    def reduce_bw_intensity_with_invertion(self, image):

        if isinstance(image, int):
            image = [image]

        new_image = []
        for row in image:
            if isinstance(row, int):
                row = [row]
            new_row = [0 if pixel == 1 else 1 for pixel in row]
            new_image.append(new_row)
        return new_image
    
    def round_value(self, value, factor):
        result = value * factor
        if result >= math.floor(result) + 0.5:
            return math.ceil(result)
        else:
            return math.floor(result)
        
    def to_bw_convert(self, value):
        return 0 if value <= 128 else 1
        
    def negative(self, value):
        limiar = 0 if value <= 128 else 1
        return self.positive(limiar - 1 - value)
    
    def positive(self, value):
        return value * -1 if value < 0 else value

    def image_to_gray_scale(self, image):

        if isinstance(image, int):
            image = [image]

        cont = 0
        pixel = 0

        new_image = []
        for row in image:
            new_row = []
            if isinstance(row, int):
                row = [row]

            for i in range(0, len(row)):
                cont += 1
                pixel += row[i]
                if (cont == 3):
                    average = self.round_value(pixel / 3, 1)                 
                    new_row.extend([average] * 3)

                    cont = 0
                    pixel = 0

            new_image.append(new_row)
            
        return new_image

    def rgb_image_with_channel(self, image, channel, isMax):

        value = 255 if isMax else 0
        idx = self.get_counter_based_on_channel(channel)
        count = 0

        if isinstance(image, int):
            image = [image]

        new_image = []
        for row in image:
            if isinstance(row, int):
                row = [row]

            new_row = []
            for pixel in row:
                if (idx == count):
                    new_row.append(value)
                    idx += 3
                else:
                    new_row.append(pixel)
                count += 1

            new_image.append(new_row)
            
        return new_image

    def get_counter_based_on_channel(self, channel):
         match channel:
            case 'R':
                return 0
            case 'G':
                return 1
            case 'B':
                return 2
            case _:
                return 0    


