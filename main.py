from LinkedList import CustomLinkedList, get_valid_input
from strategy import IteratorStrategy, FileStrategy


def menu():
    linked_list = CustomLinkedList()
    options_str = "_____Меню_____\n"
    options_str += "1 - Використати стратегію 1 для вставки в список\n"
    options_str += "2 - Використати стратегію 2 для вставки у список\n"
    options_str += "3 - Генерувати дані\n"
    options_str += "4 - Видалити елемент за вказаною позицією\n"
    options_str += "5 - Видалити декілька елементів в межах початкової та кінцевої позиції\n"
    options_str += "6 - Метод для роботи зі списком\n"
    options_str += "7 - Вивести список\n"
    options_str += "8 - Вихід\n"
    while True:
        option = input(options_str)
        if option == '1':
            linked_list.set_strategy(IteratorStrategy())
        elif option == '2':
            linked_list.set_strategy(FileStrategy())
        elif option == '3':
            linked_list.generate_data()
        elif option == '4':
            pos = get_valid_input(prompt="Input position ->", cast=int, error_message="Invalid position",
                                  condition=lambda x: x >= 0)
            linked_list.del_at_pos(pos)
        elif option == '5':
            lower_bound = get_valid_input(prompt="Input lower bound ->", cast=int, error_message="Invalid lower bound")
            upper_bound = get_valid_input(prompt="Input upper bound ->", cast=int, error_message="Invalid upper bound",
                                          condition=lambda x: x > lower_bound)
            while lower_bound <= upper_bound:
                linked_list.del_at_pos(lower_bound)
                lower_bound += 1
        elif option == '6':
            linked_list.find_min_element()
        elif option == '7':
            print(linked_list)
        elif option == '8':
            exit()


menu()
