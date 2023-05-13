import argparse
from os.path import splitext

from PIL import Image, ImageDraw, ImageFont


def drawsize(filename):
    img = Image.open(filename)

    height, width = img.size
    text = f"{height}x{width}"

    font_type = "font/Rockinline.ttf"
    IMAGE_STAMPED = "-stamped"
    FONT_SIZE = 12
    margen_x = 10
    margen_y = 10

    img = Image.open(filename)
    height, width = img.size

    draw = ImageDraw.Draw(img, "RGBA")
    font = ImageFont.truetype(font_type, size=FONT_SIZE)

    text_box = draw.textbbox((0, 0), text, font=font)
    position = (
        height - text_box[2] - margen_x,
        width - text_box[3] - margen_y,
    )
    draw.text(
        (position),
        text,
        font=font,
        fill="white",
    )

    filename_split = splitext(filename)
    filename_stamped = f"{filename_split[0]}{IMAGE_STAMPED}{filename_split[1]}"
    print(filename_stamped)
    img.save(filename_stamped)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Imagen a calcular tamaño")

    options = parser.parse_args()
    drawsize(options.filename)
