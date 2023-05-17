import os
import shutil
import tkinter
from tkinter import messagebox

# Notes:how to create folder/browser dialog
# import tkinter.filedialog
# tkinter.filedialog.askdirectory(EXPAND_END_PATH)


# Set variables
END_PATH = '~'
EXPAND_END_PATH = os.path.expanduser(END_PATH)
DOWNLOAD_PATH = os.path.join(EXPAND_END_PATH, 'Downloads')

FOLDER_EXT_PATHS = dict(mp3=os.path.join(EXPAND_END_PATH, 'Downloads', 'Music'),
                        png=os.path.join(EXPAND_END_PATH, 'Downloads', 'Pictures'),
                        pdf=os.path.join(EXPAND_END_PATH, 'Downloads', 'PDF_EPUB'),
                        docx=os.path.join(EXPAND_END_PATH, 'Documents'),
                        doc=os.path.join(EXPAND_END_PATH, 'Downloads', 'Documents'),
                        jpeg=os.path.join(EXPAND_END_PATH, 'Downloads', 'Pictures'),
                        jpg=os.path.join(EXPAND_END_PATH, 'Downloads', 'Pictures'),
                        mp4=os.path.join(EXPAND_END_PATH, 'Downloads', 'Videos'),
                        mov=os.path.join(EXPAND_END_PATH, 'Downloads', 'Videos'),
                        exe=os.path.join(EXPAND_END_PATH, 'Downloads'),
                        jar=os.path.join(EXPAND_END_PATH, 'Downloads'),
                        msi=os.path.join(EXPAND_END_PATH, 'Downloads'),
                        ppt=os.path.join(EXPAND_END_PATH, 'Documents'),
                        zip=os.path.join(EXPAND_END_PATH, 'Downloads', 'Zips'),
                        rar=os.path.join(EXPAND_END_PATH, 'Downloads'),
                        txt=os.path.join(EXPAND_END_PATH, 'Documents'),
                        gif=os.path.join(EXPAND_END_PATH, 'Downloads', 'Pictures'),
                        heic=os.path.join(EXPAND_END_PATH, 'Downloads', 'Pictures'),
                        webp=os.path.join(EXPAND_END_PATH, 'Downloads', 'Pictures'),
                        epub=os.path.join(EXPAND_END_PATH, 'Downloads', 'PDF/EPUB'),
                        dmg=os.path.join(EXPAND_END_PATH, 'Downloads', 'DMGs'),
                        apk=os.path.join(EXPAND_END_PATH, 'Downloads', 'APKs'),
                        xapk=os.path.join(EXPAND_END_PATH, 'Downloads', 'APKs'),
                        m4a=os.path.join(EXPAND_END_PATH, 'Downloads', 'Music'))


def public_arranger():
    ext_list = []
    # If the file is not already inside of the new folders, put it there
    file_list = os.listdir(DOWNLOAD_PATH)

    for file in file_list:
        if not len(file.split('.')) == 2:
            continue

        new_ext = file.split('.')[-1]
        if new_ext in FOLDER_EXT_PATHS:
            if not os.path.exists(FOLDER_EXT_PATHS[new_ext]):
                os.makedirs(FOLDER_EXT_PATHS[new_ext])
        ext = str(file.lower()).split('.')[-1]
        if ext in FOLDER_EXT_PATHS:
            path = os.path.join(FOLDER_EXT_PATHS[ext])
            if os.path.exists(path):
                print(path)

            source = os.path.join(DOWNLOAD_PATH, file)
            destination = os.path.join(FOLDER_EXT_PATHS[ext], file)

            shutil.move(source, destination)

# Displays desktop message alerting user that files have been moved
messagebox.showinfo("File Arranger", "Your file are being sorted, check the Downloads folder.",)

if __name__ == '__main__':
    public_arranger()
