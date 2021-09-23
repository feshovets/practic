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


def binary_search(square_matrix):
    key = int_input(text="Введіть шуканий елемент:\n")
    print(f'Матриця до сортування:\n{square_matrix}')
    sort_mat(square_matrix)
    print(f'Матриця після сортування:\n{square_matrix}')
    for i in range(len(square_matrix)):
        if square_matrix[i] == key:
            return True
    return False


def sort_mat(mat):
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
    for i in range(n):
        for j in range(n - i - 1):
            if temp[j] > temp[j + 1]:
                temp[j], temp[j + 1] = temp[j + 1], temp[j]
                count += 1

    # copy the elements of temp[]
    # one by one in mat[][]

    k = 0
    for i in range(0, n):
        for j in range(0, n):
            mat[i][j] = temp[k]
            k += 1
            count += 1

    print(f'\nСортування виконано за {count} операцій\n')


while True:
    matrix = menu()
    if binary_search(matrix) is True:
        print("element founded")
