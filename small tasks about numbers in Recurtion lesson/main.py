"""Дано натуральне числ N, вивести всi натурал. числа 1-N
 використовуючи рекурсiю """


def print_num(n, current = 1):
    if current <= n:
        print(current)
        print_num(n = n, current = current + 1)


"""Дано натуральне числ N, вивести "Yes" якщо 
N є степінем  2, "No" якщо нi"""


def check_pow_2(n):
    if n == 1:                  # 2/2 = 1 -> останнє дiлення вiдбулось, тому n=1
        print("Yes")
    else:
        if n % 2 == 0:          # Якщо дiлиться на 2 без залишку -> продовжуємо дiлити
            check_pow_2(n / 2)
        else:                   # Подiлилось з залишком - то не степінь 2
            print("No")


"""Дано натуральне числ N, вивести суму його цифр, 
наприклад: 125 = 1+2+5 = 8"""


def num_sum(num, sum = 0):
    sum = sum + num % 10                # додаєм залишок від ділення на 10, 125/10 = залишок(12,5) -> додаєм 5
    if num // 10 == 0:                  # Якщо цiла частина вiд дiлення на 10 = 0 -> нема ще чисел до суми
        return sum
    num = num // 10                     # Цiла частина вiд дiлення на 10, 125 // 10 = цiле(12,5) = 12
    return num_sum(num=num, sum=sum)


def print_n_to_1(n):
    if n == 0:
        return 0
    print(n)
    n -= 1
    print_n_to_1(n)


"""Напишите рекурсивную функцию, чтобы сгенерировать и вернуть список от 1 до N."""


def list_generator(n, num_list):
    if not num_list:                        # Визначаемо перший раз список
        num_list = [1]
    if len(num_list) == n:                  # Умова виходу з рекурсії
        return num_list
    num_list.append(len(num_list)+1)        # Додаємо єлемент списку
    return(list_generator(n, num_list))     # Рекурсія


"""Напишите рекурсивную функцию, чтобы сгенерировать и вернуть список от 1 до N.
Аргументом функции является только N"""


def list_generator2(n):
    if n == 0:                          # Умова виходу з рекурсії
        return []
    return [n] + list_generator2(n-1)   # Рекурсія

"""Напишите функцию, которая рекурсивно ищет в сложном объекте значение. Сложный 
объект — это будет список списков списков и т.д. Например, [1, 2, [3, 4, [5, [6, []]]]]. Функция 
должна рекурсивно заходить внутрь вложенных массивов, а если это другой тип данных 
игнорировать его"""


def val_search(list_of_lists, val):
    # ____Проходимо по елементам списку_____

    for element in list_of_lists:           # Проходимо по елементам списку
        if isinstance(element, list):       # перевіряємо чи є там список всередині
            if val_search(element, val):    # якщо є список -> рекурсивно заходимо в нього
                return True                 # якщо в ході рекурсії вернеться True - то знайшли значення і вертаємо True
        else:
            if element == val:              # порівнюємо int-елементи списку з val і шукаємо чи є таке значення
                return True
    #________________________________________

    return False                            # якщо нічого не = val, то в кінці-кінців вертаємо False

""" test functions """

#print_num(10)
#check_pow_2(16)
#print(num_sum(125))
#print_1_to_n(5)
#print(list_generator(n=5, num_list=[]))
#res = list_generator2(5)
#print(res)


k = [1, [1,2,3], 5, [1, 2, [5, 6, [7]]]]
val = 6

print(val_search(k, val))








