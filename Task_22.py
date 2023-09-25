# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# n = int(input("Type a number of set_1: "))
# set_1 = set([int(input(f"type a {i + 1} element of set_1: ")) for i in range(n)])
#
# m = int(input("Type a number of set_2: "))
# set_2 = set([int(input(f"Type a {i + 1} element of set_2: ")) for i in range(m)])
# result = list(set_1.intersection(set_2))
# result.sort()
# print(result)


n = int(input("first set: "))
m = int(input("second set: "))

for i in range(n):
    set_1 = set(int(input(f"type the {i + 1} element of set_1: ")))
print(set_1)

for i in range(m):
    set_2 = set(int(input(f"type the {i + 1} element of set_2: ")))
print(set_2)

# from random import randint
# n_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
# print(n_set)
# m_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(*s_set)



from random import randint
