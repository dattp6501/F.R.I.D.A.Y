from datetime import datetime
import os
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
import train
import pandas as pd
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
    # create model
    model = train.MyModel()
    pathfile = os.getcwd()
    x_data,y_data = model.read_file_excel(f"{pathfile}\\train.xlsx")
    # train
    model.fit(x_data,y_data)
    # test
    x_test,y_test = model.read_file_excel(f"{pathfile}\\test.xlsx")
    print("độ chính xác: " + str(model.score(x_test,y_test)))
    # start 
    label,p = -1,0
    ok = 0.5
    while(label!=0 or ok>=p):
        label,p = audiobot.listen(model)
        print(f"{label}, {p}")

    welcome()
    df = pd.read_excel(f"{pathfile}\\train.xlsx")
    options = list(str(i) for i in df.head(0))
    print(options,sep=", ")

    while TRUE:
        label,p = audiobot.listen(model)
        print(f"{label}, {p}")
        if(ok>=p):
            audiobot.speak_vn("xin lỗi! tôi không hiểu bạn nói gì")
            continue

        if(label==1):
            gb = ["xin chào! hẹn gặp lại bạn","vâng ạ!tôi sẽ đi ngay! hẹn gặp lại ạ!","rất vui khi giúp đỡ bạn"]
            for j in df[df.keys()[1]]:
                gb.append(j)
            audiobot.speak_vn(gb[random.randint(0,len(gb)-1)])
            break
        elif(label==2):
            # audiobot.speak_vn("zalo")
            app.zalo()
        elif(label==3):
            # audiobot.speak_vn("word")
            app.word()
        elif(label==4):
            # audiobot.speak_vn("excel")
            app.excel()
        elif(label==5):
            # audiobot.speak_vn("powerpoint")
            app.powerpoint()
        elif (label == 6):
            audiobot.speak_vn(timeai.time())
        elif(label == 7):
            audiobot.speak_vn(timeai.date())
        elif(label==8):
            # audiobot.speak_vn("google")
            web.google()
        elif (label==9):
            # audiobot.speak_vn("facebook")
            web.facebook()
        elif(label==10):
            # audiobot.speak_vn("youtobe")
            web.youtube()
        elif (label==11):
            # audiobot.speak_vn("gmail")
            web.gmail()
        elif(label==12):
            # audiobot.speak_vn("wiki media")
            search()
        elif(label==13):
            # audiobot.speak_vn("thời tiết")
            weather.current_weather()
        elif(label==14):
            # mạng
            # audiobot.speak_vn("mạng")
            Network.network()
        elif(label==15):
            # điều khiển
            # audiobot.speak_vn("điều khiển")
            Controller.dieukhien()
        elif(label==16):
            # âm lượng
            # audiobot.speak_vn("âm lượng")
            Volume.volume()
        elif(label==17):
            # show các chức năng
            audiobot.speak_vn("các chức năng")
            for i in range(2,len(options)-1):
                audiobot.speak_vn(options[i])