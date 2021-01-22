from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/")
driver.find_element_by_link_text("Multiple Windows").click()
driver.find_element_by_link_text("Click Here").click()
child_window = driver.window_handles[1]

# on new window
driver.switch_to.window("_blank")
new_window_text = driver.find_element_by_tag_name("h3").text
print(new_window_text)

time.sleep(3)
driver.quit()
