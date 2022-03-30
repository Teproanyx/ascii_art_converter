from PIL import Image, ImageFilter
import numpy as np

MAX_LUMINANCE = 255


def ascii_conversion(img: Image.Image) -> str:
    char_set = list(r"""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """)
    data = np.array(img.getdata(), dtype='u1').reshape(img.height, img.width)

    output = []
    for row in data:
        temp = []
        for index in row:
            temp.append(char_set[transform(index, MAX_LUMINANCE, len(char_set) - 1)])
        output.append(''.join(temp))
    return '\n'.join(output)


def transform(val: int, from_max: int, to_max: int) -> int:
    return round(val / from_max * to_max)


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
