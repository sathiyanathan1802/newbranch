from selenium import webdriver

from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

obj = webdriver.Chrome(ChromeDriverManager().install())

obj.get("https://www.oneplus.in/")

obj.maximize_window()

expectedtitle="OnePlus Official Site | OnePlus India"

actualtitle=obj.title

if expectedtitle==actualtitle:
    print("test case is passed")

else:
    print("test case is failed")