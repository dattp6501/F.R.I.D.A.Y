import random
from time import sleep
from selenium import webdriver
import botfb
import security
import audiobot
def control():
    # 100.0.4896.127
    browser = webdriver.Chrome(r"F.R.I.D.A.Y/seleniumFRIDAY/chromedriver.exe")
    botfb.open_facebook(security.USERNAME,security.PASSWORD,browser)
    sleep(random.randint(10,15))
    ask = ""
    while(ask != "dừng"):
        ask = audiobot.listen()
        if(ask == "tìm kiếm"):
            botfb.search_facebook(browser,"trương phúc đạt")
            sleep(random.randint(6,10))
        botfb.cuon_xuong(browser,100)
        sleep(random.randint(5,8))
        ask = "dừng"
if __name__ == "__main__":
    control()