import loteriaModule

dictOpcje = {"1" : loteriaModule.dodaj_Zaklad,
             "2" : loteriaModule.usun_Zaklad,
             "3" : loteriaModule.dodaj_Wygrana,
             "4" : loteriaModule.usun_Wygrana,
             "5" : loteriaModule.ile_razy,
             "6" : loteriaModule.statystyki}
liOpcje = "1. Dodaj zakład\n2. Usuń zakład\n3. Dodaj wygraną\n4. Usuń wygraną\n5. Czy się powtarza?\n6. Wyświetl statystyki\n7. Wyłącz program\n"

while __name__ == '__main__':
    print("\nLottoStats to program zapisujący twoje statystyki w loterii lotto.\nUWAGA: Program obejmuje wyłącznie losy bez wybranego systemu (6 typowanych liczb)")
    loteriaModule.statystyki()

    while True:
        print(f"Komendy (wpisz numerek jeżeli chcesz wykonać).\n{liOpcje}")
        wykonaj = str(input("Numer: ")).strip()
        if wykonaj not in dictOpcje:
            if wykonaj == "7":
                print("\nDziękuje za korzystanie z programu LottoStats.")
                break
            else:
                print(f'\nNie znaleziono takiej komendy jak {wykonaj}\n')
        else:
            dictOpcje[wykonaj]()
    break