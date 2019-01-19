import unittest
import os
from resource import *
from manager import ImageManager
import pygame
from pygame import Surface, Rect
from pygame.font import Font


class TestContainer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pygame.init()
        self._d = pygame.display.set_mode((100, 100))
        self.test_res_dir = os.path.join(os.getcwd(), "test_resources")
        self.test_image = "test.png"
        self.test_map = os.path.join(self.test_res_dir, "test_map.json")
        self.test_font = "trebuc.ttf"
        self.test_font_no_ext = "trebuc"
        self.test_im = ImageManager()
        self.test_d_map = {
            "dark_grey": Rect(0, 0, 32, 32),
            "dark_red": Rect(32, 0, 32, 32),
            "brown": Rect(0, 32, 32, 32),
            "light_grey": Rect(32, 32, 32, 32)
        }

    def tearDown(self):
        pygame.quit()

    def test_load_image(self):
        img = load_image(self.test_res_dir, self.test_image)
        self.assertEqual(type(img), Surface)
        with self.assertRaises(FileNotFoundError):
            load_image(self.test_res_dir, "FAKE_IMAGE")

    def test_load_font(self):
        ft = load_font(self.test_res_dir, self.test_font, 12)
        self.assertEqual(type(ft), Font)
        ftx = load_font(self.test_res_dir, self.test_font_no_ext, 12)
        self.assertEqual(type(ftx), Font)
        with self.assertRaises(FileNotFoundError):
            load_font(self.test_res_dir, "FAKE_FONT", 12)

    def test_load_sprite_sheet(self):
        img = load_image(self.test_res_dir, self.test_image)
        images = load_sprite_sheet(img, self.test_d_map, None)
        self.assertEqual(len(images), 4)
        for k, i in images.items():
            self.assertEqual(type(i), Surface)
        load_sprite_sheet(img, self.test_d_map, self.test_im)
        self.assertTrue(self.test_im.has_image('dark_grey'))
        self.assertTrue(type(self.test_im.get_image('dark_grey')), Surface)
        self.assertTrue(self.test_im.has_image('dark_red'))
        self.assertTrue(type(self.test_im.get_image('dark_red')), Surface)
        self.assertTrue(self.test_im.has_image('brown'))
        self.assertTrue(type(self.test_im.get_image('brown')), Surface)
        self.assertTrue(self.test_im.has_image('light_grey'))
        self.assertTrue(type(self.test_im.get_image('light_grey')), Surface)

    def test_load_sprite_sheet_map_from_json(self):
        m = load_sprite_sheet_map_from_json(self.test_map)
        self.assertTrue(m.get('dark_grey'), type(Rect))
        self.assertTrue(m.get('dark_red'), type(Rect))
        self.assertTrue(m.get('brown'), type(Rect))
        self.assertTrue(m.get('light_grey'), type(Rect))
