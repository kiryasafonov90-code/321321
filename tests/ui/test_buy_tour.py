import pytest
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from data.test_data import (
    APPROVED_CARD, DECLINED_CARD,
    VALID_MONTH, VALID_YEAR, VALID_OWNER, VALID_CVC
)


def fill_and_submit(driver, card, month=VALID_MONTH, year=VALID_YEAR,
                    owner=VALID_OWNER, cvc=VALID_CVC):
    payment = PaymentPage(driver)
    payment.fill_form(card, month, year, owner, cvc)
    payment.click_continue()
    return payment


def test_buy_approved_card(driver):
    main = MainPage(driver)
    main.click_buy()
    payment = fill_and_submit(driver, APPROVED_CARD)
    assert payment.is_success(), "Ожидается успех по карте APPROVED"


def test_buy_declined_card(driver):
    main = MainPage(driver)
    main.click_buy()
    payment = fill_and_submit(driver, DECLINED_CARD)
    assert payment.is_error(), "Ожидается отказ по карте DECLINED"


def test_credit_approved_card(driver):
    main = MainPage(driver)
    main.click_credit()
    payment = fill_and_submit(driver, APPROVED_CARD)
    assert payment.is_success(), "Ожидается успех кредита APPROVED"


def test_credit_declined_card(driver):
    main = MainPage(driver)
    main.click_credit()
    payment = fill_and_submit(driver, DECLINED_CARD)
    assert payment.is_error(), "Ожидается отказ кредита DECLINED"


@pytest.mark.parametrize("card, expected_error", [
    ("", "Поле обязательно для заполнения"),
    ("0000 0000 0000 0000", "Неверный формат"),
    ("4444 4444 4444 441", "Неверный формат"),
])
def test_buy_invalid_card_number(driver, card, expected_error):
    main = MainPage(driver)
    main.click_buy()
    payment = PaymentPage(driver)
    payment.fill_form(card, VALID_MONTH, VALID_YEAR, VALID_OWNER, VALID_CVC)
    payment.click_continue()
    assert payment.get_card_error() == expected_error


@pytest.mark.parametrize("month, expected_error", [
    ("00", "Неверный формат"),
    ("13", "Неверно указан срок действия карты"),
    ("", "Поле обязательно для заполнения"),
])
def test_buy_invalid_month(driver, month, expected_error):
    main = MainPage(driver)
    main.click_buy()
    payment = PaymentPage(driver)
    payment.fill_form(APPROVED_CARD, month, VALID_YEAR, VALID_OWNER, VALID_CVC)
    payment.click_continue()
    assert payment.get_month_error() == expected_error


@pytest.mark.parametrize("year, expected_error", [
    ("20", "Истёк срок действия карты"),
    ("00", "Неверно указан срок действия карты"),
    ("", "Поле обязательно для заполнения"),
])
def test_buy_invalid_year(driver, year, expected_error):
    main = MainPage(driver)
    main.click_buy()
    payment = PaymentPage(driver)
    payment.fill_form(APPROVED_CARD, VALID_MONTH, year, VALID_OWNER, VALID_CVC)
    payment.click_continue()
    assert payment.get_year_error() == expected_error


@pytest.mark.parametrize("owner, expected_error", [
    ("", "Поле обязательно для заполнения"),
    ("12345", "Неверный формат"),
    ("А", "Неверный формат"),
])
def test_buy_invalid_owner(driver, owner, expected_error):
    main = MainPage(driver)
    main.click_buy()
    payment = PaymentPage(driver)
    payment.fill_form(APPROVED_CARD, VALID_MONTH, VALID_YEAR, owner, VALID_CVC)
    payment.click_continue()
    assert payment.get_owner_error() == expected_error


@pytest.mark.parametrize("cvc, expected_error", [
    ("", "Поле обязательно для заполнения"),
    ("1", "Неверный формат"),
    ("abc", "Неверный формат"),
])
def test_buy_invalid_cvc(driver, cvc, expected_error):
    main = MainPage(driver)
    main.click_buy()
    payment = PaymentPage(driver)
    payment.fill_form(APPROVED_CARD, VALID_MONTH, VALID_YEAR, VALID_OWNER, cvc)
    payment.click_continue()
    assert payment.get_cvc_error() == expected_error


def test_db_after_approved_payment(driver, clean_db, db_connection):
    main = MainPage(driver)
    main.click_buy()
    payment = fill_and_submit(driver, APPROVED_CARD)
    assert payment.is_success()

    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM payment_entity")
    payments = cursor.fetchall()
    cursor.execute("SELECT * FROM order_entity")
    orders = cursor.fetchall()
    cursor.close()

    assert len(payments) == 1
    assert payments[0]["status"] == "APPROVED"
    assert len(orders) == 1
    assert orders[0]["payment_id"] == payments[0]["id"]


def test_db_after_declined_payment(driver, clean_db, db_connection):
    main = MainPage(driver)
    main.click_buy()
    payment = fill_and_submit(driver, DECLINED_CARD)
    assert payment.is_error()

    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM payment_entity")
    payments = cursor.fetchall()
    cursor.close()

    assert len(payments) == 1
    assert payments[0]["status"] == "DECLINED"


def test_db_after_approved_credit(driver, clean_db, db_connection):
    main = MainPage(driver)
    main.click_credit()
    payment = fill_and_submit(driver, APPROVED_CARD)
    assert payment.is_success()

    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM credit_request_entity")
    credits = cursor.fetchall()
    cursor.execute("SELECT * FROM order_entity")
    orders = cursor.fetchall()
    cursor.close()

    assert len(credits) == 1
    assert credits[0]["status"] == "APPROVED"
    assert len(orders) == 1
    assert orders[0]["credit_id"] == credits[0]["id"]


def test_db_after_declined_credit(driver, clean_db, db_connection):
    main = MainPage(driver)
    main.click_credit()
    payment = fill_and_submit(driver, DECLINED_CARD)
    assert payment.is_error()

    cursor = db_connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM credit_request_entity")
    credits = cursor.fetchall()
    cursor.close()

    assert len(credits) == 1
    assert credits[0]["status"] == "DECLINED"
