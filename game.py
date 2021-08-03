from entity import Entity, Potion
from typing import List
from map import Map
from hero import Hero


class Game:
    def __init__(self, game_map: Map) -> None:
        self.map = game_map
        self.player = Hero(self)
        self.entities: List[Entity] = []

        for i in range(30):
            self.map.tiles[i][i] = 0

        self.entities.append(Potion(self, 20, 10))

    def on_key_pressed(self, key, modifiers):
        self.player.on_user_input(key, modifiers)
        self.on_player_moved()

    def on_player_moved(self):
        entities = filter(
            lambda entity: entity.x == self.player.x
            and entity.y == self.player.y
            and callable(entity),
            self.entities,
        )
        for entity in entities:
            if callable(entity):
                entity(self.player)
                self.entities.remove(entity)

    def can_move_to(self, x, y):
        tile_id = self.map.tiles[y][x]
        if tile_id == -1:
            return True

        tile = self.map.game_objects[tile_id]
        return tile.walkable

    def draw_entities(self):
        for entity in self.entities:
            entity.draw()

    def draw_map(self):
        # arcade.draw_rectangle_filled(16, 16, 16, 16, arcade.color.AMARANTH)
        for y in range(len(self.map.tiles)):
            for x in range(len(self.map.tiles[0])):
                tile_id = self.map.tiles[y][x]
                if tile_id >= 0:
                    tile = self.map.game_objects[tile_id]
                    tile.draw(x, y, self.map.tile_size, self.map.tile_size)
