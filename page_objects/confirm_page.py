from selenium.webdriver.common.by import By


class ConfirmPage:
    checkout_element = (By.XPATH, "//button[contains(text(),'Checkout')]")
    country = (By.ID, "country")
    checkout_primary = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "input[value='Purchase']")
    success_text = (By.XPATH, "//strong[contains(text(),'Success')]")

    # self.driver.find_element_by_xpath("//button[contains(text(),'Checkout')]").click()
    # self.driver.find_element_by_id("country").send_keys("ind")
    # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
    # self.driver.find_element_by_css_selector("input[value='Purchase']").click()
    # self.driver.find_element_by_xpath("//strong[contains(text(),'Success')]")
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        return self.driver.find_element(*ConfirmPage.checkout_element)

    def select_country(self):
        return self.driver.find_element(*ConfirmPage.country)

    def select_checkout(self):
        return self.driver.find_element(*ConfirmPage.checkout_primary)

    def select_purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def select_success_text(self):
        return self.driver.find_element(*ConfirmPage.success_text)
