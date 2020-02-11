import random

secret = random.randint(1, 20)
guess = 0
tries = 0
print ('Карина,я создал для тебя игру!')
print ("Угадай число от 1 до 20. Я дам тебе 5 попыток.")
see_also = 1
while see_also !=6:
    guess = int(input("Твой вариант?"))
    if guess < secret:
        print ("Карина соберись! Это слишком мало!")
    elif guess > secret:
        print ("Карина ты борщишь! Это слишком много!")
    else: 
        break
    see_also += 1
    
if see_also != 6:
    print ("Карина умница! Ты угадала!")
else:
    print ("Эх Карина! Ты не угадала(((")
    
