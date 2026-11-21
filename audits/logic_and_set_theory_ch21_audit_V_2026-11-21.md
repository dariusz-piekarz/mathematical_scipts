# Logika matematyczna i teoria mnogości — rozdział 21, audyt V

Data: 21 listopada 2026 r.
Źródło: `chapters/pl/logic_and_set_theory/21-operacje-na-dowodach-i-warunki-wyprowadzalnosci.tex`, blob `f28e89efccf8e349001d9c0b44c0dc0c1a9064de`.
Tryb: kolejna kontrola **istniejących** wyników, bez dodawania twierdzeń, lematów lub przykładów.

## Kontrola matematyczna

1. Kodowanie ciągu `β`: wybór `b'=(n+1)!(R+1)` zapewnia `r_i<m_i` i parami względną pierwszość `m_i=1+(i+1)b'`. Uzasadniono, dlaczego wspólny dzielnik musi dzielić `j-i`, a następnie być równy 1. Przy `n=0` konstrukcja nadal ma sens.
2. Zmienna liczba kongruencji: użyta indukcja w PA i algorytm CRT są opisane, bez niejawnego przeniesienia argumentu do Q.
3. Totalność funkcji pierwotnie rekurencyjnych: krok rekursji prostej zawiera kodowanie wartości i indukcję PA; przypadek kompozycji oraz dowodliwa jednoznaczność są jawne.
4. Formalizacja modus ponens: przepisanie i przesunięcie indeksów, poprawność certyfikatów oraz indukcyjny niezmiennik są podane. Słusznie ograniczono twierdzenie o pierwotnie rekurencyjnym czasie do **wybranej konstrukcyjnej realizacji** weryfikatora.
5. (D2): z wewnętrznej implikacji dla dowolnych kodów i dowodliwej totalności operacji przechodzi się poprawnie do trzech kwantyfikatorów egzystencjalnych i zdania o dowodliwości.
6. Sformalizowana prawdziwość `Δ₀`: sprawdzono osobno obie polaryzacje kompilatora, obliczanie wartości termu ograniczenia, pusty przedział i zamianę `u≤t` na `u<t` plus przypadek równości; wskazano indukcję PA dla zmiennej liczby instancji.
7. Sformalizowana `Σ₁`-zupełność i (D3): formalne dołączenie świadków i podstawienie kodu zdania `Bew_T(⌜φ⌝)` uzasadnia żądaną implikację.
8. Zachowane rozróżnienie kodu dowodu i rzeczywistego dowodu; jawnie wykluczono nieuprawniony wniosek `□φ→φ`.

## Status

- W tej kontroli **nie wykryto nowej usterki w istniejących dowodach**. Tekst rozdziału 21 pozostawiono bez zmian.
- Inwentarz: 2 twierdzenia, 5 lematów, 7 dowodów, 3 przykłady, 4 uwagi; 8 etykiet, 20 odsyłaczy.
- Weryfikacja skryptowa w repozytorium obejmuje `tools/tests/test_logic_and_set_theory_ch21.py`; końcowy wynik bieżącego GitHub CI wymaga osobnego potwierdzenia.
- W tej iteracji nie wykonywano lokalnej kompilacji i nie weryfikowano wizualnie PDF; wcześniejszy audyt IV zgłosił poprawny sześciostronicowy podgląd.
