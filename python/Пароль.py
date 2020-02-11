import easygui
cod=easygui.enterbox('Введите пароль')
if cod=='1234':
    easygui.msgbox('Красавчик.продолжим')
else:
    easygui.msgbox('Нет доступа')
