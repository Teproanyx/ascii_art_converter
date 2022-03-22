from sys import argv

option = dict.fromkeys(['-e', '-s', '-nb', '-bl'], False)
minimize_size = (1, 1)


def print_help():
    pass


def processing(input_name, output_name):
    pass


if __name__ == "__main__":
    if "-h" in argv:  # help
        print_help()
        quit()

    for i in argv:  # option processing
        if i[0] == '-':
            if i.startswith('-m'):  # minimize option -- example: '-m4x4'
                minimize_size = (i[2], i[4])
            elif i in option:
                option[i] = True    # other options
        else:
            break

    if "-b" not in argv:  # one image
        image = argv[-2]
        output = argv[-1]
        processing(image, output)

    else:  # batch
        app = argv[-1]  # appended text at the end of each files
        for i in reversed(argv[:-1]):
            if i[0] != '-':
                processing(i, f'{i}_{app}')
            else:
                break

# input
# maratt mek egirl
#
# output
# maratt_egirl mek_egirl
