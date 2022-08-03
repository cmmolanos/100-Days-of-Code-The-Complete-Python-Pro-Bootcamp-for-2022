
from threading import Timer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import math


def buy_item():
    # Select the items in the store
    store = driver.find_elements(By.CSS_SELECTOR, "#store>div")
    # filter the items, if is gray in background we cannot afford it
    affordable_items = [item for item in store if item.get_attribute("class") != "grayed"]
    # Click to buy the most expensive item
    affordable_items[-1].click()


ser = Service("driver path")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

game_time = 300  # 5 minutes
game_start = time.time()
# select the 5 seconds intervals to buy items
buy_time = [game_start + 5 * buy_time for buy_time in range(1, math.floor(game_time / 5) + 1)]

cookie = driver.find_element(By.ID, 'cookie')
cookies_per_second = driver.find_element(By.ID, 'cps')


while time.time() < game_start + game_time:
    cookie.click()

    try:
        if time.time() > buy_time[0]:
            buy_item()
            buy_time.pop(0)

    except IndexError:  # cover when last buy was made but do not finish the game.
        pass

print(cookies_per_second.text)

driver.quit()
