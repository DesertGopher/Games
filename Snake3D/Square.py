from ursina import *


app = Ursina()
window.color = color.black


AmbientLight(type='ambient', color=(0.5, 0.5, 0.5, 1))
DirectionalLight(type='directional', color=(0.5, 0.5, 0.5, 1), direction=(1, 1, 1), position=(0, 100, 0))
cube = Entity(model='cube', rotation=(15, 0, 0), position=(0, 0, 0), scale=4, color=color.green)

def update():
    cube.rotation_y += time.dt * 150
    cube.x += held_keys['d'] + time.dt / 2
    cube.x -= held_keys['a'] + time.dt / 2

app.run()