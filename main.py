from game import Game
from map import Map
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Starting Template"


class GameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        map = Map(SCREEN_WIDTH, SCREEN_HEIGHT, 16)
        # self.player = Hero(map)
        self.game = Game(map)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        pass

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        self.game.on_key_pressed(key, modifiers)

    def on_draw(self):
        arcade.start_render()
        self.game.draw_map()
        self.game.draw_entities()
        self.draw_hero()

    def draw_hero(self):
        self.game.player.draw()
        self.game.player.apply_effects()


def main():
    """ Main method """
    game = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()