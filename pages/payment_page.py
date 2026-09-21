from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PaymentPage(BasePage):
    CARD_NUMBER = (By.CSS_SELECTOR, 'input[placeholder="0000 0000 0000 0000"]')
    MONTH = (By.CSS_SELECTOR, 'input[placeholder="08"]')
    YEAR = (By.CSS_SELECTOR, 'input[placeholder="22"]')
    OWNER = (By.CSS_SELECTOR, 'input[placeholder="Ivanov Ivan"]')
    CVC = (By.CSS_SELECTOR, 'input[placeholder="999"]')
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button.button')

    SUCCESS_NOTIFICATION = (By.CSS_SELECTOR, '.notification_status_ok')
    ERROR_NOTIFICATION = (By.CSS_SELECTOR, '.notification_status_error')

    def _field_error(self, field_name):
        return (
            By.XPATH,
            f'//*[self::span or self::label][normalize-space()="{field_name}"]'
            f'/ancestor::*[contains(concat(" ", normalize-space(@class), " "), " input ")][1]'
            f'//*[contains(concat(" ", normalize-space(@class), " "), " input__sub ")]'
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
        return self.get_text(self._field_error("Номер карты"))

    def get_month_error(self):
        return self.get_text(self._field_error("Месяц"))

    def get_year_error(self):
        return self.get_text(self._field_error("Год"))

    def get_owner_error(self):
        return self.get_text(self._field_error("Владелец"))

    def get_cvc_error(self):
        return self.get_text(self._field_error("CVC/CVV"))
