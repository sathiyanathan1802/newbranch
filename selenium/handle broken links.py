
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

link=driver.find_elements(By.TAG_NAME,"a")
count=0
for all in link:
    url=all.get_attribute("href")
    # try:
    #     res=requests.head(url)
    #
    # except:
    #     None

    if res.status_code>=400:
        print(url,"link is invalid")
        count=count+1
    else:
        print(url,"link is valid")

print("process completed....")


