# ce707b402145926a2f7e42eeaab3a8d8
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
import requests
import audiobot
from model import Weather
def current_weather():
    audiobot.speak_vn("Bạn muốn xem thời tiết thành phố nào")
    city = audiobot.listentotext()
    if not city:
        pass
    api_key = "ce707b402145926a2f7e42eeaab3a8d8"
    call_url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric&lang=vi"
    response = requests.get(call_url)
    data_json = response.json()
    if data_json["cod"] == "404":
        audiobot.speak_vn("tên thành phố không tồn tại")
        return
    city_res = data_json["main"]
    wther = data_json["weather"][0]
    sys = data_json["sys"]
    wther_current = Weather.Weather(data_json["name"],city_res["temp"],data_json["visibility"],city_res["pressure"],city_res["temp_min"],city_res["temp_max"],city_res["humidity"],sys["sunrise"],sys["sunset"],wther["description"])
    audiobot.speak_vn(wther_current.out())
if __name__ == "__main__":
    current_weather()