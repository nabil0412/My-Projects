from selenium import webdriver
import time
import pickle
import os

def save_cookies(driver):
    browser_cookies = driver.get_cookies()
    filename = "./cache/browser_cookies.pkl"
    with open(filename, "wb") as f:
        pickle.dump(browser_cookies, f)

def load_cookies(driver):
    cookies=[]
    filename = "./cache/browser_cookies.pkl"
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            cookies = pickle.load(f)

    for cookie in cookies:
        driver.add_cookie(cookie)        



chrome_driver_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
load_cookies(driver)
driver.refresh()

#Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

#Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items if len(item.get_attribute("id")) != 0]
print(item_ids)


timeout = time.time() + 5
five_min = time.time() + 60*5 # 5minutes

while True:
    
    cookie.click()

    #Every 5 seconds:
    if time.time() > timeout:

        save_cookies(driver)

        #Fetch <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        #Get price as an integer
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        #Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        #Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        #Find affordable upgrades currently
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                 affordable_upgrades[cost] = id

        #Purchase the most expensive of the affordable upgrade
        print(affordable_upgrades)
        if len(affordable_upgrades) == 0:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            #print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element_by_id(to_purchase_id).click()
            
        #5 seconds until the next check
        timeout = time.time() + 5

    
