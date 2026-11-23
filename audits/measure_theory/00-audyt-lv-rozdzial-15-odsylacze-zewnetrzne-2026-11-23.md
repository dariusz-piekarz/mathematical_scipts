# Audyt LV (55) — rozdział 15, korekta odsyłaczy w samodzielnym PDF

Data: 2026-11-23.
Repozytorium: dariusz-piekarz/mathematical_scipts.
Gałąź: biblioteka-matematyczna-iteracja-6.
Plik kanoniczny: chapters/pl/measure_theory/15-dualnosc-wypuklosc-i-slaba-zbieznosc-w-przestrzeniach-lp.tex.
Zweryfikowany SHA bloba rozdziału: 075e6e30bc73a28450b7ffcb6af6b8fe9a76f8ab (bez zmian względem audytów LI–LIV).

## Zidentyfikowana luka

W audycie LIV workflow kompilował osobny rozdział 15, używając preambuły z books/pl/measure_theory.tex, lecz nie importował etykiet z rozdziałów 1–14. Mimo pomyślnej kompilacji PDF odsyłacze do wcześniejszych twierdzeń mogły więc występować jako ??; kontrola logu obejmowała wyłącznie pełną książkę. Samo istnienie PDF nie zapewnia poprawności odsyłaczy. W źródle rozdziału 15 wśród odwołań zewnętrznych są: ch:przestrzenie-lp, thm:holder-14 i thm:riesz-fischer-14. Rozdział zawiera 17 własnych etykiet, które nie mogą zostać bezrefleksyjnie zaimportowane z pełnej książki, bo powstałby konflikt z etykietami lokalnymi.

## Zrealizowana poprawka

W istniejącym workflow .github/workflows/measure-theory-ch15-lii-gate.yml:
1. Po kompilacji całej książki odczytywany jest rzeczywisty plik measure_theory.aux, a z jego instrukcji newlabel wybierane są etykiety inne niż deklarowane w bieżącym rozdziale 15.
2. Tworzony jest odrębny measure_theory_ch15_external.aux, z którego pakiet xr-hyper importuje etykiety do izolowanego dokumentu; hiperłącza wskazują PDF całej książki.
3. Przyjęto licznik chapter = 14 przed rozdziałem, dzięki czemu pozostaje on rozdziałem 15 także w izolowanym PDF.
4. Dodano obligatoryjną kontrolę logu izolowanego PDF: brak nierozwiązanych referencji/cytowań, brak wielokrotnie definiowanych etykiet oraz brak komunikatu o wymaganym ponownym przebiegu dla referencji.
5. Poprawka workflow: commit 91529deff2d747916c81856ae7fd0b967da12dbe; bieżący SHA bloba workflow f26f57687f938de0054e5f97d402522ed953da19.

## Niezależna kontrola wykonalności

W lokalnym środowisku TeX wykonano dwa przebiegi testowe oparte na minimalnej dwu-rozdziałowej książce z pakietem hyperref i izolowanym rozdziałem wykorzystującym xr-hyper. W dokładniejszym wariancie:
- wygenerowano AUX całej książki i wyodrębniono trzy etykiety z wcześniejszego rozdziału, z wykluczeniem jednej etykiety lokalnej;
- uruchomiono latexmk -pdf -interaction=nonstopmode -halt-on-error dla wygenerowanego izolowanego rozdziału;
- PDF powstał poprawnie (24 598 bajtów); finalny log nie zawierał komunikatów o undefined references, multiply defined ani o ponownym przebiegu;
- ekstrakcja tekstu PDF dała poprawne wartości odsyłaczy: 1, 1.1, 1.2 oraz lokalny rozdział 2.

Jest to **test konstrukcji oraz zasad pakietu xr-hyper**, a nie kompilacja 31-rozdziałowej książki użytkownika. Nie wolno przypisywać rozdziałowi 15 własnej wizualnej kontroli na podstawie syntetycznego testu.

## Stan weryfikacji CI

Ponownie odczytano aktualny workflow z GitHub i potwierdzono SHA bloba; kanoniczny rozdział 15 nie zmienił się. Zapytania o klasyczne statusy commitu 91529deff2d747916c81856ae7fd0b967da12dbe i dostępne konektorowe wyszukiwanie przebiegów nie dały wyników. Dostępna ścieżka wyszukiwania przebiegów jest ograniczona do określonych uruchomień PR i **nie pozwala rozstrzygnąć statusu push-triggered CI**. W tej iteracji nie uzyskano identyfikatora właściwego przebiegu ani jego logów.

**Werdykt LV:**
- Poprawka architektury izolowanego PDF zapisana i potwierdzona w źródle.
- Lokalny test idei xr-hyper i konfliktów etykiet: PASS na syntetycznym przykładzie.
- Matematka rozdziału 15: wcześniejszy PASS zachowany, bez zmian treści.
- Rzeczywiste wykonanie obu zadań CI, finalne PDF-y i oględziny stron rozdziału 15: NIEPOTWIERDZONE.
- Pełna stabilizacja rozdziału 15: OTWARTA TECHNICZNIE.

## Dalszy etap

Potwierdzić konkretny run workflow Measure theory chapter 15 LII stabilization z commitem zawierającym powyższą poprawkę. Sprawdzić 8/8 testów, sukces jobów tests/pdf, brak ostrzeżeń w obu logach, prawidłową numerację rozdziału 15 i rzeczywiste obrazy stron; przy awarii poprawić rzeczywistą przyczynę. Dopiero po potwierdzeniu tej bramki zamknąć rozdział 15 i przejść do rozdziału 16.
