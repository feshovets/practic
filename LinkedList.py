from decorator import print_exception


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class CustomLinkedList:
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

    def add_from_kb(self):
        data = int(input("Input value ->"))
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

    def extend(self, iterable):
        for elem in iterable:
            self.add_at_end(elem)
