import security
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def open_facebook(username,password,browser):
    browser.get(f"http://facebook.com")
    txtUser = browser.find_element_by_id("email")
    txtPass = browser.find_element_by_id("pass")
    txtUser.send_keys(username)
    sleep(random.randint(1,2))
    txtPass.send_keys(password)
    sleep(random.randint(1,2))
    txtPass.send_keys(Keys.ENTER)
    sleep(random.randint(1,2))
def click_thongbao(browser):#dang loi
    browser.execute_script('document.querySelector("#mount_0_0_Zy > div > div:nth-child(1) > div > div:nth-child(4) > div.ehxjyohh.kr520xx4.poy2od1o.b3onmgus.hv4rvrfc.n7fi1qx3 > div.du4w35lb.l9j0dhe7.byvelhso.rl25f0pe.j83agx80.bp9cbjyn > div:nth-child(2) > span > span > div > a > div")')
def click_search(browser):#dang loi
    browser.browser.execute_script('document.querySelector("#mount_0_0_Zy > div > div:nth-child(1) > div > div:nth-child(4) > div.rq0escxv.byvelhso.q10oee1b.poy2od1o.j9ispegn.kr520xx4.ooia0uwo.kavbgo14.mhnrfdw6 > div > div > div > div > div > label > input").click()')
def search_facebook(browser,key):
    txtSearch = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div/div/div/label/input")
    txtSearch.send_keys(key)
    sleep(6.5)
    txtSearch.send_keys(Keys.ENTER)
def cuon_xuong(browser,n):
    browser.execute_script("window.scroll(0,%d)" %int(n))
if __name__ == "__main__":
    browser = webdriver.Chrome(r"C:\Users\Administrator\Documents\workspace\python\friday\chromedriver.exe")
    try :
        open_facebook(security.USERNAME,security.PASSWORD,browser)
        sleep(random.randint(5,7))
        # search_facebook(browser,"ptit")
        # click_search(browser)
        # cuon_xuong(browser, 200)
        click_thongbao(browser)
        sleep(random.randint(1,2))
    finally:
        browser.quit()