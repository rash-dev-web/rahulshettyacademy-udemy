import pytest
from selenium import webdriver

APP_URL = "https://rahulshettyacademy.com/angularpractice/"


@pytest.fixture(scope="class")
def set_up(request):
    # browser setup
    browser_name = request.config.getoption("--browser-name")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe", options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="../drivers/geckodriver.exe")
        driver.maximize_window()
    driver.get(APP_URL)
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name", action="store", default="chrome"
    )
