import random, easygui

secret = random.randint(1, 20)
guess = 0
tries = 0
easygui.msgbox('Карина,я создал для тебя игру! Угадай число от 1 до 20. Я дам тебе 5 попыток.')
see_also = 1
while see_also !=6:
    guess = easygui.integerbox("Твой вариант?")
    if guess < secret:
        easygui.msgbox(str(guess)+" Карина соберись! Это слишком мало!")
    elif guess > secret:
        easygui.msgbox(str(guess)+" Карина ты борщишь! Это слишком много!")
    else: 
        break
    see_also += 1
    
if see_also != 6:
    easygui.msgbox("Карина умница! Ты угадала!")
else:
    easygui.msgbox("Эх Карина! Ты не угадала(((")
    
