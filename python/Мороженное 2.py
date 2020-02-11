import easygui
flavor = easygui.choicebox("С каким вкусом ты любишь мороженное?",
 choices = ['Ваниль', 'Шоколад', 'Клубника'] )
easygui.msgbox ("Ты выбрал " + flavor)
