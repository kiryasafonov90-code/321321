# Дипломный проект: автоматизация тестирования aqa-shop

Автоматизация тестирования веб-сервиса покупки тура, взаимодействующего с MySQL и API платёжного шлюза.

## Требования

- Docker и Docker Compose
- Python 3.11+
- Google Chrome / Chromium
- ChromeDriver, совместимый с браузером
- Allure Commandline

## Порты

В проекте используется единый порт MySQL **3306**:
- `docker-compose.yml`: `3306:3306`
- `conftest.py`: `port=3306`
- `application.properties`: `jdbc:mysql://localhost:3306/app`

Приложение доступно на `http://localhost:8080`, gate-simulator — на `http://localhost:9999`.

## Запуск

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

pip install -r requirements.txt

docker-compose up -d
pytest tests/ui/ -v --alluredir=allure-results
allure serve allure-results
```

После завершения:

```bash
docker-compose down
```

## Структура

- `conftest.py` — фикстуры Selenium и MySQL
- `docker-compose.yml` — MySQL + gate-simulator + aqa-shop
- `application.properties` — настройки приложения
- `aqa-shop.jar` — тестируемое приложение
- `gate-simulator/` — эмулятор платёжного шлюза
- `pages/` — Page Object Model
- `data/` — тестовые данные
- `tests/ui/` — UI и DB автотесты
- `Plan.md` — план тестирования
- `Report.md` — фактический отчёт о прогоне
- `Summary.md` — итоговый статус проекта

## Результаты

Фактические `passed/failed`, скриншоты Allure и подтверждённые дефекты должны быть внесены после реального запуска команд из раздела «Запуск». Результаты заранее не подставляются.
