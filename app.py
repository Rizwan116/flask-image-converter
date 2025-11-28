from flask import Flask, render_template, request, send_file
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import os
import zipfile
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "converted"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def convert_webp_to_jpg(name, url, save_folder):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content)).convert("RGB")
        output_path = os.path.join(save_folder, f"{name}.jpg")
        img.save(output_path, "JPEG", quality=95)
        return output_path

    except Exception as e:
        print(f"Failed: {name} - {e}")
        return None


def convert_webp_to_png(name, url, save_folder):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content))
        output_path = os.path.join(save_folder, f"{name}.png")
        img.save(output_path, "PNG")
        return output_path

    except Exception as e:
        print(f"Failed: {name} - {e}")
        return None


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        excel_file = request.files.get("excel_file")
        format_choice = request.form.get("format_choice")

        if not excel_file:
            return "Please upload an Excel file."

        excel_path = os.path.join(UPLOAD_FOLDER, excel_file.filename)
        excel_file.save(excel_path)

        unique_folder = os.path.join(OUTPUT_FOLDER, str(uuid.uuid4()))
        os.makedirs(unique_folder, exist_ok=True)

        df = pd.read_excel(excel_path)

        if "name" not in df.columns or "link" not in df.columns:
            return "Excel must contain 'name' and 'link' columns."

        for _, row in df.iterrows():
            name = str(row["name"]).strip()
            url = str(row["link"]).strip()

            if format_choice == "jpg":
                convert_webp_to_jpg(name, url, unique_folder)

            elif format_choice == "png":
                convert_webp_to_png(name, url, unique_folder)

        zip_filename = unique_folder + ".zip"
        with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in os.listdir(unique_folder):
                zipf.write(os.path.join(unique_folder, file), file)

        return send_file(zip_filename, as_attachment=True)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
