# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

list = [5, 6, 8, -5, 5, 8, 'a', -11, 16, 'a']
list1 = []
count = 0
for i in range(len(list)):
    while count < len(list):
        if list[count] == list[i] and count != i:
            count = 0
            break
        count +=1
    else:
        list1.append(list[i])
        count = 0
print(list1)


