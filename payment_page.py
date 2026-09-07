from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PaymentPage:
    CARD_INPUT = (By.ID, "card-number")
    SUBMIT_BTN = (By.CSS_SELECTOR, ".submit-btn")
    SUCCESS_MSG = (By.ID, "success-message")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_payment_form(self, card_number, price):
        card_field = self.wait.until(EC.visibility_of_element_located(self.CARD_INPUT))
        card_field.clear()
        card_field.send_keys(card_number)
        # Логика выбора типа платежа (дебет/кредит) обычно здесь же

    def submit_payment(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BTN))
        btn.click()

    def is_success_message_displayed(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_MSG)).is_displayed()
        except TimeoutError:
            return False