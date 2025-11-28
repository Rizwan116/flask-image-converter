import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import os
import zipfile

# ===== SETTINGS =====
OUTPUT_FOLDER = "converted_images"   # Output folder for JPGs
ZIP_NAME = "all_images.zip"          # Final downloadable ZIP file


def download_and_convert_webp_to_jpg(name, url, output_path):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content)).convert("RGB")
        jpg_path = os.path.join(output_path, f"{name}.jpg")

        image.save(jpg_path, "JPEG", quality=95)
        print(f"✔ Converted: {name}.jpg")
        return True

    except Exception as e:
        print(f"✖ Failed for {name}: {e}")
        return False


def zip_folder(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                filepath = os.path.join(root, file)
                zf.write(filepath, os.path.basename(filepath))
    print(f"\n✔ ZIP created: {zip_name}")


def main():

    # ===== ASK USER FOR EXCEL FILE =====
    excel_path = input("Enter path to your Excel file (e.g. input.xlsx): ").strip()

    if not os.path.exists(excel_path):
        print("❌ File not found. Please check the file name and try again.")
        return

    # Load Excel
    df = pd.read_excel(excel_path)

    if "name" not in df.columns or "link" not in df.columns:
        print("❌ Excel must contain 'name' and 'link' columns.")
        return

    # Create output folder
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    print("\nStarting download & conversion...\n")

    for _, row in df.iterrows():
        name = str(row["name"]).strip()
        url = str(row["link"]).strip()

        download_and_convert_webp_to_jpg(name, url, OUTPUT_FOLDER)

    # Create ZIP
    zip_folder(OUTPUT_FOLDER, ZIP_NAME)
    print("\n✔ All tasks completed!")


if __name__ == "__main__":
    main()

