from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    print(f"Page title is : {driver.title}")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("WWE")
    search_box.send_keys(Keys.RETURN)
    time.sleep(300)
    assert "WWE" in driver.title
    print(f"New Page title after search {driver.title}")

except Exception as e:
    print("An error occured", e)

finally:
    driver.quit()
    print("Browser Closed")
