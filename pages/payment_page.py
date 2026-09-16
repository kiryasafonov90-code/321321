from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PaymentPage(BasePage):
    # Поля формы
    CARD_NUMBER = (By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')
    MONTH = (By.CSS_SELECTOR, 'input[placeholder="08"]')
    YEAR = (By.CSS_SELECTOR, 'input[placeholder="22"]')
    OWNER = (By.CSS_SELECTOR, 'input[placeholder="Ivanov Ivan"]')
    CVC = (By.CSS_SELECTOR, 'input[placeholder="999"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button.button')

    # Уведомления
    SUCCESS_NOTIFICATION = (By.CSS_SELECTOR, '.notification_status_ok')
    ERROR_NOTIFICATION = (By.CSS_SELECTOR, '.notification_status_error')

    # Сообщения об ошибках валидации (.input__sub под каждым полем)
    CARD_NUMBER_ERROR = (
        By.XPATH,
        '//span[text()="Номер карты"]/following-sibling::span[@class="input__sub"]'
    )
    MONTH_ERROR = (
        By.XPATH,
        '//span[text()="Месяц"]/following-sibling::span[@class="input__sub"]'
    )
    YEAR_ERROR = (
        By.XPATH,
        '//span[text()="Год"]/following-sibling::span[@class="input__sub"]'
    )
    OWNER_ERROR = (
        By.XPATH,
        '//span[text()="Владелец"]/following-sibling::span[@class="input__sub"]'
    )
    CVC_ERROR = (
        By.XPATH,
        '//span[text()="CVC/CVV"]/following-sibling::span[@class="input__sub"]'
    )

    def fill_form(self, card_number, month, year, owner, cvc):
        self.type_text(self.CARD_NUMBER, card_number)
        self.type_text(self.MONTH, month)
        self.type_text(self.YEAR, year)
        self.type_text(self.OWNER, owner)
        self.type_text(self.CVC, cvc)

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def is_success(self):
        return self.is_element_present(self.SUCCESS_NOTIFICATION)

    def is_error(self):
        return self.is_element_present(self.ERROR_NOTIFICATION)

    def get_card_error(self):
        return self.get_text(self.CARD_NUMBER_ERROR)

    def get_month_error(self):
        return self.get_text(self.MONTH_ERROR)

    def get_year_error(self):
        return self.get_text(self.YEAR_ERROR)

    def get_owner_error(self):
        return self.get_text(self.OWNER_ERROR)

    def get_cvc_error(self):
        return self.get_text(self.CVC_ERROR)
