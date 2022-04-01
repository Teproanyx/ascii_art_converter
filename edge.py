from PIL import ImageFilter


def laplacian(image):
    width, height = image.size
    gmax = 0
    g = image.filter(ImageFilter.FIND_EDGES)

    for i in range(width):
        for j in range(height):
            if g.load()[i, j] > gmax:
                gmax = g.load()[i, j]

    for i in range(width):
        for j in range(height):
            g.putpixel((i, j), int((g.load()[i, j] * 255) / gmax))

    return g, gmax


def threshold(g, gmax, lowThresholdRatio=0.25, highThresholdRatio=0.08):
    width, height = g.size
    highThreshold = gmax * highThresholdRatio
    lowThreshold = highThreshold * lowThresholdRatio
    weak = 25
    strong = 255
    for i in range(width):
        for j in range(height):
            if g.load()[i, j] > highThreshold:
                g.load()[i, j] = strong
            elif (g.load()[i, j] >= lowThreshold) and (g.load()[i, j] <= highThreshold):
                g.load()[i, j] = weak
            else:
                g.load()[i, j] = 0

    return g, weak, strong


def hysteresis(image, weak, strong=255):
    width, height = image.size
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            if image.load()[i, j] == weak:
                if ((image.load()[i + 1, j - 1] == strong) or (image.load()[i + 1, j] == strong) or (
                        image.load()[i + 1, j + 1] == strong)
                        or (image.load()[i, j - 1] == strong) or (image.load()[i, j + 1] == strong)
                        or (image.load()[i - 1, j - 1] == strong) or (image.load()[i - 1, j] == strong) or (
                                image.load()[i - 1, j + 1] == strong)):
                    image.load()[i, j] = strong
                else:
                    image.load()[i, j] = 0

    return image
