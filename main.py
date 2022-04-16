from datetime import datetime
from pickle import TRUE
import speech_recognition
import webbrowser
from gtts import gTTS
import wikipedia
import playsound
import os
import botfb
from time import sleep
from selenium import webdriver
import security
# phat ra loa 
#english
# def speak_en(audio):
#     friday = pyttsx3.init()
#     friday.getProperty('voices')
#     friday.setProperty('voice',name=1)
#     # print("F.R.I.D.A.Y: "+audio)
#     friday.say(audio)
#     friday.runAndWait()
#việt nam
def speak_vn(s):
    pathsound = r"E:\workspace\python\trolyao_btl\sound.mp3"
    print("F.R.I.D.A.Y: "+s)
    tts = gTTS(text=s, lang='vi', slow=False)
    tts.save(pathsound)
    playsound.playsound(pathsound,True)
    os.remove(pathsound)
# chuyen giong noi thanh string
def listen():
    bot = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("F.R.I.D.A.Y: listening...")
        bot.pause_threshold = 1 #dung 2s roi nghe lenh moi
        audio = bot.listen(mic)
    s = ""
    try:
        s = bot.recognize_google(audio, language="vi-VN")
    except speech_recognition.UnknownValueError:
        s = ""
    print("you: "+s)
    return s.lower()
def welcome():
    hour = datetime.now().hour
    if hour<=10:
        speak_vn("xin chào buổi sáng")
    elif hour<=12:
        speak_vn("xin chào buổi trưa")
    elif hour<=17:
        speak_vn("xin chào buổi chiều")
    else:
        speak_vn("xin chào buổi tối")
    speak_vn("tôi có thể giúp gì cho bạn")
def time():
    now = datetime.now()
    t = "bây giờ là %d giờ %d phút" %(now.hour,now.minute)
    return t
def date():
    now = datetime.now()
    d = "hôm nay là ngày %d tháng %d năm %d" %(now.day,now.month,now.year)
    return d
def google():
    speak_vn("bạn muốn tìm gì trên google ạ?")
    search = listen().lower()
    url = f"https://www.google.com/search?q={search}"
    webbrowser.get().open(url)
    speak_vn(f'vâng!! tôi sẽ tìm {search} trên google ngay')
def youtube():
    speak_vn("bạn muốn xem gì trên youtube ?")
    search = listen()
    url = f"https://www.youtube.com/?q={search}"
    webbrowser.get().open(url)
    speak_vn(f'vâng! tôi sẽ tìm {search} trên youtube')
def facebook():
    speak_vn("mở facebook")
    browser = webdriver.Chrome(r"C:\Users\Administrator\Documents\workspace\python\friday\chromedriver.exe")
    # mỏ facebook
    botfb.open_facebook(security.USERNAME,security.PASSWORD,browser)
    sleep(6.5)
    # if("trang chủ" in s or "home" in s or "bảng tin" in s):
    while True:
        s = listen()
        if("tìm kiếm" in s or "search" in s):
            speak_vn("bạn muốn tôi tìm kiếm gì nào")
            key = listen()
            while(key == ""):
                key = listen()    
            botfb.search_facebook(browser,key)
            sleep(10)
        elif("đóng" in s or "dừng" in s or "thôi" in s or "rừng" in s):
            speak_vn("bạn có muốn đóng facebook không?")
            ok = listen()
            # for i in range(0,2):
            #     if(ok!=""):
            #         break
            if("có" in ok or "yes" in ok):
                print("có")
                browser.close()
            else:
                print("không")
            break
    # speak_vn("bạn mở facebook để xem bảng tin hay tìm bạn bè ạ")
    # key = listen()
    # url = f"https://www.facebook.com/"
    # if("bạn bè" in key):
    #     speak_vn("tên nick bạn muốn tìm là gì vây")
    #     nick = listen()
    #     url = f"https://www.facebook.com/search/top?q={nick}"
    # webbrowser.get().open(url)
def gmail():
    url = f"https://mail.google.com/mail/u/0/#inbox"
    webbrowser.get().open(url)
def openApplication():
    speak_vn("bạn muốn mở ứng dùng nào!")
    for i in range(3):
        app = listen()
        if("zalo" in app):
            zalo()
        elif("word" in app or "soạn thảo văn bản" in app):
            word()
        elif("excel" in app or "trang tính" in app):
            excel()
        elif("powerpoint" in app or "trình chiếu" in app or "chình chiếu" in app):
            powerpoint()
        else:
            speak_vn("ứng dụng chưa được cài đặt")
def zalo():
    speak_vn("tôi sẽ mở zalo ngay")
    os.startfile(r"C:\Users\Administrator\AppData\Local\Programs\Zalo\Zalo.exe")
def word():
    speak_vn("mở word")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
def excel():
    speak_vn("mở excel")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
def powerpoint():
    speak_vn("mở powerpoint")
    os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
def search():
    wikipedia.set_lang('vi')
    speak_vn("bạn cần tìm thông tin gì ạ!")
    key = listen()
    data =  wikipedia.summary(key,1)
    speak_vn(data)
if __name__ == "__main__":
    goodbye = []
    welcome()
    while TRUE:
        s = listen()
        if("thôi" in s or "tạm biệt" in s or "đi" in s or "biến" in s or "lướt" in s or "next" in s or "goodbye" in s or "cút" in s):
            speak_vn("vâng ạ!tôi sẽ đi ngay! hẹn gặp lại ạ!")
            break
        elif("google" in s):
            google()
        elif("youtube" in s):
            youtube()
        elif ("facebook" in s):
            facebook()
        elif ("gmail" in s or "thư" in s):
            gmail()
        elif ("giờ" in s):
            speak_vn(time())
        elif("ngày" in s):
            speak_vn(date())
        elif("application" in s or "ứng dụng" in s):
            openApplication()
        elif("tìm kiếm" in s or "thông tin" in s):
            search()