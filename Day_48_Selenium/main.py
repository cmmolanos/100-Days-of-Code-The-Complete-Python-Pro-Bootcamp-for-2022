from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "driver path"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
events_dates = list(map(lambda x: x.text, driver.find_elements(By.CSS_SELECTOR, '.event-widget li time')))
events_titles = list(map(lambda x: x.text, driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')))

events = {n: {'time': events_dates[n], 'name': events_titles[n]} for n in range(len(events_dates))}
driver.quit()
print(events)
