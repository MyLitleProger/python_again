# Задание 6.
# Напишите программу банкомат:
# - Начальная сумма равна нулю;
# - Допустимые действия: пополнить, снять, выйти;
# - Сумма пополнения и снятия кратны 50 у.е.;
# - Процент снятия - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.;
# - После каждой третей операции пополнения или снятия начинаются проценты - 3%;
# - Нельзя снять больше, чем на счете;
# - При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной;
# - Любое действие выводит сумму денег.

import decimal

CMD_DEPOSIT = 'd'
CMD_WITHDRAW = 'w'
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


def view_account():
    global account
    print(f'your cash: {round(account, 2)} c.u.')


def deposit(amount):
    """
    Операция пополнения средств на счет
    :param amount: пополняемая сумма у.е.
    :return: amount - (1.5% ... 3%)
    """
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
        print('3. Exit (x)')
        print('Enter command:')
        cmd = input()
        if cmd == CMD_DEPOSIT:
            while True:
                try:
                    print('Enter amount:')
                    amount = input()
                    amount = decimal.Decimal(amount)
                    if amount < MIN_DEPOSIT:
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
                    if account - amount < MIN_ACCOUNT:
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
        elif cmd == CMD_EXIT:
            _exit()
        else:
            print('Unknown command')
