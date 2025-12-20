import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
path = os.path.abspath(r"d:\HimCoder\login.html")

try:
    driver.get(path)
    driver.maximize_window()
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "loginBtn").click()

    message = driver.find_element(By.ID, "message").text
    time.sleep(5)
    if message == "Login Successful":
        print("Test passed: ", message)
    else:
        print("Test Failed: ", message)
        assert message =="Login successful", "Login Unsuccessful"
except AssertionError as error:
    print("Assertion error", error)

except Exception as e:
    print("Error: ", e)

finally:
    driver.quit()