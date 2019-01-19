"""
Managers are generic dictionary wrappers.  You can use a dictionary to the same effect as a manager except that
managers do not provide iteration functionality nor do they provide direct access to the underlying dictionary.

These are more for organizational purposes than functional purposes.
"""


class CachedManager(object):
    """
    Generic Dict wrapper.  This just provides some managed methods for accessing a dict without giving direct
    access to the dict
    """

    def __init__(self):
        self._cache = {}

    def add(self, key, obj):
        self._cache[key] = obj

    def get(self, key):
        return self._cache.get(key)

    def has(self, key):
        return key in self._cache.keys()

    def clear(self):
        self._cache.clear()


class ImageManager(CachedManager):
    """
    Generic CachedManager with Image specific naming
    """

    def add_image(self, image_key, image_surface):
        super().add(image_key, image_surface)

    def get_image(self, image_key):
        return super().get(image_key)

    def has_image(self, image_key):
        return super().has(image_key)

    def clear_cache(self):
        super().clear()


class FontManager(CachedManager):
    """
    Generic CachedManager with Font specific naming
    """

    def add_font(self, font_key, font_obj):
        super().add(font_key, font_obj)

    def get_font(self, font_key):
        return super().get(font_key)

    def has_font(self, font_key):
        return super().has(font_key)

    def clear_cache(self):
        super().clear()
