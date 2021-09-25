from datetime import datetime
import pathlib
import piexif

'''
Changes the JPG EXIF created year
Uses the first 4-digit year on base folder
'''

p1 = pathlib.Path(r'C:/tmpdel/')
folders = [f for f in p1.iterdir() if f.is_dir()]

for folder in folders:
    year = folder.parts[-1][0:4]
    print(year)
    files = [f for f in folder.iterdir() if f.is_file()]
    for file in files:
        exif_dict = piexif.load(str(file))
        new_date = datetime(int(year), 1, 2, 0, 0, 0).strftime("%Y:%m:%d %H:%M:%S")
        exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, str(file))