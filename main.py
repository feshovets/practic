from LinkedList import CustomLinkedList
from iterator import Iterator, generator


def menu():
    my_list = CustomLinkedList()
    options_str = "_____Program menu_____\n"
    options_str += "1 - add from keyboard \n"
    options_str += "2 - print list\n"
    options_str += "3 - find function\n"
    options_str += "4 - delete element at pos\n"
    options_str += "5 - add element at pos\n"
    options_str += "6 - generate list using iterator\n"
    options_str += "7 - generate list using generator\n"
    options_str += "8 - exit\n"
    while True:
        option = input(options_str)
        if option == '1':
            my_list.add_from_kb()
        elif option == '2':
            print(my_list)
        elif option == '3':
            f = my_list.find_min_element()
            print(f)
        elif option == '4':
            pos = int(input("Input position ->"))
            my_list.del_at_pos(pos)
        elif option == '5':
            pos = int(input("Input position ->"))
            data = int(input("Input value ->"))
            my_list.add_at_pos(pos, data)
        elif option == '6':
            lower_bound = int(input("Input lower bound ->"))
            upper_bound = int(input("Input upper bound ->"))
            quantity = int(input("Input quantity of nodes ->"))
            my_list.extend(Iterator(quantity, lower_bound, upper_bound))
        elif option == '7':
            lower_bound = int(input("Input lower bound ->"))
            upper_bound = int(input("Input upper bound ->"))
            quantity = int(input("Input quantity of nodes ->"))
            my_list.extend(generator(quantity, lower_bound, upper_bound))


menu()
