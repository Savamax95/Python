from random import randint
 
print('Привет! Как тебя зовут?')
my_name = input()
print(f'Что ж, {my_name}, я загадываю число от 1 до 20.')
number = randint(1, 20)
 
print('у тебя 5 попыток')
see_also = 1
 
while see_also != 6:
    guess = int(input('Попробуй угадать. >> '))
    if guess < number:
        print('Твоё число слишком маленькое.')
    elif guess > number:
        print('Твоё число слишком большое.')
    else:
        break
    see_also += 1
 
if see_also != 6:
    print(f'Отлично, {my_name}! Ты справился за {see_also} попытки!')
else:
    print(f'Увы. Я загадала число  {number}.')
