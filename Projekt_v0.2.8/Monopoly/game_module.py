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


data = (('typ', 'cena', 'czynsz', 'czynsz_z_kolorem', 'czynsz_z_1', 'czynsz_z_2', 'czynsz_z_3', 'czynsz_z_4',
         'czynsz_z_hotelem',
         'koszt_domu', 'koszt_hotelu', 'hipoteka', 'splata_hipoteki', 'kolor', 'nazwa'),
        ('START', ''),  # +200
        ('POLE', 60, 2, 4, 10, 30, 90, 160, 250, 50, 50, 30, 33, (94, 38, 18), 'eBay', ''),
        ('KASA_SPOLECZNA', ''),
        ('POLE', 60, 4, 8, 20, 60, 180, 320, 450, 50, 50, 30, 33, (94, 38, 18), 'Autodesk', ''),
        ('PODATEK_DOCHODOWY', 200),
        ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110, (255, 255, 255), 'Satelita S', ''),  # DWORZEC
        ('POLE', 100, 6, 12, 30, 90, 270, 400, 550, 50, 50, 50, 55, (152, 245, 255), 'IBM', ''),
        ('SZANSA', ''),
        ('POLE', 100, 6, 12, 30, 90, 270, 400, 550, 50, 50, 50, 55, (152, 245, 255), 'Intel', ''),
        ('POLE', 120, 8, 16, 40, 100, 300, 450, 600, 50, 50, 60, 66, (152, 245, 255), 'NVIDIA', ''),
        ('WIEZIENIE', ''),
        ('POLE', 140, 10, 20, 50, 150, 450, 625, 750, 100, 100, 70, 77, (191, 62, 255), 'ABB', ''),
        ('POLE', 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 83, (255, 255, 255), 'Elektrownia Sł.', ''),
        # ELEKTROWNIA JESLI 1 ZAKLAD - 4*kostka, JESLI 2 - 10*kostka
        ('POLE', 140, 10, 20, 50, 150, 450, 625, 750, 100, 100, 70, 77, (191, 62, 255), 'Oracle', ''),
        ('POLE', 160, 12, 24, 60, 180, 500, 700, 900, 100, 100, 80, 88, (191, 62, 255), 'Cisco', ''),
        ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110, (255, 255, 255), 'Satelita W', ''),  # DWORZEC
        ('POLE', 180, 14, 28, 70, 200, 550, 750, 950, 100, 100, 90, 99, (255, 128, 0), 'Alibaba', ''),
        ('KASA_SPOLECZNA', ''),
        ('POLE', 180, 14, 28, 70, 200, 550, 750, 950, 100, 100, 90, 99, (255, 128, 0), 'Tencent', ''),
        ('POLE', 200, 16, 32, 80, 22, 600, 800, 1000, 100, 100, 100, 110, (255, 128, 0), 'Huawei', ''),
        ('BEZPLATNY_PARKING', ''),
        ('POLE', 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150, 110, 121, (255, 0, 0), 'Home', ''),
        ('SZANSA', ''),
        ('POLE', 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150, 110, 121, (255, 0, 0), 'Comarch', ''),
        ('POLE', 240, 20, 40, 100, 300, 750, 925, 1100, 150, 150, 120, 132, (255, 0, 0), 'CD Project', ''),
        ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110, (255, 255, 255), 'Satelita N', ''),  # DWORZEC
        ('POLE', 260, 22, 44, 110, 330, 800, 975, 1150, 150, 150, 130, 143, (255, 255, 0), 'Dell', ''),
        ('POLE', 260, 22, 44, 110, 330, 800, 975, 1150, 150, 150, 130, 143, (255, 255, 0), 'LG', ''),
        ('POLE', 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 83, (255, 255, 255), 'Elektrownia At.', ''),
        # WODOCIAG, JESLI 1 ZAKLAD - 4*kostka, JESLI 2 - 10*kostka
        ('POLE', 280, 24, 48, 120, 360, 850, 1025, 1200, 150, 150, 140, 154, (255, 255, 0), 'Samsung', ''),
        ('IDZ_DO_WIEZIENIA', ''),
        ('POLE', 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200, 150, 165, (0, 255, 0), 'Meta', ''),
        ('POLE', 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200, 150, 165, (0, 255, 0), 'Amazon', ''),
        ('KASA_SPOLECZNA', ''),
        ('POLE', 320, 28, 56, 150, 450, 1000, 1200, 1400, 200, 200, 160, 176, (0, 255, 0), 'Alphabet', ''),
        ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110, (255, 255, 255), 'Satelita E', ''),  # DWORZEC
        ('SZANSA', ''),
        ('POLE', 350, 35, 70, 175, 500, 1100, 1300, 1500, 200, 200, 175, 193, (0, 0, 255), 'Microsoft', ''),
        ('PODATEK_DOCHODOWY_DO_ZAPLATY', 100),
        ('POLE', 400, 50, 100, 200, 600, 1400, 1700, 2000, 200, 200, 200, 220, (0, 0, 255), 'Apple', ''))

chance_cards = (
    (1, 'IDŹ NA POLE START. (POBIERZ $200)'),
    (2, 'IDŹ NA RÓŻOWE POLE 1. '),
    (3, 'IDŹ NA NAJBLIŻSZE POLE SATELITY.'),
    (4, 'IDŹ NA CZERWONE POLE 3.'),
    (5, 'WYJDŹ BEZPŁATNIE Z WIĘZIENIA.'),
    (6, 'IDŹ NA POLE SATELITY 1.'),
    (7, 'IDŹ NA NAJBLIŻSZE POLE ELEKTROWNI.'),
    (8, 'WYBRANO CIĘ PREZESEM ZARZĄDU. ZAPŁAĆ KAŻDEMU $50.'),
    (9, 'COFNIJ SIĘ O TRZY POLA.'),
    (10, 'BANK WYPŁACA CI DYWIDENDĘ W KWOCIE $50.'),
    (11, 'ZAPŁAĆ ZA KAŻDY DOM $25, ZA KAŻDY HOTEL $100.'),
    (12, 'IDŹ DO WIĘZIENIA. NIE POBIERASZ $200.'),
    (13, 'IDŻ NA GRANATOWE POLE 2.'),
    (14, 'MANDAT ZA PRZEKROCZENIE PRĘDKOŚCI $15.'),
    (15, 'OTRZYMUJESZ SPŁATĘ KREDYTU. POBIERZ $150.'),
    (16, 'IDŹ NA NAJBLIŻSZE POLE SATELITY.'),
)

cards = (
    (1, 'ZAPŁAĆ: $40 ZA KAŻDY DOM $115 ZA KAŻDY HOTEL.'),
    (2, 'WYGRAŁEŚ KONKURS PIĘKNOŚCI. POBIERZ $10.'),
    (3, 'BŁĄD BANKOWY NA TWOIM KONCIE! POBIERZ $200.'),
    (4, 'WYJDŹ BEZPŁATNIE Z WIĘZIENIA.'),
    (5, 'IDŹ DO WIĘZIENIA. NIE PRZECHODŹ PRZEZ START.'),
    (6, 'MASZ URODZINY! POBIERZ $10 OD KAŻDEGO GRACZA.'),
    (7, 'FUNDUSZ ZDROWOTNY. POBIERZ $100.'),
    (8, 'ZAPŁAĆ ZA WIZYTĘ U DENTYSTY- $100.'),
    (9, 'ZAPŁAĆ CZESNE - $50.'),
    (10, 'PRZEJDŹ NA START (POBIERZ $200).'),
    (11, 'WYPRZEDAŻ! POBIERZ $50.'),
    (12, 'ZAPŁAĆ ZA WIZYTĘ LEKARSKĄ - $50.'),
    (13, 'ZWROT PODATKU. POBIERZ $20.'),
    (14, 'OTRZYMUJESZ $25 ZA PORADY FINANSOWE.'),
    (15, 'ODZIEDZICZYŁEŚ SPADEK. POBIERZ $100.'),
    (16, 'DOSTAŁEŚ PREMIĘ! POBIERZ $100.'),

)

'''satelita - peron
tax - opłata za licencje oprogramowania - luxury tax
elektrownia atomowa - wodociagi
elektrownia słoneczna - elektrownia


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
POLETAXDOL
POLESATELITAS
POLESZANSADOL
POLEJAIL
POLEELEKTROSLON
POLESATELITAW
POLEKASALEWO
POLEPARKING
POLESZANSAGORA
POLESATELITAN
POLEELEKTROATOM
POLEGOTOJAIL
POLEKASAPRAWO
POLESATELITAE
POLESZANSAPRAWO
POLETAX
'''
