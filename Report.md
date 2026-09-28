# Отчёт по итогам тестирования

## Набор тестов

- Позитивные сценарии: 4
- Негативные сценарии: 15
- Проверки БД: 4
- Всего: 23

## Фактический прогон

**Дата:** 28.09.2026  
**CI:** GitHub Actions, workflow run #4  
**Окружение:** Ubuntu 24.04.5, Python 3.11.16, pytest 7.4.3, Selenium 4.15.2, Chrome headless.

| Показатель | Значение |
|---|---:|
| Passed | 0 |
| Failed | 23 |
| Skipped / xfailed | 0 |
| Всего | 23 |
| Процент успешных | 0% |
| Время pytest | 384.20 с (6:24.20) |
| Время CI workflow | ~8:24 |

**Результат CI:** failed.

Все 23 теста завершились с `selenium.common.exceptions.TimeoutException`. Падение происходит на открытии главной страницы при ожидании кликабельной кнопки в `MainPage.click_buy()` / `MainPage.click_credit()`; до заполнения платёжной формы, проверки валидации и запросов к БД выполнение не доходит.

Таким образом, предположительные ожидания для месяца 13, года 00 и кириллицы в поле «Владелец» в этом прогоне **не подтверждены и не опровергнуты**: тесты не дошли до соответствующих assertions.

## Allure

- [Workflow #4](https://github.com/kiryasafonov90-code/321321/actions/runs/36377543706)
- [Артефакт ui-test-results с allure-report, allure-results, pytest-output.txt и allure-screenshot.png](https://github.com/kiryasafonov90-code/321321/actions/runs/36377543706/artifacts/10951726722)

Скриншот Allure-отчёта находится в артефакте как `allure-screenshot.png`.

## Подтверждённые падения

Для каждого из 23 упавших тестов создан отдельный GitHub Issue:

- #21 — `test_buy_approved_card`
- #22 — `test_buy_declined_card`
- #23 — `test_credit_approved_card`
- #24 — `test_credit_declined_card`
- #25–27 — `test_buy_invalid_card_number`
- #28–30 — `test_buy_invalid_month`
- #31–33 — `test_buy_invalid_year`
- #34–36 — `test_buy_invalid_owner`
- #37–39 — `test_buy_invalid_cvc`
- #40–43 — DB-проверки

Во всех Issues указаны окружение, шаги, ожидаемый/фактический результат, ссылка на тест и ссылка на CI/Allure-артефакт.

## Команда запуска

```bash
docker compose up -d
pytest tests/ui/ -v --alluredir=allure-results
allure serve allure-results
```
