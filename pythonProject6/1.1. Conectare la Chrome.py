import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options=Options()
chrome_options.add_experimental_option("detach",True)
'''ca sa nu se mai inchida sesiunea'''

driver_service= Service(executable_path=r'C:\Users\Mirela\PycharmProjects\pythonProject6\chromedriver.exe')

driver = webdriver.Chrome(service=driver_service,options=chrome_options)

driver.get(url="https://www.python.org/")
time.sleep(3)