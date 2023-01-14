
ten = list(range(1, 11))
evens = list(filter(lambda i: i % 2 == 0, ten))
square_lst = list(map(lambda i: i ** 2, evens))

print("Список ten: ", ten)
print("Список четных чисел evens: ", evens)
print("Список возведенных в квадрат четных чисел square_lst: ", square_lst, "\n")

def word (ten, int_index):
    return ten[int(int_index)]

if __name__ == "__main__":
    while True:
        try:
            print("Для выхода из программы введите exit\n")
            user_input = input("Введите искомый индекс: ")
            if user_input == "exit":
                print(CLEAR_SCREEN + "Программа остановлена.")
                break

            print(
                 f"Число по индексу {user_input}: ",
                word (ten, user_input),
            )
        except ValueError:
            print(CLEAR_SCREEN + "Введенный индекс должен быть целым числом!")
            continue
        except IndexError:
            len_ten = len(ten)
            if len_ten >= 1:
                print(
                    + f"Допустимый диапазон индексов от -{len_ten} до {len_ten - 1}"
                )
            else:
                print(
                    CLEAR_SCREEN
                    + "Список пуст, искать нечего. Выполняется выход из программы."
                )
                break
            continue



