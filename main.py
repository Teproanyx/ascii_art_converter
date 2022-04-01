from sys import argv
from processing import processing
import re
from os.path import splitext

option = dict.fromkeys(['-e', '-bl'], False)
option['-s'] = (100, 100)


def print_help() -> None:
    pass


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


def absolute_bs():
    quote = '\"\''
    image = argv[-2].strip(quote)
    output = argv[-1]
    with open(output, "w") as out:
        out.write(processing(image, option))


if __name__ == "__main__":
    if "-h" in argv:  # help
        print_help()
        quit()

    option_processing()

    absolute_bs()
