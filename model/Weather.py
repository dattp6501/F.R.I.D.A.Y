import datetime


class Weather():
    def __init__(self,city,temp,visibility,pressure,temp_min,temp_max,humidity,sunrise,sunset,description):
        self.city = city # thanh pho
        self.temp = temp # nhiet do
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.visibility = visibility # tam nhin xa
        self.pressure = pressure # ap suat khong khi
        self.humidity = humidity # độ ẩm
        self.sunrise = datetime.datetime.fromtimestamp(sunrise).strftime("%H:%M") # bình minh or mặt trời mọc
        self.sunset = datetime.datetime.fromtimestamp(sunset).strftime("%H:%M") # hoàng hôn or mặt trời lặn
        self.description = description # mô tả thời tiết
        
    def out(self):
        return f"""{self.city} hôm nay nhiệt độ là {self.temp} độ C
        trời hôm nay {self.description}
        tầm nhìn xa {int(self.visibility/1000)} km
        áp suất không khi {self.pressure}
        độ ẩm {self.humidity} %
        bình minh vào {self.sunrise}, hoàng hôn vào {self.sunset}
        """