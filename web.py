import webbrowser
import audiobot
def google():
    audiobot.speak_vn("bạn muốn tìm gì trên google ạ?")
    search = audiobot.listentotext().lower()
    audiobot.speak_vn(f'vâng!! tôi sẽ tìm {search} trên google ngay')
    url = f"https://www.google.com/search?q={search}"
    webbrowser.get().open(url)
def youtube():
    audiobot.speak_vn("bạn muốn xem gì trên youtube ?")
    search = audiobot.listentotext()
    audiobot.speak_vn(f'vâng! tôi sẽ tìm {search} trên youtube')
    url = f"https://www.youtube.com/?q={search}"
    webbrowser.get().open(url)
def facebook():
    audiobot.speak_vn("mở facebook")
    audiobot.speak_vn("bạn mở facebook để xem bảng tin hay tìm bạn bè ạ")
    key = audiobot.listentotext()
    url = f"https://www.facebook.com/"
    if("bạn bè" in key):
        audiobot.speak_vn("tên nick bạn muốn tìm là gì vây")
        nick = audiobot.listen()
        url = f"https://www.facebook.com/search/top?q={nick}"
    webbrowser.get().open(url)
def gmail():
    url = f"https://mail.google.com/mail/u/0/#inbox"
    webbrowser.get().open(url)