import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import mysql.connector

BASE_URL = "http://localhost:8080"


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        port=3307,
        user="app",
        password="pass",
        database="app"
    )
    yield conn
    conn.close()


@pytest.fixture(scope="function")
def clean_db(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("DELETE FROM payment_entity")
    cursor.execute("DELETE FROM credit_request_entity")
    cursor.execute("DELETE FROM order_entity")
    db_connection.commit()
    cursor.close()
