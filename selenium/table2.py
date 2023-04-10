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
column=len(noofcolumn)
for r in range(2,row+1):
    for c in range(1,column+1):
        data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text

        print(data)
print()


for r in range(2,row+1):
    author=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if author=="Amit":
        bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        subject=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[3]").text
        prices=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[4]").text
        print(author,"  ",bookname,"  ",prices)

cost=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr/td[4]")

sum=0
for p in cost:
    price=int(p.text)
    sum=sum+price
    print(p.text)


print("total of books price",sum)
