import allure
from pages.text_for_about_h2_is_correct_pages import ForTest
import pytest


# Просто коротенький UI тест c параметризацией через фикстуру
# по сути бессмысленный
@allure.feature("Selen test")
@pytest.mark.smoke
# При невозможности избежать зависимости тестов друг от друга можно определять порядок их исполнения
@pytest.mark.run(order=1)
def test_text_for_about_h2_is_correct(driver):
    user = ForTest(driver)
    with allure.step('Открыть страницу'):
        user.open()
    with allure.step('Кликнуть по About'):
        user.click_on_about()
    with allure.step('Проверить текст заголовка About'):
        user.check_h2_about_text()
