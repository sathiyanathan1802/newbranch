import pytest

def test_fill():
    import time
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get("https://www.facebook.com/")
    user=driver.find_element(By.XPATH,"//input[@type='text']")
    user.send_keys("sathya")
    password=driver.find_element(By.XPATH,"//input[@type='password']").send_keys("sathya")
    button = driver.find_element(By.XPATH, "//button[@name='login']").click()





