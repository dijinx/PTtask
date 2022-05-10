import allure
import pytest
import requests

from resources_for_tests import variables_for_tests
from resources_for_tests.variables_for_tests import cityes_names


# Имена сьютов условные, как и имена фич
class TestAPI:

    @allure.suite('Смоук')
    @allure.feature('Тест доступности эндпоинтов')
    @allure.description('Параметризированный тест')
    @pytest.mark.parametrize('breweries_names', variables_for_tests.breweries_names)
    def test_endpoints_of_breweries_is_available(self, breweries_names):
        r = requests.get(f'https://api.openbrewerydb.org/breweries/{breweries_names}')
        if r.status_code == 200:
            print(f'Статус: {r.status_code} - эндпоинт доступен {breweries_names}')
        else:
            quit(f'Статус: {r.status_code} - эндпоинт недоступен {breweries_names}')

    @allure.suite('Тест-кейс второй категории')
    @allure.feature('Проверка значения поля')
    @allure.description('Обычный тест')
    def test_country_value_banjo_brewing_fayetteville(self):
        r = requests.get('https://api.openbrewerydb.org/breweries/banjo-brewing-fayetteville')
        assert r.status_code == 200
        assert r.json()['country'] == 'United States'
        print(f'Значение поля country = верное')
        if r.json()['country'] != 'United States':
            print(f'Значение поля country = ошибочное')

    @allure.suite('Тест-кейс третьей категории')
    @allure.feature('Проверка значений всех полей json для эндпоинта common-john-brewing-co-manchester')
    @allure.description('Обычный тест')
    def test_response_body_for_common_john_brewing_co_manchester_is_correct(self):
        r = requests.get('https://api.openbrewerydb.org/breweries/common-john-brewing-co-manchester')
        assert r.status_code == 200
        assert r.json() == variables_for_tests.common_john_brewing_co_manchester_actual_json
        print('Тело ответа совпадает с образцом')

    @allure.suite('Тест-кейс четвёртой категории')
    @allure.feature('Проверка значений всех полей json для эндпоинта common-john-brewing-co-manchester')
    @allure.description('Параметризация через фикстуру')
    def test_response_body_for_common_john_brewing_co_manchester_is_correct(self, protocol):
        assert protocol.status_code == 200
        assert protocol.json() == variables_for_tests.common_john_brewing_co_manchester_actual_json
        print('Тело ответа совпадает с образцом')

    @allure.suite('Тест-кейс четвёртой категории')
    @allure.feature('Проверка значения поля city в первом json полученного ответа')
    @allure.description('Параметризированный тест')
    @pytest.mark.parametrize('cityes_names', cityes_names)
    def test_response_body_city_name(self, cityes_names):
        r = requests.get(f'https://api.openbrewerydb.org/breweries?by_city={cityes_names}')
        assert r.json()[0]['city'] == cityes_names
        if r.json()[0]['city'] == cityes_names:
            print(f"Имя города для первого элемента = {r.json()[0]['city']} ожидается {cityes_names}")
