# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Type a number of set_1: "))
set_1 = set([int(input(f"type a {i + 1} element of set_1: ")) for i in range(n)])

m = int(input("Type a number of set_2: "))
set_2 = set([int(input(f"Type a {i + 1} element of set_2: ")) for i in range(m)])
result = list(set_1.intersection(set_2))
result.sort()
print(result)
