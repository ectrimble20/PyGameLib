import pygame
import os


class ImageManager(object):
    """
    ImageManager

    This is a combination of the SpriteLoader as well as the ImageManager from the managers package.
    The aim of this is to bundle the functionality into a single class while keeping the interface
    simple.  Like the other image functions, sprite map loading is the most complex due to the key
    requirement when loading a set of images, and that's not complicated if you keep them in order.

    usage:
    # create a new manager for our image directory
    m = ImageManager("/path/to/images/")
    # load an individual image
    m.load_image("my_image.png", "image_key", (255, 0, 255))
    # load a sprite sheet
    keys = ['one', 'two', 'three', 'four']
    m.load_sprite_sheet("sheet.jpg", 1, 4, 16, 16, keys, (255, 0, 255))
    # get an image back
    i = m.get("one")  # retrieves image "one" from our sprite sheet
    i_two = m.get("image_key")  # retrieves the image loaded above
    m.remove("image_key")  # deletes the image loaded above
    """

    def __init__(self, image_dir):
        self._image_directory = image_dir  # this should be an absolute path
        if not os.path.isdir(self._image_directory):
            raise NotADirectoryError("{} is not a directory!".format(image_dir))
        self._images = {}  # dictionary of image_key => pygame.Surface

    def load_image(self, file_name, file_key, alpha=None):
        """
        Load a single image into the dictionary
        :param file_name: name of the file (should be located in the image directory)
        :param file_key: image key, used to look up the image later
        :param alpha: tuple color that should be treated as alpha
        :return: None
        """
        path_to_image = os.path.join(self._image_directory, file_name)
        if not os.path.isfile(path_to_image):
            raise FileNotFoundError("{} was not found!".format(path_to_image))
        surface = pygame.image.load(path_to_image).convert()
        if alpha is not None:
            surface.set_colorkey(alpha)
        self._images[file_key] = surface

    def load_sprite_sheet(self, file_name, rows, cols, img_w, img_h, keys, alpha=None):
        """
        Load a sprite maps images
        :param file_name: name of the file (should be located in the image directory
        :param rows: number of image rows
        :param cols: number of image columns
        :param img_w: sprite width
        :param img_h: sprite height
        :param keys: List of keys to use (use None to skip an image)
        :param alpha: tuple color that should be treated as alpha
        :return: None
        """
        if len(keys) < 1:
            raise KeyError("Expect at least 1 image key")
        self.load_image(file_name, '_temp_', alpha)
        surface = self.get('_temp_')
        keys.reverse()  # reverse the list order so we can pop the names
        for r in range(rows):
            for c in range(cols):
                k = keys.pop()
                if k is None:  # we check for None here, if it is, it's an empty image
                    continue
                surface_slice = pygame.Surface([img_w, img_h])
                surface_slice.blit(surface, (0, 0), ((c*img_w), (c*img_h), (r*img_w), (r*img_h)))
                if alpha is not None:
                    surface_slice.set_colorkey(alpha)
                self._images[k] = surface_slice
        self.remove('_temp_')

    def get(self, key):
        """
        Retrieve an image surface
        :param key: image key used to look up the image
        :return: pygame.Surface
        """
        if key in self._images:
            return self._images[key]

    def remove(self, key):
        """
        Remove/Delete an image from the dictionary
        :param key: image key used to look up the image
        :return: None
        """
        if key in self._images:
            del self._images[key]
