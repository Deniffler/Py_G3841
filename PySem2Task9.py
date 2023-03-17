# Задача No9. Решение в группах
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

#  Функция читает данные от пользователя, и преобразует их в int
def read_data(str):
    return int(input(str))

# Функция считает факториал
def fact_num(x):
    n = 1
    res = 1
    while n <= x:
        res = res * n
        n = n + 1
    return int((res))

# Вводим данные с консоли
num = read_data("Введите целое не отрицательное число: ")

# считаем факториал
fact = fact_num(num)

# выводим результат в консоль
print(fact)