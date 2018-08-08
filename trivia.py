"""
Example "Arcade" library code.

This example shows the drawing primitives and how they are used.
It does not assume the programmer knows how to define functions or classes
yet.

API documentation for the draw commands can be found here:
http://arcade.academy/quick_index.html#id1

A video explaining this example can be found here:
https://vimeo.com/167158158

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.drawing_primitives
"""

# Import the Arcade library. If this fails, then try following the instructions
# for how to install arcade:
# http://arcade.academy/installation.html
import arcade
import os

class Knight(arcade.Sprite):

    def __init__(self, filename, scale, name):

        self.name = name
        return super().__init__(filename, scale)



class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(600, 600)

        self.game_over = False

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

    def draw_scenery(self):

        arcade.set_background_color(arcade.color.LIGHT_GRAY)

        # Start the render process. This must be done before any drawing commands.
        arcade.start_render()

        # Draw a filled in polygon
        point_list = ((0, 400), (0, 0), (150, 0), (100, 400), )
        arcade.draw_polygon_filled(point_list, arcade.color.GREEN)
        point_list = ((600, 400), (600, 0), (450, 0), (500, 400), )
        arcade.draw_polygon_filled(point_list, arcade.color.GREEN)

        # Draw a filled in circle
        # arcade.draw_text("draw_circle_filled", 363, 207, arcade.color.BLACK, 10)
        for x in range(115, 490, 22):
            arcade.draw_circle_filled(x, 390, 10, arcade.color.BROWN)

        # Finish the render.
        # Nothing will be drawn without this.
        # Must happen after all draw commands


    def start_new_game(self):

        self.draw_scenery()


def main():
    window = MyGame()
    window.start_new_game()
    arcade.run()

if __name__ == "__main__":
    main()

