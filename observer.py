class Event:
    subscribers = list()

    def __init__(self, message: str, data: dict):
        self.message = message
        self.data = data
        self.notify()

    def __str__(self):
        return f"Event '{self.message}' occurred ({self.data})"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def register(subscriber):
        Event.subscribers.append(subscriber)

    def notify(self):
        for subscriber in self.subscribers:
            subscriber.update(self)


class Observer:
    events = dict()

    def __init__(self, event_name, callback):
        self.events[event_name] = callback

    @staticmethod
    def update(event: Event):
        if event.message in Observer.events.keys():
            Observer.events[event.message](event)


class Logger:

    def __init__(self, file_path=None, writing_mode=None):
        self.file_path = file_path
        self.writing_mode = writing_mode

    def print_to_file(self, event: Event):
        file = open(self.file_path, self.writing_mode)
        file.write(str(event))
