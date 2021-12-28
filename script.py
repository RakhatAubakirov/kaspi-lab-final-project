from database.table_accounts import TableAccounts
from database.table_customers import TableCustomers
from database.table_transactions_hist import TableTransactions
from database.table_replenishments_hist import TableReplenishments
from uuid import uuid4

print('Добро пожаловать в систему онлайн переводов!')

print('1 - Показать список счетов ')
ans = int(input())
table_customers = TableCustomers()
table_accounts = TableAccounts()
table_replenishment_hist = TableReplenishments()
if ans == '1':
    all_accounts = table_accounts.get_rows2()
    print('1 - Создать новый счет')
    print('2. Пополнить баланс на счету')
    request = input()
    if request == '1':
        account_id_ = uuid4()
        customer_id_ = uuid4()
        print('Ваше имя')
        name = input()
        print('Ваше фамилия')
        surname = input()
        print('Ваш номер телефона')
        phone_number = input()
        print('В какой валюте хотите открыть счет?')
        currency = input()
        table_accounts.insert_row(account_id_, phone_number, 0, currency)
        table_customers.insert_row(customer_id_, name, surname, phone_number, str(account_id_))
        all_accounts = table_accounts.get_rows2()
    elif request == '2':
        print('Введите номер получателя')
        phone_number = str(input())
        print('Сумма пополнения')
        amount = int(input())
        print('Валюта ')
        currency = input()
        balance_acc = table_accounts.get_balance(phone_number)
        balance_on_account = balance_acc + amount
        table_accounts.update_row(phone_number, balance_on_account)
        replenishment_id_ = uuid4()
        table_replenishment_hist.insert_row(replenishment_id_, phone_number, amount, currency)
        table_replenishment_hist.get_rows2()
    else:
        print('Ошибка, отсутствует данная команда')

