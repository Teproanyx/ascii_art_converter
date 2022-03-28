from sys import argv
from processing import processing
import re
from os.path import splitext

option = dict.fromkeys(['-e', '-sa', '-nb', '-bl'], False)
option['-s'] = (100, 100)


def print_help():
    pass


if __name__ == "__main__":
    if "-h" in argv:  # help
        print_help()
        quit()

    for index in argv:  # option processing
        if index[0] == '-':
            if index.startswith('-s'):  # size option
                capture = re.match(r'-s(\d+)x(\d+)', index)
                if capture:
                    option['-s'] = (capture.group(1), capture.group(2))
            elif index in option:
                option[index] = True  # other options
        else:
            break

    quote = '\"\''
    if "-b" not in argv:  # one image
        image = argv[-2].strip(quote)
        output = argv[-1]
        processing(image, splitext(output)[0] + '.txt', option)
    else:  # batch
        app = argv[-1]  # appended text at the end of each files
        for index in reversed(argv[:-1]):
            if index[0] != '-':
                image = index.strip(quote)
                processing(image, f'{splitext(image)[0]}_{app}.txt', option)
            else:
                break
