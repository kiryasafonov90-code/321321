# Что заменить и удалить

## Заменить
- README.md
- docker-compose.yml
- gate-simulator/Dockerfile
- Report.md (если его нет — создать)
- Summary.md

## Удалить
- text.2
- text.py # фикстуры driver и db_c
- text2.md
- Plan.md.code-workspace (если присутствует)
- корневой payment_page.py (если присутствует как дубликат pages/payment_page.py)
- корневой test_buy_tour.py (если присутствует как дубликат tests/ui/test_buy_tour.py)

## Не делать
Не вписывать в Report.md выдуманные результаты тестов, Allure-скриншоты или баги. Их нужно получить реальным прогоном.
