import pygame
import sys
from settings import WIDTH, HEIGHT, FPS, TITLE
from states.menu import MenuState

class Game:
    def __init__(self):
        pygame.init() #initialises game
        pygame.mixer.init() # initialises audio
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        pygame.display.set_caption('Atlas Rising')
        self.clock = pygame.time.Clock()

        #data all states share
        self.lives = 3
        self.score = 0
        self.questions_asked = 0 
        self.correct_answers = 0

        self.state = MenuState(self) # <----- starting state.
    
    def run(self):
        while True:
            dt = self.clock.tick(FPS) / 1000 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                self.state.handle_event(event) 
            
            self.state.update(dt)