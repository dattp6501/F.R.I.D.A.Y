import os
import audio



def zalo():
    audio.speak_vn("tôi sẽ mở zalo ngay")
    os.startfile(r"C:\Users\Administrator\AppData\Local\Programs\Zalo\Zalo.exe")
def word():
    audio.speak_vn("mở word")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
def excel():
    audio.speak_vn("mở excel")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
def powerpoint():
    audio.speak_vn("mở powerpoint")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")