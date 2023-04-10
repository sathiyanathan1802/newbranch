import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://letcode.in/dropdowns")   #It will open the url

driver.maximize_window()
down=driver.find_element(By.XPATH,"//select[@id='fruits']")
s=Select(down)
s.select_by_index(2)
drop=driver.find_element(By.XPATH,"//select[@id='superheros']")
s=Select(drop)
print(s.is_multiple)                #is display no of elements
s.select_by_value("ek")
s.select_by_index(4)
s.select_by_visible_text("Captain Marvel")
# s.deselect_by_index(4)




alloptions=s.options

for options in alloptions:
    txt=options.text
    print(txt)

