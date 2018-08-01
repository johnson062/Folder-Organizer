from os import listdir, mkdir
from os.path import isfile, join, splitext, isdir
from shutil import move

DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  ".pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    # "PYTHON": [".py"],
    "XML": [".xml"],
    "SHELL": [".sh"],
    "APP": [".lnk"],
    "INSTALLER": [".msi", ".exe"]

}
FILE_FORMATS = {file_format: directory
                for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}


files = []
dirs = []
for f in listdir("."):
    if isfile(f):
        files.append(f)
    elif isdir(f):
        dirs.append(f)

# Check and Create folders
for folder in DIRECTORIES.keys():
    try:
        sentence = f'{folder} created'
        mkdir(folder)
        print(sentence)
    except:
        sentence = f'{folder} is already existed'
        print(sentence)


for f in files:
    filename, file_ext = splitext(f)
    try:
        move(f, FILE_FORMATS[file_ext.lower()])
    except:
        print("some errors")
