from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
input_text = "Mir"
driver.find_element_by_css_selector("#name").send_keys(input_text)
driver.find_element_by_css_selector("#alertbtn").click()
time.sleep(3)
alert = driver.switch_to.alert
alert_text = alert.text
assert input_text in alert_text
alert.accept()
alert.dismiss()
time.sleep(2)


driver.close()