import pygame
import game_functions as gf

from settings import Settings
from the_huff import Huff


def run_game():
    # Initialize game, settings, and create a screen object. 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))


    pygame.display.set_caption("Alien Invasion")

    image = Huff(screen)

    bg_color = (230, 230, 230)

    # Start the main loop for the game.
    while True:

        gf.check_events()
        gf.update_screen(ai_settings, screen, image)
run_game()