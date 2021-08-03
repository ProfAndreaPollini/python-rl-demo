import arcade
from entity import Entity


class Hero(Entity):
    def __init__(self, game, x=5, y=5) -> None:
        super().__init__(game=game, x=x, y=y)
        self.color = arcade.color.RED

    def up(self):
        if self.game.can_move_to(self.x, self.y + 1):
            self.y += 1

    def down(self):
        if self.game.can_move_to(self.x, self.y - 1):
            self.y -= 1

    def left(self):
        if self.game.can_move_to(self.x - 1, self.y):
            self.x -= 1

    def right(self):
        if self.game.can_move_to(self.x + 1, self.y):
            self.x += 1

    def on_user_input(self, key, modifiers):
        if key == arcade.key.UP:
            self.up()
        elif key == arcade.key.DOWN:
            self.down()
        elif key == arcade.key.LEFT:
            self.left()
        elif key == arcade.key.RIGHT:
            self.right()
