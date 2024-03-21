# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


import decimal
import inspect

CMD_DEPOSIT = 'd'
CMD_WITHDRAW = 'w'
CMD_HISTORY = 'h'
CMD_EXIT = 'x'

MIN_DEPOSIT = decimal.Decimal(50)

COUNT_FREE_OPERATION = 3
OPERATION_FEE = decimal.Decimal(1.5 / 100)
OPERATION_3_FEE = decimal.Decimal(3 / 100)

MIN_WITHDRAW_FEE = decimal.Decimal(30)
MAX_WITHDRAW_FEE = decimal.Decimal(600)

RICH_FEE = decimal.Decimal(10 / 100)
RICH_ACCOUNT = decimal.Decimal(5000000)

MIN_ACCOUNT = decimal.Decimal(0)

account = decimal.Decimal(0)
count_operation = 0
operations = []


def view_account():
    global account
    print(f'your cash: {round(account, 2)} c.u.')


def deposit(amount):
    """
    Операция пополнения средств на счет
    :param amount: пополняемая сумма у.е.
    :return: amount - (1.5% ... 3%)
    """
    global operations
    global account
    global count_operation
    if account > RICH_ACCOUNT:
        account += amount * (decimal.Decimal(1) - RICH_FEE)
        count_operation += 1
    elif count_operation > COUNT_FREE_OPERATION:
        account += amount * (decimal.Decimal(1) - OPERATION_3_FEE)
        count_operation += 1
    else:
        account += amount * (decimal.Decimal(1) - OPERATION_FEE)
    operations.append(f'+{amount}')


def withdraw(amount):
    """
    Операция снятия средств со счета
    :param amount: снимаемая сумма у.е.
    :return: amount - (1.5% ... 3%)
    """
    global account
    global count_operation
    # - Процент снятия - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.;
    if count_operation > COUNT_FREE_OPERATION:
        if amount * OPERATION_3_FEE <= MIN_WITHDRAW_FEE:
            account -= amount - MIN_WITHDRAW_FEE
            count_operation += 1
        elif amount * OPERATION_3_FEE >= MAX_WITHDRAW_FEE:
            account -= amount - MAX_WITHDRAW_FEE
            count_operation += 1
        else:
            account -= amount * (decimal.Decimal(1) - OPERATION_3_FEE)
            count_operation += 1
    else:
        if amount * OPERATION_FEE <= MIN_WITHDRAW_FEE:
            account -= amount - MIN_WITHDRAW_FEE
            count_operation += 1
        elif amount * OPERATION_FEE >= MAX_WITHDRAW_FEE:
            account -= amount - MAX_WITHDRAW_FEE
            count_operation += 1
        else:
            account -= amount * (decimal.Decimal(1) - OPERATION_FEE)
            count_operation += 1
    operations.append(f'-{amount}')


def rich(amount):
    """
    Если на счете больше 5 млн.у.е., то вычитается налог на богатство 10% перед каждой операцией, даже ошибочной
    :param amount: расчетная сумма у.е.
    :return: amount - 10%
    """
    return amount * (decimal.Decimal(1) - RICH_FEE)


def _exit():
    print('Bye!')
    exit(0)


if __name__ == '__main__':
    while True:
        view_account()
        print('1. Deposit (d)')
        print('2. Withdraw (w)')
        print('3. History (h)')
        print('4. Exit (x)')
        print('Enter command:')
        cmd = input()
        if cmd == CMD_DEPOSIT:
            while True:
                try:
                    print('Enter amount:')
                    amount = input()
                    amount = decimal.Decimal(amount)
                    if amount < MIN_DEPOSIT or amount % 50 != 0:
                        print('Amount must be greater than 50')
                        break
                    else:
                        rich(amount)
                        deposit(amount)
                        break
                except ValueError:
                    print('Amount must be a number')
        elif cmd == CMD_WITHDRAW:
            while True:
                try:
                    print('Enter amount:')
                    amount = input()
                    amount = decimal.Decimal(amount)
                    if account - amount < MIN_ACCOUNT or amount % 50 != 0:
                        print('Insufficient funds')
                        break
                    elif amount < MIN_WITHDRAW_FEE:
                        print('Amount must be greater than 30')
                        break
                    else:
                        rich(amount)
                        withdraw(amount)
                        break
                except ValueError:
                    print('Amount must be a number')
        elif cmd == CMD_HISTORY:
            print('History:')
            print(operations)
        elif cmd == CMD_EXIT:
            _exit()
        else:
            print('Unknown command')
