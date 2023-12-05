import pygame
class Image_Button():
    def __init__(self,x,y,width,height,image_path,hover_image_path,sound_path = None):
        self.x=x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(width,height))
        self.hover_image = pygame.image.load(hover_image_path)
        self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.sound = None
        self.is_hovered = False
    def draw(self,screen):
        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image,self.rect.topleft)
    def check_hover(self,mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)
    def handle_event(self,event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()

