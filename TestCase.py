import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://computer-database.gatling.io/")
time.sleep(2)
driver.find_element(By.ID, 'add').click()
time.sleep(2)
driver.find_element(By.ID, 'name').send_keys('Asus Vivobook E410MA')
driver.find_element(By.ID, 'introduced').send_keys('2017-02-23')
driver.find_element(By.ID, 'discontinued').send_keys('2019-12-01')
selectDropDown = driver.find_element(By.ID, 'company')
dropDownValue = Select(selectDropDown)
dropDownValue.select_by_index(36)
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='Create this computer']").click()

                                    ## SEARCH

time.sleep(2)
driver.find_element(By.ID, "searchbox").send_keys("ASUS")
time.sleep(2)
driver.find_element(By.ID, "searchsubmit").click()

