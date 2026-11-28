# AA-51 — audyt III: domknięcie realizowalności sygnatur

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.

## Kontrola niezależna

W bieżącym środowisku wykonano rzeczywiste obliczenia Python/SymPy dla phi=(1+sqrt(5))/2, v=(0,1,phi), w_0=(0,-1,phi), w_1=(phi,0,1), w_2=(1,phi,0), w_3=(-1,phi,0), w_4=(-phi,0,1). B=(v,w_0,w_1), C=(v,w_1,w_2), R=CB^{-1}. Otrzymano det B=3+sqrt(5)=2phi², det R=1, a dokładna macierz R ma wiersze ((sqrt(5)-1)/4, -(sqrt(5)+1)/4, 1/2), ((sqrt(5)+1)/4, 1/2, (sqrt(5)-1)/4), (-1/2,(sqrt(5)-1)/4,(sqrt(5)+1)/4). Sprawdzono symbolicznie R^T R=I, pięć tożsamości Rw_i=w_(i+1 mod 5), R^5=I i wzór na det B. Proces zakończył się kodem 0. Nie jest to dowód ogólnej klasyfikacji ani zastępstwo pełnych regresji.

## Poprawki

Commit db7c0bff485f6ce7ea88c3eaf84048d449712a24, blob 99df945251c91241f6b9c996142b146c889a0b49. Ponowny odczyt z gałęzi potwierdził blob.
- Usunięto pozostałość odwołania do okręgu z pierwotnego dowodu. Wykazano jawnie, że odwzorowanie Q -> Qw_0 jest iniekcją ze stabilizatora v do pięcioelementowego zbioru: obrót ustalający dwa niezależne wektory jest identycznością.
- Uzupełniono rachunek działania diagonalnej macierzy SU(2) na współrzędną x+iy.
- Dodano uwagę dowodzącą realizowalności każdej sygnatury, a nie tylko istnienia abstrakcyjnych typów grup; dla A4, S4, A5 wykluczono typy cykliczny i dwuścienny poprzez rzędy elementów. Dla D2 doprecyzowano trzy orbity dwupunktowe.
- Nie zmieniono wcześniejszych rozdziałów ani zakresu AA-51.

## CI

Uruchomienie po audycie II: 45295683486, job 138115334419, in_progress przy odczycie. Terminologia na tym samym commicie ae70f8a654a77d220a9cb7e2695cec11a9594a4b: success (run 45295683476). Nowy commit źródła db7c0bff485f6ce7ea88c3eaf84048d449712a24: przy pierwszym odczycie listy uruchomień nie zwrócono jeszcze wyników. Nie przypisujemy mu sukcesu. PDF po poprawkach nie został sprawdzony.

## Werdykt

AA-51 W AUDYCIE: domknięto powyższe argumenty, potrzebny aktualny pełny CI oraz oględziny stron PDF. AA-52 nieotwarty.
