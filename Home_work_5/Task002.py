# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

#Без бота 
                         
# from random import * 
# user1 = input('Введите имя 1го игрока: ') 
# user2 = input('Введите имя 2го игрока: ') 
# turn = bool(randint(0, 2)) 

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x

# if turn: 
#     print(f'Начинает ходить {user1} ') 
# else: 
#     print(f'Начинает ходить {user2} ') 
# candys = 120     
# while candys > 28: 
#     print('осталось: ', candys) 
#     if turn: 
#         candys -= input_dat(user1)
#         turn = not turn 
#     else: 
#         candys -= input_dat(user2)
#         turn = not turn 
# if turn: 
#     print(f'Победа {user2} ') 
# else: 
#     print(f'Победа {user1} ') 



# С ботом 
 
from random import * 
 
user1 = input('Введите имя 1го игрока: ') 
 
turn = bool(randint(0, 2)) 
if turn: 
    print(f'Начинает ходить {user1} ') 
else: 
    print(f'Начинает ходить БОТ ') 
candys = 120     
while candys > 0: 
    print('осталось: ', candys) 
    if turn: 
        candys -= int(input(f'Ход {user1} ')) 
        turn = not turn 
    else: 
        print('Ходит БОТ') 
        if candys > 60: 
            candys -= randint(0, 29) 
        elif 30 < candys < 60: 
            candys -= randint(0, 15) 
        elif 15 < candys < 30: 
            candys -= randint(0, 5) 
        elif candys < 15: 
            candys -= randint(0, 3) 
        turn = not turn 
        
if turn: 
    print(f'Победил БОТ ') 
else: 
    print(f'Победил {user1} ')