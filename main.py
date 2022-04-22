from datetime import datetime
from pickle import TRUE
import wikipedia
import app
import timeai
import audio
import web
import weather
def welcome():
    hour = datetime.now().hour
    if hour<=10:
        audio.speak_vn("xin chào buổi sáng")
    elif hour<=12:
        audio.speak_vn("xin chào buổi trưa")
    elif hour<=17:
        audio.speak_vn("xin chào buổi chiều")
    else:
        audio.speak_vn("xin chào buổi tối")
    audio.speak_vn("tôi có thể giúp gì cho bạn")

def search():
    wikipedia.set_lang('vi')
    audio.speak_vn("bạn cần tìm thông tin gì ạ!")
    key = audio.listen()
    data =  wikipedia.summary(key,1)
    audio.speak_vn(data)
if __name__ == "__main__":
    goodbye = []
    welcome()
    while TRUE:
        s = audio.listen()
        if("thôi" in s or "tạm biệt" in s or "đi" in s or "biến" in s or "lướt" in s or "next" in s or "goodbye" in s or "cút" in s):
            audio.speak_vn("vâng ạ!tôi sẽ đi ngay! hẹn gặp lại ạ!")
            break
        elif ("giờ" in s):
            audio.speak_vn(timeai.time())
        elif("ngày" in s):
            audio.speak_vn(timeai.date())
        elif("google" in s):
            web.google()
        elif("youtube" in s):
            web.youtube()
        elif ("facebook" in s):
            web.facebook()
        elif ("gmail" in s or "thư" in s):
            web.gmail()
        elif("zalo" in s):
            app.zalo()
        elif("word" in s or "soạn thảo văn bản" in s):
            app.word()
        elif("excel" in s or "trang tính" in s):
            app.excel()
        elif("powerpoint" in s or "trình chiếu" in s or "chình chiếu" in s):
            app.powerpoint()
        elif("tìm kiếm" in s or "thông tin" in s):
            search()
        elif("thời tiết" in s):
            weather.current_weather()