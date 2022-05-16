import webbrowser
import audiobot

def google():
    audiobot.speak_vn("bạn muốn tìm gì trên google ạ?")
    search = audiobot.listentotext().lower()
    audiobot.speak_vn(f'vâng!! tôi sẽ tìm {search} trên google ngay')
    url = f"https://www.google.com/search?q={search}"
    webbrowser.get().open(url)

def gmail():
    url = f"https://mail.google.com/mail/u/0/#inbox"
    webbrowser.get().open(url)