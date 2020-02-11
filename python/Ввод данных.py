import easygui
index=easygui.enterbox('Введите ваш почтовый индекс: ')
st=easygui.enterbox('Введите вашу страну: ')
gor=easygui.enterbox('Введите ваш город: ')
addr=easygui.enterbox('Введите вашу улицу: ')
dom=easygui.enterbox('Введите номер вашего дома: ')
kv=easygui.enterbox('Введите номер вашей квартиры: ')
name=easygui.enterbox('Введите ваше имя: ')
whole_addr = index + ','+st+','+gor+','+addr+','+dom+','+kv+ '\n' + name
easygui.msgbox(whole_addr, "Вот твой адрес:")
