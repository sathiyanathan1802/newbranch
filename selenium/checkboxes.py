

import time

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

driver= webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
check=driver.find_elements(By.XPATH,"//input[contains(@id,'day')]")

# for box in check:
#     box.click()


# for box in check:
#     weekname=box.get_attribute("id")
#     if weekname=="monday" or weekname=="tuesday":
#         box.click()


length=len(check)

# for i in range(0,2):
#     check[i].click()
#
# for s in check:
#     if s.is_selected():
#         s.click()

for i in check:
    i.click()

for s in check:
    if s.is_selected():
        s.click()




