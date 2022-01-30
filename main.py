from selenium import webdriver
import time

window = webdriver.Chrome("E:\selenium\chromedriver_win32\chromedriver.exe")
window.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(2)

cookie = window.find_element_by_id("bigCookie")
shop_products = window.find_elements_by_xpath("/html/body/div[2]/div[2]/div[19]/div[3]/div[6]/*")
upgrades = window.find_elements_by_xpath("/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/*")
upgrades.reverse()
shop_products.reverse()

clicks = 0
up = 0

def buy_items():
    buy_more = False
    for item in shop_products:
        if item.get_attribute("class") == "product unlocked enabled":
            item.click()
            buy_more = True
            break
    if buy_more == True:
        buy_items()
def buy_upgrade():
    upgrade_more = False
    for item in upgrades:
        if item.get_attribute("class") == "crate upgrade enabled":
            item.click()
            break
    if upgrade_more == True:
        buy_upgrade()
while True:
    cookie.click()
    clicks+=1
    up+=1
    if clicks == 100:
        buy_items()
        clicks = 0
    if up == 200:
        buy_upgrade()
        up = 0