"""

Sprite thanks:
https://opengameart.org/content/knight-sprite

"""

import threading 

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

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def record_clap(self):
        self.claps.append(True)
        
    def setup(self):
        # Set up your game here

        self.player_list = arcade.SpriteList()
        self.monster_list = arcade.SpriteList()

        # Score
        self.score = 0

        self.player_sprite = arcade.Sprite("knight.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 400  # Starting position
        self.player_sprite.center_y = 400
        self.player_list.append(self.player_sprite)

        self.rabbit_sprite = arcade.Sprite("knight.png", SPRITE_SCALING_PLAYER)
        self.rabbit_sprite.center_x = 50  # Starting position
        self.rabbit_sprite.center_y = 50
        self.monster_list.append(self.rabbit_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, arcade.SpriteList())

        self.claps = False
        def clap_listener():
            print('listener begun')
            feed = sc.MicrophoneFeed()
            detector = sc.AmplitudeDetector(feed, threshold=12000000)
            for clap in detector:
                print('clap!')
                # self.claps = True
    
        self.clap_listener = threading.Thread(target=clap_listener)
        self.clap_listener.start()
        

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.player_list.draw()
        self.monster_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """

        for monster in self.monster_list:

            monster.center_x += sign(self.player_sprite.center_x - monster.center_x)
            monster.center_y += sign(self.player_sprite.center_y - monster.center_y)

        monsters_hit = arcade.check_for_collision_with_list(self.player_sprite, self.monster_list)
        for monster in monsters_hit:
            arcade.set_background_color(arcade.color.RED)

        self.physics_engine.update()
        
        if self.claps:
            self.player_sprite.center_x += MOVEMENT_SPEED
            self.claps = False


    MOVEMENT_SPEED = 2

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = self.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -self.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -self.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = self.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0




def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()