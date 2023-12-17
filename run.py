import pygame
from game_state_manager import GameStateManager
from main_menu import MainMenu
from menu_setting import UIMenuSetting
from game_setting import GameSetting
from game import Game
from game_interface import GameInterface

if __name__ == '__main__':
    pygame.init()
    setting = GameSetting()
    size = width, height = setting.get_display_size()
    game_state_manager = GameStateManager()

    main_menu = MainMenu(size)
    game = Game(size)
    game_interface = GameInterface(size)
    game_interface.connect(game)
    game_interface.button.on_click = lambda: game_state_manager.set_state('Main_menu')
    menu_setting = UIMenuSetting(setting, size)

    game_state_manager.add_state('Main_menu', main_menu)
    game_state_manager.add_state('Game', game_interface)
    game_state_manager.add_state('Menu_setting', menu_setting)

    main_menu.add_item('Играть',
                       lambda: game_state_manager.set_state('Game'))
    main_menu.add_item('Настройки',
                       lambda: game_state_manager.set_state('Menu_setting'))

    game_state_manager.set_state('Main_menu')

    screen = pygame.display.set_mode(size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                game_state_manager.handle_events(event)

        game_state_manager.update()
        game_state_manager.draw(screen)

        pygame.display.flip()

    setting.save('setting.txt')
    pygame.quit()
