"""
5. Напишімо функцію, яка повертає повне ім'я користувача. У базі даних переважно зберігають ім'я користувача first_name, 
його прізвище last_name та по батькові, або, як заведено в західних країнах, друге ім'я — middle_name. 
Причому middle_name — це необов'язкова змінна, вона може бути, а може й не передаватися під час виклику функції. 
Наша функція повертатиме рядок з повним ім'ям 'first_name middle_name last_name', якщо ж змінна middle_name відсутня, 
то рядок, що повертається повинен бути 'first_name last_name'.
"""
def get_fullname(first_name, last_name, middle_name = None):
# def get_fullname(first_name, last_name, middle_name = " "):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"
    # or
    # if middle_name:
    #     return f"{first_name} {middle_name} {last_name}"
    # return f"{first_name} {last_name}"
    # or
    # return f"{first_name} {middle_name} {last_name}" if middle_name else f"{first_name} {last_name}"

# Функція з middle_name
full_name_with_middle = get_fullname("Mariia", "Jn", "Savchuk")
print(full_name_with_middle)

# Функція без middle_name
full_name_without_middle = get_fullname("Olha", "Savchuk")
print(full_name_without_middle)

#get_fullname("Mariia", "Jn", "Savchuk")
#print(get_fullname)


"""
6. Наступне завдання буде суто теоретичним, і ми потренуємося працювати з довільною кількістю аргументів.
Створіть дві функції:
перша first буде мати першим параметром змінну size, а також вона може приймати будь-яку кількість позиційних 
аргументів. Функція повинна повернути суму size із загальною кількістю переданих до неї позиційних аргументів.
друга функція second так само матиме першим параметром size і прийматиме довільну кількість ключових аргументів, 
і також має повернути суму size з кількістю переданих у функцію ключових аргументів.
"""
def first(size, *arg):
    #print(arg)
    return size + len(arg)
    # sum_first = size + len(arg)
    # return sum_first
    # print(sum_first)
    
def second(size, **arg2):
    #print(arg2)
    return size + len(arg2)
    # sum_second = size + len(arg2)
    # return sum_second
    # print(sum_second)

print(first(5, "first", "second", "third")) # кортеж, позиційниі аргументи приходять як кортеджі
print(first(1, "Alex", "Boris")) # кортеж, позиційниі аргументи приходять як кортеджі
print(second(3, comment_one="first", comment_two="second", comment_third="third")) #словник, ключові аргументи приходять як словники
print(second(10, comment_one="Alex", comment_two="Boris")) #словник, ключові аргументи приходять як словники


"""
7. Онлайн-магазин "У Бобра" надає послугу експрес доставлення своїх товарів за ціною 5¤ за перший товар у замовленні 
та 2¤ - за всі наступні товари. Необхідно реалізувати функцію, яка приймає як перший параметр кількість товарів 
у замовленні quantity, але також має бути присутнім параметр, що передається тільки за ключем discount.

Параметр discount за замовчуванням має значення 0 - знижки немає. Приймає значення від 0 до 1. 
Функція cost_delivery повертає загальну суму за доставлення товару з урахуванням знижки.
Треба передбачити, що функція cost_delivery при визові може приймати будь-яку кількість позиційних аргументів.

Приклад:
cost_delivery(2, 1, 2, 3)
При такому виклику quantity дорівнює 2, а параметр discount за умовчанням має значення 0.
"""
def cost_delivery(quantity, *_, discount = 0):   # *_  - це аргументи, яки ми будемо ігнорувати, вони прийдуть кортеджем
    #нижнє підкреслення це змінна яку ми не будемо використовувати
    first_product = 5
    additional_product = 2
    total_price = (first_product + ((quantity - 1) * additional_product)) * (1 - discount)
    return total_price

# def cost_delivery(quantity, *_, discount=0):
#     total_cost = 5 + (quantity - 1) * 2
#     return (1 - discount) * total_cost

print(cost_delivery(2, 1, 2, 3)) # == 7
print(cost_delivery(3, 3)) # == 9
print(cost_delivery(1)) # == 5
print(cost_delivery(2, 1, 2, 3, discount=0.5)) # == 3.5


"""
8. Для функції попереднього завдання створіть рядки документації. Можна використовувати наступний шаблон
    "Функція повертає суму за доставлення замовлення.
    Перший параметр &mdash; кількість товарів в замовленні.
    Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."
"""
def cost_delivery(quantity, *_, discount = 0):
    """
    Функція для розрахунку вартості товару
    
    Функція приймає два аргументи quantity та discount
    - quantity - кількість товару, яку замовили
    - discount - знижка (значення від 0 до 1)

    Також функція приймає позиційні аргументи, які вона ігнорує
    """
    result = (5 + 2 * (quantity - 1)) * (1 - discount)

    return result
print(cost_delivery.__doc__)


"""
9. Ми проводимо розіграш призів серед перших 50 підписників ютуб-каналу. Ми маємо 7 призів для розіграшу. 
Може виникнути питання, скільки різних списків переможців ми можемо отримати під час розіграшу? 
Для цього ми будемо використовувати формулу сполучень без повторень

Cnk = n! / ((n - k)! · k!)
де n — це загальна кількість людей (випадків), а k — кількість людей, які отримали призи.

Напишіть функцію number_of_groups, яка приймає параметри n та k, і за допомогою функції factorial 
повертає нам скільки різних списків переможців ми можемо отримати при розіграші

Зверніть увагу на те, які великі значення ми отримуємо для факторіала. Рекурсивні висловлювання треба 
завжди застосовувати з обережністю при обчисленнях, щоб не отримати переповнення пам'яті.
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    # if n < 2:
    #     return 1
    # else:
    #     result = 1
    #     for i in range(2, n + 1):
    #         result *= i
    #     return result

def number_of_groups(n, k):
    return factorial(n) // (factorial(n - k) * factorial(k))

# тлумачення рекурсіі
# def factorial(n, depth = 0):
#     if n == 0:
#         print(f'Depth: {depth}, f({n}) = 1')
#         return 1
#     else:
#         print(f'Depth: {depth}, f({n}) = {n} * factorial({n - 1})')
#         result = n * factorial(n - 1, depth = depth + 1)
#         print(f'Depth: {depth}, f({n}) = {result}')
#         return result
#print(factorial(0))   
print(factorial(5))   

"""
10. Однією з класичних задач на розуміння рекурсії, яку часто задають на співбесідах, 
особливо початківцям-програмістам — це ряд Фібоначчі.

Ряд Фібоначчі — це послідовність чисел виду: 0, 1, 1, 2, 3, 5, 8, ... де кожне наступне 
число послідовності виходить додаванням двох попередніх членів ряду.

У загальному вигляді для обчислення n-го члена ряду Фібоначчі слід обчислити вираз:
F0 = 0
F1 = 1
Fn = Fn-1 + Fn-2.

Це завдання можна вирішити рекурсивно, викликаючи функцію, що обчислює числа послідовності доти, 
доки виклик не сягне членів ряду менше n = 1, на якій задана послідовність.
"""
def fibonacci(n):
    # if n == 0:
    #     return 0
    # elif n =+ 1:
    #     return 1
    # or 
    # print(n)
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(20))

# інший варіант
# def factorial(n, result = 1):
#     if n == 0:
#         return result
#     else:
#         return factorial(n - 1, result = n * result)
# print(factorial(25))

# інший варіант (тут щось не правильно)
# def fibonacci(n, prev=0, curr=1):
#     if n ==0 :
#         return prev
#     elif n == 1:
#         return curr
    
#     return fibonacci(n - 1, curr, prev + curr)
# print(fibonacci(3))