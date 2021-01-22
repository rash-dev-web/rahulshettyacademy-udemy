from selenium import webdriver

driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/")
driver.find_element_by_link_text("Frames").click()
driver.find_element_by_link_text("iFrame").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("Testing Text...")
driver.switch_to.default_content()


driver.close()
