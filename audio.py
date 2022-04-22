import os
from gtts import gTTS
import playsound
import speech_recognition
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