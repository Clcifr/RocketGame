import pygame
from settings import WIDTH, HEIGHT, WHITE, BLACK, FONT_FILE
import settings

user_text = ''

class text_input:
    def __init__(self, game):
        self.game = game
        self.rect = self.rect
        self.text = ''
        self.active = False
        self.font = pygame.font.Font(settings.FONT_FILE, settings.FONT_SIZES["General"])
        self.colour_active:  (WHITE) 
        self.colour_inactive: (BLACK)  
    #initialise everything your state needs

def handle_event(self, events):
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text [:-1]
            elif event.key == pygame.K_RETURN:
                return self.text
            else:
                self.text += event.unicode
        return None
        

def update(self):
    self.colour = self.colour_active if self.active else self.colur_inactive
    self.surface = self.font.render(self.text, True, self.text_colour)
    

def draw(self,screen):
    pygame.draw.rect(screen, self.colour, self.rect, border_radius=4)
    pygame.draw.rect(screen, self.border_colour, self.rect, 2, border_radius=4)
    screen.blit(self.surface, (self.rect.x + 10, self.rect.y +10))
    
