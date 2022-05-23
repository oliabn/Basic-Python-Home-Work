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


""" test functions """

#print_num(10)
#check_pow_2(16)
print(num_sum(125))