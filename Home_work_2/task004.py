# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле 
# file.txt в одной строке одно число.

n = int(input('введите число '))
list = []
for i in range(-n, n+1):
    list.append(i)
print(list)

composition = 1

data = open('file.txt', 'w')
data.write('2\n')
data.write('15\n')
data.write('0\n')
data.write('11\n')
data.write('4\n')
data.write('1\n')
data.close()

path = 'file.txt'
data = open(path, 'r')
for line in data:
    position = int(line)
    composition *= list[position]
data.close()
print(composition)
