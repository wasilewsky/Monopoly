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


data = (('typ', 'cena', 'czynsz', 'czynsz z kolorem', 'czynsz z 1', 'czynsz z 2', 'czynsz z 3', 'czynsz z 4',
         'czynsz z hotelem',
         'koszt domu', 'koszt hotelu', 'hipoteka', 'splata hipoteki', 'kolor', 'nazwa'),
        ('START', ''),  # +200
        ('POLE', 60, 2, 4, 10, 30, 90, 160, 250, 50, 50, 30, 33, (94, 38, 18), 'eBay', ''),
        ('KASA_SPOL', ''),
        ('POLE', 60, 4, 8, 20, 60, 180, 320, 450, 50, 50, 30, 33, (94, 38, 18), 'Autodesk', ''),
        ('PODATEK_DOCHODOWY', 200),
        ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110, (255, 255, 255), 'Satelita poł.', ''),  # DWORZEC
        ('POLE', 100, 6, 12, 30, 90, 270, 400, 550, 50, 50, 50, 55, (152, 245, 255), 'IBM', ''),
        ('SZANSA', ''),
        ('POLE', 100, 6, 12, 30, 90, 270, 400, 550, 50, 50, 50, 55, (152, 245, 255), 'Intel', ''),
        ('POLE', 120, 8, 16, 40, 100, 300, 450, 600, 50, 50, 60, 66, (152, 245, 255), 'NVIDIA', ''),
        ('WIEZIENIE', ''),
        ('POLE', 140, 10, 20, 50, 150, 450, 625, 750, 100, 100, 70, 77, (191, 62, 255), 'ABB', ''),
        ('POLE', 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 83, (255, 255, 255), 'Starlink', ''),
        # ELEKTROWNIA JESLI 1 ZAKLAD - 4*kostka, JESLI 2 - 10*kostka
        ('POLE', 140, 10, 20, 50, 150, 450, 625, 750, 100, 100, 70, 77, (191, 62, 255), 'Oracle', ''),
        ('POLE', 160, 12, 24, 60, 180, 500, 700, 900, 100, 100, 80, 88, (191, 62, 255), 'Cisco', ''),
        ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110, (255, 255, 255), 'Satelita zach.', ''),  # DWORZEC
        ('POLE', 180, 14, 28, 70, 200, 550, 750, 950, 100, 100, 90, 99, (255, 128, 0), 'Alibaba', ''),
        ('KASA_SPOLECZNA', ''),
        ('POLE', 180, 14, 28, 70, 200, 550, 750, 950, 100, 100, 90, 99, (255, 128, 0), 'Tencent', ''),
        ('POLE', 200, 16, 32, 80, 22, 600, 800, 1000, 100, 100, 100, 110, (255, 128, 0), 'Huawei', ''),
        ('BEZPLATNY_PARKING', ''),
        ('POLE', 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150, 110, 121, (255, 0, 0), 'Home', ''),
        ('SZANSA', ''),
        ('POLE', 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150, 110, 121, (255, 0, 0), 'Comarch', ''),
        ('POLE', 240, 20, 40, 100, 300, 750, 925, 1100, 150, 150, 120, 132, (255, 0, 0), 'CD Project', ''),
        ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110, (255, 255, 255), 'Satelita pół.', ''),  # DWORZEC
        ('POLE', 260, 22, 44, 110, 330, 800, 975, 1150, 150, 150, 130, 143, (255, 255, 0), 'Dell', ''),
        ('POLE', 260, 22, 44, 110, 330, 800, 975, 1150, 150, 150, 130, 143, (255, 255, 0), 'LG', ''),
        ('POLE', 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 83, (255, 255, 255), 'Kryptowaluty', ''),
        # WODOCIAG, JESLI 1 ZAKLAD - 4*kostka, JESLI 2 - 10*kostka
        ('POLE', 280, 24, 48, 120, 360, 850, 1025, 1200, 150, 150, 140, 154, (255, 255, 0), 'Samsung', ''),
        ('IDZ_DO_WIEZIENIA', ''),
        ('POLE', 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200, 150, 165, (0, 255, 0), 'Meta', ''),
        ('POLE', 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200, 150, 165, (0, 255, 0), 'Amazon', ''),
        ('KASA_SPOLECZNA', ''),
        ('POLE', 320, 28, 56, 150, 450, 1000, 1200, 1400, 200, 200, 160, 176, (0, 255, 0), 'Alphabet', ''),
        ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110, (255, 255, 255), 'Satelita wsch.', ''),  # DWORZEC
        ('SZANSA', ''),
        ('POLE', 350, 35, 70, 175, 500, 1100, 1300, 1500, 200, 200, 175, 193, (0, 0, 255), 'Microsoft', ''),
        ('PODATEK_DOCHODOWY_DO_ZAPLATY', 100),
        ('POLE', 400, 50, 100, 200, 600, 1400, 1700, 2000, 200, 200, 200, 220, (0, 0, 255), 'Apple', ''))


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
