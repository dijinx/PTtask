class ForTest:
    # Методы рабочие, но условные, только для демонстрации
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.openbrewerydb.org/')

    def click_on_about(self):
        self.driver.find_element_by_xpath('//*[@href="#about"]').click()

    def check_h2_about_text(self):
        assert self.driver.find_element_by_xpath('//*[@id="about"]').text == 'About'
