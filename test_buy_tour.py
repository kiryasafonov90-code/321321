import allure
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from data.valid_cards import VALID_CARDS

@allure.feature("Покупка тура")
@allure.story("Успешная оплата дебетовой картой")
def test_buy_tour_with_debit_card(driver):
    """
    Позитивный сценарий:
    1. Открыть главную страницу
    2. Выбрать тур
    3. Перейти к оплате
    4. Заполнить форму валидной дебетовой картой
    5. Убедиться в успехе на странице
    """
    with allure.step("Открытие главной страницы"):
        main_page = MainPage(driver)
        main_page.open()
    
    with allure.step("Выбор первого доступного тура"):
        tour_price = main_page.get_first_tour_price()
        main_page.select_first_tour()
    
    with allure.step("Переход на страницу оплаты"):
        payment_page = PaymentPage(driver)
        
    with allure.step(f"Оплата картой {VALID_CARDS['valid_debit']}"):
        payment_page.fill_payment_form(
            card_number=VALID_CARDS['valid_debit'],
            price=tour_price
        )
        payment_page.submit_payment()
    
    with allure.step("Проверка сообщения об успехе"):
        assert payment_page.is_success_message_displayed(), "Сообщение об успешной оплате не появилось"