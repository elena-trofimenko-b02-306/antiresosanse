import pygame
import sys
import thorpy
import time
from button import Image_Button
from draw_and_move import drawer
from phys_modelling import *



screen_width = 800
screen_height = 600

pygame.init()



screen = pygame.display.set_mode((screen_width,screen_height))
FPS = 120
gruz_driven = Gruz_Driven()
gruz_free = Gruz_Free()
spring1 = Spring()
spring2 = Spring()
objects = [gruz_driven,gruz_free,spring1,spring2]
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)




def main_menu():


    start_button = Image_Button(screen_width / 2 - 252 / 2, 100, 252, 74, "start_button.jpg","hovered_start_button.jpg")
    quit_button = Image_Button(screen_width / 2 - 50, 250, 100, 100, "quit_button.png", "hovered_quit_button.png")

    buttons = [start_button, quit_button]
    running=True
    while running:
       screen.fill((255,255,255))
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               running = False
               pygame.quit()
               sys.exit()
           for button in buttons:
               button.handle_event(event)
           if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and start_button.is_hovered:
               settings_menu()
           if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and quit_button.is_hovered:
               running=False
               pygame.quit()
               sys.exit()
       for button in buttons:
           button.check_hover(pygame.mouse.get_pos())
           button.draw(screen)
       pygame.display.flip()
def settings_menu():
    start_modelling_button = Image_Button(screen_width / 2 - 252 / 2, 50, 252, 74, "button_start-modelling.png","hovered_button_start-modelling.png")
    back_button = Image_Button(screen_width / 2 - 150 / 2, 500, 150, 74, "button_back.png","hovered_button_back.png")
    buttons=[start_modelling_button,back_button]
    slider1 = thorpy.SliderX(100, (0.01, 1000), "Масса 1 груза")

    slider2 = thorpy.SliderX(100, (0.01, 1000), "Масса 2 груза")
    slider3 = thorpy.SliderX(100, (0.01, 1000), "Жесткость 1 прижины")
    slider4 = thorpy.SliderX(100, (0.01, 1000), "Жесткость 2 пружины")
    slider4 = thorpy.SliderX(100, (0.01, 1000), "Жесткость 2 пружины")
    slider5 = thorpy.SliderX(100, (0.01, 1000), "Циклическая частота вынуждающей силы")
    box=thorpy.Box(elements=[slider1,slider2,slider3,slider4,slider5])
    reaction1 = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                reac_func=slider_reaction1,
                                event_args={"id": thorpy.constants.EVENT_SLIDE},
                                params={},
                                reac_name="slider reaction")
    slider1.add_reaction(reaction1)
    reaction2 = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
                                reac_func=slider_reaction2,
                                event_args={"id": thorpy.constants.EVENT_SLIDE},
                                params={},
                                reac_name="slider reaction")
    slider2.add_reaction(reaction2)
    menu = thorpy.Menu(box)
    for element in menu.get_population():
        element.surface = screen
    box.set_topleft((200, 150))
    running = True
    while running:
        screen.fill((255, 255, 255))
        box.blit()
        box.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for button in buttons:
                button.handle_event(event)
            if  event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_button.is_hovered:
                main_menu()
            if  event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and start_modelling_button.is_hovered:
                process_modelling()
        for button in buttons:
            button.check_hover(pygame.mouse.get_pos())
            button.draw(screen)
        pygame.display.flip()
def process_modelling():
    time_zero = None
    last_time = None
    alive = True
    running = False
    screen.fill((255, 255, 255))
    perform_execution_button = Image_Button(screen_width / 2 - 150 / 2, 500, 150, 74, "button_back.png", "hovered_button_back.png")
    clock = pygame.time.Clock()
    while alive:
        screen.fill((255, 255, 255))
        perform_execution_button.check_hover(pygame.mouse.get_pos())
        perform_execution_button.draw(screen)




        for event in pygame.event.get():
              if event.type == pygame.QUIT:
                alive = False
                pygame.quit()
                sys.exit()
              if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and perform_execution_button.is_hovered:

                    alive = False
                    running = True
        pygame.display.flip()

    while running:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
              if event.type == pygame.QUIT:
                alive = False
                pygame.quit()
                sys.exit()
        if time_zero == None:
            time_zero = time.perf_counter()
        if last_time == None:
           last_time = time_zero
        cur_time = time.perf_counter()
        execution((cur_time - last_time)*2,(cur_time - time_zero)*2)
        if (cur_time-last_time)>=0.5:
            text = "V закрепленного груза = " + str(gruz_driven.v) + "     V свободного груза  = " + str(gruz_free.v)
            draw_text(screen, text, 18, screen_width / 2, 10)
        last_time = cur_time

        pygame.display.update()
        clock.tick(FPS)



def execution(dt,model_time):
    gruz_driven.calc_force_driven(model_time,gruz_free,spring1,spring2)
    gruz_free.calc_force_free(gruz_driven, spring2)
    gruz_driven.move(dt)
    gruz_free.move(dt)
    drawer(screen,gruz_driven,gruz_free,spring1,spring2)




def slider_reaction1(event):
    gruz_driven.m = slider_to_real(event.el.get_value())
def slider_reaction2(event):
    gruz_free.m = slider_to_real(event.el.get_value())
def slider_reaction3(event):
    spring1.k = slider_to_real(event.el.get_value())
    print(spring1.k)
def slider_reaction4(event):
    spring2.k = slider_to_real(event.el.get_value())
def slider_reaction5(event):
    gruz_driven.omega_ext = slider_to_real(event.el.get_value())

def slider_to_real(val):
    return val

main_menu()