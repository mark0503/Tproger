#ЗАДАНИЕ 1
#Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
#Выведите все элементы, которые меньше 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
i = 0
for i in (a):
    if a[i] < 5:
        b.append(a[i])
        i = i + 1
print(b)

#ЗАДАНИЕ 3
#Отсортируйте словарь по значению в порядке возрастания и убывания.
import operator
result = {}
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
result = dict(sorted(d.items(), key=operator.itemgetter(1)))
print(result)
result = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=(1)))
print(result)


#ЗАДАНИЕ 4
#Напишите программу для слияния нескольких словарей в один.
a = {132: 2, 3241: 4}
b = {142: 2, 3857: 4}
c = {161: 2, 365: 4}
a.update(b)
a.update(c)
print(a)

#ЗАДАНИЕ 5
#Найдите три ключа с самыми высокими значениями в словаре
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
print(my_dict)
my_dict = dict(sorted(my_dict.items(), key=operator.itemgetter(1), reverse=(1)))
a = my_dict.keys()
b = tuple(a)
i = 0
while i < 3:
    print(b[i], end=' ')
    i += 1

