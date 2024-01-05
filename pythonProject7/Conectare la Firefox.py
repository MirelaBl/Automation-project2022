import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location= r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver_service= Service(executable_path=r'C:\Users\Mirela\PycharmProjects\pythonProject6\geckodriver.exe')
driver = webdriver.Chrome(service=driver_service, options = Options)
time.sleep(3)