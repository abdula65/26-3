file = open('file.tzt', 'w')
file.write('Бишкек, Кырыгызстан')
file.close()

with open('file.txt', 'a') as file:
    file.write('111111')
