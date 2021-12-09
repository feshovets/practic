from LinkedList import CustomLinkedList, get_valid_input
from observer import Event, Observer, Logger
from strategy import IteratorStrategy, FileStrategy


def menu():
    logger = Logger("log.txt", "w")
    Event.register(subscriber=Observer)
    Observer("add", logger.print_to_file)
    Observer("add", logger.print_to_file)
    linked_list = CustomLinkedList()
    options_str = "_____Меню_____\n""1 - Використати стратегію 1 для вставки в список\n"\
                  "2 - Використати стратегію 2 для вставки у список\n""3 - Генерувати дані\n"\
                  "4 - Видалити елемент за вказаною позицією\n"\
                  "5 - Видалити декілька елементів в межах початкової та кінцевої позиції\n"\
                  "6 - Метод для роботи зі списком\n""7 - Вивести список\n""8 - Вихід\n"
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
            linked_list.remove(position=pos)
        elif option == '5':
            position = get_valid_input(prompt="Input position ->", cast=int, error_message="Invalid position")
            quantity = get_valid_input(prompt="Input quantity ->", cast=int, error_message="Invalid quantity",
                                       condition=lambda x: x > 0)
            linked_list.remove_range(position=position, quantity=quantity)
        elif option == '6':
            linked_list.find_min_element()
        elif option == '7':
            print(linked_list)
        elif option == '8':
            exit()


menu()
