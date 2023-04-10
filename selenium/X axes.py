from selenium import webdriver

from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

obj = webdriver.Chrome(ChromeDriverManager().install())

obj.get("https://www.google.com/")

obj.maximize_window()


obj.find_element(By.XPATH,"//h2[@class='_8eso']/parent::*")


# # x path axes
# "//div[@class='RNNXgb']/ancestor::*"
# "//div[@class='RNNXgb']/descendant::*"
# "//div[@class='RNNXgb']/preceding::*"
# "//div[@class='RNNXgb']/following::*"
# "//div[@class='RNNXgb']/preceding-sibling::*"
# "//div[@class='RNNXgb']/following-sibling::*"
