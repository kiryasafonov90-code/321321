# Дипломный проект: автоматизация тестирования aqa-shop

Автоматизация тестирования веб-сервиса покупки тура, взаимодействующего с СУБД MySQL и API платёжного шлюза.

## Предварительные требования

- Docker и Docker Compose
- Python 3.11+
- Google Chrome (или Chromium)
- ChromeDriver (совместимый с версией браузера)

## Запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/kiryasafonov90-code/321321.git
cd 321321


OQ

OPOP

OQ




Function Key ~

Function Key 11
Function Key 9
Function Key 8
Function Key 6
~



[200~python -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

pip install -r requirements.txt
~
docker-compose up -d

pytest tests/ui/ -v --alluredir=allure-results

allure serve allure-results

docker-compose down

321321/
├── conftest.py              # фикстуры driver и db_connection
├── docker-compose.yml       # MySQL + gate-simulator + aqa-shop
├── application.properties    # конфигурация Spring Boot
├── aqa-shop.jar             # приложение
├── requirements.txt         # Python-зависимости
├── gate-simulator/          # эмулятор платёжного шлюза
│   ├── Dockerfile
│   ├── app.js
│   ├── data.json
│   └── package.json
├── pages/                   # Page Object Model
│   ├── __init__.py
│   ├── base_page.py
│   ├── main_page.py
│   └── payment_page.py
├── data/
│   ├── __init__.py
│   └── test_data.py         # тестовые данные (номера карт)
├── tests/
│   ├── __init__.py
│   └── ui/
│       ├── __init__.py
│       └── test_buy_tour.py # автотесты
├── Plan.md                  # план автоматизации
├── Report.md                # отчёт по итогам тестирования
└── Summary.md              # отчёт по итогам автоматизации


### 16. Report.md

```bash
cat > Report.md << 'ENDOFFILE'
# Отчёт по итогам тестирования

## Краткое описание

Проведено автоматизированное тестирование веб-сервиса покупки тура (aqa-shop).
Тесты покрывают позитивные и негативные сценарии оплаты по карте и в кредит,
а также проверку записи данных в БД.

## Количество тест-кейсов

- Позитивные (оплата/кредит): 4
- Негативные (валидация полей): 15
- Проверки БД: 4
- **Всего: 23**

## Результаты

| Показатель | Значение |
|------------|----------|
| Успешных | XX |
| Неуспешных | XX |
| Процент успешных | XX% |

## Найденные баги

1. Поле «Владелец» принимает цифры и кириллицу (ожидается — только латиница)
2. В таблице order_entity поле credit_id равно NULL при оформлении кредита (ожидается — ссылка на credit_request_entity)
3. Поле «Номер карты» ограничено 16 символами, хотя атрибут maxlength=19

## Баг-репорты

Оформлены в разделе Issues репозитория.
