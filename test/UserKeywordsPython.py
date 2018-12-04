from robot.libraries.BuiltIn import BuiltIn

def get_webdriver_instance():
    selib = BuiltIn().get_library_instance('SeleniumLibrary')
    return selib._current_browser()

def clickToElement(self, locator):
	driver = get_webdriver_instance()
    driver.find_element_by_xpath(locator).click()