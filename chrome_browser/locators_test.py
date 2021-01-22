from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Mir")
time.sleep(3)
select_gender = Select(driver.find_element_by_id("exampleFormControlSelect1"))
select_gender.select_by_index(1)
time.sleep(3)
driver.find_element_by_xpath("//input[@value='Submit']").click()
time.sleep(5)
success_text = driver.find_element_by_xpath("//strong[text()='Success!']").text
print(success_text)
assert "Success1" in success_text
driver.close()
