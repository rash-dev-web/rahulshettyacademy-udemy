from selenium.webdriver.common.by import By

from page_objects.mobile_list_page import MobileList


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")

    def shop_item(self):
        return self.driver.find_element(*HomePage.shop)
        # mobile_list = MobileList(self.driver)
        # return mobile_list


