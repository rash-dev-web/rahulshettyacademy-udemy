from selenium.webdriver.common.by import By


class MobileList:
    def __init__(self, driver):
        self.driver = driver

    card_body = (By.XPATH, "//div[@class='card-body']")
    # blackberry = (By.XPATH, "h4/a")
    checkout_button = (By.XPATH, "//a[contains(text(),'Checkout')]")

    # self.driver.find_elements_by_xpath("//div[@class='card-body']")
    # mobile.find_element_by_xpath("h4/a").text == "Blackberry":
    # self.driver.find_element_by_xpath("//a[contains(text(),'Checkout')]").click()
    def find_card_body(self):
        self.driver.find_elements(*MobileList.card_body)

    # def find_blackberry(self):
    #     return self.driver.find_element(*MobileList.blackberry)

    def checkout(self):
        return self.driver.find_element(*MobileList.checkout_button)
