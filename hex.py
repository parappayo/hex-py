import sys, time, pygame
import game_state, game_input, game_draw


def game_loop(game):
    pygame.init()
    screen = pygame.display.set_mode(game.screen_size)

    while True:
        game_input.handle_events(pygame.event.get(), game)
        game_draw.draw_frame(screen, game)
        sys.stdout.flush()
        time.sleep(0.05) # cap at 20 fps


if __name__ == '__main__':
    game = game_state.GameState()
    game_loop(game)
