# Logika matematyczna i teoria mnogości — rozdział 15, audyt III

**Data:** 21 listopada 2026 r.  
**Rozdział:** „Homomorfizmy, izomorfizmy i elementarność struktur”.  
**Źródło:** `logika_rozdzial_15_audyt_II.tex`.  
**Status:** audyt III zakończony z poprawką; tekst przekazany do niezależnego audytu IV.

## Zakres

Zweryfikowano założenia i treść wszystkich 5 twierdzeń, 1 lematu, 6 dowodów, 7 definicji, 7 przykładów i 4 uwag. Audyt obejmował reguły homomorfizmów, formuły dodatnie egzystencjalne, niezmienniczość przy izomorfizmie, podstruktury, zdania uniwersalne, kryterium Tarskiego–Vaughta oraz równoważność elementarną. Sprawdzono kontrprzykłady, wartościowania, świeżość zmiennych, odsyłacze oraz integralność środowisk LaTeX. Nie rozbudowano zakresu matematycznego.

## Usterka i poprawka

W końcowym dowodzie istnienia elementarnie równoważnych, lecz nieizomorficznych struktur występowało `c^{\mathfrak M}` po uprzednim zredukowaniu języka przez usunięcie symbolu `c`. Oznaczenie jest niepoprawne: w redukcie `c` nie jest symbolem stałej. Poprawiono zapis przez wprowadzenie modelu rozszerzonego `\mathfrak M^+`, jego reduktu `\mathfrak M=\mathfrak M^+\upharpoonright\mathcal L_{\mathrm{ar}}` oraz elementu `a=c^{\mathfrak M^+}`. W dowodzie wyjaśniono też, dlaczego `\mathfrak M\models \operatorname{Th}(\mathfrak N)` oznacza `\mathfrak M\equiv \mathfrak N`: dla zdania fałszywego w `\mathfrak N` jego negacja należy do pełnej teorii i musi być prawdziwa w `\mathfrak M`. W argumencie izomorficznym warunek `\overline m^{\mathfrak M}<^{\mathfrak M}a` przenosi się na niemożliwe `m<m`.

Poprawiono również pojedynczą usterkę interpunkcyjno-językową: po średniku w dowodzie zdań uniwersalnych zastosowano małą literę.

## Walidacja lokalna

- Liczba środowisk matematycznych pozostała bez zmian: 5 twierdzeń, 1 lemat, 6 dowodów, 7 definicji, 7 przykładów, 4 uwagi.
- 14 unikatowych etykiet i 11 odsyłaczy w rozdziale.
- Osiem testów regresyjnych PASS, w tym kontrola rozróżnienia stałej rozszerzonego języka i reduktu.
- `latexmk -pdf`: PASS; osobny PDF rozdziału zajmuje 5 stron; brak przepełnionych wierszy.
- W lokalnym, nie w pełni aktualnym zestawie starszych rozdziałów pozostały odsyłacze `ch:zf-axioms` i `thm:ls-second-order-categorical` poza rozdziałem 15. Ich status musi zostać oceniony na aktualnym stanie GitHuba.

## Decyzja

Audyt III wprowadził korektę, wobec czego nie zamyka rozdziału samodzielnie. Wymagany niezależny audyt IV, a dopiero po nim push oraz CI.