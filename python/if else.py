import easygui
gender = easygui.enterbox("Вы мальчик или девочка? ('m' or 'f') ")
if gender == 'f':
    age = int(easygui.enterbox('Сколько вам лет? '))
    if age >= 10 and age <= 12:
        easygui.msgbox ('Вы можете играть в этой команде')
    else:
        easygui.msgbox('Вы не прошли по возрасту.')
else:
    easygui.msgbox('В команду принимаются только девочки.')
