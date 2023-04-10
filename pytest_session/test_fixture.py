import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()

def test_3():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.facebook.com/")
    Title = driver.title
    print(Title)
    assert Title == "Facebook – log in or sign up"
    driver.quit()


def test_1():
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com")
    Title=driver.title
    print(Title)
    assert Title=="Google"
    driver.quit()

def test_t2():
    global driver
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.amazon.com/")
    assert driver.title == "Amazon.in : iphone"
    driver.quit()
