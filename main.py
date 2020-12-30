import vlc
import os
import time
import socket

# Add default VLC directories for libvlc.dll
try:
    os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC') # 64-Bt
except FileNotFoundError:
    pass

try:
    os.add_dll_directory(r'C:\Program Files (x86)\VideoLAN\VLC')    # 32-Bit
except FileNotFoundError:
    pass

media = vlc.MediaPlayer(r'G:\Bit\Captain Marvel (2019) [WEBRip] [1080p] [YTS.AM]'
                        r'\Captain.Marvel.2019.1080p.WEBRip.x264-[YTS.AM].mp4')

media.play()
time.sleep(5)
# Seek to a time (MS)
media.set_time(0)
media.play()
time.sleep(5)
