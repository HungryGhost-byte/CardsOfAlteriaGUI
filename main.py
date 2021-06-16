import pickle
import time
import random
import pygame
import sys
from pygame.locals import *


clock = pygame.time.Clock()

pygame.init()
pygame.mixer.init()
# Title and Icon
pygame.display.set_caption("Cards of Alteria")
icon = pygame.image.load('images/adventure/icon.jpg')
pygame.display.set_icon(icon)

# Screen size
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

base_font = pygame.font.Font(None, 32)
name = ''

input_rect = pygame.Rect(600, 550, 140, 32)
colour = pygame.Color(255, 239, 239)

cardsound1 = pygame.mixer.Sound('Sound/cardsound1.ogg')
turn_page = pygame.mixer.Sound('Sound/turnpage.mp3')

####################


def fade():
    fade = pygame.Surface((1600, 900))
    fade.fill((0, 0, 0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        redrawWindow()
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(2)


def redrawWindow():
    screen.fill((255, 255, 255))


def pause():
    paused = True

    pygame.draw.rect(screen, [255, 229, 204], (580, 330, 430, 150), 0)
    pygame.draw.rect(screen, [0, 0, 0], (580, 330, 430, 150), 2)

    test1 = base_font.render(
        "Paused", True, (0, 0, 0))
    test2 = base_font.render(
        "Press C to continue or Q to quit", True, (0, 0, 0))

    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    select_sound.play()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()

        screen.blit(test1, (WIDTH/2 - 40, 370))
        screen.blit(test2, (WIDTH/2 - 170, 410))
        pygame.display.update()
        clock.tick(5)


def show_card_album1():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card1_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album2():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card2_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album3():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card3_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album4():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card4_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album5():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card5_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album6():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card6_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album7():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card7_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album8():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card8_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album9():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card9_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album10():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card10_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album11():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card11_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album12():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card12_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)

#######


def show_card_album13():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card13_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album14():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card14_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album15():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card15_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album16():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card16_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album17():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card17_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album18():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card18_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album19():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card19_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album20():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card20_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album21():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card21_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album22():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card22_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album23():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card23_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album24():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card24_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album25():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card25_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album26():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card26_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album27():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card27_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album28():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card28_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album29():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card29_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album30():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card30_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album31():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card31_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album32():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card32_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album33():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card33_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album34():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card34_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album35():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card35_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album36():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card36_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album37():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card37_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album38():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card38_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album39():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card39_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album40():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card40_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album41():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card41_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album42():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card42_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album43():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card43_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album44():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card44_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album45():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card45_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album46():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card46_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album47():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card47_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album48():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card48_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album49():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card49_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


def show_card_album50():
    paused = True
    cardsound1.play()
    while paused:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    paused = False
        screen.blit(collection_screen, (0, 0))
        screen.blit(card50_image, (WIDTH/2 - 230, 100))
        pygame.display.update()
        clock.tick(5)


######################################################################################################
save_sound = pygame.mixer.Sound('Sound/savefile.ogg')
load_sound = pygame.mixer.Sound('Sound/loadfile.ogg')

login_sound = pygame.mixer.Sound('Sound/startadventure.mp3')

saveimage1 = pygame.image.load('images/s1.png')
saveimage2 = pygame.image.load('images/s2.png')
saveimage3 = pygame.image.load('images/s3.png')
saveimage4 = pygame.image.load('images/s4.png')
saveimage5 = pygame.image.load('images/s5.png')

loadimage1 = pygame.image.load('images/l1.png')

dupemoney1 = pygame.image.load('images/dupemoney1.png')
dupemoney2 = pygame.image.load('images/dupemoney2.png')
dupemoney3 = pygame.image.load('images/dupemoney3.png')
dupemoney4 = pygame.image.load('images/dupemoney4.png')


adventurehov = pygame.image.load('images/hovadven.png')
collectionhov = pygame.image.load('images/hovcollection.png')
shophov = pygame.image.load('images/hovshop.png')


def save():
    global collection, gold, name, cards_got
    # screen.blit(saveimage1, (0, 0))
    # screen.blit(saveimage2, (0, 0))
    # screen.blit(saveimage3, (0, 0))
    # screen.blit(saveimage4, (0, 0))
    pickle.dump(collection, open("savefile1.txt", "wb"))
    pickle.dump(gold, open("savefile2.txt", "wb"))
    pickle.dump(name, open("savefile3.txt", "wb"))
    pickle.dump(cards_got, open("savefile4.txt", "wb"))
    # screen.blit(saveimage5, (0, 0))
    save_sound.play()
    pygame.display.update()


def load():
    global collection, gold, name, cards_got
    collection = pickle.load(open("savefile1.txt", "rb"))
    gold = pickle.load(open("savefile2.txt", "rb"))
    name = pickle.load(open("savefile3.txt", "rb"))
    cards_got = pickle.load(open("savefile4.txt", "rb"))
    load_sound.play()
    # screen.blit(loadimage1, (0, 0))
    pygame.display.update()


def topcount():
    global gold, name, cards_got
    gold_count = base_font.render(
        "Gold: " + (str(gold)), True, (255, 255, 255))
    screen.blit(gold_count, (10, 10))
    card_counter = base_font.render("Cards: " + (str(cards_got)) +
                                    "/50", True, (255, 255, 255))
    screen.blit(card_counter, (150, 10))
    name_show = base_font.render("Player: " + name, True, (255, 255, 255))
    screen.blit(name_show, (320, 10))
# Various Sounds
# cardsound_unlock = pygame.mixer.music.load('Sound/cardunlock.wav')


select_sound = pygame.mixer.Sound('Sound/select.ogg')
name_error = pygame.mixer.Sound('Sound/nameerror.ogg')

escbutton = pygame.image.load('images/esc.png')
escbutton2 = pygame.image.load('images/esc2.png')
topbar = pygame.image.load('images/goldcardbar.png')

albumpage1 = pygame.image.load('images/one.png')
albumpage2 = pygame.image.load('images/two.png')
albumpage3 = pygame.image.load('images/three.png')
albumpage4 = pygame.image.load('images/four.png')
albumpage5 = pygame.image.load('images/five.png')

# Card Images
card1_image = pygame.image.load('images/cards/card1.png')
card2_image = pygame.image.load('images/cards/card2.png')
card3_image = pygame.image.load('images/cards/card3.png')
card4_image = pygame.image.load('images/cards/card4.png')
card5_image = pygame.image.load('images/cards/card5.png')
card6_image = pygame.image.load('images/cards/card6.png')
card7_image = pygame.image.load('images/cards/card7.png')
card8_image = pygame.image.load('images/cards/card8.png')
card9_image = pygame.image.load('images/cards/card9.png')
card10_image = pygame.image.load('images/cards/card10.png')
card11_image = pygame.image.load('images/cards/card11.png')
card12_image = pygame.image.load('images/cards/card12.png')
card13_image = pygame.image.load('images/cards/card13.png')
card14_image = pygame.image.load('images/cards/card14.png')
card15_image = pygame.image.load('images/cards/card15.png')
card16_image = pygame.image.load('images/cards/card16.png')
card17_image = pygame.image.load('images/cards/card17.png')
card18_image = pygame.image.load('images/cards/card18.png')
card19_image = pygame.image.load('images/cards/card19.png')
card20_image = pygame.image.load('images/cards/card20.png')
card21_image = pygame.image.load('images/cards/card21.png')
card22_image = pygame.image.load('images/cards/card22.png')
card23_image = pygame.image.load('images/cards/card23.png')
card24_image = pygame.image.load('images/cards/card24.png')
card25_image = pygame.image.load('images/cards/card25.png')
card26_image = pygame.image.load('images/cards/card26.png')
card27_image = pygame.image.load('images/cards/card27.png')
card28_image = pygame.image.load('images/cards/card28.png')
card29_image = pygame.image.load('images/cards/card29.png')
card30_image = pygame.image.load('images/cards/card30.png')
card31_image = pygame.image.load('images/cards/card31.png')
card32_image = pygame.image.load('images/cards/card32.png')
card33_image = pygame.image.load('images/cards/card33.png')
card34_image = pygame.image.load('images/cards/card34.png')
card35_image = pygame.image.load('images/cards/card35.png')
card36_image = pygame.image.load('images/cards/card36.png')
card37_image = pygame.image.load('images/cards/card37.png')
card38_image = pygame.image.load('images/cards/card38.png')
card39_image = pygame.image.load('images/cards/card39.png')
card40_image = pygame.image.load('images/cards/card40.png')
card41_image = pygame.image.load('images/cards/card41.png')
card42_image = pygame.image.load('images/cards/card42.png')
card43_image = pygame.image.load('images/cards/card43.png')
card44_image = pygame.image.load('images/cards/card44.png')
card45_image = pygame.image.load('images/cards/card45.png')
card46_image = pygame.image.load('images/cards/card46.png')
card47_image = pygame.image.load('images/cards/card47.png')
card48_image = pygame.image.load('images/cards/card48.png')
card49_image = pygame.image.load('images/cards/card49.png')
card50_image = pygame.image.load('images/cards/card50.png')
card51_image = pygame.image.load('images/cards/card51.png')


# for shop, background image when card is showing
shopcard_look = pygame.image.load('images/whenlooking.png')


# Card worth in Gold
# Common = 1
# Uncommon = 2
# Rare = 4
# Mythic = 10


gold = 0
# to show current gold value
# print(" - " + name + "'s Total Gold: " + str(gold), "-")

cards_got = 0

errorsound = pygame.mixer.Sound('Sound/errorsound.ogg')
cardsound_unlock = pygame.mixer.Sound('Sound/cardunlock.wav')
cardsound_dupe = pygame.mixer.Sound('Sound/goldspent.wav')

dupetext = base_font.render("Duplicate Card!", True, (0, 102, 204))
dupetext_common = base_font.render("Earned 1 gold!", True, (0, 102, 204))
dupetext_uncommon = base_font.render("Earned 2 gold!", True, (0, 102, 204))
dupetext_rare = base_font.render("Earned 4 gold!", True, (0, 102, 204))
dupetext_mythic = base_font.render("Earned 10 gold!", True, (0, 102, 204))


class Card:
    def __init__(self, name, number, rarity, text, image):
        self.name = name
        self.number = number
        self.rarity = rarity
        self.text = text
        self.image = image

    def acquired(self):
        cardsound_unlock.play()
        screen.blit(shopcard_look, (0, 0))
        screen.blit(self.image, (550, 70))
        print(" You have acquired: " + self.name)
        print(" This is a " + self.rarity, "card!")
        pygame.display.update()
        # time.sleep(0.5) < -- culprit for slowing down card aquisition in shop

    def dupe(self):
        global gold
        cardsound_dupe.play()
        screen.blit(shopcard_look, (0, 0))
        screen.blit(self.image, (550, 70))
        print(" You have acquired: " + self.name)
        print(" This is a duplicate card!")
        if self.rarity == "Mythic":
            screen.blit(dupemoney4, (0, 280))
            pygame.display.update()
            gold += 10
            pygame.time.delay(1000)

        elif self.rarity == "Rare":
            screen.blit(dupemoney3, (0, 280))
            print(" You have acquired 4 gold for " + self.name + " card.")
            pygame.display.update()
            gold += 4
            pygame.time.delay(1000)

        elif self.rarity == "Uncommon":
            screen.blit(dupemoney2, (0, 280))
            print(" You have acquired 2 gold for " + self.name + " card.")
            pygame.display.update()
            gold += 2
            pygame.time.delay(1000)

        else:
            screen.blit(dupemoney1, (0, 280))
            # print(" You have acquired 1 gold for " + self.name + " card.")
            pygame.display.update()
            gold += 1
            pygame.time.delay(1000)


# card_unlock checks the out come of random.choice(which pulls from collection dict)
# it first checks if the card == True in dict, to catch any duplicate
# if no dupes, it continues to acquired function
def card_unlock(result):
    global cards_got
    if result == c1:
        check_card = collection["c1"]
        if check_card == True:
            c1.dupe()
        else:
            collection["c1"] = True
            cards_got += 1
            c1.acquired()
    elif result == c2:
        check_card = collection["c2"]
        if check_card == True:
            c2.dupe()
        else:
            collection["c2"] = True
            cards_got += 1
            c2.acquired()
    elif result == c3:
        check_card = collection["c3"]
        if check_card == True:
            c3.dupe()
        else:
            collection["c3"] = True
            cards_got += 1
            c3.acquired()
    elif result == c4:
        check_card = collection["c4"]
        if check_card == True:
            c4.dupe()
        else:
            collection["c4"] = True
            cards_got += 1
            c4.acquired()
    elif result == c5:
        check_card = collection["c5"]
        if check_card == True:
            c5.dupe()
        else:
            collection["c5"] = True
            cards_got += 1
            c5.acquired()
    elif result == c6:
        check_card = collection["c6"]
        if check_card == True:
            c6.dupe()
        else:
            collection["c6"] = True
            cards_got += 1
            c6.acquired()
    elif result == c7:
        check_card = collection["c7"]
        if check_card == True:
            c7.dupe()
        else:
            collection["c7"] = True
            cards_got += 1
            c7.acquired()
    elif result == c8:
        check_card = collection["c8"]
        if check_card == True:
            c8.dupe()
        else:
            collection["c8"] = True
            cards_got += 1
            c8.acquired()
    elif result == c9:
        check_card = collection["c9"]
        if check_card == True:
            c9.dupe()
        else:
            collection["c9"] = True
            cards_got += 1
            c9.acquired()
    elif result == c10:
        check_card = collection["c10"]
        if check_card == True:
            c10.dupe()
        else:
            collection["c10"] = True
            cards_got += 1
            c10.acquired()
    elif result == c11:
        check_card = collection["c11"]
        if check_card == True:
            c11.dupe()
        else:
            collection["c11"] = True
            cards_got += 1
            c11.acquired()
    elif result == c12:
        check_card = collection["c12"]
        if check_card == True:
            c12.dupe()
        else:
            collection["c12"] = True
            cards_got += 1
            c12.acquired()
    elif result == c13:
        check_card = collection["c13"]
        if check_card == True:
            c13.dupe()
        else:
            collection["c13"] = True
            cards_got += 1
            c13.acquired()
    elif result == c14:
        check_card = collection["c14"]
        if check_card == True:
            c14.dupe()
        else:
            collection["c14"] = True
            cards_got += 1
            c14.acquired()
    elif result == c15:
        check_card = collection["c15"]
        if check_card == True:
            c15.dupe()
        else:
            collection["c15"] = True
            cards_got += 1
            c15.acquired()
    elif result == c16:
        check_card = collection["c16"]
        if check_card == True:
            c16.dupe()
        else:
            collection["c16"] = True
            cards_got += 1
            c16.acquired()
    elif result == c17:
        check_card = collection["c17"]
        if check_card == True:
            c17.dupe()
        else:
            collection["c17"] = True
            cards_got += 1
            c17.acquired()
    elif result == c18:
        check_card = collection["c18"]
        if check_card == True:
            c18.dupe()
        else:
            collection["c18"] = True
            cards_got += 1
            c18.acquired()
    elif result == c19:
        check_card = collection["c19"]
        if check_card == True:
            c19.dupe()
        else:
            collection["c19"] = True
            cards_got += 1
            c19.acquired()
    elif result == c20:
        check_card = collection["c20"]
        if check_card == True:
            c20.dupe()
        else:
            collection["c20"] = True
            cards_got += 1
            c20.acquired()
    elif result == c21:
        check_card = collection["c21"]
        if check_card == True:
            c21.dupe()
        else:
            collection["c21"] = True
            cards_got += 1
            c21.acquired()
    elif result == c22:
        check_card = collection["c22"]
        if check_card == True:
            c22.dupe()
        else:
            collection["c22"] = True
            cards_got += 1
            c22.acquired()
    elif result == c23:
        check_card = collection["c23"]
        if check_card == True:
            c23.dupe()
        else:
            collection["c23"] = True
            cards_got += 1
            c23.acquired()
    elif result == c24:
        check_card = collection["c24"]
        if check_card == True:
            c24.dupe()
        else:
            collection["c24"] = True
            cards_got += 1
            c24.acquired()
    elif result == c25:
        check_card = collection["c25"]
        if check_card == True:
            c25.dupe()
        else:
            collection["c25"] = True
            cards_got += 1
            c25.acquired()
    elif result == c26:
        check_card = collection["c26"]
        if check_card == True:
            c26.dupe()
        else:
            collection["c26"] = True
            cards_got += 1
            c26.acquired()
    elif result == c27:
        check_card = collection["c27"]
        if check_card == True:
            c27.dupe()
        else:
            collection["c27"] = True
            cards_got += 1
            c27.acquired()
    elif result == c28:
        check_card = collection["c28"]
        if check_card == True:
            c28.dupe()
        else:
            collection["c28"] = True
            cards_got += 1
            c28.acquired()
    elif result == c29:
        check_card = collection["c29"]
        if check_card == True:
            c29.dupe()
        else:
            collection["c29"] = True
            cards_got += 1
            c29.acquired()
    elif result == c30:
        check_card = collection["c30"]
        if check_card == True:
            c30.dupe()
        else:
            collection["c30"] = True
            cards_got += 1
            c30.acquired()
    elif result == c31:
        check_card = collection["c31"]
        if check_card == True:
            c31.dupe()
        else:
            collection["c31"] = True
            cards_got += 1
            c31.acquired()
    elif result == c32:
        check_card = collection["c32"]
        if check_card == True:
            c32.dupe()
        else:
            collection["c32"] = True
            cards_got += 1
            c32.acquired()
    elif result == c33:
        check_card = collection["c33"]
        if check_card == True:
            c33.dupe()
        else:
            collection["c33"] = True
            cards_got += 1
            c33.acquired()
    elif result == c34:
        check_card = collection["c34"]
        if check_card == True:
            c34.dupe()
        else:
            collection["c34"] = True
            cards_got += 1
            c34.acquired()
    elif result == c35:
        check_card = collection["c35"]
        if check_card == True:
            c35.dupe()
        else:
            collection["c35"] = True
            cards_got += 1
            c35.acquired()
    elif result == c36:
        check_card = collection["c36"]
        if check_card == True:
            c36.dupe()
        else:
            collection["c36"] = True
            cards_got += 1
            c36.acquired()
    elif result == c37:
        check_card = collection["c37"]
        if check_card == True:
            c37.dupe()
        else:
            collection["c37"] = True
            cards_got += 1
            c37.acquired()
    elif result == c38:
        check_card = collection["c38"]
        if check_card == True:
            c38.dupe()
        else:
            collection["c38"] = True
            cards_got += 1
            c38.acquired()
    elif result == c39:
        check_card = collection["c39"]
        if check_card == True:
            c39.dupe()
        else:
            collection["c39"] = True
            cards_got += 1
            c39.acquired()
    elif result == c40:
        check_card = collection["c40"]
        if check_card == True:
            c40.dupe()
        else:
            collection["c40"] = True
            cards_got += 1
            c40.acquired()
    elif result == c41:
        check_card = collection["c41"]
        if check_card == True:
            c41.dupe()
        else:
            collection["c41"] = True
            cards_got += 1
            c41.acquired()
    elif result == c42:
        check_card = collection["c42"]
        if check_card == True:
            c42.dupe()
        else:
            collection["c42"] = True
            cards_got += 1
            c42.acquired()
    elif result == c43:
        check_card = collection["c43"]
        if check_card == True:
            c43.dupe()
        else:
            collection["c43"] = True
            cards_got += 1
            c43.acquired()
    elif result == c44:
        check_card = collection["c44"]
        if check_card == True:
            c44.dupe()
        else:
            collection["c44"] = True
            cards_got += 1
            c44.acquired()
    elif result == c45:
        check_card = collection["c45"]
        if check_card == True:
            c45.dupe()
        else:
            collection["c45"] = True
            cards_got += 1
            c45.acquired()
    elif result == c46:
        check_card = collection["c46"]
        if check_card == True:
            c46.dupe()
        else:
            collection["c46"] = True
            cards_got += 1
            c46.acquired()
    elif result == c47:
        check_card = collection["c47"]
        if check_card == True:
            c47.dupe()
        else:
            collection["c47"] = True
            cards_got += 1
            c47.acquired()
    elif result == c48:
        check_card = collection["c48"]
        if check_card == True:
            c48.dupe()
        else:
            collection["c48"] = True
            cards_got += 1
            c48.acquired()
    elif result == c49:
        check_card = collection["c49"]
        if check_card == True:
            c49.dupe()
        else:
            collection["c49"] = True
            cards_got += 1
            c49.acquired()
    elif result == c50:
        check_card = collection["c50"]
        if check_card == True:
            c50.dupe()
        else:
            collection["c50"] = True
            cards_got += 1
            c50.acquired()
    else:
        return None


################ S E A S O N   1   C A R D S ##################


c1 = Card("Skeletal Knight", "1", "Common", "When the Aldrus Empire fell, its vast army was affected \n"
          " by a terrible curse. They were forced to wonder the lands\n "
          " aimlessly, even in death.", card1_image)
c2 = Card("Mountain Fairy", "2", "Common", "In the western mountains of the Edeera Region, these fairies\n"
          " call home. Unlike other fairies, they are accustomed to \n"
          " humans. It isn't out of place for them to find them in the local\n"
                                           " towns and cities.", card2_image)
c3 = Card("Dwarven Storyteller", "3", "Common", "If there is one thing Dwarves are known for besides Smithing,\n"
                                                " it's a good tale. Many have made a profession of traveling\n"
                                                " far and wide, telling tales of wonders and mystery's.", card3_image)
c4 = Card("Honest Rogue", "4", "Uncommon", "A Rogue by profession isn't known to be honest, but you always\n"
                                           " get that one...", card4_image)
c5 = Card("Valia Knight", "5", "Uncommon", "A Knight of the Valia Kingdom, north of Dragon Valley. From the age\n"
                                           " of ten, they enter into a life of servitude to their country, and\n"
                                           " undergo the most rigorous of training", card5_image)
c6 = Card("Forest Dragon", "6", "Rare", "Dragons are not a rare sight, many of which make their homes deep\n"
                                        " within forests.", card6_image)
c7 = Card("Wandering Ghost", "7", "Common", "Ghosts that wonder the world usually do so for good reason. It\n"
                                            " is not natural that they do not pass on in death.", card7_image)
c8 = Card("Whispering Tree Branch", "8", "Common", "There are tales of certain trees in the forests, that\n"
                                                   " when listened to, speak of the secrets carried to them\n"
                                                   " on the wind.", card8_image)
c9 = Card("Nomadic Merchant", "9", "Common", "Merchants hail from every corner of the land and are vital\n"
                                             " for economies.", card9_image)
c10 = Card("Sand Giant", "10", "Uncommon", "These beings are found within the deserts of Ashuu, casting \n"
                                           " shade across wide areas from their humongous size. Although \n"
                                           " they are a sight to behold, going near one is certain death.",
                                           card10_image)
c11 = Card("Woodland Prowler", "11", "Uncommon", "Wild cat-like creatures the size of an adult human - they\n"
                                                 " have an aggressive nature and move only during the night.",
                                                 card11_image)
c12 = Card("Isazahl, The Slumbering Wizard", "12", "Common", "A great wizard, but a lazy one. His magic was\n"
                                                             " so powerful that he created countless copies\n"
                                                             " of himself to work on his projects while he\n"
                                                             " took extended naps.", card12_image)
c13 = Card("Lost City of The Sunken Sands", "13", "Rare", "It is still a matter of firey debate whether the\n"
                                                          " mythical Lost City actually exists or is simply\n"
                                                          " the product of good storytelling. Some have claimed\n"
                                                          " to have seen it with their own eyes.", card13_image)
c14 = Card("Tardy Blacksmith", "14", "Common", "It's not always the case where someones name reflects their \n"
                                               " habits, but here we are.", card14_image)
c15 = Card("Babbling Brook", "15", "Common", "They say that people are buried alive near streams, so their \n"
                                             " wailing sounds like its coming from the waters. Don't ask \n"
                                             " who \"they\" are.", card15_image)
c16 = Card("Witch's Cauldron", "16", "Common", "It's what a witch usually uses to craft her potions and \n"
                                               " perfect her spells.", card16_image)
c17 = Card("Forbidden Wizard's Parchment", "17",
           "Uncommon", "Sounds cool, doesn't it.", card17_image)
c18 = Card("King Ugg the Ape", "18", "Uncommon", "A mighty gorilla that rules the jungles in southern \n"
                                                 " Bananaram.", card18_image)
c19 = Card("Scriptures of The Five Moons", "19", "Rare", "Each moon is said to be symbolic of the five \n"
                                                         " wizards that hailed from Stonebrook Castle \n"
                                                         " University.", card19_image)
c20 = Card("Vampirate", "20", "Common", "Whenever the undead is concerned, you can be sure a curse \n"
           " is not far behind. These", card20_image)
c21 = Card("Grim Reaper the Sleeper", "21", "Common", "Don't let the rhymes fool you, when the Reaper wakes, \n"
                                                      " things get a bit morbid.", card21_image)
c22 = Card("Compass of the Misty North", "22", "Common", "This magical compass is said to point towards the \n"
                                                         " lost treasure of Peg-leg Percy Plop. He was a poor \n"
                                                         " pirate, in wealth and taste.", card22_image)
c23 = Card("Queen Kit the Cat", "23", "Uncommon", "Home of the sewer strays of Dimdim City, she is able \n"
                                                  " to speak the common tongue and translate between humans \n"
                                                  " and regular cats.", card23_image)
c24 = Card("Raging Bear-owl", "24", "Uncommon", "It's still not known whether this abomination was created or \n"
                                                " occurred naturally. Don't let the innocent owl-like face \n"
                                                " deceive you, it is a vicious thing.", card24_image)
c25 = Card("Sword of the Sultan", "25", "Common",
           "There are many sultans, thus there are many swords.", card25_image,)
c26 = Card("The Ghost Ship - Grim Patron", "26", "Mythic", "This ship of death is large in size and majesty. \n"
                                                           " Appearing on foggy nights deep at sea, this \n"
                                                           " vessel is said to carry on it the riches of all \n"
                                                           " past empires. There is also an item on this ship \n"
                                                           " that is said to give a wish to any who touch it.",
                                                           card26_image)
c27 = Card("Cackling Ravens", "27", "Common", "Dark as the night, they wait among the wounded before it's safe \n"
                                              " to eat. For those poor unfortunate souls, the cackling of the \n"
                                              " ravens is the last thing they will ever hear.", card27_image)
c28 = Card("Graveyard Redcap", "28", "Common", "These Redcaps are grave-robbing goblins that travel in packs. \n"
                                               " Should you stumble across one, run. They will not hesitate \n"
                                               " to kill and loot your corpse.", card28_image)
c29 = Card("Bridge Troll", "29", "Uncommon", "While not a common sight, bridge trolls are becoming more \n"
                                             " numerous in number as threatening travelers for their gold \n"
                                             " is easy income.", card29_image)
c30 = Card("The Kings Chessboard", "30", "Uncommon", "Chess - a popular game among royalty. In some lands, \n"
                                                     " wars are not fought on the battle-field, but on the \n"
                                                     " board.", card30_image)
c31 = Card("Crocodile River", "31", "Uncommon", "Those guilty of crimes are dropped into this \n"
                                                " crocodile infested river. the crocodiles themselves \n"
                                                " are plump from the enemies of the Zumaama Kingdom.", card31_image)
c32 = Card("Sand Pirate marauder", "32", "Uncommon", "The sands are as vast as the oceans in Alteria. \n"
                                                     " Magical ships sail the sands, but it is the  \n"
                                                     " marauders that will be found far from borders of \n"
                                                     " kingdoms that pay for their heads.", card32_image)
c33 = Card("Gold-fin, the Pirate King", "33", "Rare", "This Shark-man hybrid has made a fearsome \n"
                                                      " reputation of himself. He was rich before \n"
                                                      " pirating - he just does it for the pleasure.", card33_image)
c34 = Card("Magic Mirror", "34", "Common",
           "The mirror shows the reflection you want to see.", card34_image)
c35 = Card("Stairs to the Underworld", "35", "Common", "Cold and grey, only the most unfortunate find \n"
                                                       " themselves here.", card35_image)
c36 = Card("Bell of the Misty Mire", "36", "Common", "The bell that never stops ringing. If you are close \n"
                                                     " enough to hear it, you are already too deep in the \n"
                                                     " swamp to find a way out.", card36_image)
c37 = Card("Secret Note", "37", "Uncommon", "The writing is written in code, but at the bottom it is \n"
                                            " is signed \"Ms. Mowz\".", card37_image)
c38 = Card("Sorceress Mervania", "38", "Uncommon", "A powerful spell-caster, her age is unknown, but she \n"
                                                   " has been referenced in tomes tha tare over a thousand \n"
                                                   " years old. Her castle reaches out high above the forest \n"
                                                   " it sits in.", card38_image)
c39 = Card("Ring of Titrel", "39", "Uncommon", "Wanted by many, this ring controls a mysterious cauldron \n"
                                               " that is said to play a part in brining forth the end of the \n"
                                               " world.", card39_image)
c40 = Card("Djinn", "40", "Common", "Mischievous spirits that cannot be seen with the naked eye. \n"
                                    " Your socks going missing again could be explained.", card40_image)
c41 = Card("Corrupted Ashbringer", "41", "Mythic", "A sword once infused with light, now drenched in \n"
                                                   " deceit and darkness. Whispers can be heard from \n"
                                                   " the sword from anyone who wields it.", card41_image)
c42 = Card("Golden Griffin", "42", "Common",
           "These creatures are hunted extensively for their golden feathers.", card42_image)
c43 = Card("Dragon Egg", "43", "Common",
           "Dragon eggs are a delicacy for the rich and powerful", card43_image)
c44 = Card("Mewtwo", "44", "Uncommon", "One of its kind. This creature was said to have been created \n"
                                       " in a lab.", card44_image)
c45 = Card("Dark Crow Inn", "45", "Uncommon", "Nestled in the dark corner of the grand city of Ultime, \n"
                                              " the patrons of this busy pub come in all shapes, sizes \n"
                                              " and species.", card45_image)
c46 = Card("Pirate Town - Skullmoore", "46", "Rare", "The largest port in Alteria for trade - ruled by \n"
           " no kingdom, and of pirates! If there is a place \n"
           " where pirates are safe, it's here. As for anyone else? \n"
                                                     " That's another matter.", card46_image)
c47 = Card("Kokiri Sword", "47", "Common", "A crude sword made of wood. It's rather small to be of any \n"
                                           " real use.", card47_image)
c48 = Card("Ivory Succubus", "48", "Uncommon", "These elusive creatures travel only by the light of a \n"
                                               " full moon. Their beauty is unmatched.", card48_image)
c49 = Card("Grimmswald, the Mad", "49", "Rare", "The werewolf was said to once be a man from a long, \n"
                                                " royal lineage. The savage nature has overtaken any \n"
                                                " semblance of humanity that might have remained.", card49_image)
c50 = Card("Queen of the Dead", "50", "Mythic", "As old as time itself, ruler of the Underworld and \n"
                                                " equaliser of all things. She is nameless, but she is \n"
                                                " feared by all. Her empire is endless and ever growing.", card50_image)
c51 = Card("The Ultimate Card - Legendary", "51",
           "Legendary", "Unheard of.", card51_image)


# Index cards in a dict with bool to signify if card has been collected yet or not
collection = {
    "c1": False,
    "c2": False,
    "c3": False,
    "c4": False,
    "c5": False,
    "c6": False,
    "c7": False,
    "c8": False,
    "c9": False,
    "c10": False,
    "c11": False,
    "c12": False,
    "c13": False,
    "c14": False,
    "c15": False,
    "c16": False,
    "c17": False,
    "c18": False,
    "c19": False,
    "c20": False,
    "c21": False,
    "c22": False,
    "c23": False,
    "c24": False,
    "c25": False,
    "c26": False,
    "c27": False,
    "c28": False,
    "c29": False,
    "c30": False,
    "c31": False,
    "c32": False,
    "c33": False,
    "c34": False,
    "c35": False,
    "c36": False,
    "c37": False,
    "c38": False,
    "c39": False,
    "c40": False,
    "c41": False,
    "c42": False,
    "c43": False,
    "c44": False,
    "c45": False,
    "c46": False,
    "c47": False,
    "c48": False,
    "c49": False,
    "c50": False,
    "C51": False
}
# index number of cards in a list for random.choice to pull from
cards = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13,
         c14, c15, c16, c17, c18, c19, c20, c21, c22, c23, c24, c25,
         c26, c27, c28, c29, c30, c31, c32, c33, c34, c35, c36, c37,
         c38, c39, c40, c41, c42, c43, c44, c45, c46, c47, c48, c49,
         c50, c51]


def five_pack():
    count = 0
    while count != 5:
        roll_dice()
        print("\n")
        count += 1


def ten_pack():
    count = 0
    while count != 10:
        roll_dice()
        print("\n")
        count += 1


def mythic():
    m = random.choice(cards)
    while m.rarity != "Mythic":
        m = random.choice(cards)
    else:
        card_unlock(m)


def cant_afford():
    errorsound.play()
    print(" Sorry, it seems you don't have enough gold for that!\n")
    print(" Try something else!\n")


def legendary():
    global cards_got
    if cards_got == 50:
        time.sleep(0.5)
        print("\nYou did it! You collected all the cards. Here's a gift.")
        time.sleep(2.0)
        c51.acquired()
        time.sleep(4.0)

    else:
        pass

# Random roll for a card function


def roll_dice():
    result = random.choice(cards)
    while result.name != "The Ultimate Card - Legendary":
        card_unlock(result)
        break
    else:
        pass


######################################################################################################

# Title Background
title_screen = pygame.image.load('images/title.jpg')
title_text = pygame.image.load('images/titletext.png')

# Title Music
menu_music = pygame.mixer.music.load('Sound/Menu/menu.mp3')
menu_music_loop = pygame.mixer.music.play(-1)

# Story Music
story_a = pygame.mixer.music.load('Sound/Menu/menu.mp3')
story_a_loop = pygame.mixer.music.play(-1)

# Menu Images
menu_screen = pygame.image.load('images/menu.jpg')

# Shop Images
shop_screen = pygame.image.load('images/shop.jpg')
shop_wizard = pygame.image.load('images/shopwiz.png')
shop_text1 = pygame.image.load('images/shoptextbox1.png')

shopcard1 = pygame.image.load('images/shopcard1a.png')
shopcard1hov = pygame.image.load('images/shopcard1b.png')
shopcard2 = pygame.image.load('images/shopcard2a.png')
shopcard2hov = pygame.image.load('images/shopcard2b.png')
shopcard3 = pygame.image.load('images/shopcard3a.png')
shopcard3hov = pygame.image.load('images/shopcard3b.png')
shopcard4 = pygame.image.load('images/shopcard4a.png')
shopcard4hov = pygame.image.load('images/shopcard4b.png')

shop_price1 = pygame.image.load('images/price1.png')
shop_price2 = pygame.image.load('images/price2.png')
shop_price3 = pygame.image.load('images/price3.png')
shop_price4 = pygame.image.load('images/price4.png')

collection_screen = pygame.image.load('images/collection.jpg')

# Buttons
button0 = pygame.image.load('images/Button0.png')
button1 = pygame.image.load('images/Button1.png')
button2 = pygame.image.load('images/Button2.png')
button3 = pygame.image.load('images/Button3.png')
button4 = pygame.image.load('images/Button4.png')
button5 = pygame.image.load('images/Button5.png')
button6 = pygame.image.load('images/Button6.png')

# Buttons Hover
button0hov = pygame.image.load('images/Button0hov.png')
button1hov = pygame.image.load('images/Button1hov.png')
button2hov = pygame.image.load('images/Button2hov.png')
button3hov = pygame.image.load('images/Button3hov.png')
button4hov = pygame.image.load('images/Button4hov.png')
button5hov = pygame.image.load('images/Button5hov.png')
button6hov = pygame.image.load('images/Button6hov.png')


# Card Album Images
# Page 1 Not Got
card_not1 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not2 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not3 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not4 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not5 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not6 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')

card_not7 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not8 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not9 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not10 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not11 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not12 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')

# Page 2 Not Got
card_not13 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not14 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not15 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not16 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not17 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not18 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')

card_not19 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not20 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not21 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not22 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not23 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not24 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')

# Page 3 Not Got
card_not25 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not26 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not27 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not28 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not29 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not30 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')

card_not31 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not32 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not33 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not34 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not35 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not36 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')

# Page 4 Not Got
card_not37 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not38 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not39 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not40 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not41 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not42 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')

card_not43 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not44 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not45 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not46 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not47 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not48 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')

# Page 5 Not Got
card_not49 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')
card_not50 = pygame.image.load('images/albumcard/not/cardalbum_not1.png')


# Page 1 Got

card_got1 = pygame.image.load('images/albumcard/got/got_card1.png')
card_got2 = pygame.image.load('images/albumcard/got/got_card2.png')
card_got3 = pygame.image.load('images/albumcard/got/got_card3.png')
card_got4 = pygame.image.load('images/albumcard/got/got_card4.png')
card_got5 = pygame.image.load('images/albumcard/got/got_card5.png')
card_got6 = pygame.image.load('images/albumcard/got/got_card6.png')

card_got7 = pygame.image.load('images/albumcard/got/got_card7.png')
card_got8 = pygame.image.load('images/albumcard/got/got_card8.png')
card_got9 = pygame.image.load('images/albumcard/got/got_card9.png')
card_got10 = pygame.image.load('images/albumcard/got/got_card10.png')
card_got11 = pygame.image.load('images/albumcard/got/got_card11.png')
card_got12 = pygame.image.load('images/albumcard/got/got_card12.png')

# Page 2 Got

card_got13 = pygame.image.load('images/albumcard/got/got_card13.png')
card_got14 = pygame.image.load('images/albumcard/got/got_card14.png')
card_got15 = pygame.image.load('images/albumcard/got/got_card15.png')
card_got16 = pygame.image.load('images/albumcard/got/got_card16.png')
card_got17 = pygame.image.load('images/albumcard/got/got_card17.png')
card_got18 = pygame.image.load('images/albumcard/got/got_card18.png')

card_got19 = pygame.image.load('images/albumcard/got/got_card19.png')
card_got20 = pygame.image.load('images/albumcard/got/got_card20.png')
card_got21 = pygame.image.load('images/albumcard/got/got_card21.png')
card_got22 = pygame.image.load('images/albumcard/got/got_card22.png')
card_got23 = pygame.image.load('images/albumcard/got/got_card23.png')
card_got24 = pygame.image.load('images/albumcard/got/got_card24.png')

# Page 3 Got

card_got25 = pygame.image.load('images/albumcard/got/got_card25.png')
card_got26 = pygame.image.load('images/albumcard/got/got_card26.png')
card_got27 = pygame.image.load('images/albumcard/got/got_card27.png')
card_got28 = pygame.image.load('images/albumcard/got/got_card28.png')
card_got29 = pygame.image.load('images/albumcard/got/got_card29.png')
card_got30 = pygame.image.load('images/albumcard/got/got_card30.png')

card_got31 = pygame.image.load('images/albumcard/got/got_card31.png')
card_got32 = pygame.image.load('images/albumcard/got/got_card32.png')
card_got33 = pygame.image.load('images/albumcard/got/got_card33.png')
card_got34 = pygame.image.load('images/albumcard/got/got_card34.png')
card_got35 = pygame.image.load('images/albumcard/got/got_card35.png')
card_got36 = pygame.image.load('images/albumcard/got/got_card36.png')

# Page 4 Got

card_got37 = pygame.image.load('images/albumcard/got/got_card37.png')
card_got38 = pygame.image.load('images/albumcard/got/got_card38.png')
card_got39 = pygame.image.load('images/albumcard/got/got_card39.png')
card_got40 = pygame.image.load('images/albumcard/got/got_card40.png')
card_got41 = pygame.image.load('images/albumcard/got/got_card41.png')
card_got42 = pygame.image.load('images/albumcard/got/got_card42.png')

card_got43 = pygame.image.load('images/albumcard/got/got_card43.png')
card_got44 = pygame.image.load('images/albumcard/got/got_card44.png')
card_got45 = pygame.image.load('images/albumcard/got/got_card45.png')
card_got46 = pygame.image.load('images/albumcard/got/got_card46.png')
card_got47 = pygame.image.load('images/albumcard/got/got_card47.png')
card_got48 = pygame.image.load('images/albumcard/got/got_card48.png')

# Page 5 Got

card_got49 = pygame.image.load('images/albumcard/got/got_card49.png')
card_got50 = pygame.image.load('images/albumcard/got/got_card50.png')


album_prev = pygame.image.load('images/albumprev.png')
album_next = pygame.image.load('images/albumnext.png')

doyouquit = pygame.image.load('images/doyouquit.png')
quityes = pygame.image.load('images/quityes.png')
quityeshov = pygame.image.load('images/quityeshov.png')
quitno = pygame.image.load('images/quitno.png')
quitnohov = pygame.image.load('images/quitnohov.png')

# Game loop

click = False


def text_box():
    # [colour] (position) border
    pygame.draw.rect(screen, [224, 224, 224], (380, 530, 750, 180), 0)
    pygame.draw.rect(screen, [0, 0, 0], (380, 530, 750, 180), 2)


def choice_text_boxs():
    # 1st text box
    pygame.draw.rect(screen, [224, 224, 224], (380, 730, 750, 40), 0)
    pygame.draw.rect(screen, [0, 0, 0], (380, 730, 750, 40), 2)
    # 2nd text box
    pygame.draw.rect(screen, [224, 224, 224], (380, 780, 750, 40), 0)
    pygame.draw.rect(screen, [0, 0, 0], (380, 780, 750, 40), 2)


# Items
gem = 0
map = 0

###############################  A D V E N T U R E   M O D E   S T A R T  ###################################
gem_image = pygame.image.load('images/adventure/gem.png')
page_0 = pygame.image.load('images/adventure/page0.jpg')  # fortune teller
page_1 = pygame.image.load('images/adventure/page1.jpg')  # forest start
page_2 = pygame.image.load('images/adventure/page2.jpg')  # town entrance
page_3 = pygame.image.load('images/adventure/page3.png')  # dark crow inn
page_4 = pygame.image.load('images/adventure/page4.jpg')  # town exit
page_5 = pygame.image.load('images/adventure/page5.jpg')  # hermits hut
page_6 = pygame.image.load('images/adventure/page6.png')  # swamp
page_7 = pygame.image.load('images/adventure/page7.jpg')  # ship
page_8 = pygame.image.load('images/adventure/page8.jpg')  # end screen


def story_page0d2():
    global gold
    gold += 10
    running = True

    while running:
        screen.blit(page_0, (0, 0))
        text_box()
        sen1 = base_font.render(
            "sending you hurtling out and off the edge of the tower.", True, (0, 0, 0))
        sen2 = base_font.render(
            "You die.", True, (0, 0, 0))
        sen3 = base_font.render(
            "", True, (0, 0, 0))
        sen4 = base_font.render(
            "", True, (0, 0, 0))
        sen5 = base_font.render(
            "Game over. (earned 10 gold)", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page0d():
    running = True

    while running:
        screen.blit(page_0, (0, 0))
        text_box()
        sen1 = base_font.render(
            "“Slow down. First I wanna see some coin.  What's that?", True, (0, 0, 0))
        sen2 = base_font.render(
            "You're dirt poor? Then I can't help ya, now scram, before I", True, (0, 0, 0))
        sen3 = base_font.render(
            "start flingin' my balls around.”", True, (0, 0, 0))
        sen4 = base_font.render(
            "The Dwarf gets impatient with your exit and decided to", True, (0, 0, 0))
        sen5 = base_font.render(
            "help but rolling into a ball and slamming into you,", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page0d2()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page0cb():
    global gold
    gold += 10
    running = True

    while running:
        screen.blit(page_0, (0, 0))
        text_box()
        sen1 = base_font.render(
            "untimely demise.", True, (0, 0, 0))
        sen2 = base_font.render(
            "", True, (0, 0, 0))
        sen3 = base_font.render(
            "", True, (0, 0, 0))
        sen4 = base_font.render(
            "", True, (0, 0, 0))
        sen5 = base_font.render(
            "Game over. (earned 10 gold)", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page0c():
    running = True

    while running:
        screen.blit(page_0, (0, 0))
        text_box()
        sen1 = base_font.render(
            "“Now listen here you little shit. You wanna get smart", True, (0, 0, 0))
        sen2 = base_font.render(
            "with me? Well, hows this for a fortune reading?”", True, (0, 0, 0))
        sen3 = base_font.render(
            "The Dwarf throws one of his crystal balls. With a thud, it", True, (0, 0, 0))
        sen4 = base_font.render(
            "connects squarely on your forehead, sending you hurtling", True, (0, 0, 0))
        sen5 = base_font.render(
            "out and off the edge of the stairs sending you to your", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page0cb()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page0b():
    global gem
    running = True

    while running:
        screen.blit(page_0, (0, 0))
        text_box()
        sen1 = base_font.render(
            "“Nice view from up here, eh? But I don’t think you’re", True, (0, 0, 0))
        sen2 = base_font.render(
            "here for the view," " " + name + " " ".", True, (0, 0, 0))
        sen3 = base_font.render(
            "How do I know your name?” He chuckles. “I know all.” He", True, (0, 0, 0))
        sen4 = base_font.render(
            "very mysteriously hovers his hands over his ball as he", True, (0, 0, 0))
        sen5 = base_font.render(
            "says this. “Now, what do you want?”", True, (0, 0, 0))
        choice1 = base_font.render(
            "1) I thought you knew all?", True, (0, 0, 0))
        choice2 = base_font.render(
            "2) I want to go home", True, (0, 0, 0))

        choice_text_boxs()

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))
        screen.blit(choice1, (400, 740))
        screen.blit(choice2, (400, 790))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            clock.tick(60)

        mx, my = pygame.mouse.get_pos()

        choice_1 = pygame.Rect(380, 730, 750, 40)
        choice_2 = pygame.Rect(380, 780, 750, 40)

        if choice_1.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sound/Malicious.mp3')
                pygame.mixer.music.play(-1)
                story_page0c()

        if choice_2.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sound/Malicious.mp3')
                pygame.mixer.music.play(-1)
                story_page0d()

        pygame.display.update()
        clock.tick(60)


def story_page0():  # fortune teller
    running = True

    while running:
        screen.blit(page_0, (0, 0))
        text_box()
        sen1 = base_font.render(
            "You follow some winding stone steps up along a tower to", True, (0, 0, 0))
        sen2 = base_font.render(
            "the top then pass through some hanging beads into a", True, (0, 0, 0))
        sen3 = base_font.render(
            "rather small room full of cushions and incense candles.", True, (0, 0, 0))
        sen4 = base_font.render(
            "In the middle is a balding dwarf, with his hands over a", True, (0, 0, 0))
        sen5 = base_font.render(
            "crystal ball in front of him. He looks up at you.", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page0b()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page8bd():  # missing gem missing map, bad ending - 50 gold
    global gold
    running = True

    gold += 50

    while running:
        screen.blit(page_8, (0, 0))
        text_box()
        sen1 = base_font.render(
            "Well, you got to the end but I don't know if I'd call that", True, (0, 0, 0))
        sen2 = base_font.render(
            "winning, really. Try again for a better outcome?", True, (0, 0, 0))
        sen3 = base_font.render(
            "", True, (0, 0, 0))
        sen4 = base_font.render(
            "", True, (0, 0, 0))
        sen5 = base_font.render(
            "You earned 50 gold!", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    select_sound.play()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page8bc():  # missing gem got map, ok ending - 100 gold
    global gold, gem, map
    running = True

    gold += 100
    gem = 0
    map = 0
    while running:
        screen.blit(page_8, (0, 0))
        text_box()
        sen1 = base_font.render(
            "Well done! You didn't get the best ending, but that's", True, (0, 0, 0))
        sen2 = base_font.render(
            "fine! Nettle from Dark Crows Inn is standing", True, (0, 0, 0))
        sen3 = base_font.render(
            "next to the Shark King, waving you good-bye.", True, (0, 0, 0))
        sen4 = base_font.render(
            "", True, (0, 0, 0))
        sen5 = base_font.render(
            "You earned 100 gold !", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    select_sound.play()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page8b():  # got gem missing map, ok ending - 100 gold
    global gold, gem, map
    running = True

    gold += 100
    gem = 0
    map = 0

    while running:
        screen.blit(page_8, (0, 0))
        text_box()
        sen1 = base_font.render(
            "Well done! You didn't get the best ending, but that's", True, (0, 0, 0))
        sen2 = base_font.render(
            "fine! The ghost, with his heart, is standing next to the", True, (0, 0, 0))
        sen3 = base_font.render(
            "Shark King, waving you good-bye.", True, (0, 0, 0))
        sen4 = base_font.render(
            "", True, (0, 0, 0))
        sen5 = base_font.render(
            "You earned 100 gold!", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    select_sound.play()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page8a():  # got gem and map, best ending - 200 gold
    global gold, gem, map
    running = True

    gold += 200
    gem = 0
    map = 0

    while running:
        screen.blit(page_8, (0, 0))
        text_box()
        sen1 = base_font.render(
            "Well done! You got the best ending!", True, (0, 0, 0))
        sen2 = base_font.render(
            "Nettle from Dark Crows Inn and the ghost with his heart", True, (0, 0, 0))
        sen3 = base_font.render(
            "are both standing next to the Shark King, waving you", True, (0, 0, 0))
        sen4 = base_font.render(
            "good-bye.", True, (0, 0, 0))
        sen5 = base_font.render(
            "You earned 200 gold!", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    select_sound.play()
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page7e():
    running = True

    while running:
        screen.blit(page_7, (0, 0))
        text_box()
        sen1 = base_font.render(
            "Step into the portal and you’ve won the game!”", True, (0, 0, 0))
        sen2 = base_font.render(
            "", True, (0, 0, 0))
        sen3 = base_font.render(
            "", True, (0, 0, 0))
        sen4 = base_font.render(
            "", True, (0, 0, 0))
        sen5 = base_font.render(
            "", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if gem != 0 and map != 0:
                        story_page8a()
                    elif gem != 0 and map == 0:
                        story_page8b()
                    elif gem == 0 and map != 0:
                        story_page8bc()
                    else:
                        story_page8bd()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page7d():
    running = True

    while running:
        screen.blit(page_7, (0, 0))
        text_box()
        sen1 = base_font.render(
            "You see, you’re in a game. An insultingly simplistic game that", True, (0, 0, 0))
        sen2 = base_font.render(
            "needs to come to an end now as this is just a test to showcase", True, (0, 0, 0))
        sen3 = base_font.render(
            "what he's learned with his Python coding. I don’t know what ", True, (0, 0, 0))
        sen4 = base_font.render(
            "that means either, I’m just telling you what I’ve been told.", True, (0, 0, 0))
        sen5 = base_font.render(
            "Luckily I can summon a portal home for you because magic.", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page7e()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page7c():
    running = True

    while running:
        screen.blit(page_7, (0, 0))
        text_box()
        sen1 = base_font.render(
            "sitting on a golden throne in the back.", True, (0, 0, 0))
        sen2 = base_font.render(
            "“You finally made it" " " + name + " "", wonderful!", True, (0, 0, 0))
        sen3 = base_font.render(
            "You’re probably wondering just what in Davy Jones’ Locker is", True, (0, 0, 0))
        sen4 = base_font.render(
            "going on here. Just bear in mind, I’m only the messenger, but", True, (0, 0, 0))
        sen5 = base_font.render(
            "I have direct contact with the author of all this.", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page7d()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page7b():
    running = True

    while running:
        screen.blit(page_7, (0, 0))
        text_box()
        sen1 = base_font.render(
            "red carpets. Candles are placed everywhere, even on top of other", True, (0, 0, 0))
        sen2 = base_font.render(
            "candles, all melting as one. And ghosts. A lot more ghosts.", True, (0, 0, 0))
        sen3 = base_font.render(
            "But these were not human. They were sharks, all dressed smartly", True, (0, 0, 0))
        sen4 = base_font.render(
            "in old-fashioned suits.", True, (0, 0, 0))
        sen5 = base_font.render(
            "“You there!” shouts the largest of them, who happened to be", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page7c()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page7():
    running = True

    while running:
        screen.blit(page_7, (0, 0))
        text_box()
        sen1 = base_font.render(
            "Listening to the ghost’s directions, you find yourself outside", True, (0, 0, 0))
        sen2 = base_font.render(
            "the very ship he mentioned.  Lucky for you he was telling the", True, (0, 0, 0))
        sen3 = base_font.render(
            "truth! You run inside through a gaping hole in the hull. You", True, (0, 0, 0))
        sen4 = base_font.render(
            "stand amazed as the interior looks nothing like a decrepit ship.", True, (0, 0, 0))
        sen5 = base_font.render(
            "Rows of food-stuffed tables are laid out, separated by royal", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page7b()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page6d2():  # have gem
    running = True

    while running:
        screen.blit(page_6, (0, 0))
        text_box()
        sen1 = base_font.render(
            "“Thank you so much! I always thought the living were jerks,", True, (0, 0, 0))
        sen2 = base_font.render(
            "but you’re alright. What’s that? You need to find the way out?", True, (0, 0, 0))
        sen3 = base_font.render(
            "Just head straight for that large rock in the distance,", True, (0, 0, 0))
        sen4 = base_font.render(
            "then make a right and you’ll come across an old, marooned", True, (0, 0, 0))
        sen5 = base_font.render(
            "ship. Head in through the hull and you’ll be out of here.", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page7()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page6d():  # have gem
    running = True

    while running:
        screen.blit(page_6, (0, 0))
        text_box()
        sen1 = base_font.render(
            "“Heart… I have lost… my heart… red… shiny.”", True, (0, 0, 0))
        sen2 = base_font.render(
            "You show the glowing red gem you found earlier.", True, (0, 0, 0))
        sen3 = base_font.render(
            "“MY HEART! Where did you find it? Please, return it me!”", True, (0, 0, 0))
        sen4 = base_font.render(
            "You hand over the heart. The ghost flies up and down in joy", True, (0, 0, 0))
        sen5 = base_font.render(
            "before composing himself.", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page6d2()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page6c2():  # no gem
    running = True

    while running:
        screen.blit(page_6, (0, 0))
        text_box()
        sen1 = base_font.render(
            "You shouldn’t be wondering these woods, get too deep and", True, (0, 0, 0))
        sen2 = base_font.render(
            "you’ll never make it back out. Listen, just head straight for", True, (0, 0, 0))
        sen3 = base_font.render(
            "that large rock in the distance, then make a right and you’ll", True, (0, 0, 0))
        sen4 = base_font.render(
            "come across an old, marooned ship. Head in through the hull", True, (0, 0, 0))
        sen5 = base_font.render(
            "and you’ll be out of here.”", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page7()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page6c():  # no gem
    running = True

    while running:
        screen.blit(page_6, (0, 0))
        text_box()
        sen1 = base_font.render(
            "“Heart… I have lost… my heart… red… shiny.”", True, (0, 0, 0))
        sen2 = base_font.render(
            "You show that you are in no possession of such a thing, much", True, (0, 0, 0))
        sen3 = base_font.render(
            "to the dismay of the ghost.", True, (0, 0, 0))
        sen4 = base_font.render(
            "“Well fiddlesticks. I don’t know where I lost it, but my search", True, (0, 0, 0))
        sen5 = base_font.render(
            "continues. What’s that? You, like my heart, are lost too?", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page6c2()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page6death3():
    global gold
    gold += 20
    running = True

    while running:
        screen.blit(page_6, (0, 0))
        text_box()
        sen1 = base_font.render(
            "around in circles. You give up, falling to the floor", True, (0, 0, 0))
        sen2 = base_font.render(
            "exhausted, waiting for the inevitable end. You hear bells", True, (0, 0, 0))
        sen3 = base_font.render(
            "ringing in the distance. Your world goes dark...", True, (0, 0, 0))
        sen4 = base_font.render(
            "", True, (0, 0, 0))
        sen5 = base_font.render(
            "Game over. (earned 20 gold)", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page6death2():
    running = True

    while running:
        screen.blit(page_6, (0, 0))
        text_box()
        sen1 = base_font.render(
            "I may be dead but you’re the one with dirt for brains. This is", True, (0, 0, 0))
        sen2 = base_font.render(
            "why I bloody hate the living; you ask for help and all they know", True, (0, 0, 0))
        sen3 = base_font.render(
            "what to do is resort to violence.”", True, (0, 0, 0))
        sen4 = base_font.render(
            "The ghost disappears into the mist, leaving you lost and alone.", True, (0, 0, 0))
        sen5 = base_font.render(
            "You walk on for hours but it is no good, you are just going ", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page6death3()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page6death():
    running = True

    while running:
        screen.blit(page_6, (0, 0))
        text_box()
        sen1 = base_font.render(
            "You scramble around for something to fight off the ghost", True, (0, 0, 0))
        sen2 = base_font.render(
            "with. You grab a large stone by your foot and through it as", True, (0, 0, 0))
        sen3 = base_font.render(
            "hard as you can. The ghost looks at you in disbelief as the", True, (0, 0, 0))
        sen4 = base_font.render(
            "rock completely passes through it.", True, (0, 0, 0))
        sen5 = base_font.render(
            "“Really? Of all the things, you thought that would be a good idea?", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page6death2()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page6b():
    global gem
    running = True

    while running:
        screen.blit(page_6, (0, 0))
        text_box()
        sen1 = base_font.render(
            "in a green mist, a ghost of rotting flesh and bone screams.", True, (0, 0, 0))
        sen2 = base_font.render(
            "“HeLp Me...”", True, (0, 0, 0))
        sen3 = base_font.render(
            "“HELP ME!!!”", True, (0, 0, 0))
        sen4 = base_font.render(
            "", True, (0, 0, 0))
        sen5 = base_font.render(
            "What do you do?", True, (0, 0, 0))
        choice1 = base_font.render(
            "1) Attack ghost", True, (0, 0, 0))
        choice2 = base_font.render(
            "2) Help ghost", True, (0, 0, 0))

        choice_text_boxs()

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))
        screen.blit(choice1, (400, 740))
        screen.blit(choice2, (400, 790))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            clock.tick(60)

        mx, my = pygame.mouse.get_pos()

        choice_1 = pygame.Rect(380, 730, 750, 40)
        choice_2 = pygame.Rect(380, 780, 750, 40)

        if choice_1.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sound/Malicious.mp3')
                pygame.mixer.music.play(-1)
                story_page6death()

        if choice_2.collidepoint((mx, my)):
            if click:
                select_sound.play()
                if gem == 1:
                    story_page6d()
                else:
                    story_page6c()

        pygame.display.update()
        clock.tick(60)


def story_page6():
    running = True

    while running:
        screen.blit(page_6, (0, 0))
        text_box()
        sen1 = base_font.render(
            "When your eyes open, you don’t know how much time has passed", True, (0, 0, 0))
        sen2 = base_font.render(
            "or where you are. You are no longer in the green fields outside", True, (0, 0, 0))
        sen3 = base_font.render(
            "Ultime, quite the opposite in fact. You find yourself amid", True, (0, 0, 0))
        sen4 = base_font.render(
            "structures of stone from a civilisation of past. ", True, (0, 0, 0))
        sen5 = base_font.render(
            "A rush of wind sends a chill down your spine. Appearing over you", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page6b()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page5e2():
    running = True

    while running:
        screen.blit(page_5, (0, 0))
        text_box()
        sen1 = base_font.render(
            "He flings his dagger, which plants itself firmly into the wall,", True, (0, 0, 0))
        sen2 = base_font.render(
            "inches from your face. He lunges for you. You panic, quickly stumble", True, (0, 0, 0))
        sen3 = base_font.render(
            "out of the way, and scrap your knees as you pick yourself up and run.", True, (0, 0, 0))
        sen4 = base_font.render(
            "You do not have time to think of where you are heading, but you", True, (0, 0, 0))
        sen5 = base_font.render(
            "run, not stopping for a second. You feel dizzy, everything goes dark.", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page6()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page5e1():
    running = True

    while running:
        screen.blit(page_5, (0, 0))
        text_box()
        sen1 = base_font.render(
            "The mysterious hooded figure from the Inn is standing there, with a", True, (0, 0, 0))
        sen2 = base_font.render(
            "mischievous grin. A few passers-by slow down and look in your", True, (0, 0, 0))
        sen3 = base_font.render(
            "direction. ", True, (0, 0, 0))
        sen4 = base_font.render(
            "“It seems this outsider has killed the poor hermit!” he shouts", True, (0, 0, 0))
        sen5 = base_font.render(
            "to the onlookers. “Justice must be done!”", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page5e2()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page5e():
    running = True

    while running:
        screen.blit(page_5, (0, 0))
        text_box()
        sen1 = base_font.render(
            "You peer in through the window.  It is hard to make anything", True, (0, 0, 0))
        sen2 = base_font.render(
            "out as the room is dimly lit. You spot something on the floor.", True, (0, 0, 0))
        sen3 = base_font.render(
            "To your horror, you see an old man lying still in a pool of his", True, (0, 0, 0))
        sen4 = base_font.render(
            "own blood. You jerk away from the window.", True, (0, 0, 0))
        sen5 = base_font.render(
            "“What’s this?” comes a voice from behind you.", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page5e1()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page5d2():
    running = True

    while running:
        screen.blit(page_5, (0, 0))
        text_box()
        sen1 = base_font.render(
            "pie which he eats in one gulp. His face turns green and he goes", True, (0, 0, 0))
        sen2 = base_font.render(
            "cross-eyed.", True, (0, 0, 0))
        sen3 = base_font.render(
            "“P-poison…” he mutters as he falls dead in front of you. ", True, (0, 0, 0))
        sen4 = base_font.render(
            "You hear screams as a few onlookers have witnessed what", True, (0, 0, 0))
        sen5 = base_font.render(
            "just happened.", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page5b2()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page5d():
    running = True

    while running:
        screen.blit(page_5, (0, 0))
        text_box()
        sen1 = base_font.render(
            "You decide to do as the shady man says.  Before you know it", True, (0, 0, 0))
        sen2 = base_font.render(
            "you are knocking on the door to the hermit’s outside of town. An", True, (0, 0, 0))
        sen3 = base_font.render(
            "old man opens the door and screams in delight.", True, (0, 0, 0))
        sen4 = base_font.render(
            "“My pie has arrived! Out of "
            "my way!”", True, (0, 0, 0))
        sen5 = base_font.render(
            "He snatches the parcel from you and unwraps it wildly. Inside is a", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page5d2()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page5c1():
    running = True

    while running:
        screen.blit(page_5, (0, 0))
        text_box()
        sen1 = base_font.render(
            "You bang on the door again.  This time, the door opens slowly. You", True, (0, 0, 0))
        sen2 = base_font.render(
            "see an old man dead on the floor, pie coming out of his mouth.", True, (0, 0, 0))
        sen3 = base_font.render(
            "“Murderer!” comes a shout from behind you. It’s the shady hooded", True, (0, 0, 0))
        sen4 = base_font.render(
            "figure who gave you the parcel.", True, (0, 0, 0))
        sen5 = base_font.render(
            "“I seen it with my own eyes!”", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page5b2()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page5b2():
    running = True

    while running:
        screen.blit(page_5, (0, 0))
        text_box()
        sen1 = base_font.render(
            "You panic, quickly stumble out of the way, and scrap your knees as", True, (0, 0, 0))
        sen2 = base_font.render(
            "you pick yourself up and run. You do not have time to think of", True, (0, 0, 0))
        sen3 = base_font.render(
            "where you are heading, but you run as hard as you can, not stopping", True, (0, 0, 0))
        sen4 = base_font.render(
            "for a second. Your eyes get heavy, then everything goes dark.", True, (0, 0, 0))
        sen5 = base_font.render(
            "", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page6()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page5b1():
    running = True

    while running:
        screen.blit(page_5, (0, 0))
        text_box()
        sen1 = base_font.render(
            "You bang on the door again.  This time, the door opens slowly. You", True, (0, 0, 0))
        sen2 = base_font.render(
            "see an old man dead on the floor, pie coming out of his mouth.", True, (0, 0, 0))
        sen3 = base_font.render(
            "“Murderer!” comes a shout from behind you. It’s the shady hooded", True, (0, 0, 0))
        sen4 = base_font.render(
            "figure from the Inn.", True, (0, 0, 0))
        sen5 = base_font.render(
            "“I seen it with my own eyes!”", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page5b2()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page5():
    running = True

    while running:
        screen.blit(page_5, (0, 0))
        text_box()
        sen1 = base_font.render(
            "You find yourself back outside of town, walking across a", True, (0, 0, 0))
        sen2 = base_font.render(
            "lush green hill, heading for the X marked on your map", True, (0, 0, 0))
        sen3 = base_font.render(
            "by Nettle. You see smoke drifting lazily into the blue sky", True, (0, 0, 0))
        sen4 = base_font.render(
            "and as you get nearer, a half-domed house appears. You knock on", True, (0, 0, 0))
        sen5 = base_font.render(
            "the door, but there is no answer. What do you choose?", True, (0, 0, 0))
        choice1 = base_font.render(
            "1) Knock again, but harder", True, (0, 0, 0))
        choice2 = base_font.render(
            "2) Peep through the window", True, (0, 0, 0))

        choice_text_boxs()

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))
        screen.blit(choice1, (400, 740))
        screen.blit(choice2, (400, 790))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            clock.tick(60)

        mx, my = pygame.mouse.get_pos()

        choice_1 = pygame.Rect(380, 730, 750, 40)
        choice_2 = pygame.Rect(380, 780, 750, 40)

        if choice_1.collidepoint((mx, my)):
            if click:
                select_sound.play()
                story_page5b1()

        if choice_2.collidepoint((mx, my)):
            if click:
                select_sound.play()
                story_page5e()

        pygame.display.update()
        clock.tick(60)


def story_page4deathb():
    global gold
    gold += 10
    running = True

    while running:
        screen.blit(page_4, (0, 0))
        text_box()
        sen1 = base_font.render(
            "your eyes close. Life slowly evaporates from your body.", True, (0, 0, 0))
        sen2 = base_font.render(
            "You are left for dead in a cold, dark alley.", True, (0, 0, 0))
        sen3 = base_font.render(
            "", True, (0, 0, 0))
        sen4 = base_font.render(
            "", True, (0, 0, 0))
        sen5 = base_font.render(
            "Game over. (earned 10 gold).", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page4death():
    running = True

    while running:
        screen.blit(page_4, (0, 0))
        text_box()
        sen1 = base_font.render(
            "“You refuse? Not very smart. See, we have an issue now.", True, (0, 0, 0))
        sen2 = base_font.render(
            "I can't let anyone know about this package, so I'm", True, (0, 0, 0))
        sen3 = base_font.render(
            "afraid I can't let you leave here alive.”", True, (0, 0, 0))
        sen4 = base_font.render(
            "The man opens his palm towards you and blows strange dust in", True, (0, 0, 0))
        sen5 = base_font.render(
            "your face. Before you can react, you feel your feet get heavy and", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page4deathb()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page4b():
    running = True

    while running:
        screen.blit(page_4, (0, 0))
        text_box()
        sen1 = base_font.render(
            "you aren’t from around here. I can get you home, no", True, (0, 0, 0))
        sen2 = base_font.render(
            "problem. All you have to do is make sure this gets delivered", True, (0, 0, 0))
        sen3 = base_font.render(
            "to an annoying old man outside of town.”", True, (0, 0, 0))
        sen4 = base_font.render(
            "He tries to hand you a parcel.", True, (0, 0, 0))
        sen5 = base_font.render(
            "What do you do?", True, (0, 0, 0))
        choice1 = base_font.render("1) Take parcel", True, (0, 0, 0))
        choice2 = base_font.render(
            "2) Refuse offer", True, (0, 0, 0))

        choice_text_boxs()

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))
        screen.blit(choice1, (400, 740))
        screen.blit(choice2, (400, 790))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            clock.tick(60)

        mx, my = pygame.mouse.get_pos()

        choice_1 = pygame.Rect(380, 730, 750, 40)
        choice_2 = pygame.Rect(380, 780, 750, 40)

        if choice_1.collidepoint((mx, my)):
            if click:
                select_sound.play()
                story_page5d()

        if choice_2.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sound/Malicious.mp3')
                pygame.mixer.music.play(-1)
                story_page4death()

        pygame.display.update()
        clock.tick(60)


def story_page4a():
    running = True

    while running:
        screen.blit(page_4, (0, 0))
        text_box()
        sen1 = base_font.render(
            "“Psst, hey, you! Over here”", True, (0, 0, 0))
        sen2 = base_font.render(
            "A hooded figure standing under a nearby archway beckons you over.", True, (0, 0, 0))
        sen3 = base_font.render(
            "“Looks like you're in need of help.  Well I can", True, (0, 0, 0))
        sen4 = base_font.render(
            "help you if you help me, understand? I know you’re lost,", True, (0, 0, 0))
        sen5 = base_font.render(
            "", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page4b()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page4():
    running = True

    while running:
        screen.blit(page_4, (0, 0))
        text_box()
        sen1 = base_font.render(
            "“Psst, hey, you! Over here”", True, (0, 0, 0))
        sen2 = base_font.render(
            "The hooded figure you saw staring at you from the Inn was", True, (0, 0, 0))
        sen3 = base_font.render(
            "standing under a nearby archway.", True, (0, 0, 0))
        sen4 = base_font.render(
            "“Couldn’t help over-hearing you need help.  Well I can", True, (0, 0, 0))
        sen5 = base_font.render(
            "help you if you help me, understand? I know you’re lost,", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page4b()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page3e():
    global map
    running = True
    map += 1
    while running:
        screen.blit(page_3, (0, 0))
        text_box()
        sen1 = base_font.render(
            "There is a hermit who lives just outside of town. He don’t", True, (0, 0, 0))
        sen2 = base_font.render(
            "like bein' bothered but he’ll know how to help. Just tell him", True, (0, 0, 0))
        sen3 = base_font.render(
            "Nettle sent you. And before you go, take this map, I have", True, (0, 0, 0))
        sen4 = base_font.render(
            "his location marked out for you.”", True, (0, 0, 0))
        sen5 = base_font.render(
            "Don't get lost!", True, (0, 0, 0))
        choice1 = base_font.render("1) Visit the Hermit?", True, (0, 0, 0))
        choice2 = base_font.render(
            "2) Ignore Nettle and go back to the streets outside", True, (0, 0, 0))

        choice_text_boxs()

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))
        screen.blit(choice1, (400, 740))
        screen.blit(choice2, (400, 790))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            clock.tick(60)

        mx, my = pygame.mouse.get_pos()

        choice_1 = pygame.Rect(380, 730, 750, 40)
        choice_2 = pygame.Rect(380, 780, 750, 40)

        if choice_1.collidepoint((mx, my)):
            if click:
                select_sound.play()
                story_page5()

        if choice_2.collidepoint((mx, my)):
            if click:
                select_sound.play()
                story_page4()

        pygame.display.update()
        clock.tick(60)


def story_page3d():
    running = True
    while running:
        screen.blit(page_3, (0, 0))
        text_box()
        sen1 = base_font.render(
            "Korith in all the lands of Alteria. But I suppose you haven’t", True, (0, 0, 0))
        sen2 = base_font.render(
            "a clue what I’m on about, just like the others.”", True, (0, 0, 0))
        sen3 = base_font.render(
            "Rubbing her chin, she gets lost in "
            "thought for a moment.", True, (0, 0, 0))
        sen4 = base_font.render(
            "“I guess there’s nothin’ for it. He’ll hate me but I’ll deal with", True, (0, 0, 0))
        sen5 = base_font.render(
            "that old wart later.”", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page3e()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page3c():
    running = True
    while running:
        screen.blit(page_3, (0, 0))
        text_box()
        sen1 = base_font.render(
            "“You don’t know where you are? Oh goodness me. Looks like we got", True, (0, 0, 0))
        sen2 = base_font.render(
            "another one. You’re not the first to come in here asking that lately,", True, (0, 0, 0))
        sen3 = base_font.render(
            "and I fear you may not be the last.”", True, (0, 0, 0))
        sen4 = base_font.render(
            "She sighs out of concern for you.", True, (0, 0, 0))
        sen5 = base_font.render(
            "“This "
            "here is the town of Ultime, second only to the grand city of", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page3d()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page3death2():
    global gold
    gold += 10
    running = True
    while running:
        screen.blit(page_3, (0, 0))
        text_box()
        sen1 = base_font.render(
            "the world goes dark around you.", True, (0, 0, 0))
        sen2 = base_font.render(
            "Thus ends your journey, thrown out and left for dead", True, (0, 0, 0))
        sen3 = base_font.render(
            "in a dark alley. ", True, (0, 0, 0))
        sen4 = base_font.render(
            "", True, (0, 0, 0))
        sen5 = base_font.render(
            "Game over. (earned 10 gold)", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page3death1():
    running = True
    while running:
        screen.blit(page_3, (0, 0))
        text_box()
        sen1 = base_font.render(
            "You want to order a drink but realise you have no money.", True, (0, 0, 0))
        sen2 = base_font.render(
            "There is a mug filled to the brim which looks untouched.", True, (0, 0, 0))
        sen3 = base_font.render(
            "You decide to take a chance. You grab it and chug it down.", True, (0, 0, 0))
        sen4 = base_font.render(
            "It probably wasn't the best idea to drink the contents of", True, (0, 0, 0))
        sen5 = base_font.render(
            "something you don't know of. You feel a splitting headache and", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page3death2()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page3b():
    running = True
    while running:
        screen.blit(page_3, (0, 0))
        text_box()
        sen1 = base_font.render(
            "most of their face and the hilt of a dagger playing between", True, (0, 0, 0))
        sen2 = base_font.render(
            "their fingers. As you get to the bar, a small woman springs up, ", True, (0, 0, 0))
        sen3 = base_font.render(
            "cleaning the fog from her spectacles with her apron.", True, (0, 0, 0))
        sen4 = base_font.render(
            "“Deary me, it gets so hot in here you could roast a boar!", True, (0, 0, 0))
        sen5 = base_font.render(
            "What can I do you with, "
            "my love?” she says to you.", True, (0, 0, 0))
        choice1 = base_font.render("1) Where am I?", True, (0, 0, 0))
        choice2 = base_font.render("2) Order a drink", True, (0, 0, 0))

        choice_text_boxs()

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))
        screen.blit(choice1, (400, 740))
        screen.blit(choice2, (400, 790))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            clock.tick(60)

        mx, my = pygame.mouse.get_pos()

        choice_1 = pygame.Rect(380, 730, 750, 40)
        choice_2 = pygame.Rect(380, 780, 750, 40)

        if choice_1.collidepoint((mx, my)):
            if click:
                select_sound.play()
                story_page3c()

        if choice_2.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sound/Malicious.mp3')
                pygame.mixer.music.play(-1)
                story_page3death1()

        pygame.display.update()
        clock.tick(60)


def story_page3():
    running = True
    while running:
        screen.blit(page_3, (0, 0))
        text_box()
        sen1 = base_font.render(
            "You decide to head for the Inn. While a short walk away, it was a little", True, (0, 0, 0))
        sen2 = base_font.render(
            "tricky to find as it was nestled in a dark pocket of town, snuggly", True, (0, 0, 0))
        sen3 = base_font.render(
            "between other shops. The tavern’s wooden sign creeks back and", True, (0, 0, 0))
        sen4 = base_font.render(
            "forth as you enter. You cannot help but catch the glare of others;", True, (0, 0, 0))
        sen5 = base_font.render(
            "one in particular, sitting in the back-left corner with a cowl covering", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    story_page3b()
                    click = True

            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page2():
    running = True

    while running:
        screen.blit(page_2, (0, 0))
        # main box
        pygame.draw.rect(screen, [224, 224, 224], (380, 530, 750, 210), 0)
        pygame.draw.rect(screen, [0, 0, 0], (380, 530, 750, 210), 2)
        # choice boxes
        pygame.draw.rect(screen, [224, 224, 224], (380, 730, 750, 40), 0)
        pygame.draw.rect(screen, [0, 0, 0], (380, 730, 750, 40), 2)

        pygame.draw.rect(screen, [224, 224, 224], (380, 780, 750, 40), 0)
        pygame.draw.rect(screen, [0, 0, 0], (380, 780, 750, 40), 2)

        pygame.draw.rect(screen, [224, 224, 224], (380, 830, 750, 40), 0)
        pygame.draw.rect(screen, [0, 0, 0], (380, 830, 750, 40), 2)

        sen1 = base_font.render(
            "   As you make it to the large open gates of the town, you try to", True, (0, 0, 0))
        sen2 = base_font.render(
            "catch your breath. Your eyes widen as it hits you: the smell of spices,", True, (0, 0, 0))
        sen3 = base_font.render(
            "the wash of colours and the hustle and bustle of the traders on", True, (0, 0, 0))
        sen4 = base_font.render(
            "the street.", True, (0, 0, 0))
        sen5 = base_font.render(
            "   As you walk around, a sign catches your eye.", True, (0, 0, 0))
        sen6 = base_font.render(
            "What do you choose?", True, (0, 0, 0))

        choice1 = base_font.render(
            "1) Fortune Tellers straight ahead", True, (0, 0, 0))
        choice2 = base_font.render("2) Town exit to the left", True, (0, 0, 0))
        choice3 = base_font.render(
            "3) Dark Crow Inn to the right", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))
        screen.blit(sen6, (400, 700))

        screen.blit(choice1, (400, 740))
        screen.blit(choice2, (400, 790))
        screen.blit(choice3, (400, 840))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            clock.tick(60)

        mx, my = pygame.mouse.get_pos()

        choice_1 = pygame.Rect(380, 730, 750, 40)
        choice_2 = pygame.Rect(380, 780, 750, 40)
        choice_3 = pygame.Rect(380, 830, 750, 40)

        if choice_1.collidepoint((mx, my)):
            if click:
                select_sound.play()
                story_page0()

        if choice_2.collidepoint((mx, my)):
            if click:
                select_sound.play()
                story_page4a()

        if choice_3.collidepoint((mx, my)):
            if click:
                select_sound.play()
                story_page3()

        pygame.display.update()
        clock.tick(60)


def story_page1b():
    running = True

    while running:
        screen.blit(page_1, (0, 0))

        pygame.draw.rect(screen, [224, 224, 224], (380, 530, 750, 210), 0)
        pygame.draw.rect(screen, [0, 0, 0], (380, 530, 750, 210), 2)

        sen1 = base_font.render(
            "As you slowly near the bush, a tiny, furry little creature darts", True, (0, 0, 0))
        sen2 = base_font.render(
            "out and away, causing you to fall back in surprise.  Feeling", True, (0, 0, 0))
        sen3 = base_font.render(
            "foolish for being jumpy, you pick yourself up, and that's when", True, (0, 0, 0))
        sen4 = base_font.render(
            "you see it. Something else in the bushes. You reach in and grab a", True, (0, 0, 0))
        sen5 = base_font.render(
            "red gem stone. It looks to be worth something so you pocket it", True, (0, 0, 0))
        sen6 = base_font.render(
            "quickly. You decide to quickly head for town.", True, (0, 0, 0))

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))
        screen.blit(sen6, (400, 700))
        screen.blit(gem_image, (700, 170))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
                    story_page2()
            pygame.display.update()
            clock.tick(60)

        pygame.display.update()
        clock.tick(60)


def story_page():
    global gem
    running = True
    pygame.mixer.music.load('images/adventure/storyA.mp3')
    pygame.mixer.music.play(-1)
    while running:
        screen.blit(page_1, (0, 0))
        text_box()
        sen1 = base_font.render(
            "You stand up and dust off your clothes. Your head still feels dizzy", True, (0, 0, 0))
        sen2 = base_font.render(
            "as you try to look around, you find yourself at the edge of a forest.", True, (0, 0, 0))
        sen3 = base_font.render(
            "Ahead of you in the clearing is a large town of stone and spires.", True, (0, 0, 0))
        sen4 = base_font.render(
            "Just then, you notice a rustling in the bushes near you.", True, (0, 0, 0))
        sen5 = base_font.render("What do you choose?", True, (0, 0, 0))
        choice1 = base_font.render("1) Run toward town", True, (0, 0, 0))
        choice2 = base_font.render("2) Inspect the bush", True, (0, 0, 0))

        choice_text_boxs()

        screen.blit(topbar, (0, 0))
        topcount()

        screen.blit(sen1, (400, 550))
        screen.blit(sen2, (400, 580))
        screen.blit(sen3, (400, 610))
        screen.blit(sen4, (400, 640))
        screen.blit(sen5, (400, 670))
        screen.blit(choice1, (400, 740))
        screen.blit(choice2, (400, 790))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            clock.tick(60)

        mx, my = pygame.mouse.get_pos()

        choice_1 = pygame.Rect(380, 730, 750, 40)
        choice_2 = pygame.Rect(380, 780, 750, 40)

        if choice_1.collidepoint((mx, my)):
            if click:
                select_sound.play()
                story_page2()

        if choice_2.collidepoint((mx, my)):
            if click:
                select_sound.play()
                cardsound_unlock.play()
                gem += 1
                story_page1b()

        pygame.display.update()
        clock.tick(60)


def album_page5():
    running = True

    while running:
        global cards_got

        mx, my = pygame.mouse.get_pos()
        click = False

        screen.blit(collection_screen, (0, 0))

        screen.blit(album_prev, (325, 750))
        screen.blit(escbutton2, (0, 855))
        screen.blit(escbutton, (0, 855))
        screen.blit(topbar, (0, 0))
        screen.blit(albumpage5, (0, 0))
        topcount()

        cardrect49 = pygame.Rect(75, 50, 198, 258)
        cardrect50 = pygame.Rect(325, 50, 198, 258)

        if collection["c49"] is True:
            screen.blit(card_got49, (75, 50))
            if cardrect49.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album49()
        else:
            screen.blit(card_not49, (75, 50))

        if collection["c50"] is True:
            screen.blit(card_got50, (325, 50))
            if cardrect50.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album50()
        else:
            screen.blit(card_not50, (325, 50))

        escape_back = pygame.Rect(0, 855, 312, 47)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            clock.tick(60)

        prevpage = pygame.Rect(325, 750, 280, 87)

        mx, my = pygame.mouse.get_pos()

        if prevpage.collidepoint((mx, my)):
            if click:
                turn_page.play()
                album_page4()
        if escape_back.collidepoint((mx, my)):
            if click:
                turn_page.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sound/Menu/menu.mp3')
                pygame.mixer.music.play(-1)
                menu()

        pygame.display.update()
        clock.tick(60)


def album_page4():
    running = True

    while running:
        global cards_got

        mx, my = pygame.mouse.get_pos()
        click = False

        screen.blit(collection_screen, (0, 0))

        screen.blit(album_next, (950, 753))
        screen.blit(album_prev, (325, 750))
        screen.blit(escbutton2, (0, 855))
        screen.blit(escbutton, (0, 855))
        screen.blit(topbar, (0, 0))
        screen.blit(albumpage4, (0, 0))
        topcount()

        cardrect37 = pygame.Rect(75, 50, 198, 258)
        cardrect38 = pygame.Rect(325, 50, 198, 258)
        cardrect39 = pygame.Rect(575, 50, 198, 258)
        cardrect40 = pygame.Rect(825, 50, 198, 258)
        cardrect41 = pygame.Rect(1075, 50, 198, 258)
        cardrect42 = pygame.Rect(1325, 50, 198, 258)
        cardrect43 = pygame.Rect(75, 420, 198, 258)
        cardrect44 = pygame.Rect(325, 420, 198, 258)
        cardrect45 = pygame.Rect(575, 420, 198, 258)
        cardrect46 = pygame.Rect(825, 420, 198, 258)
        cardrect47 = pygame.Rect(1075, 420, 198, 258)
        cardrect48 = pygame.Rect(1325, 420, 198, 258)

        if collection["c37"] is True:
            screen.blit(card_got37, (75, 50))
            if cardrect37.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album37()
        else:
            screen.blit(card_not37, (75, 50))

        if collection["c38"] is True:
            screen.blit(card_got38, (325, 50))
            if cardrect38.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album38()
        else:
            screen.blit(card_not38, (325, 50))

        if collection["c39"] is True:
            screen.blit(card_got39, (575, 50))
            if cardrect39.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album39()
        else:
            screen.blit(card_not39, (575, 50))

        if collection["c40"] is True:
            screen.blit(card_got40, (825, 50))
            if cardrect40.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album40()
        else:
            screen.blit(card_not40, (825, 50))

        if collection["c41"] is True:
            screen.blit(card_got41, (1075, 50))
            if cardrect41.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album41()
        else:
            screen.blit(card_not41, (1075, 50))

        if collection["c42"] is True:
            screen.blit(card_got42, (1325, 50))
            if cardrect42.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album42()
        else:
            screen.blit(card_not42, (1325, 50))

        if collection["c43"] is True:
            screen.blit(card_got43, (75, 420))
            if cardrect43.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album43()
        else:
            screen.blit(card_not43, (75, 420))

        if collection["c44"] is True:
            screen.blit(card_got44, (325, 420))
            if cardrect44.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album44()
        else:
            screen.blit(card_not44, (325, 420))

        if collection["c45"] is True:
            screen.blit(card_got45, (575, 420))
            if cardrect45.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album45()
        else:
            screen.blit(card_not45, (575, 420))

        if collection["c46"] is True:
            screen.blit(card_got46, (825, 420))
            if cardrect46.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album46()
        else:
            screen.blit(card_not46, (825, 420))

        if collection["c47"] is True:
            screen.blit(card_got47, (1075, 420))
            if cardrect47.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album47()
        else:
            screen.blit(card_not47, (1075, 420))

        if collection["c48"] is True:
            screen.blit(card_got48, (1325, 420))
            if cardrect48.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album48()
        else:
            screen.blit(card_not48, (1325, 420))

        escape_back = pygame.Rect(0, 855, 312, 47)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            clock.tick(60)

        nextpage = pygame.Rect(950, 753, 252, 80)
        prevpage = pygame.Rect(325, 750, 280, 87)

        mx, my = pygame.mouse.get_pos()

        if nextpage.collidepoint((mx, my)):
            if click:
                turn_page.play()
                album_page5()
        if prevpage.collidepoint((mx, my)):
            if click:
                turn_page.play()
                album_page3()
        if escape_back.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sound/Menu/menu.mp3')
                pygame.mixer.music.play(-1)
                menu()

        pygame.display.update()
        clock.tick(60)


def album_page3():
    running = True

    while running:
        global cards_got

        mx, my = pygame.mouse.get_pos()
        click = False

        screen.blit(collection_screen, (0, 0))

        screen.blit(album_next, (950, 753))
        screen.blit(album_prev, (325, 750))
        screen.blit(escbutton2, (0, 855))
        screen.blit(escbutton, (0, 855))
        screen.blit(topbar, (0, 0))
        screen.blit(albumpage3, (0, 0))
        topcount()

        cardrect25 = pygame.Rect(75, 50, 198, 258)
        cardrect26 = pygame.Rect(325, 50, 198, 258)
        cardrect27 = pygame.Rect(575, 50, 198, 258)
        cardrect28 = pygame.Rect(825, 50, 198, 258)
        cardrect29 = pygame.Rect(1075, 50, 198, 258)
        cardrect30 = pygame.Rect(1325, 50, 198, 258)
        cardrect31 = pygame.Rect(75, 420, 198, 258)
        cardrect32 = pygame.Rect(325, 420, 198, 258)
        cardrect33 = pygame.Rect(575, 420, 198, 258)
        cardrect34 = pygame.Rect(825, 420, 198, 258)
        cardrect35 = pygame.Rect(1075, 420, 198, 258)
        cardrect36 = pygame.Rect(1325, 420, 198, 258)

        if collection["c25"] is True:
            screen.blit(card_got25, (75, 50))
            if cardrect25.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album25()
        else:
            screen.blit(card_not25, (75, 50))

        if collection["c26"] is True:
            screen.blit(card_got26, (325, 50))
            if cardrect26.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album26()
        else:
            screen.blit(card_not26, (325, 50))

        if collection["c27"] is True:
            screen.blit(card_got27, (575, 50))
            if cardrect27.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album27()
        else:
            screen.blit(card_not27, (575, 50))

        if collection["c28"] is True:
            screen.blit(card_got28, (825, 50))
            if cardrect28.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album28()
        else:
            screen.blit(card_not28, (825, 50))

        if collection["c29"] is True:
            screen.blit(card_got29, (1075, 50))
            if cardrect29.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album29()
        else:
            screen.blit(card_not29, (1075, 50))

        if collection["c30"] is True:
            screen.blit(card_got30, (1325, 50))
            if cardrect30.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album30()
        else:
            screen.blit(card_not30, (1325, 50))

        if collection["c31"] is True:
            screen.blit(card_got31, (75, 420))
            if cardrect31.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album31()
        else:
            screen.blit(card_not31, (75, 420))

        if collection["c32"] is True:
            screen.blit(card_got32, (325, 420))
            if cardrect32.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album32()
        else:
            screen.blit(card_not32, (325, 420))

        if collection["c33"] is True:
            screen.blit(card_got33, (575, 420))
            if cardrect33.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album33()
        else:
            screen.blit(card_not33, (575, 420))

        if collection["c34"] is True:
            screen.blit(card_got34, (825, 420))
            if cardrect34.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album34()
        else:
            screen.blit(card_not34, (825, 420))

        if collection["c35"] is True:
            screen.blit(card_got35, (1075, 420))
            if cardrect35.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album35()
        else:
            screen.blit(card_not35, (1075, 420))

        if collection["c36"] is True:
            screen.blit(card_got36, (1325, 420))
            if cardrect36.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album36()
        else:
            screen.blit(card_not36, (1325, 420))

        escape_back = pygame.Rect(0, 855, 312, 47)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            clock.tick(60)

        nextpage = pygame.Rect(950, 753, 252, 80)
        prevpage = pygame.Rect(325, 750, 280, 87)

        mx, my = pygame.mouse.get_pos()

        if nextpage.collidepoint((mx, my)):
            if click:
                turn_page.play()
                album_page4()
        if prevpage.collidepoint((mx, my)):
            if click:
                turn_page.play()
                album_page2()
        if escape_back.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sound/Menu/menu.mp3')
                pygame.mixer.music.play(-1)
                menu()

        pygame.display.update()
        clock.tick(60)


def album_page2():
    running = True

    while running:
        global cards_got

        mx, my = pygame.mouse.get_pos()
        click = False

        screen.blit(collection_screen, (0, 0))

        screen.blit(album_next, (950, 753))
        screen.blit(album_prev, (325, 750))
        screen.blit(escbutton2, (0, 855))
        screen.blit(escbutton, (0, 855))
        screen.blit(topbar, (0, 0))
        screen.blit(albumpage2, (0, 0))
        topcount()

        cardrect13 = pygame.Rect(75, 50, 198, 258)
        cardrect14 = pygame.Rect(325, 50, 198, 258)
        cardrect15 = pygame.Rect(575, 50, 198, 258)
        cardrect16 = pygame.Rect(825, 50, 198, 258)
        cardrect17 = pygame.Rect(1075, 50, 198, 258)
        cardrect18 = pygame.Rect(1325, 50, 198, 258)
        cardrect19 = pygame.Rect(75, 420, 198, 258)
        cardrect20 = pygame.Rect(325, 420, 198, 258)
        cardrect21 = pygame.Rect(575, 420, 198, 258)
        cardrect22 = pygame.Rect(825, 420, 198, 258)
        cardrect23 = pygame.Rect(1075, 420, 198, 258)
        cardrect24 = pygame.Rect(1325, 420, 198, 258)

        if collection["c13"] is True:
            screen.blit(card_got13, (75, 50))
            if cardrect13.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album13()
        else:
            screen.blit(card_not13, (75, 50))

        if collection["c14"] is True:
            screen.blit(card_got14, (325, 50))
            if cardrect14.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album14()
        else:
            screen.blit(card_not14, (325, 50))

        if collection["c15"] is True:
            screen.blit(card_got15, (575, 50))
            if cardrect15.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album15()
        else:
            screen.blit(card_not15, (575, 50))

        if collection["c16"] is True:
            screen.blit(card_got16, (825, 50))
            if cardrect16.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album16()
        else:
            screen.blit(card_not16, (825, 50))

        if collection["c17"] is True:
            screen.blit(card_got17, (1075, 50))
            if cardrect17.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album17()
        else:
            screen.blit(card_not17, (1075, 50))

        if collection["c18"] is True:
            screen.blit(card_got18, (1325, 50))
            if cardrect18.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album18()
        else:
            screen.blit(card_not18, (1325, 50))

        if collection["c19"] is True:
            screen.blit(card_got19, (75, 420))
            if cardrect19.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album19()
        else:
            screen.blit(card_not19, (75, 420))

        if collection["c20"] is True:
            screen.blit(card_got20, (325, 420))
            if cardrect20.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album20()
        else:
            screen.blit(card_not20, (325, 420))

        if collection["c21"] is True:
            screen.blit(card_got21, (575, 420))
            if cardrect21.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album21()
        else:
            screen.blit(card_not21, (575, 420))

        if collection["c22"] is True:
            screen.blit(card_got22, (825, 420))
            if cardrect22.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album22()
        else:
            screen.blit(card_not22, (825, 420))

        if collection["c23"] is True:
            screen.blit(card_got23, (1075, 420))
            if cardrect23.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album23()
        else:
            screen.blit(card_not23, (1075, 420))

        if collection["c24"] is True:
            screen.blit(card_got24, (1325, 420))
            if cardrect24.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album24()
        else:
            screen.blit(card_not24, (1325, 420))

        escape_back = pygame.Rect(0, 855, 312, 47)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.update()
            clock.tick(60)

        nextpage = pygame.Rect(950, 753, 252, 80)
        prevpage = pygame.Rect(325, 750, 280, 87)

        mx, my = pygame.mouse.get_pos()

        if nextpage.collidepoint((mx, my)):
            if click:
                turn_page.play()
                album_page3()
        if prevpage.collidepoint((mx, my)):
            if click:
                turn_page.play()
                card_album()
        if escape_back.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sound/Menu/menu.mp3')
                pygame.mixer.music.play(-1)
                menu()

        pygame.display.update()
        clock.tick(60)


def card_album():

    running = True

    while running:
        global cards_got

        mx, my = pygame.mouse.get_pos()
        click = False

        screen.blit(collection_screen, (0, 0))
        screen.blit(album_next, (950, 753))
        screen.blit(escbutton2, (0, 855))
        screen.blit(escbutton, (0, 855))
        screen.blit(topbar, (0, 0))
        screen.blit(albumpage1, (0, 0))
        topcount()

        cardrect1 = pygame.Rect(75, 50, 198, 258)
        cardrect2 = pygame.Rect(325, 50, 198, 258)
        cardrect3 = pygame.Rect(575, 50, 198, 258)
        cardrect4 = pygame.Rect(825, 50, 198, 258)
        cardrect5 = pygame.Rect(1075, 50, 198, 258)
        cardrect6 = pygame.Rect(1325, 50, 198, 258)
        cardrect7 = pygame.Rect(75, 420, 198, 258)
        cardrect8 = pygame.Rect(325, 420, 198, 258)
        cardrect9 = pygame.Rect(575, 420, 198, 258)
        cardrect10 = pygame.Rect(825, 420, 198, 258)
        cardrect11 = pygame.Rect(1075, 420, 198, 258)
        cardrect12 = pygame.Rect(1325, 420, 198, 258)

        if collection["c1"] is True:
            screen.blit(card_got1, (75, 50))
            if cardrect1.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album1()
        else:
            screen.blit(card_not1, (75, 50))

        if collection["c2"] is True:
            screen.blit(card_got2, (325, 50))
            if cardrect2.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album2()
        else:
            screen.blit(card_not2, (325, 50))

        if collection["c3"] is True:
            screen.blit(card_got3, (575, 50))
            if cardrect3.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album3()
        else:
            screen.blit(card_not3, (575, 50))

        if collection["c4"] is True:
            screen.blit(card_got4, (825, 50))
            if cardrect4.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album4()
        else:
            screen.blit(card_not4, (825, 50))

        if collection["c5"] is True:
            screen.blit(card_got5, (1075, 50))
            if cardrect5.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album5()
        else:
            screen.blit(card_not5, (1075, 50))

        if collection["c6"] is True:
            screen.blit(card_got6, (1325, 50))
            if cardrect6.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album6()
        else:
            screen.blit(card_not6, (1325, 50))

        if collection["c7"] is True:
            screen.blit(card_got7, (75, 420))
            if cardrect7.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album7()
        else:
            screen.blit(card_not7, (75, 420))

        if collection["c8"] is True:
            screen.blit(card_got8, (325, 420))
            if cardrect8.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album8()
        else:
            screen.blit(card_not8, (325, 420))

        if collection["c9"] is True:
            screen.blit(card_got9, (575, 420))
            if cardrect9.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album9()
        else:
            screen.blit(card_not9, (575, 420))

        if collection["c10"] is True:
            screen.blit(card_got10, (825, 420))
            if cardrect10.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album10()
        else:
            screen.blit(card_not10, (825, 420))

        if collection["c11"] is True:
            screen.blit(card_got11, (1075, 420))
            if cardrect11.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album11()
        else:
            screen.blit(card_not11, (1075, 420))

        if collection["c12"] is True:
            screen.blit(card_got12, (1325, 420))
            if cardrect12.collidepoint((mx, my)):
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            show_card_album12()
        else:
            screen.blit(card_not12, (1325, 420))

        escape_back = pygame.Rect(0, 855, 312, 47)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        nextpage = pygame.Rect(950, 753, 252, 80)

        mx, my = pygame.mouse.get_pos()

        if nextpage.collidepoint((mx, my)):
            if click:
                turn_page.play()
                album_page2()
        if escape_back.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sound/Menu/menu.mp3')
                pygame.mixer.music.play(-1)
                menu()

        pygame.display.update()
        clock.tick(60)


def card_shop():

    running = True

    pygame.mixer.music.load('Sound/Shop/shop.mp3')
    pygame.mixer.music.play(-1)

    while running:

        screen.blit(shop_screen, (0, 0))
        screen.blit(shop_wizard, (0, 0))
        screen.blit(shop_text1, (0, 0))
        screen.blit(escbutton2, (0, 855))
        screen.blit(escbutton, (0, 855))
        screen.blit(topbar, (0, 0))
        topcount()

        this_sentence1 = base_font.render(
            "Welcome! Please, come in to my little shop of wonders.", True, (0, 0, 0))
        this_sentence2 = base_font.render(
            "Got lots of gold and don't know what to spend it on?", True, (0, 0, 0))
        this_sentence3 = base_font.render(
            "Then you've come to the right place! Please, check the ", True, (0, 0, 0))
        this_sentence4 = base_font.render(
            "offers below and see if anything catches your eye... ", True, (0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        # Normal cards hover
        shop_1 = pygame.Rect(760, 70, 380, 370)
        shop_2 = pygame.Rect(1170, 70, 380, 370)
        shop_3 = pygame.Rect(760, 480, 380, 370)
        shop_4 = pygame.Rect(1170, 480, 380, 370)
        escape_back = pygame.Rect(0, 855, 312, 47)

        # Normal cards
        screen.blit(shopcard1, (760, 85))
        screen.blit(shopcard2, (1170, 70))
        screen.blit(shopcard3, (760, 480))
        screen.blit(shopcard4, (1170, 480))

        # Card prices
        screen.blit(shop_price1, (760, 85))
        screen.blit(shop_price2, (1170, 85))
        screen.blit(shop_price3, (760, 480))
        screen.blit(shop_price4, (1170, 480))

        if shop_1.collidepoint((mx, my)):
            global gold
            screen.blit(shopcard1hov, (760, 85))
            if click:
                select_sound.play()
                if gold < int(10):
                    cant_afford()
                else:
                    gold = gold - 10
                    roll_dice()
                    print(" - " + name + "'s Total Gold: " + str(gold), "-")

        if shop_2.collidepoint((mx, my)):
            screen.blit(shopcard2hov, (1170, 70))
            if click:
                select_sound.play()
                if gold < int(50):
                    cant_afford()
                else:
                    gold = gold - 50
                    five_pack()
                    print(" - " + name + "'s Total Gold: " + str(gold), "-")
        if shop_3.collidepoint((mx, my)):
            screen.blit(shopcard3hov, (760, 480))
            if click:
                select_sound.play()
                if gold < int(100):
                    cant_afford()
                else:
                    gold = gold - 100
                    ten_pack()
                    print(" - " + name + "'s Total Gold: " + str(gold), "-")
        if shop_4.collidepoint((mx, my)):
            screen.blit(shopcard4hov, (1170, 480))
            if click:
                select_sound.play()
                if gold < int(500):
                    cant_afford()
                else:
                    gold = gold - 500
                    mythic()
                    print(" - " + name + "'s Total Gold: " + str(gold), "-")
        if escape_back.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sound/Menu/menu.mp3')
                pygame.mixer.music.play(-1)
                menu()

        screen.blit(this_sentence1, (100, 310))
        screen.blit(this_sentence2, (100, 340))
        screen.blit(this_sentence3, (100, 370))
        screen.blit(this_sentence4, (100, 400))

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('Sound/Menu/menu.mp3')
                    pygame.mixer.music.play(-1)
                    menu()
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


def menu():

    running = True

    while running:
        click = False
        screen.blit(menu_screen, (0, 0))
        screen.blit(topbar, (0, 0))
        topcount()

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(120, 100, 200, 50)
        button_2 = pygame.Rect(120, 200, 200, 50)
        button_3 = pygame.Rect(120, 300, 200, 50)
        button_4 = pygame.Rect(120, 550, 200, 50)
        button_5 = pygame.Rect(120, 660, 200, 50)
        button_6 = pygame.Rect(120, 770, 200, 50)

        screen.blit(button1, (97, 100))
        screen.blit(button2, (97, 200))
        screen.blit(button3, (97, 300))
        screen.blit(button4, (97, 550))
        screen.blit(button5, (97, 660))
        screen.blit(button6, (97, 770))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == KEYDOWN:
            #     if event.key == K_ESCAPE:
            #         running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        if button_1.collidepoint((mx, my)):  # adventure
            screen.blit(button1hov, (97, 100))
            screen.blit(adventurehov, (0, 0))
            if click:
                login_sound.play()
                pygame.mixer.music.stop()
                fade()
                story_page()
        if button_2.collidepoint((mx, my)):  # collection
            screen.blit(button2hov, (97, 200))
            screen.blit(collectionhov, (0, 0))
            if click:
                select_sound.play()
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Sound/Card/card.mp3')
                pygame.mixer.music.play(-1)
                card_album()
        if button_3.collidepoint((mx, my)):  # shop
            screen.blit(button3hov, (97, 300))
            screen.blit(shophov, (0, 0))
            if click:
                select_sound.play()
                card_shop()
        if button_4.collidepoint((mx, my)):  # save
            screen.blit(button4hov, (97, 550))
            if click:
                save()
        if button_5.collidepoint((mx, my)):  # load
            screen.blit(button5hov, (97, 660))
            if click:
                load()
        if button_6.collidepoint((mx, my)):  # exit
            screen.blit(button6hov, (97, 770))
            if click:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)


# Game Start Here
while True:
    redrawWindow()
    pygame.time.delay(10)

    screen.blit(title_screen, (0, 0))
    screen.blit(title_text, (0, 0))

    mx, my = pygame.mouse.get_pos()
    screen.blit(button0, (675, 630))

    # buttons below
    button_1 = pygame.Rect(697, 630, 200, 50)
    if button_1.collidepoint((mx, my)):
        screen.blit(button0hov, (675, 630))
        if click:
            if len(name) >= 1:
                login_sound.play()
                fade()
                menu()

            else:
                name_error.play()
                pass

        # buttons above

    click = False

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if pygame.key.get_pressed:
            if len(name) >= 21:
                name = name[:-1]
                name_error.play()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            else:
                name += event.unicode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if len(name) >= 2:
                    name = name[:-1]
                    login_sound.play()
                    fade()
                    menu()
                else:
                    name = name[:-1]
                    name_error.play()
                    pass

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True

    pygame.draw.rect(screen, colour, input_rect)

    text_surface = base_font.render(name, True, (0, 0, 0))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    input_rect.w = max(400, text_surface.get_width() + 10)

    pygame.display.update()  # update display
    clock.tick(60)  # maintain 60 dps


title()
