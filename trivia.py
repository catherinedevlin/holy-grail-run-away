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

# Set the working directory (where we expect to find files) to the same
# directory this .py file is in. You can leave this out of your own
# code, but it is needed to easily run the examples using "python -m"
# as mentioned at the top of this program.
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

# Open the window. Set the window title and dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")

# Set the background color to white
# For a list of named colors see
# http://arcade.academy/arcade.color.html
# Colors can also be specified in (red, green, blue) format and
# (red, green, blue, alpha) format.
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
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()