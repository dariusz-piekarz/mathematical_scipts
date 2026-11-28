# Algebra liniowa — rozdział 07, audyt 2 (korekty)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/07-przestrzen-dualna-i-odwzorowania-dualne.tex`

## Wykryte kwestie i poprawki

1. **Doprecyzowanie podwójnego anihilatora.** Poprzednia redakcja dowodu `(S_∘)^∘=S` zawierała niejasną identyfikację przestrzeni, w której brany jest anihilator, oraz odsyłacz do bidualności udowodnionej później. Zastąpiono ją niezależnym dowodem: dla bazy `φ_1,...,φ_s` przestrzeni `S` zastosowano liniowe odwzorowanie `L:V→K^s, v↦(φ_i(v))`. Wykazano jego surjektywność przez sprzeczność z niezależnością funkcjonałów i otrzymano `dim S_∘=n-s`; stąd inkluzja i wymiar dowodzą równości. Uwzględniono `s=0`.
2. **Błąd składu PDF.** GitHub Actions w przebiegu [44910869186](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44910869186) wykrył `Overfull \\hbox (20.34161pt too wide)` w okolicach wierszy 551–571, w dowodzie rozszerzania funkcjonału. Usunięto długi zapis bazy z jednego wiersza matematycznego i rozdzielono go na krótszy tekst i zakres wektorów. Wynik kompilacji PDF był poprawny, ale ścisły test ostrzeżeń zasadnie oznaczył poprzedni CI jako nieudany.
3. **Sprawdzono rachunki przykładów.** Baza dualna nad `R^2`, przykład działania `T^*` o wyniku `(6,5)`, anihilator płaszczyzny `x+2y-z=0` oraz ślad odwzorowania rzędu co najwyżej jeden zostały sprawdzone bez nowych błędów.
4. **Testy skończonych ciał.** Równość rzędów `rank A^T=rank A`, cykliczność śladu `tr(AB)=tr(BA)` oraz zgodność odwracalności z niezerowym wyznacznikiem przetestowano dla wszystkich **262144** par macierzy `3×3` nad `F_2` i **6561** par macierzy `2×2` nad `F_3`; brak rozbieżności. Formułę podwójnego anihilatora sprawdzono przez enumerację wszystkich **16** podprzestrzeni `F_2^3` oraz **6** podprzestrzeni `F_3^2`; brak rozbieżności.
5. **Spójność biblioteki.** Przed korektą sprawdzono 303 unikalne etykiety i 128 istniejących celów odsyłaczy w rozdziałach 01–07; kolejność w katalogu zgadza się z `\\input` w pliku książki.

## Status

Korekty zmieniają dowód i skład, dlatego rozdział **pozostaje otwarty**. Nowa kompilacja i co najmniej jeden czysty audyt stabilizacyjny są konieczne przed zamknięciem.
