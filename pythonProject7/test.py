from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# Setup chrome driver
driver = webdriver.Chrome()
# Navigate to the url
driver.get("http://www.python.org")
# Get the element by id
element_id = driver.find_element("id", "community")
##OR
##driver.find_element(By.ID, "community")
print("My element_id is:",element_id)
element_id.click()
try:
    element = driver.find_element(By.ID, "python-network")
    print("The element with id ",element," exists.")
except NoSuchElementException:
    print("The element does not exist.")
# Get the element by LINK_TEXT
linktest_element = driver.find_element(By.LINK_TEXT, "Docs")
print("My element linktest_element is:",linktest_element)
# Get the element by XPATH
xpath_element = driver.find_element(By.XPATH, "//div[@id='top']/nav/div[@class='skip-link screen-reader-text']")
print("My element xpath_element is:",xpath_element)
# Close the driver
driver.close()

uhfgufhjhghf
