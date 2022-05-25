import common
import confirm_use

def compare(path1, path2):
    path001 = r"C:\Users\norman_cheng\Desktop\voice_env\spec_music\specMusic"
    path002 = ""
    common.filterOther(path001)
    musicPath = common.folderRemake()
    fileName = common.fileNameCatch(path001)
    tempPath = common.pathSplice(musicPath, fileName)
    mp3FilePath = common.transferMP3(path001, tempPath)
    wavFilePath = common.transferWAV(path001, tempPath)
    mp3FileList = common.sortList(mp3FilePath)
    wavFileList = common.sortList(wavFilePath)
    assert len(mp3FileList) == len(wavFileList), "numbers of file not equal"
    mp3Data1, wavData1 = common.parseMusic(mp3FileList, wavFileList)
    curPath1 = common.dataSplice(mp3Data1, wavData1)


if __name__ == '__main__':
    compare(1, 2)