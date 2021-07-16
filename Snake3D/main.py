from ursina import *
from objects import *


class Game(Ursina):
    def __init__(self):
        super().__init__()
        window.color = color.black
        AmbientLight(color=(0.5, 0.5, 0.5, 1))
        DirectionalLight(color=(0.5, 0.5, 0.5, 1), direction=(1, 1, 1))
        self.Map_Size = 20
        self.new_game()
        camera.position = (self.Map_Size // 2, -20.5, -20)
        camera.rotation_x = -57

    def create_map(self, Map_Size):
        Entity(model='quad', scale=Map_Size, position=(Map_Size // 2, Map_Size // 2, 0), color=color.blue)
        Entity(model=Grid(Map_Size, Map_Size), scale=Map_Size,
               position=(Map_Size // 2, Map_Size // 2, -0.01), color=color.black)

    def new_game(self):
        scene.clear()
        # apple_texture = load_texture('appleTexture')
        self.create_map(self.Map_Size)
        self.apple = Apple(self.Map_Size, model='apple', color=color.red, rotation=(15, 90, 100),
                           position=(0, 10, 0), scale=0.15)
        self.snake = Snake(self.Map_Size)

    def input(self, key):
        if key == '2':
            camera.rotation_x = 0
            camera.position = (self.Map_Size // 2, self.Map_Size // 2, -50)
        elif key == '3':
            camera.position = (self.Map_Size // 2, -20.5, -20)
            camera.rotation_x = -57
        super().input(key)

    def check_apple_eaten(self):
        if self.snake.segment_positions[-1] == self.apple.position:
            self.snake.add_segment()
            self.apple.new_position()

    def check_game_over(self):
        snake = self.snake.segment_positions
        if 0 < snake[-1][0] < self.Map_Size and 0 < snake[-1][1] < self.Map_Size and len(snake) == len(set(snake)):
            return
        print_on_screen('GAME OVER', position=(-0.0092, 0), scale=0.12, duration=5)
        print_on_screen('New game will start in 5 seconds', position=(-0.0136, -0.007), scale=0.07, duration=5)
        self.snake.direction = Vec3(0, 0, 0)
        self.snake.permissions = dict.fromkeys(self.snake.permissions, 0)
        invoke(self.new_game, delay=5)

    def update(self):
        print_on_screen(f'Score: {self.snake.score}', position=(-0.024, 0.023), scale=0.1, duration=1 / 20)
        self.check_apple_eaten()
        self.check_game_over()
        self.snake.run()


if __name__ == '__main__':
    game = Game()
    update = game.update
    game.run()
