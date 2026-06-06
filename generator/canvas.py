from PIL import Image

def create_canvas(bg_color, size=(1080, 1080)):
    img = Image.new("RGBA", size, bg_color)
    return img, img.load()