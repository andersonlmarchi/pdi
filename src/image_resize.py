import image_manipulator as im

image = im.ImageManipulator("/images/process/EntradaEscalaCinza.pgm")
new_image = image.read_image()

# write new image on 80x80 resolution
image.write_new_image(new_image, "/images/process/EntradaEscalaCinza80x80.pgm", 80, 80)

# write new image on 480x320 resolution
image.write_new_image(new_image, "/images/process/EntradaEscalaCinza480x320.pgm", 480, 320)

# write new image on 720p resolution
image.write_new_image(new_image, "/images/process/EntradaEscalaCinzaHD.pgm", 1280, 720)

# write new image on 1080p resolution
image.write_new_image(new_image, "/images/process/EntradaEscalaCinzaFullHD.pgm", 1920, 1080)

# write new image on 4k resolution
image.write_new_image(new_image, "/images/process/EntradaEscalaCinza4k.pgm", 3840, 2160)

# write new image on 8k resolution
image.write_new_image(new_image, "/images/process/EntradaEscalaCinza8k.pgm", 7680, 4320)