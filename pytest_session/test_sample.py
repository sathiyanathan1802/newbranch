import pytest
import webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("init_driver")

class Demo:
    pass
@pytest.mark.parametrize("username,password",[("sathya1323@gmail.com","123451236"),("sathyaaaacsaerf@gamil.com","12348735")])

class Test(Demo):
    def test_google(self,username,password):
        self.driver.get("https://www.facebook.com")
        self.driver.find_element(By.ID, "email").send_keys(username)
        self.driver.find_element(By.ID, "pass").send_keys(password)
class Test_url(Demo):
    def test_url(self):
        self.driver.get("https://www.facebook.com")
        assert self.driver.current_url == "https://www.googl.com"




