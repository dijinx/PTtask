import pytest
import requests
import time
from selenium import webdriver


@pytest.fixture(params=['http', 'https'], scope='function')
def protocol(request):
    if request.param == 'http':
        return requests.get(f'http://api.openbrewerydb.org/breweries/common-john-brewing-co-manchester')

    if request.param == 'https':
        return requests.get(f'https://api.openbrewerydb.org/breweries/common-john-brewing-co-manchester')


@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(
            executable_path=r'C:\chromedriver.exe')
        driver.implicitly_wait(15)
        driver.maximize_window()
        yield driver
        time.sleep(1)
        driver.close()
        driver.quit()
    if request.param == 'firefox':
        driver = webdriver.Firefox(
            executable_path=r'C:\geckodriver.exe')
        driver.implicitly_wait(15)
        # driver.maximize_window()
        yield driver
        time.sleep(1)
        driver.close()
        driver.quit()
