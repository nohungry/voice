# import librosa
# import os
# import numpy as np
# import time
# from mutagen.mp3 import MP3
# import mp3_to_wav_and_reverse as transfer
# import frequency_transform
# # import shutil # 刪除資料夾
# import confirm_use
#
# # 計算時間
# st = time.time()
#
# # 溫州麻將範例_Path
# specPath = "C:/Users/norman_cheng/Desktop/voice/spec_music/specMusic"
# mp3Unique = r".mp3"
# wavUnique = r".wav"
#
# # 1. SPEC音樂detail都塞進list
# specMusicList = []
# specWavDetailList = []
#
# # 2. 過濾資料夾內的MP3/ WAV & 非MP3/ WAV檔案
# specMusicOther = [os.path.join(specPath, _) for _ in os.listdir(specPath) if not _.endswith(mp3Unique) and not _.endswith(wavUnique)]
# assert len(specMusicOther) <= 0, "another file in specMusic folder"
#
# # # 3. 對應頻域分析, 把MP3檔轉變為WAV檔, 也把WAV檔轉變為MP3檔, 分別存在不同的folder
# specInputPath = specPath
# specWavOutputPath = r"C:\Users\norman_cheng\Desktop\voice\spec_music\wavFile"
# specMp3OutputPath = r"C:\Users\norman_cheng\Desktop\voice\spec_music\mp3File"
# # transfer.ffmpegMp3ToWav(specInputPath, specWavOutputPath)
# # transfer.ffmpegWavToMp3(specInputPath, specMp3OutputPath)
#
# # # 測試使用
# # specWavOutputPath = r"C:\Users\norman_cheng\Desktop\voice\testusing_folder\compare_use\specwav"
# # specMp3OutputPath = r"C:\Users\norman_cheng\Desktop\voice\testusing_folder\compare_use\spec"
#
# # 4. 整理mp3 & wav檔案進list
# specWavFileList = [os.path.join(specWavOutputPath, _) for _ in os.listdir(specWavOutputPath)]
# specMp3FileList = [os.path.join(specMp3OutputPath, _) for _ in os.listdir(specMp3OutputPath)]
# assert len(specWavFileList) == len(specMp3FileList), "specMusic need be same number of files"
#
# # 5. 解析MP3檔案 & WAV頻域解析
# for mp3File in specMp3FileList:
#     if not os.path.isdir(mp3File):
#         fragment, samplingRate = librosa.load(mp3File, sr=22050)
#         effectInfo = MP3(mp3File)
#         temp = {
#             "name": os.path.splitext(os.path.basename(mp3File))[0],
#             "fragment": fragment,
#             "samplingRate": samplingRate,
#             "length": effectInfo.info.length,
#         }
#         specMusicList.append(temp)
#
# for wavFile in specWavFileList:
#     if not os.path.isdir(wavFile):
#         fft_data = frequency_transform.freqdomain(0, 11000, wavFile)
#         temp = {
#             "name": os.path.splitext(os.path.basename(wavFile))[0],
#             "fftData": fft_data,
#         }
#         specWavDetailList.append(temp)
#
# # 6. update specMusicList[i]增加頻域參數
# for i in range(len(specMusicList)):
#     assert specMusicList[i]["name"] == specWavDetailList[i]["name"], "spec folder file position wrong"
#     specMusicList[i].update(specWavDetailList[i])
#
# # -------------------------------------------------------------------------
#
# # 溫州麻將_ResourceSaver_Path
# testPath = "C:/Users/norman_cheng/Desktop/voice/website_music/testMusic"
# testPath = r"C:\Users\norman_cheng\Desktop\voice\testusing_folder\test_origin_music"
#
# # 1. website音樂detail都塞進list
# testMusicList = []
# testWavDetailList = []
#
# # 2. 過濾資料夾內的MP3/ WAV & 非MP3/ WAV檔案
# testMusicOther = [os.path.join(testPath, _) for _ in os.listdir(testPath) if not _.endswith(mp3Unique) and not _.endswith(wavUnique)]
# assert len(testMusicOther) <= 0, "another file in testMusic folder"
#
# # 3. 對應頻域分析, 把MP3檔轉變為WAV檔, 也把WAV檔轉變為MP3檔, 分別存在不同的folder
# testInputPath = testPath
# # testWavOutputPath = r"C:\Users\norman_cheng\Desktop\voice\website_music\waveFile"
# # testMp3OutputPath = r"C:\Users\norman_cheng\Desktop\voice\website_music\mp3File"
# testWavOutputPath = r"C:\Users\norman_cheng\Desktop\voice\testusing_folder\test_wav"
# testMp3OutputPath = r"C:\Users\norman_cheng\Desktop\voice\testusing_folder\test_mp3"
# transfer.ffmpegMp3ToWav(testInputPath, testWavOutputPath)
# transfer.ffmpegWavToMp3(testInputPath, testMp3OutputPath)
#
# # # 測試完後刪除該段___晚點刪除
# # testWavOutputPath = r"C:\Users\norman_cheng\Desktop\voice\testusing_folder\compare_use\testwav"
# # testMp3OutputPath = r"C:\Users\norman_cheng\Desktop\voice\testusing_folder\compare_use\test"
#
#
# # 4. 整理mp3 & wav檔案進list
# testWavFileList = [os.path.join(testWavOutputPath, _) for _ in os.listdir(testWavOutputPath)]
# testMp3FileList = [os.path.join(testMp3OutputPath, _) for _ in os.listdir(testMp3OutputPath)]
# assert len(testWavFileList) == len(testMp3FileList), "testMusic need be same number of files"
#
# # 5. 解析MP3檔案 & WAV頻域解析
# for mp3File in testMp3FileList:
#     if not os.path.isdir(mp3File):
#         fragment, samplingRate = librosa.load(mp3File, sr=22050)
#         effectInfo = MP3(mp3File)
#         temp = {
#             "name": os.path.splitext(os.path.basename(mp3File))[0],
#             "fragment": fragment,
#             "samplingRate": samplingRate,
#             "length": effectInfo.info.length,
#         }
#         testMusicList.append(temp)
#
# for wavFile in testWavFileList:
#     if not os.path.isdir(wavFile):
#         fft_data = frequency_transform.freqdomain(0, 11000, wavFile)
#         temp = {
#             "name": os.path.splitext(os.path.basename(wavFile))[0],
#             "fftData": fft_data,
#         }
#         testWavDetailList.append(temp)
#
# # 6. update specMusicList[i]增加頻域參數
# for i in range(len(testMusicList)):
#     assert testMusicList[i]["name"] == testWavDetailList[i]["name"], "test folder file position wrong"
#     testMusicList[i].update(testWavDetailList[i])
#
#
# # TODO specMusicList compare testMusicList
# # 前期測試code先行註解
# # if len(testMusicList) < len(specMusicList):
# #     raise Exception("測試的音樂檔案數目少於SPEC提供的檔案數目")
#
# # # 確認好的音檔資訊放在confrimList
# # confirmList = []
#
# #
# confirm001 = confirm_use.get_confirm_fftdata(specMusicList, testMusicList)
# print(time.time() - st)
# pass

import os
root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(root_path)
rootPath = os.path.dirname(__file__)
specPath = r"spec_music\specMusic"
aa = os.path.join(rootPath, specPath)
# for path in os.listdir(aa):
#     print(path)
# print(os.path.dirname(__file__))
print(aa)