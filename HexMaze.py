import pygame
from random import choice
import collections
import math
RES = WIDTH, HEIGHT = 1202,902
TILE = 50
cols,rows = WIDTH // TILE, HEIGHT // TILE

pygame.init()
sc = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

class Hexagon:
    def __init__(self, q_coord, r_coord, s_coord, value=0, undo_val=0):
        """initializes class"""
        self.q = q_coord
        self.r = r_coord
        self.s = s_coord
        self.visited = False
        self.walls = {1: True, 2:True, 3:True, 4:True, 5:True, 6:True}
        self.open_neighbors =[]
        self.grid = (q, r, s)
        self.empty = False
        self.value = value
        self.undo_val = undo_val
        self.neighbors = [(self.q, self.r + 1, self.s - 1),
                          (self.q, self.r - 1, self.s + 1),
                          (self.q + 1, self.r - 1, self.s),
                          (self.q + 1, self.r, self.s - 1),
                          (self.q - 1, self.r + 1, self.s),
                          (self.q - 1, self.r, self.s + 1)]

    def get_val(self):
        """returns value of tile"""
        return self.value

    def get_undo_val(self):
        """returns undo value"""
        return self.undo_val

    def set_val(self, num):
        """sets value of tile"""
        self.value = num

    def print_coord(self):
        """returns (q,r,s) coordinates of tile"""
        return self.q, self.r, self.s

    def viable_neighbors(self):
        """returns neighbors of tile that exist in the grid"""
        neighbors = []
        for neighbor in self.neighbors:
            if neighbor in hex_list_grid:
                place = hex_list_grid.index(neighbor)
                thing = hex_list[place]
                if not thing.visited:
                    neighbors.append(hex_list[place])
        return choice(neighbors) if neighbors else False



    def draw(self, size, fill = "turquoise"):
        if self.value == 0:
            fill = "turquoise"
        elif self.value == 1:
            fill = "red"
        elif self.value == 2:
            fill = "purple"
        coord = hex_to_pixel(self)
        if self.visited:
            pygame.draw.polygon(sc, pygame.Color(fill),
        [(coord.x + size * math.sin(3.14 / 2) + hi, coord.y + size * math.cos(3.14 / 2) + wi),
              (coord.x + size * math.sin(3.14 / 6) + hi, coord.y + size * math.cos(3.14 / 6) + wi),
              (coord.x + size * math.sin(11 * 3.14 / 6) + hi, coord.y + size * math.cos(11 * 3.14 / 6) + wi),
              (coord.x + size * math.sin(3 * 3.14 / 2) + hi, coord.y + size * math.cos(3 * 3.14 / 2) + wi),
              (coord.x + size * math.sin(7 * 3.14 / 6) + hi, coord.y + size * math.cos(7 * 3.14 / 6) + wi),
              (coord.x + size * math.sin(5 * 3.14 / 6) + hi, coord.y + size * math.cos(5 * 3.14 / 6) + wi)])
        if self.walls[1]:
            pygame.draw.line(sc, pygame.Color('black'),
                             ((coord.x + size * math.sin(7 * 3.14 / 6) + hi, coord.y + size * math.cos(7 * 3.14 / 6) + wi)),
                             ((coord.x + size * math.sin(5 * 3.14 / 6) + hi, coord.y + size * math.cos(5 * 3.14 / 6) + wi)),3)
        if self.walls[2]:
            pygame.draw.line(sc, pygame.Color("black"),
                             (coord.x + size * math.sin(5 * 3.14 / 6) + hi, coord.y + size * math.cos(5 * 3.14 / 6) + wi) ,
                             (coord.x + size * math.sin(3.14 / 2) + hi, coord.y + size * math.cos(3.14 / 2) + wi), 3)
        if self.walls[3]:
            pygame.draw.line(sc, pygame.Color("black"),
                             (coord.x + size * math.sin(3.14 / 2) + hi, coord.y + size * math.cos(3.14 / 2) + wi),
                             (coord.x + size * math.sin(3.14 / 6) + hi, coord.y + size * math.cos(3.14 / 6) + wi),3)
        if self.walls[4]:
            pygame.draw.line(sc, pygame.Color("black"),
                             (coord.x + size * math.sin(3.14 / 6) + hi, coord.y + size * math.cos(3.14 / 6) + wi),
                             (coord.x + size * math.sin(11 * 3.14 / 6) + hi, coord.y + size * math.cos(11 * 3.14 / 6) + wi) ,3)
        if self.walls[5]:
            pygame.draw.line(sc, pygame.Color("black"),
                             (coord.x + size * math.sin(11 * 3.14 / 6) + hi, coord.y + size * math.cos(11 * 3.14 / 6) + wi),
                             (coord.x + size * math.sin(3 * 3.14 / 2) + hi, coord.y + size * math.cos(3 * 3.14 / 2) + wi),3)
        if self.walls[6]:
            pygame.draw.line(sc, pygame.Color("black"),
                             (coord.x + size * math.sin(3 * 3.14 / 2) + hi, coord.y + size * math.cos(3 * 3.14 / 2) + wi),
                             (coord.x + size * math.sin(7 * 3.14 / 6) + hi, coord.y + size * math.cos(7 * 3.14 / 6) + wi),3)
Point = collections.namedtuple("Point", ["x", "y"])
def hex_to_pixel(h):
    """converts hex grid to pixel screen location"""
    x = (3 / 2 * h.q) * 38
    y = (math.sqrt(3.0) / 2.0 * h.q + math.sqrt(3.0) * h.r) * 38
    return Point(x + 135, y - 145)


def pixel_to_flat_hex(point):
    """converts pixel screen location to hex grid"""
    q_coord = (2 / 3 * (point[0] - 135)) / 38
    r_coord = (-1 / 3 * (point[0] - 135) + math.sqrt(3) / 3 * (point[1] + 145)) / 38
    return round(q_coord), round(r_coord)



hi = HEIGHT / 2
wi = WIDTH / 2

def remove_walls(current, next):
    if next.q < current.q:
        if next.s > current.s:
            current.walls[6] = False
            next.walls[3] = False
        if next.r > current.r:
            current.walls[5] = False
            next.walls[2] = False
    if next.q == current.q:
        if next.s > current.s:
            current.walls[1] = False
            next.walls[4] = False
        if next.r > current.r:
            current.walls[4] = False
            next.walls[1] = False
    if next.q > current.q:
        if next.r < current.r:
            current.walls[2] = False
            next.walls[5] = False
        if next.s < current.s:
            current.walls[3] = False
            next.walls[6] = False

def get_mouse():
    """takes a mouse click location and converts to hex grid location"""
    mouse_pos = pygame.mouse.get_pos()
    mouse_list = [mouse_pos[0] - hi, mouse_pos[1] - wi]
    mouse = pixel_to_flat_hex(mouse_list)
    return mouse


stack = []
hex_list = []
for q in range(-6, 7):
    for r in range(-6, 7):
        for s in range(-6, 7):
            if (q + r + s) == 0:
                cell = Hexagon(q, r, s)
                hex_list.append(cell)
hex_list_grid = [square.grid for square in hex_list]

current_cell = hex_list[0]
current_cell.set_val(1)
end_point= choice(hex_list)
end_point.set_val(2)
stack = []
while True:
    sc.fill(pygame.Color('grey'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    [hexagon.draw(39) for hexagon in hex_list]
    current_cell.visited = True
    next_cell = current_cell.viable_neighbors()
    if next_cell:
        next_cell.visited = True
        next_cell.open_neighbors.append(current_cell)
        current_cell.open_neighbors.append(next_cell)
        stack.append(current_cell)
        remove_walls(current_cell, next_cell)
        current_cell = next_cell
    elif stack:
        current_cell = stack.pop()

    new_mouse_pos = get_mouse()
    for thing in hex_list:
        if (thing.print_coord()[0], thing.print_coord()[1]) == (new_mouse_pos[0], new_mouse_pos[1]):
            for open_cell in thing.open_neighbors:
                if open_cell.get_val() == 1:
                    thing.set_val(1)



    pygame.display.flip()
    clock.tick(50)