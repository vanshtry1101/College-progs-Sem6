from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("D:\\New folder\\py1.html")

time.sleep(2)

table = driver.find_element(By.ID, "marksTable")
all_rows = table.find_element(By.TAG_NAME,"tr")
rows = all_rows[1:]

any_subject_count = 0
all_subject_count = 0

for row in rows:
    cells = row.find_elements(By.TAG_NAME,"td")
    name = cells[0].text
    maths = int(cells[1].text)
    science = int(cells[2].text)
    english = int(cells[3].text)
    marks = [maths,science,english]
    print("marks:",marks)

    if marks[0] > 60 or marks[1] > 60 or marks[3] > 60 :
        any_subject_count += 1
        print(f"{name} scored > 60 in at least one subject")
    if all(mark > 60 for mark in marks) :
        any_subject_count += 1
        print(f"{name} scored > 60 in at least one subject")

print("\nAnalysis Result:")
print("Student with >60 in any subject : ")
print("Student with >60 in all subject : ")

driver.quit()                                                                                                                             