import os
import shutil
import ctypes

# Notes:how to create folder/browser dialog
# import tkinter.filedialog
# tkinter.filedialog.askdirectory(EXPAND_END_PATH)


# Set variables
END_PATH = '~'
EXPAND_END_PATH = os.path.expanduser(END_PATH)
DOWNLOAD_PATH = os.path.join(EXPAND_END_PATH, 'Downloads')

FOLDER_EXT_PATHS = dict(mp3=os.path.join(EXPAND_END_PATH, 'Music'),
                        png=os.path.join(EXPAND_END_PATH, 'OneDrive', 'Pictures'),
                        pdf=os.path.join(EXPAND_END_PATH, 'OneDrive', 'Documents'),
                        docx=os.path.join(EXPAND_END_PATH, 'OneDrive', 'Documents'),
                        doc=os.path.join(EXPAND_END_PATH, 'OneDrive', 'Documents'),
                        jpeg=os.path.join(EXPAND_END_PATH, 'OneDrive', 'Pictures'),
                        jpg=os.path.join(EXPAND_END_PATH, 'OneDrive', 'Pictures'),
                        mp4=os.path.join(EXPAND_END_PATH, 'Videos'),
                        mov=os.path.join(EXPAND_END_PATH, 'Videos'),
                        exe=os.path.join(EXPAND_END_PATH, 'Downloads', 'Apps'),
                        jar=os.path.join(EXPAND_END_PATH, 'Downloads', 'Apps'),
                        msi=os.path.join(EXPAND_END_PATH, 'Downloads', 'Apps'),
                        ppt=os.path.join(EXPAND_END_PATH, 'OneDrive', 'Documents'),
                        zip=os.path.join(EXPAND_END_PATH, 'Downloads'),
                        rar=os.path.join(EXPAND_END_PATH, 'Downloads'),
                        txt=os.path.join(EXPAND_END_PATH, 'OneDrive', 'Documents'),
                        gif=os.path.join(EXPAND_END_PATH, 'OneDrive', 'Pictures'),
                        m4a=os.path.join(EXPAND_END_PATH, 'Music'))


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

    Mbox('File Arranger', 'Your file are being sorted, check the "This PC" folder.', 0)


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


if __name__ == '__main__':
    public_arranger()
