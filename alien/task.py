import sys
#import pygame which we just installed in pip
import pygame
#import from settings.py
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    
    #using settings from the settings.py file
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.
        screen_height))
    pygame.display.set_caption("Alien Invastion")

    ship = Ship(ai_settings, screen)
    
    #sets the background colour, set it as light green
    bg_color = (173, 250, 232)

    while True:
        #from game_functions.py
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)



run_game()

