import audiobot
import keyboard
import os
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BotYoutube:
    def __init__(self):
        pathfile = os.getcwd()
        self.browser = webdriver.Chrome(f"{pathfile}\\seleniumFRIDAY\\chromedriver.exe")
        self.browser.maximize_window()
        sleep(random.randint(1,3))
        self.browser.get(f"https://www.youtube.com/")
        sleep(random.randint(4,7))

    def controll(self):
        audiobot.speak_vn("bạn cần tôi giúp gì ở youtube nào")
        try:
            while True:
                req = audiobot.listentotext()
                if("trang chủ" in req or "tin" in req):
                    self.trangchu()
                elif("tìm" in req):
                    self.timkiem()
                elif("xuống" in req):
                    self.cuonxuong()
                elif("lên" in req):
                    self.cuonglen()
                elif("thôi" in req or "dừng" in req or "thoát" in req):
                    break
                elif("video" in req):
                    self.video()
        finally:
            self.browser.quit()
            audiobot.speak_vn("youtube đã đóng")

    def trangchu(self):
        try:
            xpath = '/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[1]/a/tp-yt-paper-item'
            elements = self.browser.find_elements_by_xpath(xpath)
            print(elements)
            elements[0].click()
        except:
            pass

    def timkiem(self):
        try:
            xpath = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
            elements = self.browser.find_elements_by_xpath(xpath)
            print(elements)
            audiobot.speak_vn("Bạn muốn tìm gì")
            key = audiobot.listentotext()
            elements[0].send_keys(key)
            sleep(random.randint(2,3))
            elements[0].send_keys(Keys.ENTER)
        except:
            pass
    
    def cuonxuong(self):
        audiobot.speak_vn("phím cách để dừng, phím u để tăng tốc độ, phím d để giảm tốc độ")
        delay = 2
        html = self.browser.find_element_by_tag_name('html')
        while not keyboard.is_pressed("space"):
            html.send_keys(Keys.PAGE_DOWN)
            if(keyboard.is_pressed('u')):
                if(delay>0.2):
                    delay -= 0.2
            elif(keyboard.is_pressed('d')):
                delay += 0.2
            sleep(delay)
            keyboard.block_key("u")
            keyboard.block_key("d")
        keyboard.block_key("space")

    def cuonglen(self):
        audiobot.speak_vn("phím cách để dừng, phím u để tăng tốc độ, phím d để giảm tốc độ")
        delay = 2
        html = self.browser.find_element_by_tag_name('html')
        while not keyboard.is_pressed("space"):
            html.send_keys(Keys.PAGE_UP)
            if(keyboard.is_pressed('u')):
                if(delay>0.2):
                    delay -= 0.2
            elif(keyboard.is_pressed('d')):
                delay += 0.2
            sleep(delay)
            keyboard.block_key("u")
            keyboard.block_key("d")

    def video(self):
        pass
        # try:
        #     elements = self.browser.find_elements_by_id("details")
        #     sleep(random.randint(3,5))
        #     list_video = []
        #     # for element in elements:
        #     title_video = elements[0].find_element_by_id("video-title-link")
        #     title_video
        #     list_video.append(
        #         {
        #             "title": ""
        #         }
        #     )
        # except:
        #     pass