from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://demo.automationtesting.in/Frames.html")   #It will open the url

driver.maximize_window()

driver.switch_to.frame(0)

frame1=driver.find_element(By.XPATH,"//input[@type='text']").send_keys("sathya")

driver.switch_to.default_content()

driver.find_element(By.XPATH,"//a[text()='Iframe with in an Iframe']").click()

outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)
innerframe=driver.find_element(By.XPATH,"//h5[text()='Nested iFrames']/following-sibling::iframe")
driver.switch_to.frame(innerframe)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("sathya")
driver.switch_to.parent_frame()
text=driver.find_element(By.XPATH,"//h5[text()='Nested iFrames']").text
print(text)


driver.switch_to.default_content()

click1=driver.find_element(By.XPATH,"//a[@href='WebTable.html']").click()
