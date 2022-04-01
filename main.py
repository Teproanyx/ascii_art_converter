from sys import argv
from processing import processing
import re
from os.path import splitext

option = dict.fromkeys(['-e', '-b'], False)
option['-s'] = (100, 100)


def print_help() -> None:
    print("""Usage: py.exe main.py [options] <input_file> <output_filename>
          Options:
          -s<a>x<b> ->  Resize image to <a>% width and <b>% height
          -e        ->  Edge Processing
          -b       ->  Blur""")


def option_processing() -> None:
    for i in argv[1:]:  # option processing
        if i.startswith('-s'):  # size option
            capture = re.match(r'-s(\d+)x(\d+)', i)
            if capture:
                option['-s'] = (int(capture.group(1)), int(capture.group(2)))
        elif i in option:
            option[i] = True  # other options
        elif not i.startswith('-'):
            break


def absolute_bs() -> None:
    quote = '\"\''
    image = argv[-2].strip(quote)
    output = argv[-1]
    with open(splitext(output)[0] + '.txt', "w") as out:
        out.write(processing(image, option))


if __name__ == "__main__":
    if "-h" in argv:  # help
        print_help()
        quit()

    option_processing()

    absolute_bs()
