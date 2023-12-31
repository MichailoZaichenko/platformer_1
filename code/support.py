from csv import reader
import pygame
from settings import tile_size
from os import walk

# Imports all images from a path
def import_folder(path):
    surface_list = []
    
    for _,__,img_files in walk(path):
        for img in img_files:  
            full_path = path + '/' + img
            img_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surf)

    return surface_list

# Reads csv file, map.
def import_csv_layout(path):
    terrain_map = []
    with open(path) as map:
        level = reader(map,delimiter=',')
        for row in level:
            terrain_map.append(list(row))

    return terrain_map

# Cuts up a tileset and returns a list of all tiles in it of size tile_size
def import_cut_graphic(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_width()/tile_size)
    tile_num_y = int(surface.get_width()/tile_size)

    cut_tiles = []

    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tile_size
            y = row * tile_size

            # Here we blit a rect from the original surface into a new surface (the cut tile)
            new_surf = pygame.Surface((tile_size, tile_size), flags=pygame.SRCALPHA)
            new_surf.blit(surface, (0,0), pygame.Rect(x,y,tile_size,tile_size))
            cut_tiles.append(new_surf)
    
    return cut_tiles

