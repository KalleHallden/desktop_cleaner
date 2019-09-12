from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'kalle':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)

extensions_folders = {
#No name
    'noname' : "/Users/kalle/Desktop/kalle/Other/Uncategorized",
#Audio
    '.aif' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.cda' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.mid' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.midi' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.mp3' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.mpa' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.ogg' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.wav' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.wma' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.wpl' : "/Users/kalle/Desktop/kalle/Media/Audio",
    '.m3u' : "/Users/kalle/Desktop/kalle/Media/Audio",
#Text
    '.txt' : "/Users/kalle/Desktop/kalle/Text/TextFiles",
    '.doc' : "/Users/kalle/Desktop/kalle/Text/Microsoft/Word",
    '.docx' : "/Users/kalle/Desktop/kalle/Text/Microsoft/Word",
    '.odt ' : "/Users/kalle/Desktop/kalle/Text/TextFiles",
    '.pdf': "/Users/kalle/Desktop/kalle/Text/PDF",
    '.rtf': "/Users/kalle/Desktop/kalle/Text/TextFiles",
    '.tex': "/Users/kalle/Desktop/kalle/Text/TextFiles",
    '.wks ': "/Users/kalle/Desktop/kalle/Text/TextFiles",
    '.wps': "/Users/kalle/Desktop/kalle/Text/TextFiles",
    '.wpd': "/Users/kalle/Desktop/kalle/Text/TextFiles",
#Video
    '.3g2': "/Users/kalle/Desktop/kalle/Media/Video",
    '.3gp': "/Users/kalle/Desktop/kalle/Media/Video",
    '.avi': "/Users/kalle/Desktop/kalle/Media/Video",
    '.flv': "/Users/kalle/Desktop/kalle/Media/Video",
    '.h264': "/Users/kalle/Desktop/kalle/Media/Video",
    '.m4v': "/Users/kalle/Desktop/kalle/Media/Video",
    '.mkv': "/Users/kalle/Desktop/kalle/Media/Video",
    '.mov': "/Users/kalle/Desktop/kalle/Media/Video",
    '.mp4': "/Users/kalle/Desktop/kalle/Media/Video",
    '.mpg': "/Users/kalle/Desktop/kalle/Media/Video",
    '.mpeg': "/Users/kalle/Desktop/kalle/Media/Video",
    '.rm': "/Users/kalle/Desktop/kalle/Media/Video",
    '.swf': "/Users/kalle/Desktop/kalle/Media/Video",
    '.vob': "/Users/kalle/Desktop/kalle/Media/Video",
    '.wmv': "/Users/kalle/Desktop/kalle/Media/Video",
#Images
    '.ai': "/Users/kalle/Desktop/kalle/Media/Images",
    '.bmp': "/Users/kalle/Desktop/kalle/Media/Images",
    '.gif': "/Users/kalle/Desktop/kalle/Media/Images",
    '.ico': "/Users/kalle/Desktop/kalle/Media/Images",
    '.jpg': "/Users/kalle/Desktop/kalle/Media/Images",
    '.jpeg': "/Users/kalle/Desktop/kalle/Media/Images",
    '.png': "/Users/kalle/Desktop/kalle/Media/Images",
    '.ps': "/Users/kalle/Desktop/kalle/Media/Images",
    '.psd': "/Users/kalle/Desktop/kalle/Media/Images",
    '.svg': "/Users/kalle/Desktop/kalle/Media/Images",
    '.tif': "/Users/kalle/Desktop/kalle/Media/Images",
    '.tiff': "/Users/kalle/Desktop/kalle/Media/Images",
#Internet
    '.asp': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.aspx': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.cer': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.cfm': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.cgi': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.pl': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.css': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.htm': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.js': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.jsp': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.part': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.php': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.rss': "/Users/kalle/Desktop/kalle/Other/Internet",
    '.xhtml': "/Users/kalle/Desktop/kalle/Other/Internet",
#Compressed
    '.7z': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.arj': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.deb': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.pkg': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.rar': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.rpm': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.tar.gz': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.z': "/Users/kalle/Desktop/kalle/Other/Compressed",
    '.zip': "/Users/kalle/Desktop/kalle/Other/Compressed",
#Disc
    '.bin': "/Users/kalle/Desktop/kalle/Other/Disc",
    '.dmg': "/Users/kalle/Desktop/kalle/Other/Disc",
    '.iso': "/Users/kalle/Desktop/kalle/Other/Disc",
    '.toast': "/Users/kalle/Desktop/kalle/Other/Disc",
    '.vcd': "/Users/kalle/Desktop/kalle/Other/Disc",
#Data
    '.csv': "/Users/kalle/Desktop/kalle/Programming/Database",
    '.dat': "/Users/kalle/Desktop/kalle/Programming/Database",
    '.db': "/Users/kalle/Desktop/kalle/Programming/Database",
    '.dbf': "/Users/kalle/Desktop/kalle/Programming/Database",
    '.log': "/Users/kalle/Desktop/kalle/Programming/Database",
    '.mdb': "/Users/kalle/Desktop/kalle/Programming/Database",
    '.sav': "/Users/kalle/Desktop/kalle/Programming/Database",
    '.sql': "/Users/kalle/Desktop/kalle/Programming/Database",
    '.tar': "/Users/kalle/Desktop/kalle/Programming/Database",
    '.xml': "/Users/kalle/Desktop/kalle/Programming/Database",
    '.json': "/Users/kalle/Desktop/kalle/Programming/Database",
#Executables
    '.apk': "/Users/kalle/Desktop/kalle/Other/Executables",
    '.bat': "/Users/kalle/Desktop/kalle/Other/Executables",
    '.com': "/Users/kalle/Desktop/kalle/Other/Executables",
    '.exe': "/Users/kalle/Desktop/kalle/Other/Executables",
    '.gadget': "/Users/kalle/Desktop/kalle/Other/Executables",
    '.jar': "/Users/kalle/Desktop/kalle/Other/Executables",
    '.wsf': "/Users/kalle/Desktop/kalle/Other/Executables",
#Fonts
    '.fnt': "/Users/kalle/Desktop/kalle/Other/Fonts",
    '.fon': "/Users/kalle/Desktop/kalle/Other/Fonts",
    '.otf': "/Users/kalle/Desktop/kalle/Other/Fonts",
    '.ttf': "/Users/kalle/Desktop/kalle/Other/Fonts",
#Presentations
    '.key': "/Users/kalle/Desktop/kalle/Text/Presentations",
    '.odp': "/Users/kalle/Desktop/kalle/Text/Presentations",
    '.pps': "/Users/kalle/Desktop/kalle/Text/Presentations",
    '.ppt': "/Users/kalle/Desktop/kalle/Text/Presentations",
    '.pptx': "/Users/kalle/Desktop/kalle/Text/Presentations",
#Programming
    '.c': "/Users/kalle/Desktop/kalle/Programming/C&C++",
    '.class': "/Users/kalle/Desktop/kalle/Programming/Java",
    '.dart': "/Users/kalle/Desktop/kalle/Programming/Dart",
    '.py': "/Users/kalle/Desktop/kalle/Programming/Python",
    '.sh': "/Users/kalle/Desktop/kalle/Programming/Shell",
    '.swift': "/Users/kalle/Desktop/kalle/Programming/Swift",
    '.html': "/Users/kalle/Desktop/kalle/Programming/C&C++",
    '.h': "/Users/kalle/Desktop/kalle/Programming/C&C++",
#Spreadsheets
    '.ods' : "/Users/kalle/Desktop/kalle/Text/Microsoft/Excel",
    '.xlr' : "/Users/kalle/Desktop/kalle/Text/Microsoft/Excel",
    '.xls' : "/Users/kalle/Desktop/kalle/Text/Microsoft/Excel",
    '.xlsx' : "/Users/kalle/Desktop/kalle/Text/Microsoft/Excel",
#System
    '.bak' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.cab' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.cfg' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.cpl' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.cur' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.dll' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.dmp' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.drv' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.icns' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.ico' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.ini' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.lnk' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.msi' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.sys' : "/Users/kalle/Desktop/kalle/Text/Other/System",
    '.tmp' : "/Users/kalle/Desktop/kalle/Text/Other/System",
}

folder_to_track = '/Users/kalle/Desktop'
folder_destination = '/Users/kalle/Desktop/kalle'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()