import audiobot
import pyautogui
def dieukhien():
    while True:
        audiobot.speak_vn("Bạn có thể điều khiển bằng lệnh")
        text=audiobot.listentotext()
        if 'lên' in text:
            pyautogui.press('up')
        elif 'xuống' in text:
            pyautogui.press('down')
        elif 'trái' in text:
            pyautogui.press('left')
        elif 'phải' in text:
            pyautogui.press('right')
        elif 'chọn'in text:
            pyautogui.press('enter')
        elif 'chuyển màn'in text:
            pyautogui.hotkey('alt','tab')
        elif 'tắt màn'in text:
            pyautogui.hotkey('alt','f4')
        elif 'đa nhiệm' in text:
            pyautogui.hotkey('win','tab')
        elif 'đóng trang' in text:
            pyautogui.hotkey('ctrl','w')
        elif 'video' in text:
            pyautogui.press('playpause')
        elif 'thoát'or'ra'or'bảng'or'chính' in text:
            break
        else :
            audiobot.speak_vn('Tôi chưa nghe rõ')