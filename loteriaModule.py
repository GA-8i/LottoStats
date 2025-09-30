import datetime
from collections import Counter
import json

class LottoStats:
    def __init__(self):
        self.wczesZaklady = []
        self.licz_zaklady = []
        self.Wygrane = []
        self.licz_wygrane = []

    def dodaj_dane_Zaklady(self):
        with open("dane_Zaklady.json", "w") as plik:
            json.dump(self.wczesZaklady, plik, indent=4)

    def odczytaj_dane_Zaklady(self):
        try:
            with open("dane_Zaklady.json", "r") as plik:
                self.wczesZaklady = json.load(plik)
                self.licz_zaklady = [
                    tuple(int(n) for n in wpis.split("dodany")[0].strip("()").split(","))
                    for wpis in self.wczesZaklady
                ]
        except FileNotFoundError:
            self.wczesZaklady = []
            self.licz_zaklady = []


    def dodaj_dane_Wygrane(self):
        with open("dane_Wygrane.json", "w") as plik:
            json.dump(self.Wygrane, plik, indent=4)

    def odczytaj_dane_Wygrane(self):
        try:
            with open("dane_Wygrane.json", "r") as plik:
                self.Wygrane = json.load(plik)
                self.licz_wygrane = [
                    float(wpis.split("zł")[0]) for wpis in self.Wygrane
                ]
        except FileNotFoundError:
            self.Wygrane = []
            self.licz_wygrane = []

    def popularna_liczba(self):
        if not self.licz_zaklady:
            print("\nBrak zakładów do analizy!\n")
        else:
            liczby = [num for zaklad in self.licz_zaklady for num in zaklad]
            licznik = Counter(liczby)
            topka = licznik.most_common(3)
            print('\nTwoje top 3 najpopularniejsze liczby w zakładach: ')
            for i, (liczba, ile) in enumerate(topka, 1):
                print(f"{i}. {liczba} - pojawia się {ile} razy\n")
    
    def dodaj_Zaklad(self):
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
            wpis = (f'{nowyZaklad} dodany {dataDodania}')
            self.wczesZaklady.append(wpis)
            self.licz_zaklady.append(nowyZaklad)
            self.dodaj_dane_Zaklady
            self.odczytaj_dane_Zaklady()
            print("Pomyślnie dodano zakład do listy twoich zakładów.\n")
            break

    def usun_Zaklad(self):
        self.disp_wczes_zaklady()
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
            if doUsun in self.wczesZaklady:
                self.wczesZaklady.remove(doUsun)
                self.licz_zaklady.remove(usun)
                self.odczytaj_dane_Zaklady()
                
                print("Pomyślnie usunięto zakład z listy twoich zakładów.\n")
                break
            else:
                print(f"\nBrak takiego zakładu jak '{usun}' z dnia '{Data}' na liście twoich zakładów\n")
                break

    def oblicz_wydane_Pieniadze(self):
        ilosc_zakladow = len(self.wczesZaklady)
        straty = ilosc_zakladow * 3
        return straty

    def dodaj_Wygrana(self):
        while True:
            try:
                wygrana = float(input("\nGratulacje!\nWysokość twojej wygranej (zł): ").strip())
            except ValueError:
                print("\nWygrana musi być podana liczbowo.\n")
                continue
            else:
                dataDodania = datetime.datetime.now().strftime("%x")
                self.Wygrane.append(f'{wygrana}zł dodane {dataDodania}')
                self.licz_wygrane.append(wygrana)
                self.dodaj_dane_Wygrane()
                self.odczytaj_dane_Wygrane()
                print("Pomyślnie dodano wygraną do listy twoich wygranych.\n")
                break

    def oblicz_zyskane_Pieniadze(self):
        zyski = sum(self.licz_wygrane)
        return zyski
        
    def usun_Wygrana(self):
        self.disp_wygrane()
        while True:
            try:
                usun = float(input("Podaj wygraną którą chcesz usunąć (zł): "))
            except ValueError:
                print("\nWygrana musi być podana liczbowo.\n")
                continue
            Data = input("Podaj datę dodania tej wygranej (MM/DD/YY): ").strip()
            doUsun = (f'{usun}zł dodane {Data}')
            if doUsun in self.Wygrane:
                self.Wygrane.remove(doUsun)
                self.licz_wygrane.remove(usun)
                self.odczytaj_dane_Wygrane()
                print("Pomyślnie usunięto wygraną z listy twoich wygranych.\n")
                break
            else:
                print(f"\nBrak takiej wygranej jak '{usun}' z dnia '{Data}' na liście twoich wygranych\n")
            break

    def ile_razy(self):
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

            razy = self.licz_zaklady.count(powtarza)
            print(f'Zakład {powtarza} powtarza się {razy} razy.\n')
            if razy >= 5:
                print("Wow! Naprawdę musisz lubić te liczby. ;)\n")
            break

    def oblicz_Zysk(self):
        Zysk = self.oblicz_zyskane_Pieniadze() - self.oblicz_wydane_Pieniadze()
        if Zysk >= 0:
            print(f'\nW loterii Lotto zyskałeś łącznie {Zysk}zł.\n')
        else:
            print(f'\nW loterii Lotto straciłeś łącznie {Zysk}zł. :(\n')

    def disp_wczes_zaklady(self):
        print("\nTwoje zakłady:")
        if self.wczesZaklady == []:
            print('Jeszcze nic tu nie ma!\n')
        else:
            for x in self.wczesZaklady:
                print(f'- {x}')
            print('\n')

    def disp_wygrane(self):
        print("\nTwoje wygrane:")
        if self.Wygrane == []:
            print('Jeszcze nic tu nie ma!\n')
        else:
            for x in self.Wygrane:
                print(f'- {x}')
            print('\n')

    def statystyki(self):
        print("\nTWOJE STATYSTYKI:\n")
        self.disp_wczes_zaklady()
        self.disp_wygrane()
        self.oblicz_Zysk()