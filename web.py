
from time import sleep
import webbrowser
import audio
from selenium import webdriver
import botfb
import security
def google():
    audio.speak_vn("bạn muốn tìm gì trên google ạ?")
    search = audio.listen().lower()
    url = f"https://www.google.com/search?q={search}"
    webbrowser.get().open(url)
    audio.speak_vn(f'vâng!! tôi sẽ tìm {search} trên google ngay')
def youtube():
    audio.speak_vn("bạn muốn xem gì trên youtube ?")
    search = audio.listen()
    url = f"https://www.youtube.com/?q={search}"
    webbrowser.get().open(url)
    audio.speak_vn(f'vâng! tôi sẽ tìm {search} trên youtube')
def facebook():
    audio.speak_vn("mở facebook")
    browser = webdriver.Chrome(r"C:\Users\Administrator\Documents\workspace\python\friday\chromedriver.exe")
    # mỏ facebook
    botfb.open_facebook(security.USERNAME,security.PASSWORD,browser)
    sleep(6.5)
    # if("trang chủ" in s or "home" in s or "bảng tin" in s):
    while True:
        s = audio.listen()
        if("tìm kiếm" in s or "search" in s):
            audio.speak_vn("bạn muốn tôi tìm kiếm gì nào")
            key = audio.listen()
            while(key == ""):
                key = audio.listen()    
            botfb.search_facebook(browser,key)
            sleep(10)
        elif("đóng" in s or "dừng" in s or "thôi" in s or "rừng" in s):
            audio.speak_vn("bạn có muốn đóng facebook không?")
            ok = audio.listen()
            # for i in range(0,2):
            #     if(ok!=""):
            #         break
            if("có" in ok or "yes" in ok):
                print("có")
                browser.close()
            else:
                print("không")
            break
    # audio.speak_vn("bạn mở facebook để xem bảng tin hay tìm bạn bè ạ")
    # key = audio.listen()
    # url = f"https://www.facebook.com/"
    # if("bạn bè" in key):
    #     audio.speak_vn("tên nick bạn muốn tìm là gì vây")
    #     nick = audio.listen()
    #     url = f"https://www.facebook.com/search/top?q={nick}"
    # webbrowser.get().open(url)
def gmail():
    url = f"https://mail.google.com/mail/u/0/#inbox"
    webbrowser.get().open(url)
