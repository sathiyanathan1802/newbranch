import time

import driver as driver
from _multiprocessing import send
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

noofrow=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
row=len(noofrow)
noofcolumn=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
colum=len(noofcolumn)

for r in range(2,row+1):
    for c in range(1,colum+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(data)
    print()

print()

for r in range(2,row+1):
    author=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]")

    if author=="Amod":
        bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        subject= driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[3]").text
        price=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[3]").text

        print(bookname,"  ",subject,"  ",price)


