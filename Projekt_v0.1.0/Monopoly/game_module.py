import pygame
import os

SIZESCREEN = WIDTH, HEIGHT = 1920, 1080

LIGHTBLUE = pygame.color.THECOLORS['lightblue']

screen = pygame.display.set_mode(SIZESCREEN)

path = os.path.join(os.pardir, 'images')
file_names = sorted(os.listdir(path))

file_names.remove('background.png')
BACKGROUND = pygame.image.load(os.path.join(path, 'background.png')).convert()
for file_name in file_names:
    image_name = file_name[:-4].upper()
    globals()[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(BACKGROUND)


data = (('typ', 'cena', 'czynsz', 'czynsz_kolor', 'czynsz1', 'czynsz2', 'czynsz3', 'czynsz4', 'czynszh', 'kosztd', 'koszth', 'hipoteka', 'splatahipoteki'),
            ('START', ''),  # +200
            ('POLE', 60, 2, 4, 10, 30, 90, 160, 250, 50, 50, 30, 33, ''),
            ('KASA_SPOL', ''),
            ('POLE', 60, 4, 8, 20, 60, 180, 320, 450, 50, 50, 30, 33, ''),
            ('PODATEK_DOCHODOWY', 200),
            ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110, ''),  # DWORZEC
            ('POLE', 100, 6, 12, 30, 90, 270, 400, 550, 50, 50, 50, 55, ''),
            ('SZANSA', ''),
            ('POLE', 100, 6, 12, 30, 90, 270, 400, 550, 50, 50, 50, 55, ''),
            ('POLE', 120, 8, 16, 40, 100, 300, 450, 600, 50, 50, 60, 66, ''),
            ('WIEZIENIE', ''),
            ('POLE', 140, 10, 20, 50, 150, 450, 625, 750, 100, 100, 70, 77, ''),
            ('POLE', 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 83, ''), #ELEKTROWNIA JESLI 1 ZAKLAD - 4*kostka, JESLI 2 - 10*kostka
            ('POLE', 140, 10, 20, 50, 150, 450, 625, 750, 100, 100, 70, 77, ''),
            ('POLE', 160, 12, 24, 60, 180, 500, 700, 900, 100, 100, 80, 88, ''),
            ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110, ''),  # DWORZEC
            ('POLE', 180, 14, 28, 70, 200, 550, 750, 950, 100, 100, 90, 99, ''),
            ('KASA_SPOLECZNA', ''),
            ('POLE', 180, 14, 28, 70, 200, 550, 750, 950, 100, 100, 90, 99, ''),
            ('POLE', 200, 16, 32, 80, 22, 600, 800, 1000, 100, 100, 100, 110, ''),
            ('BEZPLATNY_PARKING', ''),
            ('POLE', 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150, 110, 121, ''),
            ('SZANSA', ''),
            ('POLE', 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150, 110, 121, ''),
            ('POLE', 240, 20, 40, 100, 300, 750, 925, 1100, 150, 150, 120, 132, ''),
            ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110, ''),  # DWORZEC
            ('POLE', 22, 44, 110, 330, 800, 975, 1150, 150, 150, 130, 143, ''),
            ('POLE', 22, 44, 110, 330, 800, 975, 1150, 150, 150, 130, 143, ''),
            ('POLE', 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 83, ''),  # WODOCIAG, JESLI 1 ZAKLAD - 4*kostka, JESLI 2 - 10*kostka
            ('POLE', 280, 24, 48, 120, 360, 850, 1025, 1200, 150, 150, 140, 154, ''),
            ('IDZ_DO_WIEZIENIA', ''),
            ('POLE', 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200, 150, 165, ''),
            ('POLE', 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200, 150, 165, ''),
            ('KASA_SPOLECZNA', ''),
            ('POLE', 320, 28, 56, 150, 450, 1000, 1200, 1400, 200, 200, 160, 176, ''),
            ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110, ''),  # DWORZEC
            ('SZANSA', ''),
            ('POLE', 350, 35, 70, 175, 500, 1100, 1300, 1500, 200, 200, 175, 193, ''),
            ('PODATEK_DOCHODOWY_DO_ZAPLATY', 100),
            ('POLE', 400, 50, 100, 200, 600, 1400, 1700, 2000, 200, 200, 200, 220, ''))


'''satelita - peron
tax - opłata za licencje oprogramowania - luxury tax
cloud - wodociagi
internet - elektrownia


POLEBROWN
POLELIGHTBLUE
POLEPINK
POLEORANGE
POLERED
POLEYELLOW
POLEGREEN
POLEDARKBLUE

POLESTART
POLEKASADOL
POLETAX
POLESATELITAS
POLESZANSADOL
POLEJAIL
POLEINTERNET
POLESATELITAW
POLEKASALEWO
POLEPARKING
POLESZANSAGORA
POLESATELITAN
POLECLOUD
POLEGOTOJAIL
POLEKASAPRAWO
POLESATELITAE
POLESZANSAPRAWO

trzeba TAXPDOL

niepotrzebne xd:
POLEKASAGORA
POLESZANSALEWO

'''
