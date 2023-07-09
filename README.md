# Имитация работы банка со счетами клиентов

### Требования к сервису:

- работа с сервисом должна осуществляться через `Interactive CLI`
- состояние счетов хранится только в рамках одной сессии
- у клиента может быть только один счет
- валюта у всех счетов одинаковая - `USD`

### Поддерживаемые операции:

- deposit - операция пополнения счета на сумму, аргументы: client, amount, description
- withdraw - операция снятия со счета, аргументы: client, amount, description
- show_bank_statement - вывод на экран выписки со счета за период, аргументы: client, since ,till

### Пример
```bash
deposit --client="John Jones" --amount=100 --description="ATM Deposit"
```

```bash
withdraw --client="John Jones" --amount=100 --description="ATM Withdrawal"
```

```bash
show_bank_statement --client="John Jones" --since="2023-05-29 00:00:00" --till="2023-05-31 00:00:00"
```

# Установка:

### Необходимые инструменты и технологии

- [Python 3.10+](https://www.python.org/)

1.Склонируйте к себе данный репозиторий при помощи команды:

```bash
git clone https://github.com/YaroslavNogovitsyn/NtPRO
```

2.Выполните команду для создания виртуального окружения:
```bash
poetry install
```
3.Для активации запустите файл:
```bash
python main.py
```
