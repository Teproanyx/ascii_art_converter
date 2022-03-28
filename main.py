from sys import argv
import processing
import re

option = dict.fromkeys(['-e', '-sa', '-nb', '-bl'], False)
option['-s'] = (100, 100)


def print_help():
    pass


if __name__ == "__main__":
    if "-h" in argv:  # help
        print_help()
        quit()

    for i in argv:  # option processing
        if i[0] == '-':
            if i.startswith('-s'):  # size option
                capture = re.match(r'-s(\d+)x(\d+)', i)
                if capture:
                    option['-s'] = (capture.group(1), capture.group(2))
            elif i in option:
                option[i] = True    # other options
        else:
            break

    if "-b" not in argv:  # one image
        image = argv[-2]
        output = argv[-1]
        processing(image, output, option)

    else:  # batch
        app = argv[-1]  # appended text at the end of each files
        for i in reversed(argv[:-1]):
            if i[0] != '-':
                processing(i, f'{i}_{app}', option)
            else:
                break
