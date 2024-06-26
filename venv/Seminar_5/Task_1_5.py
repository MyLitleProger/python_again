# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово "Fizz"
# Вместо чисел, кратных пяти, программа должна выводить слово "Buzz"
# Если число кратно и 3, и 5, то нужно выводить слово "FizzBuzz"
# *Превратите решение в генераторное выражение.

fizzbuzz = []
for i in range(1, 101):
    if i % 15 == 0:
        fizzbuzz.append("FizzBuzz")
    elif i % 3 == 0:
        fizzbuzz.append("Fizz")
    elif i % 5 == 0:
        fizzbuzz.append("Buzz")
    else:
        fizzbuzz.append(i)

print(*fizzbuzz)

fizzbuzz_gen = ("FizzBuzz" if i % 15 == 0 else
                "Fizz" if i % 3 == 0 else
                "Buzz" if i % 5 == 0 else i
                for i in range(1, 101))
print(*fizzbuzz_gen)