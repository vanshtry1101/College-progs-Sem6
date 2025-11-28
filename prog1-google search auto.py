from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()


try:
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    print(f"Page title is :{driver.title }")
    search_box=driver.find_element(By.NAME,"q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)
    print("Enter Key Is Pressed")
    time.sleep(30)
    
    assert "Selenium" in driver.title
    print(f"new page title after search {driver.title}")
except Exception as e:
    print("An Error Occured",e)
finally:
    driver.quit()
    print("browser closed")    