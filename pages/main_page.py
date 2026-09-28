from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    BUY_BUTTON = (By.XPATH, "//button[normalize-space(.)='Купить']")
    CREDIT_BUTTON = (By.XPATH, "//button[normalize-space(.)='Купить в кредит']")

    def click_buy(self):
        self.click(self.BUY_BUTTON)

    def click_credit(self):
        self.click(self.CREDIT_BUTTON)
