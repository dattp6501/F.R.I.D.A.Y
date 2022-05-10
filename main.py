from datetime import datetime
from pickle import TRUE
import wikipedia
import app
import timeai
import audiobot
import web
import weather
def welcome():
    hour = datetime.now().hour
    if hour<=10:
        audiobot.speak_vn("xin chào buổi sáng")
    elif hour<=12:
        audiobot.speak_vn("xin chào buổi trưa")
    elif hour<=17:
        audiobot.speak_vn("xin chào buổi chiều")
    else:
        audiobot.speak_vn("xin chào buổi tối")
    audiobot.speak_vn("tôi có thể giúp gì cho bạn")

def search():
    wikipedia.set_lang('vi')
    audiobot.speak_vn("bạn cần tìm thông tin gì ạ!")
    key = audiobot.listen()
    data =  wikipedia.summary(key,1)
    audiobot.speak_vn(data)
if __name__ == "__main__":
    s = -1
    while(s != 0):
        s = audiobot.listen()



    welcome()
    while TRUE:
        s = audiobot.listen()
        if(s==1):
            audiobot.speak_vn("vâng ạ!tôi sẽ đi ngay! hẹn gặp lại ạ!")
            break
        elif (s == 6):
            audiobot.speak_vn(timeai.time())
        elif(s == 7):
            audiobot.speak_vn(timeai.date())
        elif(s==8):
            web.google()
        elif(s==10):
            web.youtube()
        elif (s==9):
            web.facebook()
        elif (s==11):
            web.gmail()
        elif(s==2):
            app.zalo()
        elif(s==3):
            app.word()
        elif(s==4):
            app.excel()
        elif(s==5):
            app.powerpoint()
        elif(s==12):
            search()
        elif(s==13):
            weather.current_weather()