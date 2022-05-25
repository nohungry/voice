import common
import confirm_use

def compare(path1, path2):
    path001 = r"C:\Users\norman_cheng\Desktop\voice_env\spec_music\specMusic"
    path002 = ""
    common.filterOther(path001)
    musicPath = common.folderRemake()
    fileName = common.fileNameCatch(path001)
    tempPath = common.pathSplice(musicPath, fileName)
    pass


if __name__ == '__main__':
    compare(1, 2)