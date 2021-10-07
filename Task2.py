from random import choices


def menu():
    while True:
        try:
            n = input('Меню:\n"1" - ввести масив для сортування\n'
                      '"2" - згенерувати масив для сортування\n'
                      '"exit" - вихід з програми\n')
            if n == 'exit':
                print('програма завершила свою роботу')
                exit()
            elif n == "1":
                size = get_input(prompt="Введіть розмір матриці:", cast=int, condition=lambda x: x > 0,
                                 error_message="Розмір матриці повинен бути быльшим за нуль")
                m = input_matrix(size)
                return calculations(m)
            elif n == "2":
                size = get_input(prompt="Введіть розмір матриці:", cast=int, condition=lambda x: x > 0, 
                                 error_message="Розмір матриці повинен бути быльшим за нуль")
                m = generate_matrix(size)
                return calculations(m)
            else:
                n = int('error')
                return n
        except ValueError:
            print('Такої опції немає. Спробуйте ще раз\n')
            continue


def get_input(prompt="", cast=None, condition=None, error_message=None):
    while True:
        try:
            res = (cast or str)(input(prompt))
            assert condition is None or condition(res)
            return res
        except (ValueError, Exception):
            print(error_message or "Помилка. Спробуйте ще раз")


def input_matrix(n):
    arr = []
    print('Введіть значення матриці:')
    for i in range(n):
        a = []
        for j in range(n):
            a.append(get_input(cast=int))
        arr.append(a)
    return arr


def generate_matrix(n):
    arr = []
    from_ = get_input(prompt="Введіть діапазон від:", cast=int)
    to_ = get_input(prompt="До:", cast=int, condition=lambda x: x > from_, error_message="Неправильний діапазон")
    for i in range(n):
        m = choices(range(from_, to_), k=n)
        arr.append(m)
    return arr


def convert_to_array(sq_matrix):
    temp = []
    for i in range(len(sq_matrix)):
        for j in range(len(sq_matrix)):
            temp.append(sq_matrix[i][j])
    return temp


def sort_mat(array):
    # sort
    count = 0
    swapped = True
    while swapped:
        swapped = False
        for x in range(len(array) - 1):
            if array[x] > array[x + 1]:
                # Swap the elements
                array[x], array[x + 1] = array[x + 1], array[x]
                count += 1
                # Set True loop again
                swapped = True
    print(f'\nСортування виконано за {count} операцій\n')
    return array


def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        print("Елемент не знайдено")
        return -1


def calculations(m):
    print("Матриця:", m)
    m_arr = convert_to_array(m)
    print("Масив:", m_arr)
    m_arr = sort_mat(m_arr)
    print("Посортований масив:", m_arr)
    search_el = get_input(prompt="Введіть шуканий елемент:", cast=int)
    print("Індекс елемента в масиві:", (binary_search(m_arr, 0, len(m_arr)-1, search_el)), "\n\n")


while True:
    menu()

