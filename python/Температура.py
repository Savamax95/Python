
import easygui

easygui.msgbox('Эта прога преобразует градусы Цельсия в градусы Фаренгейта')
temp=easygui.enterbox('Ведите температуру в градусах Цельсия:')
cel=float(temp)
fahr=9/5*float(temp)+32
easygui.msgbox('Это '+str(fahr)+' градусов Фаренгейта')
