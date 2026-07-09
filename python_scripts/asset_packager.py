#!/usr/bin/env python3
"""
asset_packager.py

Organizes approved product assets into a production-ready delivery structure
and creates a ZIP package for distribution.

Example
-----------------------------------------------------------------------------

Input:

approved_assets/

MUG001_editorial_01.png
MUG001_editorial_02.png
MUG001_lifestyle_01.png

Result:

deliveries/
└── MUG001/
    ├── images/
    │   ├── MUG001_editorial_01.png
    │   ├── MUG001_editorial_02.png
    │   └── MUG001_lifestyle_01.png
    ├── manifest.txt
    └── MUG001.zip

How to run this script:

python asset_packager.py \
    --input ./approved_assets \
    --output ./deliveries \
    --sku MUG001
"""

from pathlib import Path
import argparse
import shutil
import zipfile
from datetime import datetime

SUPPORTED_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".tif",
    ".tiff",
}


def create_manifest(images, manifest_path, sku):
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(f"SKU: {sku}\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n")
        f.write(f"Total Assets: {len(images)}\n\n")

        f.write("Included Files:\n")

        for image in images:
            f.write(f"- {image.name}\n")


def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:

        for file in folder_path.rglob("*"):

            if file == zip_path:
                continue

            archive.write(file, arcname=file.relative_to(folder_path))


def package_assets(input_dir, output_dir, sku):

    input_dir = Path(input_dir)
    output_dir = Path(output_dir)

    if not input_dir.exists():
        raise FileNotFoundError(f"Input folder not found: {input_dir}")

    images = sorted([
        file for file in input_dir.iterdir()
        if file.suffix.lower() in SUPPORTED_EXTENSIONS
    ])

    if not images:
        print("No approved assets found.")
        return

    delivery_folder = output_dir / sku
    images_folder = delivery_folder / "images"

    images_folder.mkdir(parents=True, exist_ok=True)

    print(f"\nPackaging {len(images)} assets...\n")

    copied_files = []

    for image in images:

        destination = images_folder / image.name

        shutil.copy2(image, destination)

        copied_files.append(destination)

        print(f"✓ {image.name}")

    manifest = delivery_folder / "manifest.txt"

    create_manifest(copied_files, manifest, sku)

    zip_path = delivery_folder / f"{sku}.zip"

    zip_folder(delivery_folder, zip_path)

    print("\nPackage created successfully.")
    print(f"Folder : {delivery_folder}")
    print(f"Archive: {zip_path}")


def main():

    parser = argparse.ArgumentParser(
        description="Package approved product assets for delivery."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Folder containing approved assets."
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Delivery folder."
    )

    parser.add_argument(
        "--sku",
        required=True,
        help="Product SKU."
    )

    args = parser.parse_args()

    package_assets(
        args.input,
        args.output,
        args.sku,
    )


if __name__ == "__main__":
    main()
