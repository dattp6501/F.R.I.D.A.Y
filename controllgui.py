import pyautogui
import audio
def control():
    pyautogui.press("win")
    pyautogui.sleep(0.5)
    pyautogui.write("thiss pc")
    pyautogui.sleep(1)
    pyautogui.press("enter")
    pyautogui.sleep(1)
   
    ask = ""
    while(ask != "thôi"):
        ask = "phải"
        if(ask == "phải"):
            pyautogui.press("right")
        ask = "thôi"
if __name__ == "__main__":
    control()
