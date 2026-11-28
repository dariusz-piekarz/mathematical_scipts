# Algebra liniowa — globalny audyt 37: dodatkowy niezależny audyt sceptyczny całej książki (zamknięcie)

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Status:** +1, BEZ USTEREK; niezależny audyt końcowy po dwóch czystych globalnych iteracjach [35](iteration_35.md) i [36](iteration_36.md).

## Stabilne, rzeczywiście zweryfikowane źródła

Przed rozpoczęciem kontroli sprawdzono aktualną gałąź i cztery zmieniane przy eliminacji ostrzeżeń bloby: LA-13 `ddf705004f13f4df7289036d82c13ff64fe89f56`, LA-22 `735db5c063d9ac9c148894a8ffdcc681339e9611`, LA-23 `0a79284e9d1f0db121800c733ab1fd2cecf0bf5c` oraz LA-32 `9ed35f18a5300f6e9ee70e8654ef0092e260af2f`. **Żaden nie zmienił się od audytów 35 i 36.** W audycie 37 nie edytowano matematyki, dowodów, wykresów ani etykiet.

## Niezależna ewidencja wszystkich dowodów

Ponownie przetworzono **32 rzeczywiste pliki źródłowe z artefaktu finalnego CI**, a nie tylko historyczne deklaracje w `status.md`. Policzone liczby domkniętych dowodów według rozdziałów:

| Rozdziały | Liczba `\\begin{proof}` w kolejności |
|---|---|
| 01–08 | 24, 16, 17, 15, 10, 11, 20, 14 |
| 09–16 | 14, 20, 19, 13, 15, 17, 13, 12 |
| 17–24 | 7, 6, 7, 7, 9, 10, 7, 8 |
| 25–32 | 17, 9, 10, 10, 6, 3, 6, 10 |

Suma: **382/382**, dla każdego rozdziału liczba zakończeń `\\end{proof}` odpowiada liczbie rozpoczęć, bez przypadku niezbilansowanego. W poprzednich iteracjach globalnych 1–33 zarejestrowano merytoryczne odczytanie tych dowodów, w szczególności ostatnich dziesięciu z LA-32 w audycie 33. Skończona kontrola struktury nie jest dowodem twierdzeń i nie może tego udawać.

## Niezależny test integralności i zależności między rozdziałami

W `books/pl/linear_algebra.tex` znajduje się dokładnie **32** instrukcje `\\input`, każda do istniejącego pliku i dokładnie w porządku 01–32 bez duplikatów. Zbadano w całej książce **1083/1083 unikalne etykiety** i **660/660 rozwiązywanych `\\ref`/`\\eqref`** (0 braków). Prześledzono w szczególności:
- LA-13 → LA-09 i LA-12: formy, ortogonalność i iloczyny skalarne, odpowiednio 2 i 4 odsyłacze;
- LA-22 → LA-16–21: elementy nilpotentne, postać Jordana, pierwotne podprzestrzenie i operator Sylvestera (12 odsyłaczy zewnętrznych);
- LA-23 → LA-14, LA-17, LA-18 i LA-22: kryterium Schura, potęgi bloków i rozwiązania równań Stein (5 odsyłaczy zewnętrznych);
- LA-29 → LA-10 i LA-11: własności iloczynu zewnętrznego i Plückera (8);
- LA-30 → LA-11: relacje Clifforda i algebry zewnętrznej (7);
- LA-31 → LA-29 i LA-30: spinory i geometria Grassmannianów (9);
- LA-32 → LA-29 i LA-31: incydencja, kwadryka Kleina i spinory (4).

Wszystkie cele znaleziono w konkretnej, aktualnej kanonicznej książce. Nie zmieniano ich nazw. Jednocześnie zweryfikowano, że zamiana trzech `\\choose` na `\\binom` nie zmieniła pojęć, kwantyfikatorów, granic sumowania ani założeń `k=a+b-1`. Przeanalizowano szczególnie przykład kwaternionowej fibracji LA-32 i lokalne warunki użycia transformaty Penrose'a; wynik kohomologiczny nie jest fałszywie przedstawiony jako udowodniony.

## Dodatkowe niezależne regresje i potwierdzony skład

Powtórnie uruchomione po ostatniej edycji zestawy dokładne:
- **853/853** (nilpotentność, LA-22), **544/544** (potęgi Jordana LA-23),
- **7019/7019** (LA-32, wyznaczniki, incydencja, Plücker, Penrose, kwaterniony),
- **6603/6603** (odrębny wyczerpujący model `M₂(F₃)`: incydencja, Segre i flagi),
- **13799/13799** (projekcje LA-13, `J` i stereografia LA-32).
Są to kontrole różnych tożsamości matematycznych, a nie niezależne dowody wszystkich twierdzeń skryptu.

**[CI 45133440134](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45133440134): completed/success**, commit `3774f90a56fce37490cb795b381338586984c5c0`. Sprawdzono osobno kroki testów, ochronę przed modyfikacją źródeł przez testy, dwukrotny skład PDF i rygorystyczną kontrolę końcowego logu. Artefakt książki i kompletu źródeł: `linear-algebra-ch01-ch32`, ID `14799410071`.

W rzeczywistym PDF (320 stron, SHA256 `c9cfb86da685609100793c0eae7b13069fa8edb8a695cbe86556e219f68065b8`) zidentyfikowano **32** odpowiadające rozdziałom zakładki najwyższego poziomu oraz **261** zakładek ogółem. Strony LA-13 zaczynają się na PDF 132, LA-22 na 214, LA-23 na 222, LA-32 na 312. Oddzielnie sprawdzono układ stron 130, 134, 137, 223, 226, 231, 312, 315, 317, 319, w tym rysunki Penrose'a i twistorowej fibracji, bez widocznych kolizji; kontrola programowa wszystkich 320 stron wykazała 0 bloków tekstu poza stroną. Końcowy log ma **0** ostrzeżeń `LaTeX` lub `Package`, 0 `Overfull`/`Underfull`, 0 `Missing character`, 0 niezdefiniowanych referencji i błędów. Usunięto łącznie 8 problemów `hyperref` i trzy przestarzałe wystąpienia `\\choose` w LA-22/23.

## Werdykt i reguła zatrzymania

**GLOBALNY AUDYT AL: STABILNY / ZAMKNIĘTY.** Przyjęte kryterium zostało spełnione: (i) 382/382 dowodów ujętych w pełnej ewidencji i audytach per-rozdziałowych; (ii) ostatnie modyfikacje źródeł audytowane w dwóch odrębnych czystych przebiegach 35–36 na niezmienionych blobach; (iii) dodatkowy krytyczny audyt 37 bez nowych usterek; (iv) rzeczywisty CI z testami, źródłami, PDF i logiem ma wynik SUCCESS. Ewentualne przyszłe kontrole powiązań z innymi tomami są odrębną pracą i nie powinny powodować resetowania zamkniętego zakresu bez konkretnego błędu.

Zamknięcie jest zgodne z przyjętym procesem jakości, **nie jest formalnym sprawdzeniem w Lean** wszystkich twierdzeń. Nie rozpoczynać kolejny raz reaudytu od LA-12 ani nie dodawać LA-33 bez nowej decyzji.
