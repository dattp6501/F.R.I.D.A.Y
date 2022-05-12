import  pyautogui
import audiobot
def volume():
    while True:
        audiobot.speak_vn("Bạn muốn điều chỉnh âm lượng như thế nào?")
        volume=audiobot.listentotext()
        s=volume.split()
        if 'tăng'or'ăng'or'răng' in volume:
            pyautogui.press("volumeup",presses=(len(s)+1))
        elif 'giảm'or'dảm'or'rảm' in volume:
            pyautogui.press("volumedown",presses=(len(s)+1))
        elif 'xong' in volume:
            break