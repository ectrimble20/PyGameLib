import unittest
from container import *


class TestContainer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_linked_list(self):
        t_ll = LinkedList()
        self.assertTrue(t_ll.is_empty())
        t_ll.add(1)
        self.assertFalse(t_ll.is_empty())
        t_ll.add(2)
        self.assertFalse(t_ll.is_empty())
        t_ll.add(3)
        t_ll.add(4)
        t_ll.add(5)
        t_ll.add(6)
        self.assertEqual(len(t_ll), 6)
        t_ll.delete(6)
        self.assertEqual(len(t_ll), 5)
        i = 1
        for val in t_ll:
            self.assertEqual(val, i)
            i += 1
        t_ll.after(5, 6)
        i = 1
        for val in t_ll:
            self.assertEqual(val, i)
            i += 1

    def test_stack(self):
        t_stack = Stack()
        t_stack.push(1)
        t_stack.push(2)
        t_stack.push(3)
        self.assertEqual(t_stack.count(), 3)
        self.assertEqual(t_stack.pop(), 3)
        self.assertEqual(t_stack.pop(), 2)
        self.assertEqual(t_stack.pop(), 1)
        t_stack.push(1)
        t_stack.push(2)
        self.assertEqual(t_stack.peek(), 2)
        t_stack.pop()
        self.assertEqual(t_stack.peek(), 1)
        t_stack.push(5)
        t_stack.push(6)
        t_stack.push(7)
        t_stack.clear()
        self.assertEqual(t_stack.count(), 0)
        t_stack = Stack(4)
        t_stack.push(1)
        t_stack.push(2)
        t_stack.push(3)
        t_stack.push(4)
        with self.assertRaises(RuntimeError):
            t_stack.push(5)

    def test_queue(self):
        t_queue = Queue()
        t_queue.enqueue(1)
        t_queue.enqueue(2)
        t_queue.enqueue(3)
        t_queue.enqueue(4)
        self.assertEqual(t_queue.count(), 4)
        self.assertEqual(t_queue.dequeue(), 1)
        self.assertEqual(t_queue.dequeue(), 2)
        self.assertEqual(t_queue.dequeue(), 3)
        self.assertEqual(t_queue.dequeue(), 4)
        t_queue.enqueue(1)
        t_queue.enqueue(2)
        self.assertEqual(t_queue.peek(), 1)
        t_queue.dequeue()
        self.assertEqual(t_queue.peek(), 2)
        t_queue.enqueue(3)
        t_queue.enqueue(4)
        t_queue.enqueue(5)
        t_queue.clear()
        self.assertEqual(t_queue.count(), 0)
