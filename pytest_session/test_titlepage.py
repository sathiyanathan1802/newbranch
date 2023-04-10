

import pytest


def test_title():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.facebook.com/")
    Title=driver.title
    print(Title)
    assert Title=="Facebook – log in or sign up"

