from datetime import datetime
from pickle import TRUE
import random
import wikipedia
import app
import timeai
import audiobot
import web
import weather
import Network
import Controller
import Volume
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
            gb = ["xin chào! hẹn gặp lại bạn","vâng ạ!tôi sẽ đi ngay! hẹn gặp lại ạ!","rất vui khi giúp đỡ bạn"]
            audiobot.speak_vn(gb[random.randint(0,len(gb))])
            break
        elif(s==2):
            audiobot.speak_vn("zalo")
            # app.zalo()
        elif(s==3):
            audiobot.speak_vn("word")
            # app.word()
        elif(s==4):
            audiobot.speak_vn("excel")
            # app.excel()
        elif(s==5):
            audiobot.speak_vn("powerpoint")
            # app.powerpoint()
        elif (s == 6):
            audiobot.speak_vn(timeai.time())
        elif(s == 7):
            audiobot.speak_vn(timeai.date())
        elif(s==8):
            audiobot.speak_vn("google")
            # web.google()
        elif (s==9):
            audiobot.speak_vn("facebook")
            # web.facebook()
        elif(s==10):
            audiobot.speak_vn("youtobe")
            # web.youtube()
        elif (s==11):
            audiobot.speak_vn("gmail")
            # web.gmail()
        elif(s==12):
            audiobot.speak_vn("wiki media")
            # search()
        elif(s==13):
            audiobot.speak_vn("thời tiết")
            # weather.current_weather()
        elif(s==14):
            # mạng
            audiobot.speak_vn("mạng")
            # Network.network()
        elif(s==15):
            # điều khiển
            audiobot.speak_vn("điều khiển")
            # Controller.dieukhien()
        elif(s==16):
            # âm lượng
            audiobot.speak_vn("âm lượng")
            # Volume.volume()
        else:
            audiobot.speak_vn("xin lỗi! tôi không hiểu bạn nói gì")