import numpy as np
import time

def get_confirm_fftdata(speclist, testlist):
    confirmList = []
    specMusicList = speclist
    testMusicList = testlist

    for specMusic in specMusicList:
        count = 0
        for testMusic in testMusicList:
            # 分為單/ 雙聲道, 已dict.Keys()
            if len(specMusic["fftData"].keys()) == 1:
                if len(testMusic["fftData"].keys()) == 1:
                    if (np.array_equal(specMusic["fftData"]["monoaural"], testMusic["fftData"]["monoaural"])):
                        temp = {
                            "specMusic": specMusic["name"],
                            "testMusic": testMusic["name"],
                        }
                        # 測試資料比對正確後, popout後續比對可以減少一次
                        testData = testMusicList.pop(count)
                        # 比對完成的資料放置於confirmList
                        confirmList.append(temp)
                        break
                    count += 1
                elif len(testMusic["fftData"].keys()) == 2:
                    count += 1
            elif len(specMusic["fftData"].keys()) == 2:
                if len(testMusic["fftData"].keys()) == 1:
                    count += 1
                elif len(testMusic["fftData"].keys()) == 2:
                    if (
                    np.array_equal(specMusic["fftData"]["left_channel"], testMusic["fftData"]["left_channel"])) and (
                    np.array_equal(specMusic["fftData"]["right_channel"], testMusic["fftData"]["right_channel"])):
                        temp = {
                            "specMusic": specMusic["name"],
                            "testMusic": testMusic["name"],
                        }
                        # 測試資料比對正確後, popout後續比對可以減少一次
                        testData = testMusicList.pop(count)
                        # 比對完成的資料放置於confirmList
                        confirmList.append(temp)
                        break
                    count += 1
            else:
                raise Exception("解析的音檔資料格式陣列要小於2")
    return confirmList

def get_confirm_fragment(speclist, testlist):
    confirmList = []
    specMusicList = speclist
    testMusicList = testlist

    for specMusic in specMusicList:
        count = 0
        for testMusic in testMusicList:
            if len(specMusic["fragment"].shape) == 1 and len(testMusic["fragment"].shape) == 1:
                if np.array_equal(specMusic["fragment"], testMusic["fragment"]):
                    temp = {
                        "specMusic": specMusic["name"],
                        "testMusic": testMusic["name"],
                    }
                    # 測試資料比對正確後, popout後續比對可以減少一次
                    popout = testMusicList.pop(count)
                    # 比對完成的資料放置於confirmList
                    confirmList.append(temp)
                    break
                count += 1
            else:
                raise Exception("解析的音檔資料格式陣列要小於等於1")
    return confirmList