import audiobot
import keyboard
from seleniumFRIDAY import security
import os
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BotFB:
    def __init__(self):
        pathfile = os.getcwd()
        self.browser = webdriver.Chrome(f"{pathfile}\\seleniumFRIDAY\\chromedriver.exe")
        self.browser.maximize_window()
        sleep(random.randint(1,3))
        self.browser.get(f"http://facebook.com")
        txtUser = self.browser.find_element_by_id("email")
        txtPass = self.browser.find_element_by_id("pass")
        txtUser.send_keys(security.USERNAME)
        sleep(random.randint(1,2))
        txtPass.send_keys(security.PASSWORD)
        sleep(random.randint(1,2))
        txtPass.send_keys(Keys.ENTER)
        sleep(random.randint(4,7))
    
    def controll(self):
        audiobot.speak_vn("bạn cần tôi giúp gì ở facebook nào")
        try:
            while True:
                req = audiobot.listentotext()
                if("trang chủ" in req or "tin" in req):
                    self.trangchu()
                elif("thông báo" in req):
                    self.thongbao()
                elif("tìm" in req):
                    self.timkiem()
                elif("xuống" in req):
                    self.cuonxuong()
                elif("lên" in req):
                    self.cuonglen()
                elif("thôi" in req or "dừng" in req or "thoát" in req):
                    break
        finally:
            self.browser.quit()
            audiobot.speak_vn("facebook đã đóng")

    def trangchu(self):
        try:
            xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a'
            elements = self.browser.find_elements_by_xpath(xpath)
            elements[0].click()
        except:
            pass

    def thongbao(self):
        try:
            xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div[4]/div[1]/div[1]/span/span/div/a'
            elements = self.browser.find_elements_by_xpath(xpath)
            elements[0].click()
        except:
            pass
    
    def timkiem(self):
        try:
            xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label'
            elements = self.browser.find_elements_by_xpath(xpath)
            audiobot.speak_vn("Bạn muốn tìm gì")
            key = audiobot.listentotext()
            elements[0].send_keys(key)
            sleep(random.randint(2,3))
            elements[0].send_keys(Keys.ENTER)
        except:
            pass
    
    def cuonxuong(self):
        audiobot.speak_vn("phím cách để dừng, phím u để tăng tốc độ, phím d để giảm tốc độ")
        heightmax = self.browser.execute_script("return document.body.scrollHeight")
        step = 100
        delay = 0.3
        n = step
        while not keyboard.is_pressed("space"):
            self.browser.execute_script("window.scroll(0,%d)" %int(n))
            heightmax = self.browser.execute_script("return document.body.scrollHeight")
            n += step
            if(n >= heightmax):
                break
            if(keyboard.is_pressed('u')):
                if(delay>0.1):
                    delay -= 0.07
            elif(keyboard.is_pressed('d')):
                delay += 0.07
            keyboard.unhook_all_hotkeys
            sleep(delay)
            
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
            keyboard.unhook_all_hotkeys
            sleep(delay)