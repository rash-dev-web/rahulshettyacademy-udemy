from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)
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

driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
promo_info = driver.find_element_by_css_selector(".promoInfo").text
assert "Code applied" in promo_info
# print(promo_info)
driver.close()
