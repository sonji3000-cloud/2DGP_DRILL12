from pico2d import *
from boy import Boy
from grass import Grass
from grass2 import Grass2

# Game object class here
import game_world   # 게임 월드 임포트

def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)



def reset_world():
    global world
    global boy

    boy = Boy()
    game_world.add_object(boy, 1)

    grass = Grass()
    game_world.add_object(grass, 0)  # 게임 월드에 객체를 담는 함수 호출

    grass2 = Grass2()
    game_world.add_object(grass2, 0)






def update_world():
    game_world.update()
    pass


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


running = True



open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
