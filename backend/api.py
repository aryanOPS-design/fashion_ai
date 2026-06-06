from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import os, shutil, zipfile

from generator.engine import build_carousel

app = FastAPI()

@app.get("/")
def root():
    return {"status": "alive"}

@app.post("/generate")
async def generate(
    product_name: str = Form(...),
    price: str = Form(...),
    image: UploadFile = File(...)
):

    os.makedirs("input", exist_ok=True)
    os.makedirs("output", exist_ok=True)

    image_path = f"input/{image.filename}"

    with open(image_path, "wb") as f:
        shutil.copyfileobj(image.file, f)

    content = {
        "product_name": product_name,
        "price": price,
        "image_path": image_path,
        "features": ["Premium Quality", "Streetwear Fit", "Limited Edition"],
        "uses": ["Daily Wear", "Street Style", "Outfits"]
    }

    output_folder = f"output/{product_name}"

    build_carousel(content, "streetwear", output_folder)

zip_path = f"{output_folder}.zip"

with zipfile.ZipFile(zip_path, "w") as zipf:

    for file in os.listdir(output_folder):

        file_path = os.path.join(output_folder, file)

        zipf.write(
            file_path,
            arcname=file
        )
        
    return FileResponse(
    zip_path,
    media_type="application/zip",
    filename=f"{product_name}.zip"
)
