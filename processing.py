from PIL import Image, ImageFilter

MAX_LUMINANCE = 255


def ascii_conversion(img: Image.Image) -> str:
    char_set = list(r"""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """)
    width, height = img.size
    data = img.getdata()

    output = []
    for i in range(width):
        for j in range(height):
            output.append(char_set[transform(data[i + j * width], MAX_LUMINANCE, len(char_set) - 1)])
        output.append('\n')
    return ''.join(output)


def transform(val: int, from_max: int, to_max: int) -> int:
    return round(val / from_max * to_max)


def processing(img: str, output_name: str, options: dict) -> None:
    image = Image.open(img).convert("L")
    og_width, og_height = image.size
    width = int((options['-s'][0] / 100) * og_width)
    height = int((options['-s'][1] / 100) * og_height)
    image.resize((width, height))

    if options['-bl']:
        image = image.filter(ImageFilter.BLUR)
