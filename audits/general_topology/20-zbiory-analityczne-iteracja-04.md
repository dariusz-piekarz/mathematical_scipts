# Topologia ogólna — rozdział 20, audyt 04 (korekta kodowania zbioru uniwersalnego)

**Data:** 2026-11-22. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Plik źródłowy:** `chapters/pl/general_topology/20-zbiory-analityczne-i-operacja-suslina.tex`.
**Blob wejściowy:** `c7644dae32a49ae9ac1403f4932018d440586e9b`.
**Blob po poprawce:** `2607376331f94935063107dee49148b45cc1679f`.
**Wynik audytu 04:** **NIECZYSTY — błąd poprawności dowodu twierdzenia o nieborelowskim zbiorze analitycznym, poprawiony w źródle**.
**Licznik stabilizacji:** **0/2** czystych audytów od najnowszej zmiany. Kolejny audyt musi niezależnie zweryfikować nowy blob.

## 1. Problem krytyczny — wadliwe kodowanie zbioru uniwersalnego

W dowodzie Lematu `lem:topog20-universal` kod drzewa par skończonych prefiksów `(s,t)` był zadany przez predykat `c_{e(s,t)}>0`, przy `c\in\mathcal N=\mathbb N^{\mathbb N}`.
Skrypt używa indeksów naturalnych od 1 i jawnie odróżnia `\mathbb N_0=\{0,1,2,\dots\}`, więc przy naturalnej konwencji `\mathbb N=\{1,2,\dots\}` **każda** współrzędna `c` jest dodatnia. Poprzedni predykat był wtedy tautologią: dla każdego kodu `c` zbiór `H_c` był całym `\mathcal N^2`, nawet gdy kod miał odpowiadać pustemu `F`.
Nie jest to detal redakcyjny: zanikała uniwersalność `U`, więc dowód diagonalny Twierdzenia `thm:topog20-nonborel` nie miał podstawy.

**Poprawka:** przyjęto kod wartościami `1` i `2` (obie należą do `\mathbb N` niezależnie od przyjęcia zera jako liczby naturalnej):
- `c_{e(s,t)}=1` wtedy i tylko wtedy, gdy `(s,t)` należy do kodowanego drzewa;
- `c_{e(s,t)}=2` w przeciwnym przypadku;
- definicja `H` wymaga `c_{e(x|n,y|n)}=1` dla każdego `n\ge1`.

Po tej zmianie argument jest poprawny: dla domkniętego `F\subseteq\mathcal N^2` drzewo `T_F` składa się z dokładnie tych równodługich prefiksów, których cylindry przecinają `F`. Gdy wszystkie prefiksy pary `(x,y)` należą do `T_F`, wybieramy punkty `(x_n,y_n)\in F\cap([x|n]\times[y|n])`. Zbieżność do `(x,y)` i domkniętość `F` dowodzą, że `(x,y)\in F`. W drugą stronę każdy punkt `F` ma wszystkie prefiksy w `T_F`. Zatem przekrój `H_c=F`, a `U_c=\pi_1(F)`.

**Commity:**
- [93c9929](https://github.com/dariusz-piekarz/mathematical_scipts/commit/93c9929ec1d7f35f24f65dcd414c3b4fc196e50c) — poprawa matematycznego kodowania w rozdziale;
- [1472998](https://github.com/dariusz-piekarz/mathematical_scipts/commit/14729987a729b894821bdc0bfbff25f3aa28929c) — test regresyjny kodowania drzewa przez dwie dodatnie wartości.

## 2. Niezależny przegląd pozostałych argumentów

1. **Surjekcja `\mathcal N\to X`:** konstrukcja domkniętych pokryć `F_s` daje niepuste następniki, kontrolę średnicy i surjekcję; w dowodzie nie potrzeba zwartości. Przypadek pustej przestrzeni jest wyłączony w sformułowaniu.
2. **Rzuty domkniętych:** dla niepustego `A` graf ciągłego odwzorowania jest domknięty w iloczynie; w drugą stronę niepusty domknięty podzbiór polskiego produktu jest polski i jest ciągłym obrazem `\mathcal N`. Pusty przypadek jest osobny.
3. **Zamknięcie analitycznych na przeliczalne sumy i przecięcia:** kody świadków `\mathbb N\times\mathcal N` oraz `\mathcal N^{\mathbb N}` dają przestrzenie homeomorficzne do `\mathcal N`; domkniętość przez otwarto-domknięte włókna i przeciwobrazy domkniętych; wybór przeliczalnych świadków mieści się w ZFC.
4. **Obrazy i przeciwobrazy ciągłych odwzorowań:** kompozycja obrazów oraz produktowy przeciwobraz domkniętego zbioru świadków poprawne.
5. **Borelowskie są analityczne i koanalityczne:** `\sigma`-algebra wspólnych klas, otwarte typu `F_\sigma` w metryzowalnej przestrzeni i domknięte polskie podprzestrzenie, bez kołowego argumentowania.
6. **Zgodność z definicją przez rzut borelowski:** zakodowanie `\mathcal N` w zbiorze `G_\delta` przestrzeni Cantora, osadzenie trójkowe w prostej i użycie domkniętości względnej dają borelowski rzut w `\mathbb R^{n+1}`; poprawne także dla zbioru pustego.
7. **Operacja Suslina:** domkniętość zbioru par `(x,\alpha)` przez rozkład przestrzeni Baire'a na cylindry i odtworzenie punktu z domkniętego `H` przy pomocy zgodnych prefiksów — poprawne.
8. **Przekątniowanie:** po naprawieniu kodowania `U` uniwersalność jest uzasadniona; nieanalityczność `D=` `\{x:(x,x)\notin U\}` daje nieborelowskość jego analitycznego dopełnienia `E`.
9. **Granice zakresu:** tekst nie podaje uniwersalnej mierzalności ani twierdzenia o rozdzielaniu jako udowodnionych; nie powtarza teorii gier rozdziału 30 skryptu logiki.

## 3. Testy, LaTeX i stan CI

Dodano model regresyjny `universal_tree_coding_models()`: dla skończonych drzew kodowanych wyłącznie wartościami `1` oraz `2` odtworzony zbiór gałęzi ma dokładnie podaną relację; osobno sprawdzany jest przypadek pusty i pełny. Dodatkowe asercje w pliku testowym pilnują występowania predykatu `=1` i definicji wartości `2`, a nie `>0`.
Niezależny model skończony o tym samym znaczeniu sprawdzono w 130 przypadkach, włącznie z pustym i pełnym: PASS. Jest to kontrola skończona, **nie** formalny dowód twierdzenia dla nieskończonych ciągów.
Nie zmieniono etykiet, odsyłaczy, spisu treści, plików graficznych ani zależności książki.

Poprzednia poprawka źródła (`c7644dae...`) ma udane [CI 45023273463](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023273463), ale ten wynik **nie** weryfikuje aktualnego kodowania. Nowa walidacja `general topology`, [run 45040786110](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45040786110), była **in_progress** w momencie kontroli. Nie deklaruje się sukcesu dla bieżącego bloba bez zakończonego wyniku i oględzin jego PDF. Brak lokalnego pobrania PDF do samodzielnego przeglądu wizualnego po tej zmianie.

## 4. Status

**Rozdział 20: OTWARTY (0/2).** Audyt 04 zmienił krytyczną część dowodu, dlatego licznik czystych audytów jest zerowany. Następny krok to **audyt 05** na nowym blobie, obejmujący ponowną niezależną weryfikację kodowania, diagonalizacji i CI. Nie rozpoczynać rozdziału 21 przed stabilizacją rozdziału 20. Opcjonalne rozszerzenia (np. własność zbioru doskonałego) wymagają odrębnej decyzji użytkownika, nie są częścią tego audytu.
