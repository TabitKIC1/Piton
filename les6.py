# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


a1, d, n = int(input()), int(input()), int(input())
for i in range (1,n+1):
    print(a1+i*d)




# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
 
lo, hi = 3, 8
data = [randint(1, 10) for _ in range(20)]
print("Масив", data, sep='\n')
indexes = [i for i, v in enumerate(data) if lo <= v <= hi]
print("индекс:", indexes, sep='\n')
result = []
i = len(indexes)
while i :
    i -= 1
    result.append(data.pop(indexes[i]))
print("Элемент", data, sep='\n')
print("Элемент", result, sep='\n')