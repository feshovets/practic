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
                return input_matrix()
            elif n == "2":
                return generate_matrix()
            else:
                n = int('error')
                return n
        except ValueError:
            print('Такої опції немає. Спробуйте ще раз\n')
            continue


def int_input(text=""):
    while True:
        try:
            n = int(input(text))
            return n

        except ValueError:
            print(" SYNTAX ERROR ")
            continue


def input_matrix():
    # Initialize matrix
    size = int_input(text="Введіть розмір матриці:")
    square_matrix = []
    # User input values
    print("Введіть значення елементів матриці:")
    for i in range(size):
        a = []
        for j in range(size):
            a.append(int_input())
        square_matrix.append(a)
    return square_matrix


def generate_matrix():
    # Initialize matrix
    size = int_input(text="Введіть розмір матриці:")
    square_matrix = []
    # User input range of values
    a = int_input(text="Введіть діапазон від:\n")
    b = int_input(text="До:\n")
    for i in range(size):
        m = choices(range(a, b), k=size)
        square_matrix.append(m)

    return square_matrix


def start(square_matrix):
    key = int_input(text="Введіть шуканий елемент:\n")
    print(f'Матриця до сортування:\n{square_matrix}')
    sort_mat(square_matrix, key)
    print(f'Матриця після сортування:\n{square_matrix}')


def sort_mat(mat, key):
    # Temporary matrix of size n^2
    n = len(mat)
    temp = [0] * (n * n)
    k = 0
    count = 0

    # Copy the elements of matrix
    # one by one into temp[]
    for i in range(0, n):
        for j in range(0, n):
            temp[k] = mat[i][j]
            k += 1
            count += 1

    # sort temp[]
    swapped = True
    while swapped:
        swapped = False
        for x in range(len(temp) - 1):
            if temp[x] > temp[x + 1]:
                # Swap the elements
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
                count += 1
                # Set True loop again
                swapped = True
    binary_search(temp, 0, len(temp) - 1, key)
    # copy the elements of temp[]
    # one by one in mat[][]
    k = 0
    for i in range(0, n):
        for j in range(0, n):
            mat[i][j] = temp[k]
            k += 1
            count += 1

    print(f'\nСортування виконано за {count} операцій\n')


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
        return -1


while True:
    matrix = menu()
    if start(matrix) is False:
        print("Елемент не знайдено")
    else:
        print("Елемент знайдено")
