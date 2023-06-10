import os
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory

# prompt user for folders
Tk().withdraw()
jfif_folder = askdirectory(title='Select folder with jfif images:')
jpg_folder = askdirectory(title='Select folder to save converted jpg images:')

# check if folders exist, else create them
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# loop through all files in the jfif folder
for file_name in os.listdir(jfif_folder):
    if file_name.endswith('.jfif') or file_name.endswith('.JFIF'):
        # open jfif image and convert to jpg
        jfif_file_path = os.path.join(jfif_folder, file_name)
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)
        jfif_image = Image.open(jfif_file_path)

        # save jpg image with maximum quality
        jfif_image.save(jpg_file_path, 'JPEG', quality=100)

print(f'All jfif images in {jfif_folder} converted to jpg and saved in {jpg_folder}.')

#softy_plug