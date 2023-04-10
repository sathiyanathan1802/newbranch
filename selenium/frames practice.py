

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://chercher.tech/practice/frames")   #It will open the url

driver.maximize_window()

frame1=driver.find_element(By.XPATH,"//iframe[@id='frame1']")
driver.switch_to.frame(frame1)
inputtext=driver.find_element(By.XPATH,"//b[text()='Topic :']/following-sibling::input")
inputtext.send_keys("sathya")

frame3=driver.find_element(By.XPATH,"//iframe[@id='frame3']")
driver.switch_to.frame(frame3)
checkbox=driver.find_element_by_id("a")
checkbox.click()

driver.switch_to.default_content()

frame2=driver.find_element(By.XPATH,"//iframe[@id='frame2']")
driver.switch_to.frame(frame2)
dropdown=driver.find_element(By.XPATH,"//select[@id='animals']")
s=Select(dropdown)
s.select_by_visible_text("Big Baby Cat")

driver.find_element(By.XPATH,"//a[text()='Selenium [Python]']").click()





