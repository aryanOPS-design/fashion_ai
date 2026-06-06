from generator.engine import build_carousel

print("Carousel Generator Started")

product_name = input("Product Name: ")
price = input("Price: ")
image_path = input("Product Image Path:")

template_name = "minimal"

content = {
    "product_name": product_name,
    "price": price,
    "image_path": image_path,
    "features": ["Premium Quality", "Streetwear Fit", "Limited Edition"],
    "uses": ["Casual Wear", "Street Style", "Daily Outfit"]
}

output_folder = f"output/{product_name}"

build_carousel(content, template_name, output_folder)