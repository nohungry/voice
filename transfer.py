import os
import subprocess

"""
    音樂檔轉換:
        mp3 > wav
        wav > mp3
"""

def ffmpegMp3ToWav(input_path, output_path):
    # windows cmd
    # c:\users\xxxx\xx\test_string>ffmpeg -i input_path output_path
    # 可以單獨轉換一個mp3 file 成為 wav file
    fileName = os.listdir(input_path)
    for file in fileName:
        mp3FilePath = input_path + "\\" + file
        wavFilePath = output_path + "\\" + os.path.splitext(file)[0]
        cmd = "ffmpeg -i " + mp3FilePath + " " + wavFilePath + ".wav"
        subprocess.call(cmd, shell=True)

def ffmpegWavToMp3(input_path, output_path):
    # windows cmd
    # c:\users\xxxx\xx\test_string>ffmpeg -i input_path output_path
    # 可以單獨轉換一個wav file 成為 mp3 file
    fileName = os.listdir(input_path)
    for file in fileName:
        wavFilePath = input_path + "\\" + file
        mp3FilePath = output_path + "\\" + os.path.splitext(file)[0]
        cmd = "ffmpeg -i " + wavFilePath + " " + mp3FilePath + ".mp3"
        subprocess.call(cmd, shell=True)

# if __name__ == '__main__':
    # # covert folder all .mp3 to .wav
    # input_path = r"C:\Users\norman_cheng\Desktop\voice\spec_music\specMusic"
    # output_path = r"C:\Users\norman_cheng\Desktop\voice\spec_music\wavFile"
    # ffmpegMp3ToWav(input_path, output_path)

    # # covert folder all .wav to .mp3
    # input_path = r"C:\Users\norman_cheng\Desktop\voice\spec_music\specMusic"
    # output_path = r"C:\Users\norman_cheng\Desktop\voice\spec_music\mp3File"
    # ffmpegWavToMp3(input_path, output_path)