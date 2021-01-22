from selenium import webdriver
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("--headless")
chrome_option.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome("../drivers/chromedriver.exe", options=chrome_option)
# driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Test")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script("return document.getElementsByName('name')[0].value;"))
shop_link = driver.find_element_by_link_text("Shop")
driver.execute_script("arguments[0].click()", shop_link)
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(3)
driver.close()
