# https://rahulshettyacademy.com/dropdownsPractise/

from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(3)
countries = driver.find_elements_by_css_selector("[class='ui-menu-item'] a")


for country in countries:
    if country.text == "India":
        country.click()
        break
time.sleep(3)
driver.close()
