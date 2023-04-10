from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)


driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")   #It will open the url

driver.maximize_window()

min=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
max=driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")
print(min.location)
print(max.location)

act=ActionChains(driver)
act.drag_and_drop_by_offset(min,100,0).perform()
act.drag_and_drop_by_offset(max,-79,0,).perform()
