# Photo Sorter

A Python script to automatically sort JPEG photos into folders based on their year of capture, extracted from metadata. If no metadata is found, the file's modification year is used as a fallback.

## Features

- Extracts **DateTimeOriginal** metadata from photos.
- Uses the **modification date** as a fallback when metadata is unavailable.
- Sorts photos into **year-based folders**.
- Uses **multithreading** for faster processing.
- Displays **execution time** for performance tracking.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `Pillow`
  - `icecream`

## Installation

1. Clone or download this repository.
2. Install dependencies using:

   ```bash
   pip install Pillow icecream
   ```

## Usage

1. Run the script:

   ```bash
   python PhotoYearOrganizer.py
   ```

2. Enter the folder path containing the photos when prompted.

## How It Works

1. **Extracting Metadata**  
   - Reads the **DateTimeOriginal** tag from EXIF data.
   - If unavailable, falls back to the file's last modification year.

2. **Sorting Photos**  
   - Creates folders based on the year.
   - Moves photos into respective **year-based** folders.

3. **Performance Optimization**  
   - Uses a **ThreadPoolExecutor** to extract metadata faster.
   - **Prints execution time** for each run.

## Example

### Before Sorting
```
/photos
 ├── image1.jpg
 ├── image2.jpg
 ├── image3.jpg
```

### After Sorting
```
/photos
 ├── 2022
 │   ├── image1.jpg
 ├── 2023
 │   ├── image2.jpg
 │   ├── image3.jpg
```

## Notes

- This script **only processes `.jpg` files**.
- Any errors while reading metadata or moving files are logged.

## License

This project is licensed under the MIT License.
