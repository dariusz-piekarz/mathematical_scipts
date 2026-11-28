# Algebra liniowa — globalny audyt 34: dodatkowe ostrzeżenie amsmath, korekta LA-22

**Data:** 23 listopada 2026. **Zakres:** niezależny odbiór składu 320-stronicowej książki po poprawkach LA-13 i LA-32 oraz krytyczna kontrola lokalna LA-22.

## Wykryta usterka redakcyjna

W poprzednim audycie 33 poprawiono osiem ostrzeżeń `Package hyperref Warning`; nowy [CI 45131006863](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45131006863) ma wynik `completed/success`, a pobrany plik `linear_algebra.pdf` (320 stron) nie zawiera już żadnego `hyperref Warning`. Porównano wszystkie **320/320 stron rastrowo** z poprzednim PDF — obrazy identyczne, zero bloków tekstu poza obszarem stron. Oglądnięto spis zakładek: LA-13 ma obecnie `Dopełnienia ortogonalne nad R i C`, LA-32 `Macierze 2x2` i `Kwaternionowa struktura na C4`.

**Nowa usterka G34-01**: w finalnym logu występuje jedno ostrzeżenie `Package amsmath Warning: Foreign command \\atopwithdelims` (LA-22, wiersz 468), ponieważ stary zapis `{k\\choose j}` działa przez przestarzałą prymitywną składnię TeX. Nie jest to błąd matematyczny, lecz uchybienie techniczne niewykryte wcześniejszą bramką.

**Naprawiono** w LA-22: `{k\\choose j}` zastąpiono `\\binom{k}{j}`, bez zmiany znaczenia wzoru dwumianowego, hipotez, dowodu, numeracji ani odsyłaczy. Poprzedni blob `dfa3d790bfed4c92c66642ea626a6213bc06ad3f`, nowy `735db5c063d9ac9c148894a8ffdcc681339e9611`; [commit 58b9d78e](https://github.com/dariusz-piekarz/mathematical_scipts/commit/58b9d78e22266b1bf165f4f3e511a9669fb54bcd).

CI zaostrzono do wykrywania **dowolnych** ostrzeżeń `Package ... Warning:` (w miejsce ograniczenia do `hyperref`); [commit 3ca7370f](https://github.com/dariusz-piekarz/mathematical_scipts/commit/3ca7370f631daeeddd816a54488434b0144f5f0d).

## Niezależna kontrola matematyczna zmienionego miejsca

Dla nilpotentnych bloków Jordana `N_a, N_b` rozważono operator `T(X)=N_aX−XN_b` na macierzach `a×b`. Zweryfikowano, że `T^{a+b−1}=0`; każdy składnik wzoru dwumianowego znika, gdy `a+b−1−j≥a` albo `j≥b`. Dokładna implementacja (całkowite macierze i wszystkie jednostki macierzowe dla `1≤a,b≤7`) przeszła **853/853** testów, także ostrość wykładnika i `Σ_j binom(k,j)=2^k` dla `0≤k<20`. Kod kontrolny `/mnt/data/la_audit/la22_nilpotent_confirm.py` działa niezależnie od biblioteki; nie jest formalnym dowodem dla wszystkich rozmiarów.

## Decyzja

**Globalny audyt 34: KOREKCYJNY, NIE ZAMKNIĘTY.** Kontrola LA-32 w poprzednim audycie domknęła rejestr **382/382 dowodów**, jednak modyfikacja LA-22 zeruje licznik nowych czystych reaudytów jej bloba. Należy potwierdzić nowy CI bez ostrzeżeń `amsmath` i wykonać dwie niezależne bezusterkowe kontrole poprawionych LA-13, LA-22, LA-32 oraz końcowy audyt sceptyczny całej książki. Nie przypisywać poprzedniego CI wynikowi przyszłego commitu ani nowemu źródłu LA-22.
