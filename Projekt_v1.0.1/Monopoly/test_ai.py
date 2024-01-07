

# dane do analizy

index_gracza = 1       #[1-4]
pozycja = 7            # [1-40]
wartosc_pola = 40
pieniadze = 1000
wlasciciel = 0         #[0-4] 0 - brak; reszta index
cena_pola = 100
cena_domku = 50
cena_hotelu = 50
domki_na_danym_polu = 0   # [0-4]
hotele_na_danym_polu = 0  # [0-4]
inne_pola_koloru = [[2, 0, 0], [1, 0, 0]]  # [(wlasciciel, domki, hotele), ...]
wszystkie_pola_koloru = [[wlasciciel, 0, 0], [1, 0, 0], [1, 0, 0]]

fields = ('2', '4',          # czarne
          '7', '9', '10',    # niebieskie
          '12', '14', '15',  # rózowe
          '17', '19', '20',  # pomorańcz
          '22', '24', '25',  # czerwone
          '27', '28', '30',  # zółte
          '32', '33', '35',  # zielone
          '38', '40')        # fiolet

wartosci = (20, 20,          # czarne
          20, 20, 20,        # niebieskie
          40, 40, 40,        # rózowe
          100, 100, 100,     # pomorańcz
          100, 100, 100,     # czerwone
          40, 40, 40,        # zółte
          20, 20, 20,        # zielone
          20, 20)            # fiolet



# =======akcje========
def evaluate():
    w = [0]*9  # - zbiór wartości akcji

# === kupowanie pola w(0) ===

    if wlasciciel != 0:
        w[0] = 0
    elif pieniadze <= cena_pola:
        w[0] = 0
    else:
        w[0] = wartosc_pola

        inne_pola_zajete = 0
        inne_pola_nasze = 0
        for x in inne_pola_koloru:
            if x[0] != index_gracza and x[0] != 0:
                inne_pola_zajete += 1
            if x[0] == index_gracza:
                inne_pola_nasze += 1
        if inne_pola_zajete == 1:
            w[0] = w[0] * 1/2
        elif inne_pola_zajete == 2:
            w[0] = w[0] * 1/4
        else:
            w[0] = w[0] - (cena_pola/pieniadze)*100
            if inne_pola_nasze == 1:
                w[0] += 30
            if inne_pola_nasze == 2:
                w[0] += 50

# === kupowanie domku 1 w(1) ===
    global wszystkie_pola_koloru
    czy_monopol = True
    ilosc_domkow = 0
    ilosc_hoteli = 0
    x_count = 0
    #print(wszystkie_pola_koloru)
    for x in wszystkie_pola_koloru:
        x_count += 1
        if x[0] != index_gracza:
            czy_monopol = False
        else:
            ilosc_domkow += x[1]
            ilosc_hoteli += x[2]

    if not czy_monopol:
        w[1] = 0
    elif pieniadze <= cena_domku:
        w[1] = 0
    else:
        w[1] = (wartosc_pola + (cena_domku/pieniadze)*100) - 10 * ilosc_domkow
    #print(ilosc_domkow)
    if ilosc_domkow >= x_count:
        w[1] = 0

    return w
# === kupowanie domku 2 w(2) ===
#   if nie ma domku 1:
#       w(2) = 0
#   elif brak pieniedzy:
#       w(2) = 0
#   else:
#       w(2) = (20 * kasa/cena) + 10 * ilosc domkow na inncy polach danego koloru

# === kupowanie domku 3 w(3) ===
#   if nie ma domku 2:
#       w(3) = 0
#   elif brak pieniedzy:
#       w(3) = 0
#   elif brak 2 domkow na wszystkich polach koloru
#       w(3) = 0
#   else:
#       w(3) = (10 * kasa/cena) + 5 * ilosc domkow na inncy polach danego koloru
#

# === kupowanie domku 4 w(4) ===
#   if nie ma domku 3:
#       w(4) = 0
#   elif brak pieniedzy:
#       w(4) = 0
#   elif brak 3 domkow na wszystkich polach koloru
#       w(4) = 0
#   else:
#       w(4) = (5 * kasa/cena) + 5 * ilosc domkow na inncy polach danego koloru

# === kupowanie hotelu 1 w(5) ===

# === kupowanie hotelu 2 w(6) ===

# === kupowanie hotelu 3 w(7) ===

# === kupowanie hotelu 4 w(8) ===

# return w


# =======akcja========

# wykonuj akcje o najwyższej wartości akcji t momentu aż będzie ona niższa niż 20
def select_action(w):
    # znajdywanie najlepszego ruchu

    max_action_value = max(w)

    while max_action_value >= 30:
        print(w)

        # wykonanie akcji o danym indeksie
        print(f'wykonanie akcji {w.index(max_action_value)} o wartosci akcji: {max_action_value}')
        make_action(w.index(max_action_value))


        # na nowo wartościowanie
        w = evaluate()

        # na nowo szukanie max
        max_action_value = max(w)
        print('===================')

    # koniec ruchu gdy nie ma dobrych akcji
    # self.switch_player()
    print(w)
    #print(wszystkie_pola_koloru)
    print("koniec ruchu")


def make_action(index):
    # print("wykonana akcja: ", index)
    global pieniadze, wlasciciel, wszystkie_pola_koloru
    if index == 0:
        print("akcja 0 kupowanie pola")
        pieniadze -= cena_pola
        wlasciciel = index_gracza
        wszystkie_pola_koloru[0][0] = wlasciciel
        #print(wszystkie_pola_koloru)

    if index == 1:
        print("akcja 1 kupowanie domku")
        pieniadze -= cena_domku

        for x in wszystkie_pola_koloru:
            if x[1] == 0:
                x[1] = 1
                return





select_action(evaluate())




