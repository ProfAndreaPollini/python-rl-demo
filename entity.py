from functools import partial
from typing import Any, List
import arcade
from abc import ABC


class Effect(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.actions: List[Any] = []

    def add_action(self, action):
        self.actions.append(action)


class PermanentEffect(Effect):
    pass


class EphemeralEffect(Effect):
    def __init__(self, turns: int) -> None:
        super().__init__()
        self.turns = turns


class Entity:  # entitá attive nel gioco
    def __init__(self, game, x=0, y=0) -> None:
        self.x = x
        self.y = y
        self.color = arcade.color.WHITE
        self.game = game
        self.effects: List[Effect] = []

    def add_effect(self, effect: Effect):
        self.effects.append(effect)

    @property
    def tile_size(self):
        return (16, 16)

    def draw(self):
        screen_x = (self.x + 0.5) * self.tile_size[0]
        screen_y = (self.y + 0.5) * self.tile_size[1]

        arcade.draw_rectangle_filled(
            screen_x,
            screen_y,
            self.tile_size[0],
            self.tile_size[1],
            self.color,
        )

    def apply_effects(self):
        effects = self.effects[:]

        for effect in self.effects:
            for action in effect.actions:
                action(entity=self)
            if isinstance(effect, EphemeralEffect):
                effect.turns -= 1
                if effect.turns < 0:
                    effects.remove(effect)
                    self.effects = effects


def change_color(entity, color):
    """[summary]

    TODO: Creare un function object che salvi la parte di stato che gli interessa e la ripristini quando léffetto svanisce

    Args:
        entity ([type]): [description]
        color ([type]): [description]
    """
    entity.color = color


class Potion(Entity):
    def __init__(self, game, x, y) -> None:
        super().__init__(game, x=x, y=y)
        self.color = arcade.color.BLACK

    def __call__(self, entity):
        effect = EphemeralEffect(5)  # Ogni pozione ha uno o piú effetti.
        # un effetto ha una azione
        effect.add_action(partial(change_color, color=arcade.color.BLUE))
        entity.add_effect(effect)
