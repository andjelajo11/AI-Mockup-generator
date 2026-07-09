#!/usr/bin/env python3
"""
batch_rename.py

Rename generated product mockups into a consistent production naming convention.

Example:

Output folder before running this script:

outputs/

2a8d91.png
abc91.png
output.png

After running this script:

outputs/

MUG001_editorial_01.png
MUG001_editorial_02.png
MUG001_editorial_03.png

How to run :
python batch_rename.py \
    --input ./outputs \
    --sku MUG001 \
    --style editorial
"""

from pathlib import Path
import argparse
import sys

SUPPORTED_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".tif",
    ".tiff"
}


def rename_images(input_folder: Path, sku: str, style: str):

    if not input_folder.exists():
        print(f"Folder not found: {input_folder}")
        sys.exit(1)

    images = sorted([
        file for file in input_folder.iterdir()
        if file.suffix.lower() in SUPPORTED_EXTENSIONS
    ])

    if not images:
        print("No images found.")
        return

    print(f"\nFound {len(images)} image(s)\n")

    for index, image in enumerate(images, start=1):

        new_name = f"{sku}_{style}_{index:02d}{image.suffix.lower()}"

        destination = image.with_name(new_name)

        if destination.exists():
            print(f"Skipping (already exists): {destination.name}")
            continue

        image.rename(destination)

        print(f"{image.name}")
        print(f"   → {destination.name}")

    print("\nDone.")


def main():

    parser = argparse.ArgumentParser(
        description="Batch rename generated product mockups."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Folder containing generated images."
    )

    parser.add_argument(
        "--sku",
        required=True,
        help="Product SKU or identifier."
    )

    parser.add_argument(
        "--style",
        default="mockup",
        help="Style name (editorial, cinematic, lifestyle, etc.)."
    )

    args = parser.parse_args()

    rename_images(
        Path(args.input),
        args.sku,
        args.style
    )


if __name__ == "__main__":
    main()
