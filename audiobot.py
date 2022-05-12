import os
from gtts import gTTS
import playsound
import speech_recognition
from train import nlp,model
import numpy as np
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
    pathsound = os.getcwd()+"\sound.mp3"
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
        print("you: " + s)
        s = np.array(model.predict_proba([nlp(s).vector]))
    except speech_recognition.UnknownValueError:
        return -1

    maxx = round(np.max(s[0]),2)
    print(maxx)
    if(maxx < 0.65):
        return -1
    for i in range(np.size(s)):
        if(round(s[0][i],2) == maxx):
            return i
    return -1
print(listen())
def listentotext():
    bot = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        print("F.R.I.D.A.Y: listening...")
        bot.pause_threshold = 1 #dung 2s roi nghe lenh moi
        audio = bot.listen(mic)
    s = ""
    try:
        s = bot.recognize_google(audio, language="vi-VN")
        print("you: "+s)
    except speech_recognition.UnknownValueError:
        return ""
    return s