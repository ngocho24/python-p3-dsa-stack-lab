class Stack:
    def __init__(self, items=None, limit=100):
        """
        Constructor for the Stack class.

        :param items: Initial items in the stack (defaults to an empty list).
        :param limit: Maximum limit of the stack (defaults to 100).
        """
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        """
        Check if the stack is empty.

        :return: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Add an item to the top of the stack.

        :param item: The item to be added.
        :return: None
        """
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            print("Stack is full. Cannot push item.")

    def pop(self):
        """
        Remove and return the item from the top of the stack.

        :return: The item popped from the stack.
        """
        if not self.isEmpty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop item.")

    def peek(self):
        """
        Return the item from the top of the stack without removing it.

        :return: The item at the top of the stack.
        """
        if not self.isEmpty():
            return self.items[-1]
        else:
            print("Stack is empty. No item to peek.")

    def size(self):
        """
        Get the number of items in the stack.

        :return: The size of the stack.
        """
        return len(self.items)

    def full(self):
        """
        Check if the stack is full.

        :return: True if the stack is full, False otherwise.
        """
        return len(self.items) == self.limit

    def search(self, target):
        """
        Search for a specific item in the stack.

        :param target: The item to search for.
        :return: The position of the item from the top of the stack (1-based index),
                 or -1 if the item is not found.
        """
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i
        return -1


