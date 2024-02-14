fin=open('game.txt','r',encoding='utf-8') #открытие файла
title=fin.readline() #чтение первой строки
print(title)
game=[x.strip().split('$') for x in fin] #создание массива из данных файла
fin.close() #закрытие файла

#x[0] - название игры
#x[1] - название персонажа
#x[2] - номер ошибки
#x[3] - дата
for x in game: #прохождение программы по каждой строке
    if '55' in x[2]: #нахождение багов с числом 55
        print(f'У персонажа\t<{x[1]}>\tв игре\t<{x[0]}>\tнашлась ошибка с кодом:\t <{x[2]}.\tДата фиксации:\t {x[3]}')
        x[2]='Done'
        x[3]='0000-00-00'

fout=open('game-new.csv','w',encoding='utf-8')
fout.write(title)
for x in game:
    s = '$'.join(x)+'\n'
    fout.write(s)
    print(s)
fout.close()