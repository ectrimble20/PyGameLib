class Node(object):
    """
    LinkedList node, contains an object (data) and a reference to the next node (no node if None)
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):
    """
    Node-based linked list implemented in pure Python
    """

    def __init__(self):
        self._head = None
        self._tmp = None

    def is_empty(self):
        """
        Quick check if the node contains a leading node and is not empty
        :return: bool
        """
        return self._head is None

    def __len__(self):
        """
        Implements data model to allow len() built in call on the object
        :return: int
        """
        c = 0
        n = self._head
        while n is not None:
            n = n.next_node
            c += 1
        return c

    def __iter__(self):
        """
        Implements data model to allow `for N in LL` built in call on the object
        :return: LinkedList
        """
        self._tmp = self._head
        return self

    def __next__(self):
        """
        Implements data model to allow `for N in LL` next method for built in iteration
        :return: Next node until nodes are exhausted, then raises StopIteration
        """
        t = self._tmp
        if t is None:
            raise StopIteration
        else:
            self._tmp = self._tmp.next_node
            return t.data

    def add(self, value):
        """
        Add a new node
        :param value: object
        :return: None
        """
        if self._head is None:
            self._head = Node(value, None)
            return
        n = self._head
        p = None
        while True:
            if n is None:
                p.next_node = Node(value)
                break
            else:
                p = n
                n = n.next_node

    def after(self, check, value):
        """
        Insert a new node after a specific value/object
        :param check: object to insert after
        :param value: object to insert
        :return: None
        """
        n = self._head
        s = Node(value, None)
        while n is not None:
            if n.data == check:
                s.next_node = n.next_node
                n.next_node = s
                break
            else:
                n = n.next_node

    def before(self, check, value):
        """
        Insert a new node before a specific value/object
        :param check: object to insert before
        :param value: object to insert
        :return: None
        """
        n = self._head
        p = None
        s = Node(value, None)
        while n is not None:
            if n.data == check:
                s.next_node = n
                if p is None:
                    self._head = s
                else:
                    p.next_node = s
                break
            else:
                p = n
                n = n.next_node

    def delete(self, check):
        """
        Delete a specific object from the list
        :param check: object to delete
        :return: None
        """
        n = self._head
        p = None
        while n is not None:
            if n.data == check:
                if p is None:
                    self._head = n.next_node
                else:
                    p.next_node = n.next_node
                break
            else:
                p = n
                n = n.next_node

    def debug_out(self):
        """
        Prints a debug message with the contents of the linked list
        :return: None
        """
        n = self._head
        pos = 1
        while n is not None:
            print("Position {} is value {}".format(pos, n.data))
            n = n.next_node
            pos += 1
        print("=====================================")

    def copy(self):
        """
        Creates a deep cope of the linked list
        :return: LinkedList
        """
        c = LinkedList()
        for n in self:
            c.add(n)
        return c


class Queue(object):
    """
    First In First Out (FIFO) queue implementation in pure python
    """

    def __init__(self):
        self._queue = []

    def enqueue(self, obj):
        """
        Add a new object to the Queue
        :param obj: object
        :return: None
        """
        self._queue.append(obj)

    def dequeue(self):
        """
        Remove and return next object in queue
        :return: object|None if empty
        """
        if self.count() > 0:
            return self._queue.pop(0)
        else:
            return None

    def peek(self):
        """
        Return next object without removing it from the queue
        :return: object|None if empty
        """
        if self.count() > 0:
            return self._queue[0]
        else:
            return None

    def clear(self):
        """
        Clear the queue
        :return: None
        """
        self._queue.clear()

    def count(self):
        """
        Return the number of objects in the queue
        :return: int
        """
        return len(self._queue)


class Stack(object):
    """
    Last In First Out (LIFO) stack implementation in pure python
    """

    def __init__(self, max_size=0):
        self._max_size = max_size
        self._stack = []

    def push(self, obj):
        """
        Add an object to the stack
        :param obj: object
        :return: None
        """
        if self._max_size != 0 and self.count() >= self._max_size:
            raise RuntimeError("Stack size exceeds maximum set stack size")
        self._stack.append(obj)

    def pop(self):
        """
        Return and remove the next object in the stack
        :return: object|None if empty
        """
        if self.count() > 0:
            return self._stack.pop(len(self._stack) - 1)
        else:
            return None

    def peek(self):
        """
        Return the next object in the stack without removing it
        :return: object|None
        """
        if self.count() > 0:
            return self._stack[len(self._stack) - 1]
        else:
            return None

    def clear(self):
        """
        Clear the stack
        :return: None
        """
        self._stack.clear()

    def count(self):
        """
        Return the number of objects in the stack
        :return: int
        """
        return len(self._stack)
