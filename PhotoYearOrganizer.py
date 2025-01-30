import os
import shutil
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
from PIL.ExifTags import TAGS
from icecream import ic
import time

# Function to extract the year from the photo's metadata
def get_photo_year(photo_path):
    try:
        image = Image.open(photo_path)
        exif_data = image._getexif()
        if exif_data:
            for tag, value in exif_data.items():
                if TAGS.get(tag) == 'DateTimeOriginal':
                    year = datetime.strptime(value, '%Y:%m:%d %H:%M:%S').year
                    return str(year)
        # If no metadata is found, use file's modification year as fallback
        return str(datetime.fromtimestamp(os.path.getmtime(photo_path)).year)
    except Exception as e:
        ic(f"Error processing {os.path.normpath(photo_path)}: {e}")
        return None

# Function to cache photo years
def cache_photo_year(photo_path):
    photo_path = os.path.normpath(photo_path)
    year = get_photo_year(photo_path)
    return photo_path, year

# Function to measure and print the elapsed time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken for {func.__name__}: {end_time - start_time:.2f} seconds")
        return result
    return wrapper

@measure_time
# Main function
def sort_photos(base_path):
    base_path = os.path.normpath(base_path)
    if not os.path.isdir(base_path):
        print(f"Invalid folder path: {base_path}")
        return

    photos = [os.path.normpath(os.path.join(base_path, f)) for f in os.listdir(base_path) if f.lower().endswith('.jpg')]
    if not photos:
        print("No JPG photos found in the folder.")
        return

    max_threads = os.cpu_count() // 2

    # Phase 1: Cache photo years
    print("Extracting metadata...")
    cached_data = []
    with ThreadPoolExecutor(max_threads) as executor:
        cached_data = list(executor.map(cache_photo_year, photos))

    # Phase 2: Move photos
    print("Moving photos...")
    for photo_path, year in cached_data:
        if year:
            year_folder = os.path.join(base_path, year)
            if not os.path.exists(year_folder):
                os.makedirs(year_folder)
            try:
                shutil.move(photo_path, os.path.join(year_folder, os.path.basename(photo_path)))
            except Exception as e:
                ic(f"Error moving {photo_path}: {e}")

    print("Photo sorting completed.")

if __name__ == "__main__":
    folder_path = input("Enter the folder path to sort photos: ").strip()
    sort_photos(folder_path)
