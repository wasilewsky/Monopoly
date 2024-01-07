from monopoly import *

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = "1"
screen = pygame.display.set_mode(settings.SIZESCREEN)




def game(c):
    #system = System()
    #system.create_game(c)
    b = Board()


    # ============================================== nieskończona pętla gry
    window_open = True
    while window_open:
        screen.blit(image.BACKGROUND, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False

        b.draw(screen)
        #system.draw_game(False, True)

        # if system.rzut_button.click() and system.rzut_button_on:
        #     system.rzut_button_on = False
        #     system.dice.double_roll()
        #     system.message.add_message(f"gracz {system.players[0].name} poruszył się o {system.dice.show_turn_value()}")
        #     for x in range(0, system.dice.show_turn_value()):
        #         system.players[0].move(1)
        #         pygame.time.delay(200)
        #         system.draw_game(False, False)
        #     system.players[0].moving = False  # informacja ze jest na ostatnim polu
        #     # pygame.time.delay(1000)
        #
        # if system.dom_button.click():
        #     if system.dom_button.click() and not system.rzut_button_on:
        #         current_player = system.players[0]
        #         system.game_board.buy_house(current_player)
        #         pygame.time.delay(200)
        #
        # if system.kup_button.click():
        #     if system.kup_button.click() and not system.rzut_button_on:
        #         current_player = system.players[0]
        #         system.game_board.buy_field(current_player)
        #         pygame.time.delay(200)
        #
        # if system.dalej_button.click() and not system.rzut_button_on:
        #     system.kup_button.set_visible(False)
        #     system.dom_button.set_visible(False)
        #     system.dalej_button.set_visible(False)
        #
        #     system.rzut_button_on = True
        #     system.switch_player()

        pygame.display.flip()


def color():
    pygame.time.delay(100)
    window_open = True

    redBtn = Button(screen.get_width() / 2 - image.REDBTN.get_width() / 2, 180, image.REDBTN, True)
    blueBtn = Button(screen.get_width() / 2 - image.BLUEBTN.get_width() / 2, 330, image.BLUEBTN, True)
    greenBtn = Button(screen.get_width() / 2 - image.GREENBTN.get_width() / 2, 480, image.GREENBTN, True)
    purpleBtn = Button(screen.get_width() / 2 - image.PURPLEBTN.get_width() / 2, 630, image.PURPLEBTN, True)

    while window_open:
        screen.fill(image.LIGHTBLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False

        if redBtn.click():
            window_open = False
            if not game("red"):
                window_open = True

        if blueBtn.click():
            window_open = False
            if not game("blue"):
                window_open = True
        if greenBtn.click():
            window_open = False
            if not game("green"):
                window_open = True
        if purpleBtn.click():
            window_open = False
            if not game("purple"):
                window_open = True

        redBtn.draw(screen)
        blueBtn.draw(screen)
        greenBtn.draw(screen)
        purpleBtn.draw(screen)

        pygame.display.flip()


def main():
    window_open = True
    play_button = Button(screen.get_width() / 2 - image.PLAY_BUTTON.get_width() / 2, 230, image.PLAY_BUTTON, True)
    exit_button = Button(screen.get_width() / 2 - image.PLAY_BUTTON.get_width() / 2, 480, image.EXIT_BUTTON, True)

    while window_open:
        screen.fill(image.LIGHTBLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False

        if play_button.click():
            window_open = False
            if not color():
                window_open = True

        if exit_button.click():
            window_open = False

        play_button.draw(screen)
        exit_button.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()

pygame.quit()
