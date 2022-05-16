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
                elif("video" in req):
                    self.trangchu()
                    sleep(random.randint(3,4))
                    list_video = self.read_video_home()
                    list_video[0]["element video"].click()
                elif("thôi" in req or "dừng" in req or "thoát" in req):
                    break
        finally:
            self.browser.quit()
            audiobot.speak_vn("youtube đã đóng")

    def trangchu(self):
        try:
            xpath = '/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[1]/a'
            elements = self.browser.find_elements_by_xpath(xpath)
            elements[0].click()

            # list_video = self.read_video_home()
            # sleep(random.randint(3,4))
            # list_video[0]["element video"].click()
        except:
            pass

    def timkiem(self):
        # try:
            xpath = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
            elements = self.browser.find_elements_by_xpath(xpath)
            audiobot.speak_vn("Bạn muốn tìm gì")
            key = audiobot.listentotext()
            elements[0].send_keys(key)
            sleep(random.randint(2,3))
            elements[0].send_keys(Keys.ENTER)
            sleep(random.randint(3,5))

            list_video = self.read_video_search()
            sleep(random.randint(3,5))
            print(list_video[0])
            list_video[0]["element video"].click()

        # except:
        #     pass
    
    def cuonxuong(self):
        try:
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
                keyboard.clear_all_hotkeys
        except:
            pass

    def cuonglen(self):
        try:
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
                keyboard.clear_all_hotkeys
        except:
            pass

    def read_video_search(self):
        list_video = []
        # try:
        xpath_hangs = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer'
        sohang = len(self.browser.find_elements_by_xpath(xpath_hangs))
        sleep(random.randint(3,5))
        print(f"có :{sohang} video")
        
        for i in range(1,sohang+1):
            # tieu de video  /html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[2]/ytd-channel-name/div/div/yt-formatted-string/a      
            xpath_tieude = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[2]/ytd-channel-name/div/div/yt-formatted-string/a'
            element_tieude = self.browser.find_element_by_xpath(xpath_tieude)
            tieude_video = element_tieude.text
            
            # element de vao kenh
            xpath_kenh = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[2]/ytd-channel-name/div/div/yt-formatted-string/a'
            kenh = self.browser.find_element_by_xpath(xpath_kenh)
            # ten kenh
            ten_kenh = kenh.text
            #                 /html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow/img
            xpath_element = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/ytd-thumbnail/a/yt-img-shadow/img'
            element = self.browser.find_element_by_xpath(xpath_element)
            
            list_video.append(
                {
                    "ten kenh" : ten_kenh,
                    "element kenh": kenh,
                    "element video" : element,
                    "tieu de" : tieude_video
                }
            )
        return list_video
        # except:
        #     pass
        # return list_video

    def read_video_home(self):
        try:
            xpath_hangs = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row'
            xpath_cots = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer'
            sohang = len(self.browser.find_elements_by_xpath(xpath_hangs))
            socot = len(self.browser.find_elements_by_xpath(xpath_cots))
            sleep(random.randint(3,5))
            print(sohang,socot)
            list_video = []
            for i in range(1,sohang+1):
                for j in range(1,socot+1):
                    # tieu de video
                    #               /html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[2]/div[1]/h3/a
                    xpath_tieude = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[{i}]/div/ytd-rich-item-renderer[{j}]/div/ytd-rich-grid-media/div[1]/div[2]/div[1]/h3/a'
                    element_tieude = self.browser.find_element_by_xpath(xpath_tieude)
                    tieude_video = element_tieude.text
                    # ten kenh
                    xpath_ten_kenh = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[{i}]/div/ytd-rich-item-renderer[{j}]/div/ytd-rich-grid-media/div[1]/div[2]/div[1]/ytd-video-meta-block/div[1]/div[1]/ytd-channel-name'
                    element_ten_kenh = self.browser.find_element_by_xpath(xpath_ten_kenh)
                    ten_kenh = element_ten_kenh.text
                    # element de vao kenh
                    xpath_kenh = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[{i}]/div/ytd-rich-item-renderer[{j}]/div/ytd-rich-grid-media/div[1]/div[2]/a/yt-img-shadow'
                    kenh = self.browser.find_element_by_xpath(xpath_kenh)
                    #               /html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[1]/div
                    xpath_element = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[{i}]/div/ytd-rich-item-renderer[{j}]/div'
                    element = self.browser.find_element_by_xpath(xpath_element)
                    
                    list_video.append(
                        {
                            "ten kenh" : ten_kenh,
                            "element kenh": kenh,
                            "element video" : element,
                            "tieu de" : tieude_video
                        }
                    )
            return list_video
        except:
            pass
        return None