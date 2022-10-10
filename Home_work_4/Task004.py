# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import*

k = 2
a = randint(0, 101)
b = randint(0, 101)
c = randint(0, 101)
print(a, b, c)
result = ''
if b ==0: result = f'{a}*x**{k} + {c}*x**{k-2} = 0'
if b == 0 and c == 0: result = f'{a}*x**{k} = 0'
if c == 0: result = f'{a}*x**{k} + {b}*x**{k-1} = 0'
else: result = f'{a}*x**{k} + {b}*x**{k-1} + {c}*x**{k-2} = 0'

# with open('C:\\УЧЕБА\\Python\\Home_work_4\\file44.txt', 'w') as file44:
#     file44.write(result)

with open('C:\\УЧЕБА\\Python\\Home_work_4\\file444.txt', 'w') as file444:
    file444.write(result)
