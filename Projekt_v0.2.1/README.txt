# do raportu 2
--------------------
Damian:
- ruch dla pionka w zależności od wbranego koloru (gracza)
- skakanie pionka po wszystkich polach podczas ruchu
- odpowiednia pozycja na polu więdzienie (odwiedzający)

- rozszerzenie klasy message by wyświetlała 10 ostatnich komunikatów
- dodnie klasy System tworzącej instancje wszystkich innych klas, trzymająca referencje i zajmującą się  rysowaniem
  oraz odświeżaniem planszy oraz zarządzaniem kolejką i akcjami AI
--------------------
Hubert:
wyświetlanie karty
po najechaniu widać kolor pola, nazwę i inne atrybuty
nie pokazuje się na polach specjalnych
--------------------
Wojtek:
klasa do komunikatów
--------------------


# rzeczy do zrobienia po kolei grupami
# rzeczy z następnej grupy potrzebują czegoś gotowego z poprzedniej by było możliwe zajęcie się tym
$ oznacza zrobione zadanie
============================================
$ 0.1 wyświetlanie karty (hubert)
    $ - po najechaniu widać kolor pola, nazwę i inne atrybuty
    $ - nie pokazuje się na polach specjalnych

$ 0.2 garfika jednego pola (wojtek?)
    $ - uzupełnienie brakującej grafiki

$ 0.3 klasa do komunikatów
    $ - pole tabela stringów z poprzednimi komunikatami (nie jeśli tylko aktualny komunikat wyświetlamy)
    $ - matoda dostająca jako parametr string, wypisująca go w odpowiednim miejscu
    $ - metoda rysująca pole z komunikatem

============================================

1.1 Zaznaczanie kolorem własności danego pola
    - punkt/punkty w klasie field informujący ze dany gracz posiada pole
    - lista w klasie player posiadanych pol
    == albo lista u graczy aktualizuje się na podstawie zazanczonych pol albo pola zaznaczają się z list graczy
    - metoda w klasie field rysująca pasek w danym kolorze (gracza właściciela)
1.2 kupowanie domków (wojtek)
    - przycisk stawiający domek graczowi na danym polu
        - po kliknięciu wywołuje metodę z parametrem (player) - wiadomo gdzie stoi i można mu odjąć kasę (dodatkowa metoda w player)
        - sprawdza ile jest domków i wypisuje komunikat (lub nieaktywny przycisk) gdy nie da się kolejnego kupić
    - metoda rysująca domek na danym polu
        - na podstawie ilości domków zmienia się położenie kolejnego do narysowanie
        - trzeba oganąć dla 4 wariantów w zależności od boku planszy, na którym jest pole
    - pole z informacją o ilości domków
1.3 idzies do więdzienia
    $ - ogarnięcie wysowania graczy na polu więdzienie( odwiedzający i więźniowie)
    - parametr boolowski dla gracza, że jest w więzieniu
    *- wstrzymywanie kolejki ( dopiero jak będzie system od kolejki 2.3)
1.4 karty szans - wstęp (hubert)
    - jakaś struktura z treścią kart do losowania (najlepiej jakaś kolejka lub stos)
    - każda nowa gra losuje kolejność kart
    - po wylosowaniu karta ląduje na końcu/dnie struktury
    - na początek może być przycis od odkrywania kolejnych kart bez dodatkowych funkcji

1.5 poprawa sposobu wyświetlania graczy by było na podstawie pola position klasy player i była metoda odświeżania
    łątwiej wtedy będzie przenosić graczy np do więdzienia lub start

1.6 klasa message - ogarnąc żeby zapisywało do 10 ostatnich wiadomośc

===========================================

2.1 kupno hotelu
    - analogicznie do domku albo rozszerzenie metody z 1.2

2.2 karty szans - funkcjonalność
    - karta jest losowana po stanięciu na odpowiednim polu
        - metoda w klasie field(lub nowa klasa z dziedziczeniem po field z tą metodą) która wywołuje metodę pokazującą kartę
        - na podstawie karty dzieje się rzecz z zawartości ( może będą to odpowiednie metody w klasie od kart albo w klasie field)

*2.3 wstęp do AI (system zarządania kolejką graczy) - z gwiazdką bo może trzeba jeszcze wcześniej zacząć pisać tak ważną klasę
    - klasa (np system) mająca inforamację którego gracza jest kolej na ruch
    - wpływa ona metodami na widocznośc przycisków w zależności od kolejki i pola na którym stoją gracze

===========================================


3.1 handel posiadanymi polami (potrzebne już AI w miarę gotowe)
    - przycisk wywojący cały proces
    == do uzupełnienia później xd
3.2 lepsze grafiki
    - pola
    - tło
    - przyciski
3.3 muzyka
    #- ambient w menu
    #- muzyka podczas gry?
    - rzut kostą
    - skakania pionka
    - kupowanie pól
    - stawianie domków
    - klikanie przycisków
    - handel
    - przjście przez start
    - odkrywanie kart szans
    - wykrana/bankructwo

===========================================

#4.1 poziomy trudności ai
#4.2 opcje dla gracza
#4.3 responsywne okno
#4.4 "czy na pewno chcesz zakończyć grę?"