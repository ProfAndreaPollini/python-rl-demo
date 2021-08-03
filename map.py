from typing import List, Optional

import arcade


class Tile:
    def __init__(self) -> None:
        self.walkable = True

    def draw(self, x, y, size_x, size_y):
        pass


class Wall(Tile):
    def __init__(self) -> None:
        super().__init__()
        self.walkable = False
        self.color = arcade.color.AVOCADO

    def draw(self, x, y, size_x, size_y):
        screen_x = (x + 0.5) * size_x
        screen_y = (y + 0.5) * size_y

        arcade.draw_rectangle_filled(
            screen_x,
            screen_y,
            size_x,
            size_y,
            self.color,
        )


class MapManager:
    def __init__(self) -> None:
        self.map: Optional[Map] = None


class Map:
    def __init__(self, screen_height, screen_width, tile_size=16) -> None:
        self.rows = screen_height // tile_size
        self.cols = screen_width // tile_size
        self.tile_size = tile_size

        self.tiles: List[List[int]] = [
            [-1 for x in range(self.cols)] for y in range(self.rows)
        ]
        self.game_objects: List[Tile] = [
            Wall(),
        ]
