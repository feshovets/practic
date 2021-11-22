from decorator import print_exception, get_valid_input, validate_file_path
from strategy import Strategy
from iterator import Iterator


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class CustomLinkedList:
    strategy: Strategy

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    @print_exception
    def add_from_kb(self):
        data = get_valid_input(prompt="Input value ->", cast=int, error_message="Invalid data")
        self.add_at_end(data)

    @print_exception
    def add_at_end(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = temp

    @print_exception
    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    @print_exception
    def del_at_pos(self, position):
        if self.head is None:
            raise Exception("Empty Linked List")
        if position > len(self):
            raise Exception("Unavailable position")
        else:
            current = self.head
            previous = None
            count = 1
            while count < position:
                previous = current
                current = current.next
                count += 1
            previous.next = current.next
            del current

    @print_exception
    def add_at_pos(self, position, data):
        if position == 0:
            self.add_at_beginning(data)
        elif position-1 == len(self):
            self.add_at_end(data)
        else:
            if position-1 > len(self):
                raise Exception("Unavailable position")
            current = self.head
            count = 1
            while count < position - 1:
                current = current.next
                count += 1
            temp = Node(data)
            temp.next = current.next
            current.next = temp

    @print_exception
    def find_min_element(self):
        len_l = len(self)
        if len_l % 2 == 1:
            raise Exception("Function doesn't work with even list")
        first = self.head
        second = self.head.next
        min_list = [int(first.data)*int(second.data)]
        count = 0
        while count < len_l and second.next is not None:
            first = second.next
            second = first.next
            min_list.append(int(first.data)*int(second.data))
            count += 2
        return min(min_list)

    @print_exception
    def extend(self, iterable):
        for elem in iterable:
            self.add_at_end(elem)

    @print_exception
    def extend_at_pos(self, iterable, position):
        for elem in iterable:
            position += 1
            self.add_at_pos(position=position, data=elem)

    @print_exception
    def set_strategy(self, strategy: Strategy) -> None:
        try:
            self.strategy = strategy
        except Exception or ValueError:
            raise ValueError('Unknown strategy')

    def iterator_generation(self):
        lower_bound = get_valid_input(prompt="Input lower bound ->", cast=int, error_message="Invalid lower bound")
        upper_bound = get_valid_input(prompt="Input upper bound ->", cast=int, error_message="Invalid upper bound",
                                      condition=lambda x: x > lower_bound)
        quantity = get_valid_input(prompt="Input upper quantity ->", cast=int, error_message="Invalid quantity",
                                   condition=lambda x: x > 0)
        pos = get_valid_input(prompt="Input position ->", cast=int, error_message="Invalid position",
                              condition=lambda x: x >= 0)
        iterator = Iterator(quantity, lower_bound, upper_bound)
        self.extend_at_pos(iterable=iterator, position=pos)

    def file_generation(self):

        file_name = get_valid_input(prompt="Input file name ->", cast=str, error_message="Invalid file name",
                                    condition=lambda x: validate_file_path(x))
        pos = get_valid_input(prompt="Input position ->", cast=int, error_message="Invalid position",
                              condition=lambda x: x >= 0)
        file = open(file_name, mode='r')
        for line in file:
            elements = line.split(",")
            self.extend_at_pos(position=pos, iterable=elements)
        file.close()

    @print_exception
    def generate_data(self):
        if self.strategy.execute() == "IteratorStrategy":
            self.iterator_generation()
        elif self.strategy.execute() == "FileStrategy":
            self.file_generation()
        else:
            raise Exception("No strategy (^_^)")
