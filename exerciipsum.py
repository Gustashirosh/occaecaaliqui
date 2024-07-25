class EventManager:
    def __init__(self):
        self.handlers = []  # Initialize the handlers list

    def add_handler(self, handler):
        self.handlers.append(handler)  # Add a handler to the list

    def remove_handler(self, handler):
        self.handlers.remove(handler)  # Remove a handler from the list

    def trigger(self, event):
        for handler in self.handlers:
            handler(event)  # Call each handler with the event


def handler1(event):
    print("Handler 1", event)

def handler2(event):
    print("Handler 2", event)


manager = EventManager()
manager.add_handler(handler1)
manager.add_handler(handler2)

manager.trigger({'type': 'click'})  # Trigger an event
