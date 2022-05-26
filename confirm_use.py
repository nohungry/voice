import numpy as np

def get_confirm_fftdata(list1, list2):
    confirmList = []
    list1 = list1
    list2 = list2

    for music1 in list1:
        count = 0
        for music2 in list2:
            # 分為單/ 雙聲道, 已dict.Keys()
            if len(music1["fftData"].keys()) == 1:
                if len(music2["fftData"].keys()) == 1:
                    if (np.array_equal(music1["fftData"]["monoaural"], music2["fftData"]["monoaural"])):
                        temp = {
                            "Music1": music1["name"],
                            "Music2": music2["name"],
                        }
                        # 測試資料比對正確後, popout後續比對可以減少一次
                        testData = list2.pop(count)
                        # 比對完成的資料放置於confirmList
                        confirmList.append(temp)
                        break
                    count += 1
                elif len(music2["fftData"].keys()) == 2:
                    count += 1
            elif len(music1["fftData"].keys()) == 2:
                if len(music2["fftData"].keys()) == 1:
                    count += 1
                elif len(music2["fftData"].keys()) == 2:
                    if (
                    np.array_equal(music1["fftData"]["left_channel"], music2["fftData"]["left_channel"])) and (
                    np.array_equal(music1["fftData"]["right_channel"], music2["fftData"]["right_channel"])):
                        temp = {
                            "Music1": music1["name"],
                            "Music2": music2["name"],
                        }
                        # 測試資料比對正確後, popout後續比對可以減少一次
                        testData = list2.pop(count)
                        # 比對完成的資料放置於confirmList
                        confirmList.append(temp)
                        break
                    count += 1
            else:
                raise Exception("解析的音檔資料格式陣列要小於2")
    return confirmList

def get_confirm_fragment(speclist, testlist):
    confirmList = []
    list1 = speclist
    list2 = testlist

    for music1 in list1:
        count = 0
        for music2 in list2:
            if len(music1["fragment"].shape) == 1 and len(music2["fragment"].shape) == 1:
                if np.array_equal(music1["fragment"], music2["fragment"]):
                    temp = {
                        "Music1": music1["name"],
                        "Music2": music2["name"],
                    }
                    # 測試資料比對正確後, popout後續比對可以減少一次
                    popout = list2.pop(count)
                    # 比對完成的資料放置於confirmList
                    confirmList.append(temp)
                    break
                count += 1
            else:
                raise Exception("解析的音檔資料格式陣列要小於等於1")
    return confirmList