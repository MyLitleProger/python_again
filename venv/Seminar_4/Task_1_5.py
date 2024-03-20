# Функция принимает на вход три списка одинаковой длины:
# имена str,
# ставка int,
# премия str с указанием процентов вида "10.25%".
# Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитана как ставка умноженная на процент премии.


def calculate_salary(names, salary, percent):
    result = {}
    for i in range(len(names)):
        result[names[i]] = salary[i] * (float(percent[i][:-1]) / 100)
    return result


print(calculate_salary(["Ivan", "Petr", "Sidor"], [1000, 2000, 3000], ["10.25%", "15.5%", "20.75%"]))
