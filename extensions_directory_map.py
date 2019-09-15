ext_dir_map = {
    # No name
    ('noname',): ("Other", "Uncategorized"),
    # Audio
    ('.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma', '.wpl', '.m3u'): ("Media", "Audio"),
    # Text
    ('.txt', '.rtf', '.tex', '.wks', '.wps', '.wpd', '.odt'): ("Text", "TextFiles"),
    ('.doc', '.docx'): ("Text", "Microsoft", "Word"),
    ('.pdf',): ("Text", "PDF"),

    # Video
    ('.3g2', '.3gp', '.avi', '.flv', '.h264', '.m4v', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm', '.swf', '.vob',
     '.wmv'): ("Media", "Video"),

    # Images ,
    ('.ai', '.bmp', '.gif', '.ico', '.jpg', '.jpeg', '.png', '.ps', '.psd', '.svg', '.tif', '.tiff',
     '.CR2'): ("Media", "Images"),

    # Internet
    ('.asp', '.aspx', '.cer', '.cfm', '.cgi', '.pl', '.css', '.htm', '.js', '.jsp', '.part', '.php', '.rss',
     '.xhtml',): ("Other", "Internet"),
    # Compressed
    ('.7z', '.arj', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip',): ("Other", "Compressed"),
    # Disc
    ('.bin', '.dmg', '.iso', '.toast', '.vcd'): ("Other", "Disc"),

    # Data
    ('.csv', '.dat', '.db', '.dbf', '.log', '.mdb', '.sav', '.sql', '.tar', '.xml', '.json'): (
        "Programming", "Database"),
    # Executables
    ('.apk', '.bat', '.com', '.exe', '.gadget', '.jar', '.wsf',): ("Other", "Executables"),
    # Fonts
    ('.fnt', '.fon', '.otf', '.ttf'): ("Other", "Fonts"),

    # Presentations
    ('.key', '.odp', '.pps', '.ppt', '.pptx'): ("Text", "Presentations"),

    # Programming
    ('.c', '.class', '.dart', '.py', '.sh', '.swift', '.html', '.h'): (
        "Programming", "C&C++"),

    # Spreadsheets
    ('.ods', '.xlr', '.xls', '.xlsx'): ("Text", "Microsoft", "Excel"),

    # System
    ('.bak', '.cab', '.cfg', '.cpl', '.cur', '.dll', '.dmp', '.drv', '.icns', '.ico', '.ini', '.lnk', '.msi', '.sys',
     '.tmp'): ("Text", "Other", "System"),
}