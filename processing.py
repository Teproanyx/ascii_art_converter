from PIL import Image, ImageFilter
import numpy as np
from edge import *

MAX_LUMINANCE = 255


def ascii_conversion(img: Image.Image) -> str:
    char_set = list(r"""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """)
    data = np.array(img.getdata(), dtype='u1').reshape(img.height, img.width)

    # round interpolated value to int
    data = np.rint(np.interp(data, [0, MAX_LUMINANCE], [0, len(char_set) - 1])).astype('u1')
    data = np.array(char_set)[data]  # index each pixel to corresponding ascii representation

    return '\n'.join([''.join(row) for row in data])    # turn ascii matrix into a multiline string


def processing(img: str, options: dict) -> str:
    with Image.open(img).convert("L") as image:
        og_width, og_height = image.size
        width = int((options['-s'][0] / 100) * og_width)
        height = int((options['-s'][1] / 100) * og_height)
        image = image.resize((width, height))

        if options['-bl']:
            image = image.filter(ImageFilter.BLUR)

        if options['-e']:
            g, gmax = laplacian(image)
            g, weak, strong = threshold(g, gmax, lowThresholdRatio=0.25, highThresholdRatio=0.08)
            image = hysteresis(g, weak, strong=255)

        return ascii_conversion(image)


