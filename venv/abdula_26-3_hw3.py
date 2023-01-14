sogl = "бвгджзйклмнпрстфхцчшщdcfghjklmnpqrstvwxyz"
gls = "aeiouyaoыэяюёие"
while True:
    sogla = 0
    gla = 0
    f = input('Для выхода нажмите "exit", "выход"\n'
              'Введите слово:').lower()
    if f == 'exit' or f == 'выход':
       print('Программа завершина')
       break
    letters = len(f)
    for i in f:
        if i in sogl:
            sogla += 1
        elif i in gls:
            gla += 1
    print(f"Количество букв: {letters}\nКоличество согласных: {sogla}\nКоличество гласных: {gla}")
    print(f'Гласные/согласные: {round(gla/letters * 100, 2)}% {round(sogla/letters * 100,2)}%')