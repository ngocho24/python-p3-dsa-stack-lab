class Stack:
    def __init__(self, items=None, limit=100):
        """
        Initialize a new Stack.

        Parameters:
        - items: A list of initial items in the stack.
        - limit: Maximum number of elements the stack can hold.
        """
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        """
        Check if the stack is empty.

        Returns:
        - True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item):
        """
        Add an item to the top of the stack.

        Parameters:
        - item: The item to be added.

        Raises:
        - ValueError if the stack is full.
        """
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise ValueError("Stack is full. Cannot push item.")

    def pop(self):
        """
        Remove and return the item from the top of the stack.

        Raises:
        - ValueError if the stack is empty.

        Returns:
        - The popped item.
        """
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise ValueError("Stack is empty. Cannot pop item.")

    def size(self):
        """
        Get the number of elements in the stack.

        Returns:
        - The number of elements in the stack.
        """
        return len(self.items)

    def full(self):
        """
        Check if the stack is full.

        Returns:
        - True if the stack is full, False otherwise.
        """
        return len(self.items) == self.limit

    def search(self, target):
        """
        Search for the target element in the stack.

        Parameters:
        - target: The element to search for.

        Returns:
        - The distance between the top of the stack and the target element if present; -1 otherwise.
        """
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i
        return -1
