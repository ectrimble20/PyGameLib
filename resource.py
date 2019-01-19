from os import path
import pygame
import json


def load_image(image_dir, image_name, color_key=None, use_alpha=False):
    full_path = path.join(image_dir, image_name)
    if not path.isfile(full_path):
        raise FileNotFoundError("Expected image file {} was not found".format(full_path))
    surface = pygame.image.load(image_name)
    if use_alpha:
        surface = surface.convert_alpha()
    else:
        surface = surface.convert()
    if color_key is not None:
        surface.set_colorkey(color_key)
    return surface


def load_font(font_dir, font_name, font_size):
    # check that we have a font_file with an extension, if not, append TTF
    file, ext = path.splitext(font_name)
    if ext == '':
        font_name = "{}.ttf".format(font_name)
    full_path = path.join(font_dir, font_name)
    if not path.isfile(full_path):
        raise FileNotFoundError("Expected font file {} was not found".format(full_path))
    return pygame.font.Font(full_path, font_size)


def load_sprite_sheet(sheet_surface, sheet_map, image_manager=None):
    if not type(sheet_surface) == pygame.Surface:
        raise TypeError("load_sprite_sheet expects a pygame.Surface object, not a {}".format(type(sheet_surface)))
    if not type(sheet_map) == dict:
        raise TypeError("load_sprite_sheet expects a dict map not a {}".format(type(sheet_map)))
    sub_images = {}
    for key, rect in sheet_map.items():
        if image_manager is None:
            sub_images[key] = sheet_surface.subsurface(rect)
        else:
            image_manager.add_image(key, sheet_surface.subsurface(rect))
    if image_manager is None:
        return sub_images
    else:
        return None


def load_sprite_sheet_map_from_json(json_file) -> dict:
    if not path.isfile(json):
        raise FileNotFoundError("load_sprite_sheet_map_from_json expects JSON file to be a full path")
    with open(json_file, "r") as handle:
        j_data = json.load(handle)
    j_sprite_map = {}
    for key, map_data in j_data.items():
        j_sprite_map[key] = pygame.Rect(map_data['x'], map_data['y'], map_data['w'], map_data['h'])
    return j_sprite_map
