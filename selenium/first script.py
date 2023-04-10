

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

obj = webdriver.Chrome(ChromeDriverManager().install())

obj.get('https://www.facebook.com/')

obj.maximize_window()
sathya=obj.title
print(sathya)

url=obj.current_url
print(url)
obj.close()
