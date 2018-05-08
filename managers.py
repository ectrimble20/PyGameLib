from pygame.sprite import Group
from pygame import Surface
import pygame


class GroupManager(object):
    """
    GroupManager

    Helper class to facilitate creation and management of pygame.sprite.Group instances.
    """
    def __init__(self):
        self._groups = {}
        self._order = []

    def add_group(self, name):
        """
        Add a new group to the list.  Appends the name to the order list as well.
        :param name: str group key name
        :return: None
        """
        self._groups[name] = Group()
        self._order.append(name)

    def insert(self, name, sprite):
        """
        Add a sprite to a specific group, uses the pygame.sprite.Group's .add() function
        :param name: str group key name
        :param sprite: pygame.sprite.Sprite() sprite you wish to add to the group
        :return: None
        """
        if name in self._groups:
            self._groups[name].add(sprite)

    def delete(self, name, sprite):
        """
        Removes a sprite from a specific group, uses the pygame.sprite.Group's .remove() function
        :param name: str group key name
        :param sprite: pygame.sprite.Sprite() sprite you wish to remove from the group
        :return: None
        """
        if name in self._groups:
            self._groups[name].remove(sprite)

    def draw(self, surface):
        """
        Issues the draw() function for all groups.  Draws in the order that they were added.  Uses
        the pygame.sprite.Group's .draw() function handing it the surface.
        :param surface: pygame.Surface
        :return: None
        """
        for n in self._order:
            self._groups[n].draw(surface)

    def count(self, name) -> int:
        """
        Returns the number of sprites in the requested group.
        :param name: str group key name
        :return: int count of sprites in the group
        """
        if name in self._groups:
            return len(self.get_sprites(name))

    def get_sprites(self, name) -> list:
        """
        Returns a list of sprites in the requested group
        :param name: str group key name
        :return: list[pygame.sprite.Sprite()]
        """
        if name in self._groups:
            return self._groups[name].sprites()

    def get_raw_group(self, name) -> Group:
        """
        Returns the instance of pygame.sprite.Group, this is useful when you need to hand the group to pygame sprite
        functions such as groupcollide or spritecollideany and need to directly access the Group object.
        :param name: str group key name
        :return: pygame.sprite.Group
        """
        if name in self._groups:
            return self._groups[name]


class ImageManagerDep(object):
    """
    This class should be considered depreciated in favor of the imagemanager.ImageManager class
    ImageManager

    Centralized image resource holder, this holds Surfaces (images) and their access key, it allows adding, removing
    and retrieving of images.
    """
    def __init__(self):
        self._images = {}

    def load_image_list(self, image_list: dict):
        """
        Loads a list of images from a dictionary, this does not use a dictionary join because the images dict can
        be empty and this will fail with an error in that instance
        :param image_list: dictionary of image keys and image surfaces
        :return: None
        """
        for k, img in image_list.items():
            self.add(k, img)

    def add(self, name: str, surface: Surface):
        """
        Adds an image to the dictionary
        :param name: images access key
        :param surface: image surface
        :return: None
        """
        self._images[name] = surface

    def get(self, name: str) -> Surface:
        """
        Retrieve an image if it exists, returns an empty 0,0 surface if image doesn't exist to attempt to prevent
        an error where a surface is expected by not found.
        :param name: images access key
        :return: pygame.Surface
        """
        return self._images.get(name, Surface([0, 0]))

    def remove(self, name):
        """
        Removes an image surface from the list
        :param name: images access key
        :return: None
        """
        if name in self._images:
            del self._images[name]

    def count(self):
        """
        Returns the length of the image list which is the count of images
        :return: int
        """
        return len(self._images)

    def keys(self):
        """
        Returns a list of the image keys
        :return: list
        """
        return self._images.keys()


class EventManager(object):
    """
    Event Manager, this class is designed to simply watch the state of keys and mouse buttons.

    It provides functions to allow the polling of the state of specific buttons, as well as watching
    for the pygame.QUIT event.

    Note:  This class can be used on it's own, however, it's better used in support of other modules.
    For instance using the polling system on the mouse allows you to easily tell if a button is being
    dragged or for movement, polling the WASD keys can be done with 4 calls to see if they're being
    held down.
    """
    def __init__(self):
        self._key_down = {}
        self._mouse_down = {}
        self._quit_event = False

    def update(self):
        """
        Updates key and mouse button states based on the event queue
        :return: None
        """
        for e in pygame.event.get():
            if e.type == pygame.QUIT:               # window exit was requested
                self._quit_event = True
            if e.type == pygame.KEYDOWN:            # a key was pressed
                self._key_down[e.key] = True
            if e.type == pygame.KEYUP:              # a key was released
                self._key_down[e.key] = False
            if e.type == pygame.MOUSEBUTTONDOWN:    # a mouse button was pressed
                self._mouse_down[e.button] = True
            if e.type == pygame.MOUSEBUTTONUP:      # a mouse button was released
                self._mouse_down[e.button] = False
            if e.type == pygame.MOUSEMOTION:        # Mouse was moved
                pass

    @property
    def mouse_position(self):
        """
        Quick interface for pygame mouse position
        :return: tuple (x, y)
        """
        return pygame.mouse.get_pos()

    def poll_key(self, key: pygame.key):
        """
        Polls a key to see if it's in the pressed state
        :param key: pygame.key constant
        :return: bool
        """
        if key in self._key_down and self._key_down[key] is True:
            return True
        else:
            return False

    def poll_mouse(self, btn):
        """
        Polls the mouse buttons to see if the button is in the pressed state
        :param btn: int value of the button (1 - left, 2 - middle, 3 - right)
        :return: bool
        """
        if btn in (1, 2, 3):  # make sure we were handed a valid button to test
            if btn in self._mouse_down and self._mouse_down[btn] is True:
                return True
        return False

    def quit_event_caught(self):
        """
        Signals if the pygame event QUIT was caught
        :return: bool
        """
        return self._quit_event

    def get_all_keys_down(self):
        """
        Returns all keys flagged as currently down
        :return: list[pygame.key]
        """
        down = []
        for key, state in self._key_down.items():
            if state:
                down.append(key)
        return down
