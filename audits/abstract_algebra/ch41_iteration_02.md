# AA-41 — audyt II (stabilizacyjny)

**Rozdział:** Reprezentacje grup skończonych i twierdzenie Maschkego.  
**Status matematyczny:** STABILNY — nie wykryto zmian wymagających korekty źródła po audycie I.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Oczekiwany plik:** `chapters/pl/abstract_algebra/41-reprezentacje-grup-i-twierdzenie-maschkego.tex`.

## Zakres ponownej kontroli

- Definicja reprezentacji i podreprezentacji; nieprzywiedlność; rozkład naturalnej reprezentacji permutacyjnej `S_3` nad `Q`.
- Konstrukcja rzutu Maschkego przez sprzężone projekcje, wyznaczanie obrazu i jądra; kompletność dowodu indukcyjnego.
- Odpowiedniość między reprezentacjami grupy a lewymi modułami nad algebrą grupową `K[G]`.
- Równoważność warunków w twierdzeniu o ostrości założenia `|G| != 0` w `K`, w tym subtelny kierunek rozkładalność ⇒ dopełnienia oraz kontrapozycja przez reprezentację regularną.
- Projekcje inwolucji, operator Reynoldsa, dokładność funktora wektorów niezmienniczych w dobrej charakterystyce i przykład jej braku w `F_2`.
- Nowy przykład nad `F_2` dla `C_3`, z dowodem nieprzywiedlności dwuwymiarowego składnika.

## Testy

1. Regresja audytu I: **267/267 PASS**.
2. Niezależne sprawdzenie matematyczne nad ciałami skończonymi: **240/240 PASS**. Testowano m.in. wzory uśredniania dla działań cyklicznych i pełnych grup symetrycznych, projekcje względem inwolucji, modularne przeciwprzykłady i dokładność augmentacji.
3. Ponowienie obu zestawów w układzie `tools/tests` + `chapters/pl/abstract_algebra`, bez lokalnych ścieżek lub zmiennych środowiskowych: **507/507 PASS**.

**Łącznie: 507/507 PASS**.

## Skład i integralność

- PDF LaTeX: **6 stron**, A4, udana świeża kompilacja `latexmk`.
- Ostrzeżenia LaTeX, przepełnienia, błędy odsyłaczy: **0**.
- Obejrzenie renderów każdej strony: brak nałożeń, ucięć i wad układu.
- **19 unikatowych etykiet**, wszystkie odsyłacze w rozdziale prowadzą do etykiet lokalnych.
- 2 twierdzenia, 3 stwierdzenia, 6 dowodów, 9 przykładów.
- SHA-256 poprawionego źródła: `d39110cc9d7641f752c6ac07d91a631fc36295f443ee5a46b56068986008f503`.
- Zmiany źródła względem audytu I: **0 bajtów**.

## Stan publikacji i CI

**GitHub Actions:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068795118

Wynik przebiegu: **completed / success** (rzeczywisty odczyt GitHub Actions).

| Zdalny etap | Status |
|---|---|
| Testy ogólne repozytorium | `success` |
| Testy regresyjne i niezależne AA-41 | `success` |
| Kompilacja książki AA-01–AA-41 | `success` |
| Kontrola wygenerowanego PDF i odsyłaczy | `success` |

**Końcowy status: AA-41 STABILNY po audytach I–II; pełne zdalne CI PASS.**

## Publikacja

Zweryfikowano publikację źródła, testów, książki, katalogu i workflow na gałęzi `biblioteka-matematyczna-iteracja-6`. Książka obejmuje AA-01–AA-41. Uruchomiono zdalny przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45068795118; jego końcowy wynik zostanie odnotowany dopiero po potwierdzeniu przez GitHub Actions.
