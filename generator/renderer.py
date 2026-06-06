import os
from PIL import Image, ImageFont, ImageDraw

try:
    from rembg import remove
    REMBG_AVAILABLE = True
except:
    REMBG_AVAILABLE = False


# =========================
# CANVAS
# =========================
def create_canvas(bg):
    return Image.new("RGBA", (1080, 1080), bg)


# =========================
# TEXT CENTER
# =========================
def center_text(draw, text, font, y, fill="white"):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    x = (1080 - w) // 2
    draw.text((x, y), text, font=font, fill=fill)


# =========================
# SAVE IMAGE
# =========================
def save(img, path):
    img.convert("RGB").save(path, "JPEG", quality=95)


# =========================
# LOAD PRODUCT IMAGE
# =========================
def load_image(path, size=(520, 520)):
    img = Image.open(path).convert("RGBA")

    if REMBG_AVAILABLE:
        try:
            img = remove(img)
        except:
            pass

    img.thumbnail(size)
    return img


# =========================
# SAFE LAYOUT HANDLER
# =========================
def get_layout(theme):
    return theme.get("layout", "right_image")


def get_position(layout):
    if layout == "left_image":
        return 80, 260
    if layout == "center_image":
        return 280, 260
    return 620, 260


# =========================
# SLIDE 1 (HERO)
# =========================
def slide_1(content, theme, output_path):

    img = create_canvas(theme["bg"])
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype("assets/fonts/Poppins-Bold.ttf", 78)
    body_font = ImageFont.truetype("assets/fonts/Poppins-Bold.ttf", 38)

    layout = get_layout(theme)

    pad = 60 if layout != "luxury" else 90
    radius = 80 if layout == "luxury" else 60

    # main card
    draw.rounded_rectangle(
        (pad, pad, 1080 - pad, 1080 - pad),
        radius=radius,
        fill=theme["card"]
    )

    # text block
    draw.text((110, 140), content["product_name"].upper(), font=title_font, fill=theme["text"])
    draw.text((110, 260), str(content["price"]), font=body_font, fill=theme["accent"])
    draw.text((110, 340), "PREMIUM DROP", font=body_font, fill=theme["muted"])

    # CTA
    draw.rounded_rectangle((110, 820, 420, 900), radius=40, fill="white")
    draw.text((170, 845), "SHOP NOW", font=body_font, fill="black")

    # product image
    try:
        product = load_image(content["image_path"])
        x, y = get_position(layout)

        # shadow
        shadow = Image.new("RGBA", product.size, (0, 0, 0, 110))
        img.paste(shadow, (x + 15, y + 20), shadow)

        img.paste(product, (x, y), product)

    except Exception as e:
        print("Slide 1 image error:", e)

    save(img, output_path)


# =========================
# SLIDE 2 (FEATURES)
# =========================
def slide_2(content, theme, output_path):

    img = create_canvas(theme["bg"])
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("assets/fonts/Poppins-Bold.ttf", 52)

    center_text(draw, "FEATURES", font, 80, fill=theme["text"])

    y = 220
    for f in content.get("features", []):
        draw.rounded_rectangle((120, y, 960, y + 110), radius=30, fill=theme["card"])
        draw.text((160, y + 35), f, font=font, fill=theme["text"])
        y += 150

    save(img, output_path)


# =========================
# SLIDE 3 (USES)
# =========================
def slide_3(content, theme, output_path):

    img = create_canvas(theme["bg"])
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("assets/fonts/Poppins-Bold.ttf", 52)

    center_text(draw, "PERFECT FOR", font, 80, fill=theme["text"])

    y = 220
    for u in content.get("uses", []):
        draw.rounded_rectangle((120, y, 960, y + 110), radius=30, fill=theme["card"])
        draw.text((160, y + 35), u, font=font, fill=theme["text"])
        y += 150

    save(img, output_path)


# =========================
# SLIDE 4 (CTA)
# =========================
def slide_4(content, theme, output_path):

    img = create_canvas(theme["bg"])
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("assets/fonts/Poppins-Bold.ttf", 68)

    draw.rounded_rectangle((80, 200, 1000, 900), radius=80, fill=theme["card"])

    center_text(draw, "LIMITED DROP", font, 320, fill=theme["text"])
    center_text(draw, "DON'T MISS OUT", font, 420, fill=theme["muted"])

    draw.rounded_rectangle((280, 620, 800, 740), radius=50, fill=theme["accent"])
    center_text(draw, "BUY NOW", font, 650, fill="white")

    save(img, output_path)


# =========================
# SLIDE 5 (END)
# =========================
def slide_5(content, theme, output_path):

    img = create_canvas(theme["bg"])
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("assets/fonts/Poppins-Bold.ttf", 64)

    center_text(draw, "THANK YOU", font, 420, fill=theme["text"])
    center_text(draw, "FOR SHOPPING WITH US", font, 520, fill=theme["muted"])

    save(img, output_path)


# =========================
# BUILDER
# =========================
def build_carousel(content, theme, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    slide_1(content, theme, f"{output_folder}/slide_1.jpg")
    slide_2(content, theme, f"{output_folder}/slide_2.jpg")
    slide_3(content, theme, f"{output_folder}/slide_3.jpg")
    slide_4(content, theme, f"{output_folder}/slide_4.jpg")
    slide_5(content, theme, f"{output_folder}/slide_5.jpg")