import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("init_driver")
class Test():      #Base class
    pass
@pytest.mark.parametrize ("username,password",
                          [("sathiya@gamil.com","123456123"),
                          ("sathya@gmail.com","789123456"),
                            ("agil@gamil.com","132548455")])
class Test_fb(Test):
    def test_login(self,username,password):
        self.driver.get("https://www.facebook.com")
        self.driver.find_element(By.ID,"email").send_keys(username)
        self.driver.find_element(By.ID,"pass").send_keys(password)
        self.driver.find_element(By.XPATH,"//button[@name='login']").click()


        time.sleep(5)

