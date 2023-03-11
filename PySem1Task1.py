# Задача No1. 
# За день машина проезжает n километров. Сколько дней нужно, 
# чтобы проехать маршрут длиной m километров? 
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.


# Подключаем библиотеку math
import math

#  Функция читает данные от пользователя, и преобразует их в int
def read_data(str):
    return int(input(str))

# Функция считает необходимое количество дней
def day_of_dist(dist_per_day,all_dist):

    # Округление вверх math.ceil()
    res = math.ceil(all_dist/dist_per_day)
    return res


# Основной код программы
# Вводим данные с консоли
dist_per_day = read_data("Сколько машина проезжает km за 1 день? ")
dist_all = read_data("Введите общий киллометраж маршрута ")
day_all = day_of_dist(dist_per_day,dist_all)
print(f"Что бы проехать {dist_all} км, машине необходимо {day_all} дней")

