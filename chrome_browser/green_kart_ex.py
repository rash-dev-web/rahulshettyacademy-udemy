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

# declare list for search item and cart
search_veggie_list = []
veggie_in_cart = []

filtered_item = driver.find_elements_by_css_selector("div.product-action")
for item in filtered_item:
    search_veggie_list.append(item.find_element_by_xpath("parent::div//h4").text)
    item.click()

# print(search_veggie_list)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".promoCode")))

veggies_cart = driver.find_elements_by_css_selector("p.product-name")
for veg in veggies_cart:
    veggie_in_cart.append(veg.text)

# print(veggie_in_cart)
assert search_veggie_list == veggie_in_cart

original_amount = driver.find_element_by_css_selector(".discountAmt").text

driver.find_element_by_css_selector(".promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()


wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
promo_info_ele = driver.find_element_by_css_selector(".promoInfo")
promo_info = promo_info_ele.text
assert "Code applied" in promo_info

discounted_amount = driver.find_element_by_css_selector(".discountAmt").text
assert float(discounted_amount) < float(original_amount)

# verify the cart amount with total
veggie_prices = driver.find_elements_by_xpath("//tr/td[5]/p[@class='amount']")
veggie_sum = 0
for veg in veggie_prices:
    veggie_sum += int(veg.text)

# print(veggie_sum)
total_amount = driver.find_element_by_css_selector(".totAmt").text
assert veggie_sum == int(total_amount)


driver.close()
