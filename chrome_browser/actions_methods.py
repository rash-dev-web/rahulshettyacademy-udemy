from selenium import webdriver
from selenium.webdriver import ActionChains
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome("../drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://stqatools.com/demo/DoubleClick.php")
double_click_button = driver.find_element_by_xpath("//button[contains(text(),'Double')]")
action = ActionChains(driver)
action.double_click(double_click_button).perform()
# time.sleep(3)
wait = WebDriverWait(driver, 5)
wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='dblClicks' and text()='1']")))
double_click_count = driver.find_element_by_xpath("//span[@id='dblClicks' and text()='1']").text
print(type(double_click_count))
assert int(double_click_count) == 1

driver.close()
