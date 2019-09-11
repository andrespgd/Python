# make sure destination folder does not exist!!!!

dirs_to_copy = [r'J:\Data\Folder_A', r'J:\Data\Folder_B']
destination_dir = r'J:\Data\DestinationFolder'

for files in dirs_to_copy:
    shutil.copytree(files, destination_dir, ignore=shutil.ignore_patterns('*.bin', '*.mp4'))
