import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)


driver.get("https://en.wikipedia.org/wiki/Main_Page")   #It will open the url

#Scroll down page by pixel

driver.maximize_window()
driver.execute_script("window.scrollBy(0,1500);")
value=driver.execute_script(("return window.pageYOffset;"))
print("Number of pixcel moved:",value)

# Scrolll down page titll the element to element is visible
element=driver.find_element_by_id("From_today's_featured_article")
driver.execute_script("arguments[0].scrollIntoView();",element)
value=driver.execute_script(("return window.pageYOffset;"))
print("Number of pixcel moved:",value)

time.sleep(2)

element1=driver.find_element_by_id("Other_areas_of_Wikipedia")
driver.execute_script("arguments[0].scrollIntoView();",element1)
value=driver.execute_script(("return window.pageYOffset;"))
print("Number of pixcel moved:",value)
