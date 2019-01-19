import unittest
from manager import *


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

    def test_cached_manager(self):
        cm = CachedManager()
        cm.add('1', 1)
        cm.add('2', 2)
        cm.add('3', 3)
        cm.add('4', 4)
        self.assertEqual(cm.get('1'), 1)
        self.assertEqual(cm.get('2'), 2)
        self.assertEqual(cm.get('3'), 3)
        self.assertEqual(cm.get('4'), 4)
        self.assertTrue(cm.has('1'))
        self.assertFalse(cm.has('32'))
        cm.clear()
        self.assertFalse(cm.has('1'))

    def test_image_manager(self):
        cm = ImageManager()
        cm.add_image('1', 1)
        cm.add_image('2', 2)
        cm.add_image('3', 3)
        cm.add_image('4', 4)
        self.assertEqual(cm.get_image('1'), 1)
        self.assertEqual(cm.get_image('2'), 2)
        self.assertEqual(cm.get_image('3'), 3)
        self.assertEqual(cm.get_image('4'), 4)
        self.assertTrue(cm.has_image('1'))
        self.assertFalse(cm.has_image('32'))
        cm.clear()
        self.assertFalse(cm.has_image('1'))

    def test_font_manager(self):
        cm = FontManager()
        cm.add_font('1', 1)
        cm.add_font('2', 2)
        cm.add_font('3', 3)
        cm.add_font('4', 4)
        self.assertEqual(cm.get_font('1'), 1)
        self.assertEqual(cm.get_font('2'), 2)
        self.assertEqual(cm.get_font('3'), 3)
        self.assertEqual(cm.get_font('4'), 4)
        self.assertTrue(cm.has_font('1'))
        self.assertFalse(cm.has_font('32'))
        cm.clear()
        self.assertFalse(cm.has_font('1'))
