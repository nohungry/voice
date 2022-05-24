import os
import shutil

def filterOther(filterpath):
    mp3Unique = r".mp3"
    wavUnique = r".wav"
    musicOther = [os.path.join(filterpath, _) for _ in os.listdir(filterpath) if not _.endswith(mp3Unique) and not _.endswith(wavUnique)]
    return musicOther

def folderRemake():
    desktop = os.path.join(os.path.expanduser("~"), "Desktop") + "\\"
    comparePath = os.path.join(desktop, r"Music_compare")
    if os.path.isdir(comparePath):
        try:
            shutil.rmtree(comparePath)
        except OSError as e:
            print(e)
        os.mkdir(comparePath)
    else:
        os.mkdir(comparePath)

def transferMP3()