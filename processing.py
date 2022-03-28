from PIL import Image, ImageFilter


def processing(img: str, output_name: str, options: dict) -> None:
    image = Image.open(img).convert("L")
    og_width, og_height = image.size
    width = int((options['-s'][0] / 100) * og_width)
    height = int((options['-s'][1] / 100) * og_height)
    image.resize((width, height))

    if options['-bl']:
        image = image.filter(ImageFilter.BLUR)
