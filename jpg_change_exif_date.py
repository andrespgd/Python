from datetime import datetime
import pathlib
import piexif
import shutil

'''
Changes the JPG EXIF created year
Uses the first 4-digit year on base folder
'''

'''
TODO:
    -using Windows Metadata++
        -select a group of images
        -change the EXIF "artist" tag to "chosica-casa-gastelumendi"
    -in Python have a dictionary of place -> lat/lon
        -click on image(s) and change EXIF location to "chosica-casa-gastelumendi"
        -have a "master" dictionary:
            "chosica-casa-gastelumendi":[-34.099888,80.008875725]
            "chosica-casa-munoznajar":  [-34.199888,80.002875725]
            "playa_ancon":  [-34.199888,80.002875725]
            "playa_miramar":  [-34.199888,80.002875725]
            "house_813phoenix":  [-34.199888,80.002875725]
            "levanto": [+20.09090,-10.0490583]
'''

p_inp = pathlib.Path(r'C:/tmp_inp/')
p_out = pathlib.Path(r'C:/tmp_out/')

folders_input = [f for f in p_inp.iterdir() if f.is_dir()]

for folder in folders_input:
    print(str(folder))
    year  = folder.parts[-1][0:4]
    month = folder.parts[-1][5:7]
    date  = folder.parts[-1][8:10]
    # create a NEW folder
    new_folder_name = str(folder.name) + '_EXIF_Date_Change'
    folder_new = pathlib.Path(p_out / new_folder_name)
    folder_new.mkdir(parents=True, exist_ok=True)
    # change the date on every JPG and put it in the NEW folder
    files_inp = [f for f in folder.iterdir() if f.is_file()]
    for file in files_inp:
        shutil.copy(file, folder_new/pathlib.Path(file).name)
    files_out = [f for f in folder_new.iterdir() if f.is_file()]
    # change date
    for file in files_out:
        exif_dict = piexif.load(str(file))
        new_date = datetime(int(year), int(month), int(date), 12, 0, 0).strftime("%Y:%m:%d %H:%M:%S")
        exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date
        exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date
        exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date
        exif_bytes = piexif.dump(exif_dict)
        piexif.insert(exif_bytes, str(file))