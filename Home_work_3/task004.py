# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n=int(input())
# m=n
# p=1
# d1=0
# while m>0:
#     d1=d1+m%2*p
#     p=p*10
#     m=m//2
# print(d1)

x = 150
y = str(bin(x))
print(y[2:])

