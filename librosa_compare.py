import librosa
import os
import time
from mutagen.mp3 import MP3
import mp3_to_wav_and_reverse as transfer
import frequency_transform
import shutil # 刪除資料夾
import confirm_use

# root dir
rootPath = os.path.dirname(__file__)

# 計算時間
st = time.time()

# 溫州麻將範例_Path
specFolder = r"spec_music\specMusic"
specPath = os.path.join(rootPath, specFolder)
mp3Unique = r".mp3"
wavUnique = r".wav"

# 1. SPEC音樂detail都塞進list
specMusicList = []
specWavDetailList = []

# 2. 過濾資料夾內的MP3/ WAV & 非MP3/ WAV檔案
specMusicOther = [os.path.join(specPath, _) for _ in os.listdir(specPath) if not _.endswith(mp3Unique) and not _.endswith(wavUnique)]
assert len(specMusicOther) <= 0, "another file in specMusic folder"

# 3. 對應頻域分析, 把MP3檔轉變為WAV檔, 也把WAV檔轉變為MP3檔, 分別存在不同的folder
specInputPath = specPath
specWavFolder = r"spec_music\wavFile"
specMp3Folder = r"spec_music\mp3File"
specWavOutputPath = os.path.join(rootPath, specWavFolder)
specMp3OutputPath = os.path.join(rootPath, specMp3Folder)
# 刪除清空原先已有的folder
if os.path.isdir(specWavOutputPath):
    try:
        shutil.rmtree(specWavOutputPath)
    except OSError as e:
        print(e)
    os.mkdir(specWavOutputPath)
else:
    os.mkdir(specWavOutputPath)
if os.path.isdir(specMp3OutputPath):
    try:
        shutil.rmtree(specMp3OutputPath)
    except OSError as e:
        print(e)
    os.mkdir(specMp3OutputPath)
else:
    os.mkdir(specMp3OutputPath)
transfer.ffmpegMp3ToWav(specInputPath, specWavOutputPath)
transfer.ffmpegWavToMp3(specInputPath, specMp3OutputPath)

# 4. 整理mp3 & wav檔案進list
specWavFileList = [os.path.join(specWavOutputPath, _) for _ in os.listdir(specWavOutputPath)]
specMp3FileList = [os.path.join(specMp3OutputPath, _) for _ in os.listdir(specMp3OutputPath)]
assert len(specWavFileList) == len(specMp3FileList), "specMusic need be same number of files"

# 5. 解析MP3檔案 & WAV頻域解析
for mp3File in specMp3FileList:
    if not os.path.isdir(mp3File):
        fragment, samplingRate = librosa.load(mp3File, sr=22050)
        effectInfo = MP3(mp3File)
        temp = {
            "name": os.path.splitext(os.path.basename(mp3File))[0],
            "fragment": fragment,
            "samplingRate": samplingRate,
            "length": effectInfo.info.length,
        }
        specMusicList.append(temp)

for wavFile in specWavFileList:
    if not os.path.isdir(wavFile):
        fft_data = frequency_transform.freqdomain(0, 11000, wavFile)
        temp = {
            "name": os.path.splitext(os.path.basename(wavFile))[0],
            "fftData": fft_data,
        }
        specWavDetailList.append(temp)

# 6. update specMusicList[i]增加頻域參數
for i in range(len(specMusicList)):
    assert specMusicList[i]["name"] == specWavDetailList[i]["name"], "spec folder file position wrong"
    specMusicList[i].update(specWavDetailList[i])

# -------------------------------------------------------------------------

# 溫州麻將_ResourceSaver_Path
testFolder = r"website_music\testMusic"
testPath = os.path.join(rootPath, testFolder)

# 1. website音樂detail都塞進list
testMusicList = []
testWavDetailList = []

# 2. 過濾資料夾內的MP3/ WAV & 非MP3/ WAV檔案
testMusicOther = [os.path.join(testPath, _) for _ in os.listdir(testPath) if not _.endswith(mp3Unique) and not _.endswith(wavUnique)]
assert len(testMusicOther) <= 0, "another file in testMusic folder"

# 3. 對應頻域分析, 把MP3檔轉變為WAV檔, 也把WAV檔轉變為MP3檔, 分別存在不同的folder
testInputPath = testPath
testWavFolder = r"website_music\waveFile"
testMp3Folder = r"website_music\mp3File"
testWavOutputPath = os.path.join(rootPath, testWavFolder)
testMp3OutputPath = os.path.join(rootPath, testMp3Folder)
# 刪除清空原先已有的folder
if os.path.isdir(testWavOutputPath):
    try:
        shutil.rmtree(testWavOutputPath)
    except OSError as e:
        print(e)
    os.mkdir(testWavOutputPath)
else:
    os.mkdir(testWavOutputPath)
if os.path.isdir(testMp3OutputPath):
    try:
        shutil.rmtree(testMp3OutputPath)
    except OSError as e:
        print(e)
    os.mkdir(testMp3OutputPath)
else:
    os.mkdir(testMp3OutputPath)
transfer.ffmpegMp3ToWav(testInputPath, testWavOutputPath)
transfer.ffmpegWavToMp3(testInputPath, testMp3OutputPath)

# 4. 整理mp3 & wav檔案進list
testWavFileList = [os.path.join(testWavOutputPath, _) for _ in os.listdir(testWavOutputPath)]
testMp3FileList = [os.path.join(testMp3OutputPath, _) for _ in os.listdir(testMp3OutputPath)]
assert len(testWavFileList) == len(testMp3FileList), "testMusic need be same number of files"

# 5. 解析MP3檔案 & WAV頻域解析
for mp3File in testMp3FileList:
    if not os.path.isdir(mp3File):
        fragment, samplingRate = librosa.load(mp3File, sr=22050)
        effectInfo = MP3(mp3File)
        temp = {
            "name": os.path.splitext(os.path.basename(mp3File))[0],
            "fragment": fragment,
            "samplingRate": samplingRate,
            "length": effectInfo.info.length,
        }
        testMusicList.append(temp)

for wavFile in testWavFileList:
    if not os.path.isdir(wavFile):
        fft_data = frequency_transform.freqdomain(0, 11000, wavFile)
        temp = {
            "name": os.path.splitext(os.path.basename(wavFile))[0],
            "fftData": fft_data,
        }
        testWavDetailList.append(temp)

# 6. update specMusicList[i]增加頻域參數
for i in range(len(testMusicList)):
    assert testMusicList[i]["name"] == testWavDetailList[i]["name"], "test folder file position wrong"
    testMusicList[i].update(testWavDetailList[i])


# TODO specMusicList compare testMusicList
# 前期測試code先行註解
# if len(testMusicList) < len(specMusicList):
#     raise Exception("測試的音樂檔案數目少於SPEC提供的檔案數目")

# 音樂音效SpecMusic & TestMusic開始比對, 回傳對應的音檔
confirmList = confirm_use.get_confirm_fftdata(specMusicList, testMusicList)
