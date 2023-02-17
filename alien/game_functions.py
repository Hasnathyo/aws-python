import sys

import pygame

def check_events(ship):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                    #moves the ship to the right by one value
                #    ship.rect.centerx += 1
                
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                #    ship.rect.centerx -= 1
            
                elif event.type == pygame.KEYUP: 
                    if event.key == pygame.K_RIGHT:
                        ship.moving_right = False
                    
                    elif event.key == pygame.K_LEFT:
                        ship.moving_left = False
                    
                        
def update_screen(ai_settings, screen, ship):

        #fills the screen with the colour we set in settings.py
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        #makes the screen visible
        pygame.display.flip()

