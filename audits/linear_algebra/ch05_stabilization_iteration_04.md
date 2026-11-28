# Algebra liniowa — rozdział 05: audyt stabilizacyjny IV (drugi czysty po korekcie)

**Data:** 22 listopada 2026.
**Rozdział:** \`chapters/pl/linear_algebra/05-eliminacja-gaussa-i-uklady-liniowe.tex\`.
**Identyczny SHA źródła w audytach III i IV:** \`c238cb3232b69fb19d0dfe1062af05a2a0d8ddb8\` — bez żadnych zmian w rozdziale.

## Nowa, niezależna kontrola matematyczna

1. **Elementarne operacje:** ponownie wyprowadzono je z macierzy jednostkowej \`I_m\`, wykazując obustronną odwracalność i składanie \`P=E_s...E_1\`. Sprawdzono, że ta sama macierz \`P\` działająca na \`[A|b]\` zachowuje dokładnie zbiór rozwiązań. Zwrócono uwagę, że obrazy \`A\` i \`PA\` nie muszą być identyczne, choć mają równy wymiar.
2. **Poprawność eliminacji:** algorytm kończy się po najwyżej \`n\` kolumnach, wybiera co najwyżej \`\min(m,n)\` pivotów, nie dzieli przez zero, zachowuje zerowanie wcześniejszych kolumn i potrafi odwracalnymi operacjami osiągnąć zarówno REF, jak RREF.
3. **Rząd i bazy:** dla REF rzut \(\ker U\to K^{n-r}\) na współrzędne swobodne jest dobrze określonym liniowym izomorfizmem. Dla RREF wektory wyznaczone przez \(-R_{if}\) tworzą niezależną bazę jądra. Dla obrazu tylko kolumny z **pierwotnej** \`A\` o indeksach pivotów tworzą żądaną bazę; sprawdzono pośrednictwo \`P^{-1}\`.
4. **Układy \(Ax=b\):** brak sprzecznego wiersza macierzy schodkowej jest równoważny znalezieniu rozwiązania przez podstawianie wstecz i warunkowi \(\operatorname{rk}[A|b]=\operatorname{rk}A\). Dla \(b\ne0\) zbiór rozwiązań zgodnego układu nie zawiera zera, więc **nigdy nie jest podprzestrzenią** — ten krok jest już jawnie uzasadniony w poprawionym źródle.
5. **Jednoznaczność RREF:** z przestrzeni wierszy \(H\) jednoznacznie odzyskuje się zbiór indeksów pivotowych jako pozycje pierwszych niezerowych współrzędnych wektorów \(H\). Wartości w kolumnach pivotowych jednoznacznie odzyskują wszystkie zredukowane wiersze, w tym przypadki rzędu 0.
6. **Odwracanie:** na macierzy \([A|I_n]\) stosujemy te same operacje, otrzymując \([PA|P]\); kryterium \`PA=I_n\` i obustronna odwracalność \`P\` dają \(P=A^{-1}\). Dokładnie zweryfikowano pełen rachunek liczbowy przykładu.

## Weryfikacja techniczna

- Przejrzano niezmienione **752 wiersze źródła**, 10 dowodów i 4 przykłady. Wszystkie 27 etykiet rozdziału 05 są różne; wśród 226 etykiet rozdziałów 01–05 nie ma kolizji. Wszystkie 16 odsyłaczy 05 prowadzą do istniejących celów. Stos środowisk LaTeX jest pusty po kontroli \`begin/end\`.
- Regresja nad \(\mathbb F_2,\mathbb F_3\): 1553 macierze, 12558 układów, porównanie różnych wyborów pivotów, wzory rzędu, pełne jądra i obrazy, ich bazy, kryterium zgodności i odwracalność — wszystkie PASS. Niezależna kontrola nad \(\mathbb Q\): 800 macierzy z porównaniem z SymPy, również PASS.
- Wydzielony z ostatniej poprawnej kompilacji dla wcześniejszego SHA PDF ma 7 stron bez problemów składu. Ponieważ w audycie II doprecyzowano jedno zdanie, **kontrola PDF wygenerowanego z nowego SHA musi zostać przeprowadzona osobno i nie może być zastąpiona wcześniejszym wynikiem**.
- Workflow dla nowego SHA (rozpoczęty jako [45006722306](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45006722306)) przechodzi kroki testowe, ale pełne końcowe \`SUCCESS\` należy potwierdzić po zakończeniu wszystkich kroków.

**Wynik:** druga czysta iteracja III–IV na identycznym źródle. **Status matematyczny: stabilny**. Ostateczne potwierdzenie techniczne wymaga wyniku końcowego CI i kontroli nowego PDF, co zostanie odnotowane w tabeli statusów.
