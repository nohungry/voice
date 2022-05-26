import common
import confirm_use

def compare(path1, path2):
    # 刪除已有的資料夾重新創建
    musicPath = common.folderRemake()
    path001 = r"C:\Users\norman_cheng\Desktop\voice_env\spec_music\specMusic"
    path002 = ""
    # process start
    common.filterOther(path001)
    fileName1 = common.fileNameCatch(path001)
    tempPath1 = common.pathSplice(musicPath, fileName1)
    mp3FilePath1 = common.transferMP3(path001, tempPath1)
    wavFilePath1 = common.transferWAV(path001, tempPath1)
    mp3FileList1 = common.sortList(mp3FilePath1)
    wavFileList1 = common.sortList(wavFilePath1)
    assert len(mp3FileList1) == len(wavFileList1), "numbers of file not equal"
    mp3Data1, wavData1 = common.parseMusic(mp3FileList1, wavFileList1)
    curPath1 = common.dataSplice(mp3Data1, wavData1)
    # ----------------------------------------------------------------------
    common.filterOther(path002)
    fileName2 = common.fileNameCatch(path002)
    tempPath2 = common.pathSplice(musicPath, fileName2)
    mp3FilePath2 = common.transferMP3(path002, tempPath2)
    wavFilePath2 = common.transferWAV(path002, tempPath2)
    mp3FileList2 = common.sortList(mp3FilePath2)
    wavFileList2 = common.sortList(wavFilePath2)
    assert len(mp3FileList2) == len(wavFileList2), "numbers of file not equal"
    mp3Data2, wavData2 = common.parseMusic(mp3FileList2, wavFileList2)
    curPath2 = common.dataSplice(mp3Data2, wavData2)

if __name__ == '__main__':
    compare(1, 2)