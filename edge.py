from PIL import Image, ImageFilter
import math


def sobel_filters(image):
    width, height = image.size
    theta = Image.new(mode="L", size=(width, height))
    g = Image.new(mode="L", size=(width, height))

    x_sobel = image.filter(ImageFilter.Kernel((3, 3), (-1, 0, 1, -2, 0, 2, -1, 0, 1), 1, 0))
    y_sobel = image.filter(ImageFilter.Kernel((3, 3), (1, 2, 1, 0, 0, 0, -1, -2, -1), 1, 0))

    x_squared = x_sobel.point(lambda x: x ** 2)
    y_squared = y_sobel.point(lambda x: x ** 2)

    for i in range(width):
        for j in range(height):
            g.putpixel((i, j), int(math.sqrt(x_squared.load()[i, j] + y_squared.load()[i, j])))
            theta.putpixel((i, j), int((math.atan2(x_sobel.load()[i, j], y_sobel.load()[i, j])) * 180 / math.pi))

    return g, theta


def non_max_suppression(image):
    pass
