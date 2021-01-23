import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# @pytest.mark.usefixtures("set_up")
from page_objects.confirm_page import ConfirmPage
from page_objects.home_page import HomePage
from page_objects.mobile_list_page import MobileList
from utilities.base_test import BaseClass


class TestMethod(BaseClass):
    def test_test_one(self):

        home = HomePage(self.driver)
        home.shop_item().click()

        # self.driver.find_element_by_link_text("Shop").click()
        mobile_list = MobileList(self.driver)
        mobile_products = mobile_list.find_card_body()
        for mobile in mobile_products:
            if mobile.find_element_by_xpath("h4/a").text == "Blackberry":
                mobile.find_element_by_xpath("following-sibling::div/button").click()
                break

        # self.driver.find_element_by_xpath("//a[contains(text(),'Checkout')]").click()
        mobile_list.checkout().click()
        confirm_page = ConfirmPage(self.driver)
        confirm_page.checkout().click()
        # self.driver.find_element_by_xpath("//button[contains(text(),'Checkout')]").click()
        # self.driver.find_element_by_id("country").send_keys("ind")
        confirm_page.select_country().send_keys("ind")

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='India']")))

        self.driver.find_element_by_link_text("India").click()

        # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        confirm_page.select_checkout().click()

        # self.driver.find_element_by_css_selector("input[value='Purchase']").click()
        confirm_page.select_purchase().click()

        # success_text = self.driver.find_element_by_xpath("//strong[contains(text(),'Success')]")
        success_text = confirm_page.select_success_text()

        assert "Success" in success_text.text
        self.driver.get_screenshot_as_file("test.png")
