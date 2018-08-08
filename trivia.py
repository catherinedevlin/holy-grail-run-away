import arcade
from background import draw_background

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

    def setup(self):
        # Set up your game here
        pass

    def on_draw(self):
        """ Render the screen. """

        arcade.set_background_color(arcade.color.LIGHT_GRAY)
        arcade.start_render()
        draw_background()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
