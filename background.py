import arcade
arcade.set_background_color(arcade.color.LIGHT_GRAY)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()

def draw_valley():
    point_list = ((0, 400), (0, 0), (150, 0), (100, 400, ))
    arcade.draw_polygon_filled(point_list, arcade.color.GREEN)
    point_list = ((800, 400), (800, 0), (650, 0), (700, 400), )
    arcade.draw_polygon_filled(point_list, arcade.color.GREEN)

def draw_bridge():
    for x in range(115, 690, 22):
        arcade.draw_circle_filled(x, 390, 10, arcade.color.BROWN)

def draw_background():
    draw_valley()
    draw_bridge()

# arcade.draw_text("draw_circle_filled", 363, 207, arcade.color.BLACK, 10)
