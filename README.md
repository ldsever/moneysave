# Expense Tracker

Простой трекер расходов на Python.

## Возможности

- добавление расходов
- просмотр списка расходов
- обновление расхода
- удаление расхода
- общая сумма расходов
- сумма за месяц
- экспорт в CSV
- хранение данных в SQLite

## Запуск

```bash
python3 main.py add --description "Lunch" --amount 20
python3 main.py list
python3 main.py summary
python3 main.py summary --month 8
python3 main.py update --id 1 --description "Dinner" --amount 30
python3 main.py delete --id 1
python3 main.py export
