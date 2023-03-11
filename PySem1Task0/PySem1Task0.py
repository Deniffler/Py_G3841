# Задача №0
# Найти наибольшее число из двух

#  Функция читает данные от пользователя, и преобразует их в int
def ReadData(str):
    return int(input(str))

# Функция находит наибольшее число из двух

def MaxNum(num1,num2):
    maxNum = 0
    if num1 > num2:
        maxNum = num1
        print(f"Максимальное число равно: {maxNum}")
    elif num1 == num2:
        print(f"Число А {num1} = числу Б {num2}")
    else:
        maxNum = num2
        print(f"Максимальное число равно: {maxNum}")
    

# Основной код программы
# Вводим данные с консоли
firstNum = ReadData("Введите число А: ")
secondNum = ReadData("Введите число Б: ")

# Вычисляем макс введенное число
MaxNum(firstNum,secondNum)

