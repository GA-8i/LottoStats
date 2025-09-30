import loteriaModule
import time

staty = loteriaModule.LottoStats()

dictOpcje = {"1" : staty.dodaj_Zaklad,
             "2" : staty.usun_Zaklad,
             "3" : staty.dodaj_Wygrana,
             "4" : staty.usun_Wygrana,
             "5" : staty.ile_razy,
             "6" : staty.popularna_liczba,
             "7" : staty.statystyki}
liOpcje = "1. Dodaj zakład\n2. Usuń zakład\n3. Dodaj wygraną\n4. Usuń wygraną\n5. Czy się powtarza?\n6. Najpopularniejsza liczba\n7. Wyświetl statystyki\n8. Wyłącz program\n"

while __name__ == '__main__':
    print("\nLottoStats to program zapisujący twoje statystyki w loterii lotto.\nUWAGA: Program obejmuje wyłącznie losy bez wybranego systemu (6 typowanych liczb)")
    staty.statystyki()

    while True:
        time.sleep(1)
        print(f"Komendy (wpisz numerek jeżeli chcesz wykonać).\n{liOpcje}")
        wykonaj = str(input("Numer: ")).strip()
        if wykonaj not in dictOpcje:
            if wykonaj == "8":
                print("\nDziękuje za korzystanie z programu LottoStats.")
                break
            else:
                print(f'\nNie znaleziono takiej komendy jak {wykonaj}\n')
        else:
            dictOpcje[wykonaj]()
    break