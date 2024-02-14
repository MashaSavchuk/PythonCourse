"""
2. У нас є три логічні змінні.
Перша визначає статус користувача is_active, яка дорівнює True або False.
Друга is_admin визначає, чи є у користувача права адміністратора теж булевого типу.
Третя is_permission — чи дозволено доступ, теж булевого типу.
Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.

Надайте змінній access значення, яке покаже, чи є доступ у користувача. Використовуйте логічні оператори.
Адміністратор завжди має доступ, незалежно від значень змінних is_permission та is_active.
Користувач має доступ, тільки якщо is_permission дорівнює True та is_active також дорівнює True.
"""

is_active = input("Is the user active? ") == '1' # 1 or 0 (True or False)
is_admin = input("Is the user administrator? ") == '1'
is_permission = input("Does the user have access? ") == '1'

# access = is_admin or (is_active and is_permission)
# print(access)


"""
10. Напишіть два подвійні цикли. У першому циклі while ми постійно запитуємо ціле число, 
а у другому за допомогою циклу for обчислюємо суму парних чисел від 0 до введеного числа. 
Вихід з першого циклу здійснюємо, якщо ввели число 0 за допомогою оператора break.
"""
sum = 0
while True:
    num = int(input("Enter integer (0 for output): "))
    if num == 0:
        break
    for number in range(1, num + 1):
        if number % 2 == 0:
            sum += number
    #for number in range(0, num + 1, 2):
    #    sum += number

print(f"Сума чисел від 0 до {num}: {sum}")
#print(sum)