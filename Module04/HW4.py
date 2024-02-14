"""
2. При аналізі даних часто виникає необхідність позбавитися екстремальних значень, 
перш ніж почати працювати з даними далі. Напишіть функцію prepare_data, яка видаляє з 
переданого списку найбільше та найменше значення, сортує його в порядку зростання 
і повертає змінений список як результат.
"""
def prepare_data(data):
    max_value = max(data)
    min_value = min(data)
    data.remove(max_value)
    data.remove(min_value)
    #data.sort() # sort() ця ф-ція ничого не повертає None
    return sorted(data)
    #return sorted(data)[1:-1]

    # data.remove(min(data))
    # data.remove(max(data))
    # sorted_data = sorted(data)
    # return sorted_data

list = [2, 5, 4, 3, 2, 1]
# print(list.sort())
# print(list)
# print(sorted(list))
# print(list)
print(prepare_data(list))


"""
3. Сучасна система оцінок в університеті має такий вигляд:
Оцінка	Бали	Оцінка ECTS	Пояснення
1	0-34	F	Unsatisfactorily
2	35-59	FX	Unsatisfactorily
3	60-66	E	Enough
3	67-74	D	Satisfactorily
4	75-89	C	Good
5	90-95	В	Very good
5	96-100	A	Perfectly
Реалізуйте дві функції. Перша буде використовуватись у бухгалтерії при розрахунку стипендії, 
get_grade приймає ключ у вигляді оцінки ECTS, і має повертати відповідну п'ятибальну оцінку 
(перший стовпчик таблиці). Друга get_description теж приймає ключ у вигляді оцінки ECTS, 
але повертатиме пояснення оцінки в текстовому форматі (останній стовпчик таблиці) і буде використана 
в електронній заліковій книжці студента. На відсутній ключ функції повинні повертати значення None .
"""
def get_grade(key):
    ects_to_five_scale = {
        'F': 1,
        'FX': 2,
        'E': 3,
        'D': 3,
        'C': 4,
        'B': 5,
        'A': 5
    }
    return ects_to_five_scale.get(key)
    #return ects_to_five_scale[key]
print(get_grade('A'))

def get_description(key):
    ects_descriptions = {
        'F': 'Unsatisfactorily',
        'FX': 'Unsatisfactorily',
        'E': 'Enough',
        'D': 'Satisfactorily',
        'C': 'Good',
        'B': 'Very good',
        'A': 'Perfectly'
    }
    return ects_descriptions.get(key, None)
print(get_description('A'))

# or
# grade_description = {
#     'F': '1 Unsatisfactorily',
#     'FX': '2 Unsatisfactorily',
#     'E': '3 Enough',
#     'D': '3 Satisfactorily',
#     'C': '4 Good',
#     'B': '5 Very good',
#     'A': '5 Perfectly'
# }
# def get_grade(key):
#     return int(grade_description.get(key)[0:1])
# print(get_grade('A'))

# def get_description(key):
#     return grade_description.get(key)[2:]
# print(get_description('A'))


"""
4. Як ми знаємо, ключ у словнику має бути унікальним, тоді як значення його ні. Реалізуйте функцію lookup_key 
для пошуку всіх ключів за значенням у словнику. Першим параметром у функцію ми передаємо словник, а другим — значення, 
що хочемо знайти. Таким чином, результат може бути як список ключів, так і порожній список, якщо ми нічого не знайдемо.
"""
{'a': 1}.items()
def lookup_key(data, value):
    result_key = []
    # print(data.items())
    for key, dict_value in data.items():
        if dict_value == value:
            result_key.append(key)
    return result_key

print(lookup_key({'key1':1, 'key2': 2, 'key3': 3, 'key4': 2}, 2))

# or
# def lookup_key(data, value):
#     result_key = []
#     for key in data.keys():
#         if data[key] == value:
#             result_key.append(key)
#     return result_key

# print(lookup_key({'key1':1, 'key2': 2, 'key3': 3, 'key4': 2}, 2))


"""
5. У нас є список показників студентів групи – це список з отриманими балами з тестування. 
Необхідно поділити список на дві частини. Напишіть функцію split_list, яка приймає список (цілі числа), 
знаходить середнє значення бала у списку та ділить його на два списки. У перший потрапляють значення менше 
середнього, включаючи середнє значення, тоді як у другий — строго більше від середнього. Функція повертає 
кортеж цих двох списків. Для порожнього списку повертаємо два порожні списки.
"""
def split_list(grade):
    if len(grade) == 0:
        return [], []
    below_average = []
    above_average = []
    below_average, above_average = [], []
    average_grade = sum(grade) / len(grade)
    
    for student_grade in grade:
        if student_grade <= average_grade:
            below_average.append(student_grade)
        else:
            above_average.append(student_grade)
    return below_average, above_average

grades_list = [75, 90, 80, 65, 85, 95]
result = split_list(grades_list)

print(f"Below average grades: {result[0]}")
print(f"Above average grades: {result[1]}")


"""
6. Потрібно написати функцію реалізації наступного ігрового алгоритму. На вхід функції game подається 
два аргументи: список, що складається зі списків, та початкове значення power - енергія гравця. 
Внутрішні списки — це списки з числовим значенням енергії, які може поглинути гравець, якщо вони менші 
або дорівнюють його енергії. Після поглинання елементу списку він рухається за списком далі та, 
або поглинає список повністю до кінця, або, якщо знаходить енергію вище за власну, залишає його і 
переходить до наступного списку. Наприкінці обходу всіх списків функція повинна повернути загальну 
отриману енергію гравця.

Приклад списку:
[[1, 1, 5, 10], [10, 2], [1, 1, 1]]
Для цього списку і початкової енергії рівної 1 гравець поглине з першого списку перші два значення і 
залишить його, зустрівши значення 5, через те, що на цей момент матиме енергію в 3. Другий список 
пропустить відразу, а третій повністю поглине та отримає остаточну енергію в 6.
"""
def game(terra, power):
    for sub_list in terra:
        for element in sub_list:
            if element <= power:
                power += element
            else:
                break
    return power
    
print(game([[1, 1, 5, 10], [10, 2], [1, 1, 1]], 2))
print(game([[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]], 1)) #  == 11


"""
7. Всім відомо, що для доступу до кредитної картки банку потрібний пін-код. Класично склалося, 
що це поєднання чотири цифри. Нам необхідно вирішити наступне програмістське завдання. 
Є підготовлений перелік пін-кодів. Напишіть функцію is_valid_pin_codes, яка буде приймати 
як параметр список цих пін-кодів — рядок з чотирьох цифр і повертати логічне значення — 
валідний список чи ні. Переконайтеся, що серед цих пін-кодів у списку не буде дублікатів, 
всі вони зберігаються у вигляді рядків, їх довжина дорівнює 4 символам і містять вони тільки цифри.

Приклад аргументу для функції is_valid_pin_codes:
['1101', '9034', '0011']
Якщо список відповідає всім поставленим умовам, функція повертає логічне значення True. 
Якщо хоч одну з умов порушено, повертається значення — False. Передбачити перевірку 
на порожній список в аргументі функції та повернути при цьому значення False.
"""
def is_valid_pin_codes(pin_codes):
    repeating_value = len(set(pin_codes)) == len(pin_codes)
    if len(pin_codes) == 0:
        return False
    for pin_code in pin_codes:
        if len(pin_code) != 4:
            return False
        if not (isinstance(pin_code, str)):
            return False
        if not pin_code.isdigit():
            return False
    return repeating_value

print(is_valid_pin_codes(['1101', '9034', '0011']) == True)


"""
8. Другий етап. Необхідно написати функцію is_valid_password, яка перевірятиме отриманий 
параметр — пароль на надійність.

Критерії надійного пароля:

Довжина рядка пароля вісім символів.
Містить хоча б одну літеру у верхньому регістрі.
Містить хоча б одну літеру у нижньому регістрі.
Містить хоча б одну цифру.
Функція is_valid_password повинна повернути True, якщо переданий параметр пароль 
відповідає вимогам на надійність. Інакше повернути False.
"""
def is_valid_password(password):
    if len(password) != 8:
        return False
    is_title = False
    is_lower = False
    is_number = False
    for character in password:
        if character.istitle():
            is_title = True
        if character.islower():
            is_lower = True
        if character.isdigit():
            is_number = True
    return is_title and is_lower and is_number

print(is_valid_password('NmlDl1V0'))
print(is_valid_password('NmlDl1V0') == True)


"""
9. Напишіть функцію parse_folder, вона приймає єдиний параметр path, який є об'єктом Path. 
Функція повинна просканувати директорію path та повернути кортеж із двох списків. 
Перший — це список файлів усередині директорії, другий — список директорій.

Приклад виводу функції:

(['.gitignore', 'readme.md'],
 ['.git', '.idea', '.vscode', 'module-01', 'module-02', 'module-03', 'module-04', 'module-05', 'module-06', 'module-07',
  'module-08', 'module-09', 'module-10', 'module-11', 'module-12'])
"""
from pathlib import Path

def parse_folder(path):
    files = []
    folders = []

    for element in path.iterdir():
        if element.is_dir():
            folders.append(element.name)
        else:
            files.append(element.name)

    return files, folders

print(parse_folder(Path('.')))


"""
10. Створіть функцію parse_args, яка повертає рядок, складений з аргументів командного рядка, 
розділених пробілами. Наприклад, якщо скрипт був викликаний командою: python run.py first second, 
то функція parse_args повинна повернути рядок наступного виду 'first second'.
"""
import sys

def parse_args():
    result = ""
    # print(sys.argv)
    # for arg in sys.argv:
    for arg in sys.argv[1:]:
        result += arg + ' '

    return result.strip()  # strip() щоб прибрати пробіл в кінці

# or
    # return ' '.join(sys.argv[1:])

print(parse_args())
# python3 Module04/HW4.py first second third це запускаємо в терміналі