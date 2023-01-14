start = 0
finish = 100
mid = (start + finish) // 2
i = 0
with open('results.txt', 'w', encoding='UTF-8') as file:
 while True:
    print(f"Вы загадали {mid}?")
    answer = input("да!, меньше: < или больше: > :")
    i += 1
    if answer.lower() == 'да!':
            file.write(f"Попытки: {i}\n")
            file.write(f"Ваше число: {mid}\n")
            file.write(f'Программа завершила задачу:>')
            print("Программа завершено!")
            break
    elif answer == '>':
        start = mid
        mid = (start + finish) // 2
    elif answer == '<':
        finish = mid
        mid = (start + finish) // 2
    else:
        print("попробуйте еще  раз :")