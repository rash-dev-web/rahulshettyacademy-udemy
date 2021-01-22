from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
mouse_hover = driver.find_element_by_id("mousehover")
action.move_to_element(mouse_hover).perform()
time.sleep(2)
element_top = driver.find_element_by_link_text("Top")
time.sleep(2)
action.move_to_element(element_top).click()
time.sleep(2)
driver.close()
