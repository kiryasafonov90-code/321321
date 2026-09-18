# Дипломный проект: автоматизация тестирования aqa-shop

Автоматизация тестирования веб-сервиса покупки тура, взаимодействующего с MySQL и API платёжного шлюза.

## Требования

- Docker и Docker Compose
- Python 3.11+
- Google Chrome или Chromium
- ChromeDriver, совместимый с браузером
- Allure Commandline — для просмотра Allure-отчёта

## Установка

```bash
git clone https://github.com/kiryasafonov90-code/321321.git
cd 321321
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск приложения

```bash
docker-compose up -d
```

Приложение: `http://localhost:8080`

## Запуск автотестов

```bash
pytest tests/ui/ -v --alluredir=allure-results
```

## Allure

```bash
allure serve allure-results
```

## Остановка

```bash
docker-compose down
```

## Важно

Фактические результаты тестового прогона и подтверждённые дефекты должны заноситься в `Report.md` только после реального запуска тестов.
