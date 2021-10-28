from LinkedList import CustomLinkedList


def menu():
    my_list = CustomLinkedList()
    options_str = "_____Program menu_____\n"
    options_str += "1 - add from keyboard \n"
    options_str += "2 - add from range\n"
    options_str += "3 - print list\n"
    options_str += "4 - find function\n"

    while True:
        option = input(options_str)
        if option == '1':
            my_list.add_from_kb()
        elif option == '2':
            my_list.add_from_range()
        elif option == '3':
            print(my_list)
        elif option == '4':
            f = my_list.find_min_element()
            print(f)
