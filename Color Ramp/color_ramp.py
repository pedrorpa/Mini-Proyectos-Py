from PIL import Image, ImageDraw

im = Image.new("RGB", (256, 256), "black")
width, height = im.size
draw = ImageDraw.Draw(im)
for x in range(height):
    for y in range(width):
        im.putpixel((x, y), (x, y, (x + y) // 2))

im.show()
