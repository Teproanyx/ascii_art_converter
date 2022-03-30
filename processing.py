from PIL import Image, ImageFilter
import numpy as np

MAX_LUMINANCE = 255


def ascii_conversion(img: Image.Image) -> str:
    char_set = list(r"""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """)
    data = np.array(img.getdata(), dtype='u1').reshape(img.height, img.width)

    data = np.rint(np.interp(data, [0, 255], [0, len(char_set) - 1])).astype('u1')  # round interpolated value to int
    data = np.array(char_set)[data]  # index each pixel to corresponding ascii representation

    return '\n'.join([''.join(row) for row in data])    # turn ascii matrix into a multiline string


def processing(img: str, output_name: str, options: dict) -> None:
    with Image.open(img).convert("L") as image:
        og_width, og_height = image.size
        width = int((options['-s'][0] / 100) * og_width)
        height = int((options['-s'][1] / 100) * og_height)
        image = image.resize((width, height))

        if options['-bl']:
            image = image.filter(ImageFilter.BLUR)

        with open(output_name, "w") as out:
            out.write(ascii_conversion(image))
