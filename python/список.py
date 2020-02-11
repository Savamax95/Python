list=[]
print('Добавить или искать слово(a/l)?')
for i in range(5):
    name=input()
    list.append(name)
print('Вот эти имена',list)
print('Вот эти имена после сортировки',sorted(list))

