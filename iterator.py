import random


class Iterator:
    def __init__(self, quantity, *args):
        self.quantity = quantity
        self.args = args

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == self.quantity:
            raise StopIteration
        self.counter += 1
        return random.randint(*self.args)


def generator(quantity, *args):
    counter = 0
    while counter != quantity:
        counter += 1
        yield random.randint(*args)
