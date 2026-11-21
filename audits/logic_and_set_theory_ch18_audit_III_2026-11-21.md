# Logika matematyczna i teoria mnogości — rozdział 18 — audyt III

Data: 2026-11-21. Rozdział: **Reprezentowalność i diagonalizacja**.

## Zakres i wynik

Niezależna weryfikacja całego rozdziału po audycie II: wszystkie twierdzenia i ich przesłanki, dowody (szczególnie reprezentowalność w Q), definicje, przykłady, konstrukcja \(\beta\), predykat dowodu, formuła diagonalna, odsyłacze, terminologia polska i LaTeX. Zachowano niezmieniony zestaw wyników (2 twierdzenia, 5 lematów, 7 dowodów; 3 definicje, 4 przykłady i 3 uwagi).

## Stwierdzone usterki i naprawy

1. **Brak uzasadnienia przejścia z chwili \(j\) do \(j+1\) w dowodzie silnej reprezentowalności.** Warunek \(U\) gwarantuje jednoznaczność odczytu tylko przy indeksach nieprzekraczających \(t\). Dopisano osobny argument w \(Q\), że dla *ustalonego standardowego* \(j\) zachodzi \((\overline j<t)\to(\overline{j+1}\le t)\). Z (Q8) otrzymuje się \(t=z+S(\overline j)\); rozbicie (Q3) na \(z=0\) lub \(z=S(w)\) daje odpowiednio \(t=\overline{j+1}\) lub \(\overline{j+1}<t\). W ten sposób wolno stosować \(U\) również do następnego odczytu. Wszystkie rozwinięcia wykonywane są dla ustalonej liczby standardowej, bez postulowania indukcji w \(Q\).
2. **Niewypisany dowód wymuszenia kolejnej konfiguracji.** Wyjaśniono, że po podstawieniu numerałów rzeczywistej konfiguracji pojedynczą gałąź formuły \(S_e\) wyznaczają aksjomaty (Q1)–(Q7) i skończony rachunek na numerałach. Nie stosuje się ogólnej deterministyczności dla dowolnych niestandardowych danych bez uzasadnienia.
3. **Nienumerałowy zapis wyniku w formalnym predykacie dowodu.** W formule \(C_{V_T}\) zastąpiono argument zapisany jako \(1\) właściwym termem \(\overline1=S(0)\).
4. Poprawiono polskie sformułowanie odwołania do lematu.

Nie dodano żadnych nowych twierdzeń ani lematów. Nie zmieniono kodowania, definicji reprezentowalności ani zakresu rozdziału.

## Walidacja lokalna

- Po poprawkach kompilacja `latexmk -pdf` zakończyła się sukcesem: **7 stron rozdziału 18**, bez błędów i przepełnień `Overfull`.
- Rysunek diagonalizacji oraz strony z dowodem zostały skontrolowane w renderach; brak kolizji tekstu.
- **17/17 PASS**: osiem niezależnych testów audytu III oraz dziewięć testów audytu II wykonanych na nowej wersji. Kontrola arytmetyki standardowej ma charakter pomocniczy — **nie zastępuje formalnych dowodów wewnątrz \(Q\)**.
- **13 unikatowych etykiet, 29 odsyłaczy**, cele istnieją w rozdziałach 16–18. PDF samego rozdziału nie zawiera znaków nieznanych odsyłaczy.
- Cztery ostrzeżenia `undefined reference` w lokalnej kompilacji fragmentu *rozdziałów 16–18* dotyczą etykiet z wcześniejszych rozdziałów, których nie było w lokalnej składance. Nie są brakami w rozdziale 18.

**Status audytu III:** poprawki naniesione; wymagany niezależny audyt stabilizacyjny IV przed formalnym zamknięciem i wysłaniem na GitHuba.