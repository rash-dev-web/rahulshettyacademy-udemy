from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

APP_URL = "https://rahulshettyacademy.com/angularpractice/"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("../drivers/chromedriver.exe", options=options)


driver.get(APP_URL)
driver.find_element_by_link_text("Shop").click()
mobile_products = driver.find_elements_by_xpath("//div[@class='card-body']")
for mobile in mobile_products:
    if mobile.find_element_by_xpath("h4/a").text == "Blackberry":
        mobile.find_element_by_xpath("following-sibling::div/button").click()
        break

driver.find_element_by_xpath("//a[contains(text(),'Checkout')]").click()
driver.find_element_by_xpath("//button[contains(text(),'Checkout')]").click()
driver.find_element_by_id("country").send_keys("ind")

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='India']")))

driver.find_element_by_link_text("India").click()

driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

driver.find_element_by_css_selector("input[value='Purchase']").click()

assert "Success" in driver.find_element_by_xpath("//strong[contains(text(),'Success')]").text
driver.get_screenshot_as_file("test.png")

driver.close()
