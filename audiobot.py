import os
from gtts import gTTS
import playsound
import speech_recognition
from intent import nlp,neigh,label
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
    # bot = speech_recognition.Recognizer()
    # with speech_recognition.Microphone() as mic:
    #     print("F.R.I.D.A.Y: listening...")
    #     bot.pause_threshold = 1 #dung 2s roi nghe lenh moi
    #     audio = bot.listen(mic)
    s = "giáo sư"
    try:
        # s = bot.recognize_google(audio, language="vi-VN")
        print("you: "+s)
        s = neigh.predict([nlp(s).vector])
    except speech_recognition.UnknownValueError:
        return -1
    return s[0]
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