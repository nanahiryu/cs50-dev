from PIL import Image, ImageFilter

before = Image.open("img/yard.bmp")
after = before.filter(ImageFilter.BoxBlur(1))
after.save("img/out.bmp")
