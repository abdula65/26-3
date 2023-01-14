day = int(input('Введите день рождени: '))
month = int(input('Введите месяц рождения: '))
if (day >= 21 and day <= 31 and month == 3)or(day >= 1 and day <=20 and month == 4):
    print('Овен ')
elif (day >= 21 and day <=30 and month == 4)or(month == 5 and day >= 1 and day <= 21):
    print('Телец ')
elif (day >= 22 and day <= 31 and month == 5)or(month == 6 and day >= 1 and day <= 21):
    print('Близнецы')
elif (day >= 22 and day <= 30 and month == 6)or(month == 7 and day >= 1 and day <= 22):
    print('Рак')
elif (day >= 23 and day <= 30 and month == 7)or(month == 8 and day >= 1 and day <= 21):
    print('Лев')
elif (day >= 22 and day <= 31 and month == 8)or(month == 9 and day >= 1 and day <= 23):
    print('Дева')
elif (day >= 24 and day <= 30 and month == 9)or(month == 10 and day >= 1 and day <= 23):
    print('Весы')
elif (day >= 24 and day <= 31 and month == 10)or(month == 11 and day >= 1 and day <= 22):
    print('Скорпион')
elif (day >= 23 and day <= 30 and month == 11)or(month == 12 and day >= 1 and day <= 22):
    print('Стрелец')
elif (day >= 23 and day <= 31 and month == 12)or(month == 13 and day >= 1 and day <= 20):
    print('Козерог')
elif (day >= 21 and day <= 31 and month == 13)or(month == 14 and day >= 1 and day <= 19):
    print('Водолей')
elif (day >= 20 and day <= 28 and month == 14)or(month == 15 and day >= 1 and day <= 20):
    print('Рыбы')
else:
    print('введна неверная дата')