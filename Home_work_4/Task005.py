# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.

# вариант 1
# result = 0
# with open('C:\\УЧЕБА\\Python\\Home_work_4\\file44.txt', 'r') as file1:
#     st1 = file1.read()
# with open('C:\\УЧЕБА\\Python\\Home_work_4\\file444.txt', 'r') as file2:
#     st2 = file2.read()
# result = st1 + ' + ' + st2
# print(result)
# with open ('C:\\УЧЕБА\\Python\\Home_work_4\\result.txt', 'w') as result:
#     result.write(result)

with open('C:\\УЧЕБА\\Python\\Home_work_4\\file44.txt', 'r') as file44:
    data1 = file44.read()
with open('C:\\УЧЕБА\\Python\\Home_work_4\\file444.txt', 'r') as file444:
    data2 = file444.read()
if len(data1) > 20:
    a = int(data1[0:2])
    b = int(data1[10:12])
    c = int(data1[20:21])
    print(a, b, c)
if len(data2) > 20:
    d = int(data2[0:2])
    e = int(data2[10:12])
    f = int(data2[20:21])
    print(d, e, f)
result = f'{a+d}*x**2 + {b+e}*x**1 + {c+f}*x** = 0'
final_result = str(result)
print(final_result)

with open ('C:\\УЧЕБА\\Python\\Home_work_4\\result.txt', 'w') as result:
    result.write(final_result)
