from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from time import sleep
#open Chrome
driver = webdriver.Chrome()
#navigate to the site
driver.get("https://books.toscrape.com/")

sleep(2)
button=driver.find_element(By.XPATH,'//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[2]/article/div[1]/a')
# driver.execute_script("window.scrollBy(0, 2000)")
sleep(2)
button.send_keys(Keys.RETURN)
sleep(2)
driver.close()

#find the h1 element
# h1 = driver.find_element(By.CSS_SELECTOR, "h1")
#print the h1 element
# print(f"H1 element: {h1.text}")

# print(f"button element: {button.text}")