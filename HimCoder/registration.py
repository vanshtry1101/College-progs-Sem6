from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("D:/HimCoder/registration.html")

time.sleep(2)
driver.find_element(By.ID,"fname").send_keys("kh")
driver.find_element(By.ID,"lname").send_keys("ha")
driver.find_element(By.ID,"email").send_keys("kha@gmail.com")
driver.find_element(By.ID,"password").send_keys("1234")


