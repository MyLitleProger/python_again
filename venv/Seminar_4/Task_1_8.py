# Создайте несколько переменных заканчивающихся и не оканчивающихся на "s".
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноименные переменные без s на конце.


def replace_s():
    globals_var = globals()
    new_var = {}
    for key, value in globals_var.items():
        if key.endswith('s') and key != 's':
            new_var[key[:-1]] = globals_var[key]
            globals_var[key] = None
    for key, value in new_var.items():
        globals_var[key] = value


datas = [42, 73, 12, 34, 56, 78, 90, 123, 456, 789, 1234, 5678, 9012, 34567, 67890, 123456, 789012, 3456789, 90123456]
s = 'Hello world!'
names = ('NoName', 'OtherName', 'NewName')
sx = 42

replace_s()
print(globals())
