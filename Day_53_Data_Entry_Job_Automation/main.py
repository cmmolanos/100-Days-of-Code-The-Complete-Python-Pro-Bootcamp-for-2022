import requests
import json
import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


FORMULARY_URL = "form link"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
             "%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22" \
             "%3A37.66978948403931%2C%22north%22%3A37.880643083037015%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22" \
             "%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1" \
             "%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B" \
             "%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C" \
             "%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B" \
             "%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22days%22%7D%7D%2C%22isListVisible%22%3Atrue%7D"

CHROME_DRIVER = os.environ['PATH_CHROME_DRIVER']
headers = {
    "accept-language": 'en-US,en;q=0.9',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, br",
}

# Step 1: get all the information with bs4
response = requests.get(url=ZILLOW_URL, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

scripts = soup.find_all(name="script", type="application/json")
script_mobile = json.loads(scripts[1].text.lstrip('<!--').rstrip('--!>'))
list_of_results = script_mobile['cat1']['searchResults']['listResults']

zillow_domain = "https://www.zillow.com"
links = [zillow_domain + result['detailUrl'] if zillow_domain not in result['detailUrl'] else result['detailUrl']
         for result in list_of_results]

prices = []
for result in list_of_results:
    try:
        prices.append(result["price"])
    except KeyError:
        prices.append(result["units"][0]["price"])

addresses = [result["address"] for result in list_of_results]


# Step 2: push the information to google form
ser = Service(CHROME_DRIVER)
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)


for address, price, link in zip(addresses, prices, links):
    driver.get(FORMULARY_URL)

    questions = driver.find_elements(By.CSS_SELECTOR, "input.whsOnd.zHQkBf")
    button = driver.find_element(By.CSS_SELECTOR, "span.l4V7wb.Fxmcue")

    time.sleep(0.01)

    questions[0].send_keys(address)
    questions[1].send_keys(price)
    questions[2].send_keys(link)
    button.click()

driver.quit()





