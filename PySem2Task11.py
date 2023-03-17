# Задача N11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Input: 5 Output: 6

#  Функция читает данные от пользователя, и преобразует их в int
def read_data(str):
    return int(input(str))


# Вводим данные с консоли
num = read_data("Введите целое не отрицательное число: ")

fibo = 0
num1 = 0 
num2 = 1
count = 3
while fibo < num:
    fibo = num1 + num2
    temp_num = num2
    num2 = fibo
    num1 = temp_num
    count +=1
    
if num == fibo:
    print(f"число {num} является {count-1} по счету числом в последовательности Фиббоначи")
else:
    print ("-1")