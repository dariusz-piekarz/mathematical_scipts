# Topologia ogólna — rozdział 20, audyt 07 (dodatkowy audyt po stabilizacji)

**Data:** 2026-11-22. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Badany rozdział:** `chapters/pl/general_topology/20-zbiory-analityczne-i-operacja-suslina.tex`.
**Blob:** `2607376331f94935063107dee49148b45cc1679f` — identyczny jak w audytach 05 i 06.
**Wynik:** **CZYSTY (3/2)**, w tym dodatkowy audyt po uzyskaniu stabilności. Nie zmieniano matematycznej treści rozdziału.

## Kontrola granicznych przypadków i powiązań twierdzeń

- **Przestrzeń pusta i zbiór pusty:** parametryzacja przez `\mathcal N` wymaga niepustej przestrzeni polskiej, lecz definicja analitycznego obejmuje `\varnothing`; równoważności z domkniętymi rzutami, operacją Suslina i zamknięciem na przeliczalne działania zachowują ten wyjątek.
- **Zbieżność na gałęziach:** malejące niepuste domknięte `F_{\alpha|k}` o średnicach `\to0` w zupełnej metryce mają dokładnie jeden wspólny punkt. Zbieżność `u_n\to\alpha` w charakterystyce Suslina wynika bez metryki Baire’a wprost ze zgodności prefiksów.
- **Analytic vs. Borel:** dowód zamknięcia analitycznych na przecięcia przeliczalne stosuje wybór przeliczalny, jawnie dozwolony w ZFC. Nie deklaruje zamknięcia na dopełnienia. Wniosek `\mathrm{Borel}(X)\subseteq\mathrm{Analityczne}(X)\cap\mathrm{Koanalityczne}(X)` jest jednokierunkowy.
- **Kodowanie drzew:** wszystkie wartości kodu `c_{e(s,t)}` należą do `\{1,2\}\subseteq\mathbb N`. Dla `F=\varnothing` nie ma akceptowanych gałęzi; dla `F=\mathcal N^2` akceptowane są wszystkie. W przypadku ogólnym dokładny rzut zamkniętego `F` zostaje zrealizowany przez przekrój `U_c`. Brak pozostałości predykatu `>0`.
- **Przekątniowanie:** sprzeczność `c\in D\iff c\notin D` działa dzięki uniwersalności `U`; analityczność `E` wynika z ciągłości przekątnej. Teza o ścisłym zawieraniu jest poprawnie ograniczona do przestrzeni Baire’a.
- **Zgodność z poprzednim materiałem:** wszystkie cztery odsyłacze do rozdziału 19 mają realne cele. Rozdział nie powtarza teorii determinacji ani redukcji Wadge’a ze skryptu logiki, a mierzalności analitycznych nie przedstawia jako już dowiedzionej.

## Kontrola techniczna i stan integracji

- Rozdział 20: 859 wierszy, 23 unikatowe etykiety, 23 odsyłacze, zrównoważone środowiska matematyczne; brak kolizji w jego obrębie i brak niewyjaśnionych odsyłaczy zewnętrznych.
- Test regresyjny `tools/tests/test_general_topology_ch20.py` nadal zawiera model `universal_tree_coding_models` i asercje chroniące prawidłowe rozróżnienie kodów 1 i 2.
- Walidacja na commicie zawierającym poprawiony rozdział i testy: [45040786110](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45040786110), **completed/success**. Potwierdzono kroki testowania matematycznych modeli, kompilację całej książki, osobnego rozdziału 20 i kontrolę logów.
- Pobrany z tej walidacji, rzeczywisty sześciostronicowy PDF rozdziału 20 został wyrenderowany; układ stron 1–6 i szczegóły stron 5–6 (uniwersalne drzewo oraz diagonalizacja) są prawidłowe, bez nakładek i ucięć.
- `books/pl/general_topology.tex` jest zaktualizowany: **„Wersja 1.20 — rozdziały 01–20 stabilne”** (blob `016ef70ae48fecffe3d0631f2a78630c3b5911ba`). Dodatkowa walidacja po tej zmianie [45041242783](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45041242783) była **in_progress** przy spisywaniu audytu; jej sukces nie jest deklarowany przed ukończeniem. Poprzednie pełne CI obejmuje jednak identyczny rozdział i testy.

## Status i kolejność dalszych prac

**ROZDZIAŁ 20: STABILNY, 2/2 + 1 dodatkowy audyt czysty.**
W razie błędu bieżącej walidacji książki wrócić do diagnostyki integracji, bez nieuzasadnionego wyzerowania czystych matematycznych audytów rozdziału.

Ponieważ rozdział 18 zawiera już topologię zwarto-otwartą i przestrzenie odwzorowań, nie należy powtarzać dawnego punktu planu „21 — topologie na przestrzeniach odwzorowań”. Najbliższy niepowielający rozdział to **21 — Topologie na rodzinach podzbiorów** (topologia Vietorisa, topologia Fella, metryka Hausdorffa i relacje między konstrukcjami), po wcześniejszej kontroli nakładania się z istniejącymi skryptami. Zgodnie z przyjętymi zasadami rozdział 21 powinien zostać opracowany i wielokrotnie audytowany jako osobny etap.
