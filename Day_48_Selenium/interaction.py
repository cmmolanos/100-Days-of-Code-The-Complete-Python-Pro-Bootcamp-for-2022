from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys


driver = webdriver.Chrome(executable_path="driver path")

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# n_articles = int(driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]').text.replace(",", ""))
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, 'fName')
f_name.send_keys("Carlos")

l_name = driver.find_element(By.NAME, 'lName')
l_name.send_keys("Molano")

email = driver.find_element(By.NAME, 'email')
email.send_keys("cmmolanos@gmail.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()

#driver.quit()

