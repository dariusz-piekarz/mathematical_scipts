# Migracja źródłowa II — KH, McShane, Denjoy, Lebesgue (fragment porównawczy)

Źródło: AM1-36, commit ebc49ca10eeeae7de3d8fb4cccf8a6c6eff457bc, chapters/pl/mathematical_analysis_i/36-calka-kurzweila-henstocka.tex. AM1-36 sam wywodzi się z wcześniejszej adaptacji Teorii całki; przeniesiono z powrotem wersje opracowane w AM1, nie traktując samej migracji jako niezależnego dowodu poprawności.

- 04: definicje, własności, pochodne, lemat Saksa–Henstocka, osobliwości, mnożniki, podstawienie i zbieżność; zachowano uwagę o całce Stieltjesa.
- 07: definicja, inkluzje i bezwzględna całkowalność; zachowano własne przykłady, konstrukcję dla funkcji charakterystycznych i prostych.
- 08: pełny fragment o wąskiej całce Denjoya i charakteryzacji pierwotnych. 
- 11: wymieniono tylko fragment porównawczy z KH i McShane'em, normę Alexiewicza i twierdzenia graniczne KH. Konstrukcja Lebesgue'a i jej twierdzenia graniczne pozostają do migracji z TM.
- Pozostawiono historyczne etykiety IT obok oryginalnych etykiet AM1; dostosowano skrót HK do skryptu docelowego. Zachowano podział tematyczny i uniknięto ponownego wklejania porównania całek w 07 i 11.
- Kontrola statyczna: 32 starych etykiet zachowanych, 62 etykiet unikalnych w zmienionych plikach, 24 wystąpień lokalnych odsyłaczy rozwiązywalnych w 01, 02, 04, 07, 08, 11; pary środowisk poprawne. Kompilacja i CI nieuruchomione w tej sesji. Audyty matematyczne i rozszerzenia odłożone do zakończenia migracji.
