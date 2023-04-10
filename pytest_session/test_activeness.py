import pytest

def test_active():
    import time
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.facebook.com/")
    driver.maximize_window()
    forgotten=driver.find_element(By.XPATH,"//a[contains(text(),'Forgotten password?')]")
    print(forgotten.is_enabled())



