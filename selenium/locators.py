from selenium import webdriver

from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

obj = webdriver.Chrome(ChromeDriverManager().install())

obj.get("https://www.facebook.com/")

obj.maximize_window()

obj.find_element(By.ID,"email").send_keys("sathiyanthancsa@gmail.com")
#
obj.find_element(By.ID,"pass").send_keys("Sagi@1802")

link12=obj.find_element(By.XPATH,"//button[text()='Log in']")
link12.click()

# link1=obj.find_element(By.LINK_TEXT,"Create new account")
# link1.click()
#
# obj.find_element(By.ID,"u_2_b_Br").send_keys("sathya")
# # obj.find_element(By.CLASS_NAME,"lastname").send_keys("nathan")
# # obj.find_element(By.CLASS_NAME,"reg_email__").send_keys("sathya@gmail.com")
# # obj.find_element(By.CLASS_NAME,"reg_passwd__").send_keys("sathya")
# # # obj.find_element(By.CLASS_NAME,"birthday_day").send_keys("18")


obj.close()