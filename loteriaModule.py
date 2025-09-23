import datetime

wczesZaklady = []
licz_zaklady = []
Wygrane = []
licz_wygrane = []

def dodaj_Zaklad():
    global wczesZaklady
    while True:
        try:
            nowyZaklad = (input("\nWybierz swoje liczby (wymień po przecinku): ")).split(",")
            nowyZaklad = [int(x.strip()) for x in nowyZaklad]
        except ValueError:
            print("\nMożna typować tylko liczby (w zakresie od 1 do 49 włącznie).")
            continue

        nowyZaklad = tuple(sorted(set(nowyZaklad)))
        if any(x < 1 or x > 49 for x in nowyZaklad):
            print('\nWybrane liczby muszą znajdować się w zakresie od 1 do 49 włącznie.')
            continue
        if len(nowyZaklad) != 6:
            print("\nPrzy braku wybranego systemu zakładów trzeba wybrać dokładnie 6 liczb.\nLiczby nie mogą się powtarzać.")
            continue

        dataDodania = datetime.datetime.now().strftime("%x")
        wczesZaklady.append(f'{nowyZaklad} dodany {dataDodania}')
        licz_zaklady.append(nowyZaklad)
        print("Pomyślnie dodano zakład do listy twoich zakładów.\n")
        break


def usun_Zaklad():
    global wczesZaklady
    disp_wczes_zaklady()
    while True:
        try:
            usun = input("Podaj zakład który chcesz usunąć: ").split(",")
            usun = [int(x.strip()) for x in usun]
        except ValueError:
            print("\nMożna typować tylko liczby (w zakresie od 1 do 49 włącznie).")
            continue

        usun = tuple(sorted(set(usun)))
        if any(x < 1 or x > 49 for x in usun):
            print('\nWybrane liczby muszą znajdować się w zakresie od 1 do 49 włącznie.')
            continue
        if len(usun) != 6:
            print("\nPrzy braku wybranego systemu zakładów trzeba wybrać dokładnie 6 liczb.\nLiczby nie mogą się powtarzać.")
            continue

        Data = input("Podaj datę dodania tego zakładu (MM/DD/YY): ").strip()
        doUsun = (f'{usun} dodany {Data}')
        if doUsun in wczesZaklady:
            wczesZaklady.remove(doUsun)
            licz_zaklady.remove(usun)
            print("Pomyślnie usunięto zakład z listy twoich zakładów.\n")
            break
        else:
            print(f"\nBrak takiego zakładu jak '{usun}' z dnia '{Data}' na liście twoich zakładów\n")
            break

def oblicz_wydane_Pieniadze():
    ilosc_zakladow = len(wczesZaklady)
    straty = ilosc_zakladow * 3
    return straty

def dodaj_Wygrana():
    global Wygrane
    global licz_wygrane
    while True:
        try:
            wygrana = float(input("\nGratulacje!\nWysokość twojej wygranej (zł): ").strip())
        except ValueError:
            print("\nWygrana musi być podana liczbowo.\n")
            continue
        else:
            dataDodania = datetime.datetime.now().strftime("%x")
            Wygrane.append(f'{wygrana}zł dodane {dataDodania}')
            licz_wygrane.append(wygrana)
            print("Pomyślnie dodano wygraną do listy twoich wygranych.\n")
            break

def oblicz_zyskane_Pieniadze():
    global licz_wygrane
    zyski = sum(licz_wygrane)
    return zyski
    
def usun_Wygrana():
    global Wygrane
    disp_wygrane()
    while True:
        try:
            usun = float(input("Podaj wygraną którą chcesz usunąć (zł): "))
        except ValueError:
            print("\nWygrana musi być podana liczbowo.\n")
            continue
        Data = input("Podaj datę dodania tej wygranej (MM/DD/YY): ").strip()
        doUsun = (f'{usun}zł dodane {Data}')
        if doUsun in Wygrane:
            Wygrane.remove(doUsun)
            licz_wygrane.remove(usun)
            print("Pomyślnie usunięto wygraną z listy twoich wygranych.\n")
            break
        else:
            print(f"\nBrak takiej wygranej jak '{usun}' z dnia '{Data}' na liście twoich wygranych\n")
        break

def ile_razy():
    global licz_zaklady
    while True:
        try:
            powtarza = (input("\nPodaj liczby, na które chcesz sprawdzić ile razy już postawiłeś: ")).split(",")
            powtarza = [int(x.strip()) for x in powtarza]
        except ValueError:
            print("\nMożna typować tylko liczby (w zakresie od 1 do 49 włącznie).")
            continue

        powtarza = tuple(sorted(set(powtarza)))
        if any(x < 1 or x > 49 for x in powtarza):
            print('\nWybrane liczby muszą znajdować się w zakresie od 1 do 49 włącznie.')
            continue
        if len(powtarza) != 6:
            print("\nPrzy braku wybranego systemu zakładów trzeba wybrać dokładnie 6 liczb.\nLiczby nie mogą się powtarzać.")
            continue

        razy = licz_zaklady.count(powtarza)
        print(f'Zakład {powtarza} powtarza się {razy} razy.\n')
        if razy >= 5:
            print("Wow! Naprawdę musisz lubić te liczby. ;)\n")
        break

def oblicz_Zysk():
    Zysk = oblicz_zyskane_Pieniadze() - oblicz_wydane_Pieniadze()
    if Zysk >= 0:
        print(f'\nW loterii Lotto zyskałeś łącznie {Zysk}zł.\n')
    else:
        print(f'\nW loterii Lotto straciłeś łącznie {Zysk}zł. :(\n')

def disp_wczes_zaklady():
    global wczesZaklady
    print("\nTwoje zakłady:")
    if wczesZaklady == []:
        print('Jeszcze nic tu nie ma!\n')
    else:
        for x in wczesZaklady:
            print(f'- {x}')
        print('\n')

def disp_wygrane():
    global Wygrane
    print("\nTwoje wygrane:")
    if Wygrane == []:
        print('Jeszcze nic tu nie ma!\n')
    else:
        for x in Wygrane:
            print(f'- {x}')
        print('\n')

def statystyki():
    print("\nTWOJE STATYSTYKI:\n")
    disp_wczes_zaklady()
    disp_wygrane()
    oblicz_Zysk()
