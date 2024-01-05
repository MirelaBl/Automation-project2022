import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

driver_service= Service(executable_path=r'C:\Users\Mirela\PycharmProjects\pythonProject7\chromedriver.exe')

driver = webdriver.Chrome(service=driver_service)
driver.get("http://www.python.org")
##time.sleep(10)
##driver.close()