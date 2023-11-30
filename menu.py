import pygame

screen_width = 800
screen_height = 600

def draw_start_menu():
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Антирезонанс', True, (255, 0, 255))
    start_button = font.render('Начать', True, (255, 255, 255))
    quit_button=font.render('Выйти', True, (255, 255, 255))
    screen.blit(title, (300, 0))
    screen.blit(start_button, (screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2))
    screen.blit(quit_button,(screen_width/2 - start_button.get_width()/2, screen_height/2 + start_button.get_height()/2+99))
    pygame.display.update()


game_state = "start_menu"

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
window = pygame.display.set_mode((screen_width, screen_height))

while True:

   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
           quit()

   if game_state == "start_menu":
       draw_start_menu()

   if game_state == "game":
       keys = pygame.key.get_pressed()

pygame.quit()
