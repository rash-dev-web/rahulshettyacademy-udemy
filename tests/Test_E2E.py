import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# @pytest.mark.usefixtures("set_up")
from utilities.base_test import BaseClass


class TestMethod(BaseClass):
    def test_test_one(self):

        self.driver.find_element_by_link_text("Shop").click()
        mobile_products = self.driver.find_elements_by_xpath("//div[@class='card-body']")
        for mobile in mobile_products:
            if mobile.find_element_by_xpath("h4/a").text == "Blackberry":
                mobile.find_element_by_xpath("following-sibling::div/button").click()
                break

        self.driver.find_element_by_xpath("//a[contains(text(),'Checkout')]").click()
        self.driver.find_element_by_xpath("//button[contains(text(),'Checkout')]").click()
        self.driver.find_element_by_id("country").send_keys("ind")

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='India']")))

        self.driver.find_element_by_link_text("India").click()

        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

        self.driver.find_element_by_css_selector("input[value='Purchase']").click()

        assert "Success" in self.driver.find_element_by_xpath("//strong[contains(text(),'Success')]").text
        self.driver.get_screenshot_as_file("test.png")
