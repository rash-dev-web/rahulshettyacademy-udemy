from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
total_item = driver.find_elements_by_xpath("//div[@class='products']/div")
assert len(total_item) == 3

filtered_item = driver.find_elements_by_css_selector("div.product-action")
for item in filtered_item:
    item.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".promoCode")))
driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
promo_info_ele = driver.find_element_by_css_selector(".promoInfo")
promo_info = promo_info_ele.text
assert "Code applied" in promo_info
# print(promo_info)
driver.close()
