import wave
# import pyaudio
# import pylab
# import matplotlib.pyplot as plt
import numpy as np

def get_framerate(wavfile):
    # '''
    #     input file get framerate
    # :param wavefile: file path
    # e.g. file_path = r"C:\Users\norman_cheng\Desktop\voice\spec_music\waveFile\BtnClick.wav"
    # :return: framerate
    # '''
    wf = wave.open(wavfile, "rb")
    params = wf.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    return framerate

def get_nframes(wavfile):
    # '''
    #     input file get nframerate
    # :param wavefile: file path
    # e.g. file_path = r"C:\Users\norman_cheng\Desktop\voice\spec_music\waveFile\BtnClick.wav"
    # :return: nframerate
    # '''
    wf = wave.open(wavfile, "rb")  # 打開wav
    params = wf.getparams()  # 參數獲取
    nchannels, sampwidth, framerate, nframes = params[:4]
    return nframes

def get_nchannels(wavfile):
    # '''
    #     confirm music nchannel, 確認WAV聲音檔案為單聲道/ 雙聲道
    # :param wavfile:
    # :return: nchannel
    # '''
    wf = wave.open(wavfile, "rb")
    nchannels = wf.getnchannels()
    return nchannels

def get_time(wavfile):
    framerate = get_framerate(wavfile)
    nframes = get_nframes(wavfile)
    duration = np.arange(0, nframes) * (1.0 / framerate)
    assert type(duration) == np.ndarray, "WAV檔案解析後, 音樂時間無法解析成ndarray"
    # 取array最後一個值 (音樂持續時間)
    return duration[-1]

def get_wavedata(wavfile):
    # '''
    #     input file get N-2 voice array
    # :param wavefile: file path
    # :return: wave_data
    # '''
    wf = wave.open(wavfile, "rb")
    params = wf.getparams()  # 參數獲取
    nchannels, sampwidth, framerate, nframes = params[:4]
    # 讀取完整的幀數據到str_data中，這是一個string類型的數據
    str_data = wf.readframes(nframes)
    wf.close()  # 關閉wave

    #####2.將波形數據轉換爲數組
    # 先行判斷單聲道/ 雙聲道
    # 單聲道 N-1 covert 一維數組
    if nchannels == 1:
        wav_data = np.frombuffer(str_data, dtype=np.short)
        # 將數組轉置爲 N-2 目標數組
        wav_data = wav_data.T
        # wav音檔播放長度
        # time = (np.arange(0, nframes) * (1.0 / framerate))[-1]
    # 雙聲道
    elif nchannels == 2:
        wav_data = np.frombuffer(str_data, dtype=np.short)
        # 2-N N維數組
        wav_data.shape = -1, 2
        # 將數組轉置爲 N-2 目標數組
        wav_data = wav_data.T
        # time = (np.arange(0, nframes) * (1.0 / framerate))[-1]
    else:
        raise Exception("(默認音訊檔案皆為單聲道 & 雙聲道) \n 目前解析的音訊檔案 > 雙聲道")

    return wav_data

def timedomain(wavfile):
    wave_data = get_wavedata(wavfile)  # 獲取處理好的wave數據
    framerate = get_framerate(wavfile)  # 獲取幀率
    nframes = get_nframes(wavfile)  # 獲取幀數

    #####3.構建橫座標
    time = np.arange(0, nframes) * (1.0 / framerate)

    #####4.畫圖
    # pylab.figure(figsize=(40, 10))
    # pylab.subplot(211)
    # pylab.plot(time, wave_data[0])  # 第一幅圖：左聲道
    # pylab.subplot(212)
    # pylab.plot(time, wave_data[1], c="g")  # 第二幅圖：右聲道
    # pylab.xlabel("time (seconds)")
    # pylab.show()

    return None

def freqdomain(start, fft_size, wavfile):
    # '''
    #     return left & right voice array
    # :param start:
    # :param fft_size:
    # :param wavefile:
    # :return: return left & right voice array
    # '''
    waveData = get_wavedata(wavfile)  # 獲取wave數據
    framerate = get_framerate(wavfile)  # 獲取幀率數據

    #### 1.取出所需部分進行傅里葉變換，並得到幅值
    # rfft，對稱保留一半，結果爲 fft_size/2-1 維複數數組
    if waveData.ndim == 1:
        fft_y1 = np.fft.rfft(waveData[start:start + fft_size - 1]) / fft_size  # 單聲道
        fft_y1 = np.abs(fft_y1)
        fftData = {
            "monoaural": fft_y1
        }
        return fftData
    elif waveData.ndim == 2:
        fft_y1 = np.fft.rfft(waveData[0][start:start + fft_size - 1]) / fft_size  # 左聲部
        fft_y2 = np.fft.rfft(waveData[1][start:start + fft_size - 1]) / fft_size  # 右聲部
        fft_y1 = np.abs(fft_y1)
        fft_y2 = np.abs(fft_y2)
        fftData = {
            "left_channel": fft_y1,
            "right_channel": fft_y2
        }
        return fftData
    else:
        raise Exception("(默認音訊檔案皆為單聲道 & 雙聲道) \n 目前解析的音訊檔案 > 雙聲道")

    #### 2.計算頻域圖x值
    # 最小值爲0Hz，最大值一般設爲採樣頻率的一半
    # param1 = framerate // 2
    # param2 = fft_size // 2
    # freqs = np.linspace(0, param1, param2)
    #
    # leftVoice = np.abs(fft_y1)
    # rightVoice = np.abs(fft_y2)

    #### 3.畫圖
    # plt.figure(figsize=(20, 10))
    # pylab.subplot(211)
    # plt.plot(freqs, np.abs(fft_y1))
    # pylab.xlabel("frequence(Hz)")
    # pylab.subplot(212)
    # plt.plot(freqs, np.abs(fft_y2), c='g')
    # pylab.xlabel("frequence(Hz)")
    # plt.show()

# if __name__ == '__main__':
#     wavfile = r"C:\Users\norman_cheng\Desktop\voice\spec_music\waveFile\BtnClick.wav"
#     left, right = freqdomain(0, 4000, wavfile)
#     print((left == right).all())
