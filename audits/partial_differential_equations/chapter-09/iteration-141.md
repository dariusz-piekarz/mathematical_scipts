# PDE — rozdział 09 — iteracja 141, kontrola techniczna

Data: 2026-11-25. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło rozdziału: blob 30d48c49e6db0d013e8fff4cfc9960323e25342b (ostatnia zmiana matematyczna c6db5521f96c7121e51464a94a72e28213b3c12e).

## Kontrole wykonane

- 37/37 etykiet unikalnych; 64 wystąpienia odsyłaczy rozpoznane, 15 różnych celów zewnętrznych odnalezionych w rozdziałach 07, 08, 10.
- 81/81 identyfikatorów kryteriów unikalnych i przypisanych do istniejących etykiet; stos środowisk poprawny.
- Zgodność listy input z manifestem, pozycja 9, kanoniczny styl listingów w książce i Atlasie.
- Korekta arytmetyczna bilansu iteracji 135–140: 9+4+6+5+5+7=36 uściślonych kryteriów, 13+9+6+8+3+5=44 bez zmian, 1 kontrola źródła rysunku. Łącznie 81; wcześniejszy zapis 37/43 w iteracji 140 był omyłką sumowania.

## Wykonywalne regresje i CI

Dodano test_sobolev.py (commit 7e2e9bb5ae55cfe87f16df53a63ec95736c833c4) i workflow rozdziału 09 (commit c41381c202bacb282cdb09e2fa0693e1caf3e926).
Cztery metody testowe obejmują skończone rachunki dokładne: PDE-09-025, 066, 076, 079–080. Nie są formalizacją ogólnych twierdzeń ani testami wszystkich 81 kryteriów.
Workflow wykorzystuje kanoniczną preambułę oraz numerowe odsyłacze zewnętrzne w izolowanym rozdziale; nie zastępuje pełnej kompilacji książki.

Run: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45611895966
Head: c41381c202bacb282cdb09e2fa0693e1caf3e926.
Potwierdzono przez API jobs: testy wykonywalne — success; kontrola odsyłaczy i przygotowanie rozdziału — success; kompilacja — in_progress; diagnostyka, render i artefakty — pending w chwili odczytu.
Nie potwierdzono jeszcze wyniku końcowego ani nie obejrzano PDF. Globalne CI aplikacji i teorii całki miały także nieudane przebiegi na współdzielonej gałęzi (np. 45611677793 i 45611703909); bez pełnej diagnozy nie przypisujemy ich rozdziałowi 09. Nie uruchamiano Lean.

Status: kontrola strukturalna i dedykowane testy wykonane; końcowe CI, inspekcja wizualna oraz niezależny audyt kontrolny pozostają otwarte. Kolejna iteracja 142: odczyt wyniku tego przebiegu, naprawa ewentualnych usterek, weryfikacja PDF i diagnostyki przed audytem kontrolnym. Nie uznawać rozdziału za ustabilizowany.
