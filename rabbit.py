"""

Sprite thanks:
https://opengameart.org/content/knight-sprite
https://opengameart.org/content/bunny-rabbit-lpc-style-for-pixelfarm
https://opengameart.org/content/blood-splats

"""

import multiprocessing

import arcade
import slowclap as sc

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING_PLAYER = 1.0


def sign(val):

    try:
        return val / abs(val)
    except ZeroDivisionError:
        return 0


def clap_listener(queue):
    feed = sc.MicrophoneFeed()
    detector = sc.AmplitudeDetector(feed, threshold=12000000)
    for clap in detector:
        print('clap!')


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        self.alive = True
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Set up your game here

        self.player_list = arcade.SpriteList()
        self.monster_list = arcade.SpriteList()

        # Score
        self.score = 0
        self.won = False

        self.player_sprite = arcade.Sprite("knight.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400  # Starting position
        self.player_sprite.center_y = 400
        self.player_list.append(self.player_sprite)

        self.rabbit_sprite = arcade.Sprite("bunny.png", SPRITE_SCALING_PLAYER)
        self.rabbit_sprite.center_x = 50  # Starting position
        self.rabbit_sprite.center_y = 50
        self.monster_list.append(self.rabbit_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, arcade.SpriteList())

        self.clap_queue = multiprocessing.Queue()
        self.clap_listener = multiprocessing.Process(
            target=clap_listener, args=(self.clap_queue, ))
        self.clap_listener.start()

    def on_draw(self):
        """ Render the screen. """

        if self.alive and not self.won:
            self.draw_game()
        else:
            self.draw_game_over()

    def draw_game(self):

        arcade.start_render()
        self.player_list.draw()
        self.monster_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """

        for monster in self.monster_list:

            monster.center_x += sign(self.player_sprite.center_x -
                                     monster.center_x)
            monster.center_y += sign(self.player_sprite.center_y -
                                     monster.center_y)

        caught = arcade.check_for_collision(self.player_sprite,
                                            self.rabbit_sprite)
        if caught:
            self.alive = False
            self.player_sprite.texture = arcade.load_texture(
                'bloodsplats_0004.png')
            self.player_list.draw()
            self.monster_list.draw()

        self.physics_engine.update()
        if self.player_sprite.center_x > SCREEN_WIDTH:
            self.won = True
            self.score += 100

        while not self.clap_queue.empty():
            self.clap_queue.get()
            self.player_sprite.center_x += MOVEMENT_SPEED

    MOVEMENT_SPEED = 2

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if (key == arcade.key.SPACE):
            self.alive = True
            self.won = False
            self.setup()

        if not self.alive:
            return

        if key == arcade.key.UP:
            self.player_sprite.change_y = self.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -self.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -self.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.score += 1
            self.player_sprite.change_x = self.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """

        output = "RUN AWAY!!!"
        arcade.draw_text(output, 200, 500, arcade.color.WHITE, 54)

        if self.won:
            output = "You have escaped!"
            arcade.draw_text(output, 80, 400, arcade.color.WHITE, 54)

        output = "<space> to start"
        arcade.draw_text(output, 250, 100, arcade.color.WHITE, 24)

        arcade.draw_text(str(self.score), 700, 50, arcade.color.WHITE, 24)


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
