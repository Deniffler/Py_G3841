# Задача N7. Решение в группах

# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер 
# кратен 4, но не кратен 100, а также если он кратен 400.
# 
# Input: 2016 
# Output: YES

#  Функция читает данные от пользователя, и преобразует их в int
def read_data(str):
    return int(input(str))

# Функция проверяет год на високосность
def leap_year(num):
    if num % 400 == 0:
        print(f"Год {num} - високосный")
    elif num % 4 == 0 and num % 100 != 0:
        print(f"Год {num} - високосный")
    else:
        print(f"Год {num} - не високосный")

# Основной код программы

# Вводим данные с консоли
year = read_data ("Введите год: ")
# Выводим результат в консоль
leap_year(year)
