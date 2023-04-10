import pytest

from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# driver=webdriver.Chrome(ChromeDriverManager().install())

@pytest.mark.usefixtures("init_driver")
class Basetest:
    pass

class Test_chrome(Basetest):
    def test_google(self):
        self.driver.get("https://www.google.com")
        self.driver.maximize_window()
        assert self.driver.title=="Google"

class Test_firefox(Basetest):
    def test_firefox(self):
        self.driver.get("https://www.facebook.com")
        self.driver.maximize_window()
        assert self.driver.current_url=="https://www.facebook.com"





