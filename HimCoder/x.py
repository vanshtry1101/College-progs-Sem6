from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Selenium Manager will automatically pick correct ChromeDriver
driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    print("Google opened.")

    # Wait until Google loads the search box
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("YouTube")
    search_box.send_keys(Keys.RETURN)

    # Wait until search results load
    first_result = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "h3"))
    )
    first_result.click()

    print("Website opened automatically!")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
    print("Program finished.")
