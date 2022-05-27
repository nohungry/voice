import os
import shutil
import transfer
import librosa
from mutagen.mp3 import MP3
import frequency_transform
import copy
from  datetime import datetime
import json

def filterOther(filter_path):
    mp3Unique = r".mp3"
    wavUnique = r".wav"
    musicOther = [os.path.join(filter_path, _) for _ in os.listdir(filter_path) if not _.endswith(mp3Unique) and not _.endswith(wavUnique)]
    assert len(musicOther) <= 0, "another file in music folder"

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
    return comparePath

def fileNameCatch(file_path):
    # filepath = os.path.splitext(file_path)[0]
    # fileName = filepath.split("/")[-1]
    fileName = file_path.split("\\")[-1]
    return fileName

def pathSplice(path1, path2):
    # 預計path1: "C:\Users\xxxx\Desktop\Music_compare"
    # 預計path2: "\fileName"
    path = os.path.join(path1, path2)
    return path

def mkMusicDir(path, word):
    musicPath = path + r"_%s" %word
    os.mkdir(musicPath)

def transferMP3(folder_path, output_path):
    # 預計folderpath_是.wav檔案的原始音樂folder
    # 預計output_path給的參數是"C:\Users\xxxx\Desktop\Music_compare\fileName"
    output_path = output_path + r"_mp3"
    transfer.ffmpegWavToMp3(folder_path, output_path)
    return output_path

def transferWAV(folder_path, output_path):
    # 預計folderpath_是.mp3檔案的原始音樂folder
    # 預計output_path給的參數是"C:\Users\xxxx\Desktop\Music_compare\fileName"
    output_path = output_path + r"_wav"
    transfer.ffmpegMp3ToWav(folder_path, output_path)
    return output_path

def sortList(path):
    # 預計path是"\Desktop\Music_compare\fileName_wav or _mp3"
    arrange = [os.path.join(path, _) for _ in os.listdir(path)]
    return arrange

def parseMusic(mp3_list, wav_list):
    mp3Parse = []
    for mp3File in mp3_list:
        if not os.path.isdir(mp3File):
            fragment, samplingRate = librosa.load(mp3File, sr=22050)
            effectInfo = MP3(mp3File)
            temp = {
                "name": os.path.splitext(os.path.basename(mp3File))[0],
                "fragment": fragment,
                "samplingRate": samplingRate,
                "length": effectInfo.info.length,
            }
            mp3Parse.append(temp)

    wavParse = []
    for wavFile in wav_list:
        if not os.path.isdir(wavFile):
            fft_data = frequency_transform.freqdomain(0, 11000, wavFile)
            temp = {
                "name": os.path.splitext(os.path.basename(wavFile))[0],
                "fftData": fft_data,
            }
            wavParse.append(temp)

    return mp3Parse, wavParse

def dataSplice(mp3, wav):
    # mp3: []
    # wav: []
    assert len(mp3) == len(wav), "file quantity not equal"
    for index in range(len(mp3)):
        assert mp3[index]["name"] == wav[index]["name"], "list file position wrong"
        mp3[index].update(wav[index])
    current = copy.deepcopy(mp3)
    return current

def createLog(result):
    # result: []
    desktop = os.path.join(os.path.expanduser("~"), "Desktop") + "\\"
    logFolderPath = os.path.join(desktop, r"Music_Log")
    if not os.path.exists(logFolderPath):
        os.mkdir(logFolderPath)
    nowTime = datetime.today().strftime("%Y%m%d_%H%M")
    logText = os.path.join(logFolderPath, r"log_" + nowTime + ".txt")
    if len(result) <= 0 :
        popoutMessage = "compare fail or music files are not equal"
        with open(logText, "w") as f:
            f.write(popoutMessage)
    f = open(logText, "w")
    for index in result:
        f.write(json.dumps(index))
        f.write("\r\n")
    f.write("# ------------------\r\n")
    f.write("numbers of equal files: %d" %len(result))
    f.close()

