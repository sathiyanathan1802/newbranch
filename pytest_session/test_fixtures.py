import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='module')
def init_setup():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield
    print("...Tear down...")

def test_title(init_setup):       #apporoach 1
    assert driver.title=="Google"
    driver.quit()
# @pytest.mark.usefixtures("init_setup")
# def test_fburl():
#     assert driver.current_url=="https://www.facebook.com/"
