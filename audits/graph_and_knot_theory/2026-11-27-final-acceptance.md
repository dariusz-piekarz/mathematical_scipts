# Odbiór końcowy GT — 2026-11-27

## Wersja i dowody wykonania

- Skrypt: 42 pliki (GT00 i 41 rozdziałów merytorycznych); poprzednie raporty audytów szczegółowych uzgodniono w 2026-11-27-reconciliation-and-gt14.md. Nie odzyskano SHA wszystkich historycznych audytów.
- Kontrola zbiorcza etykiet: 755 definicji, 655 odsyłaczy, 303 różne cele, 0 duplikatów, 0 brakujących celów (cross-2026-11-27/result.json). Późniejsze zmiany terminologiczne zachowały etykiety i odsyłacze.
- Pełny PDF, commit d3ba57716d6353d0de2ea5df484bc87e7dd716da, przebieg 46031006325, zadanie 140614477768: 415 stron A4, trzy przebiegi pdflatex, 0 ostrzeżeń wg bramki CI. Artefakt 15214262846 pobrany i otwarty lokalnie.
- Kontrola wizualna tego PDF: wykryto kolorową grafikę wektorową na 94 stronach. Wyrenderowano 104 obszary (grupowanie ścieżek według położenia pionowego), obejrzano wszystkie na 9 arkuszach kontaktowych. Nie zauważono problemów renderowania, nachodzenia elementów ani obcięcia grafiki w sprawdzonych obszarach. Nie jest to bijektywna identyfikacja wszystkich środowisk TikZ ani ponowny dowód poprawności matematycznej każdego diagramu.
- Naprawa testu diagramów skrzyżowań: commit 17b4b409856734f2f4a3a66fa7f588388569c68a, sześć asercji kodu rzeczywistych pasm zamiast nieaktualnego podpisu.
- Pełny globalny workflow GT po tej naprawie: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/46031437836, zakończony success. Zadanie structural-audit 140615962261: wszystkie 32 kroki success; full-book-pdf 140615961529: wszystkie 7 kroków success.
- Oddzielny audyt algorytmów oraz terminologia: success na e6c052c6ccf3eede979d9f801198825b987fdc91 (przebiegi 46022709112 i 46022709482); nie utożsamiać z najnowszym przebiegiem całego repozytorium.

Porównanie po 17b4b40 z bieżącą gałęzią przed zapisaniem raportu: pięć dalszych commitów, żadnej zmiany plików GT. Odbiór skryptu GT zakończony w zakresie globalnego workflow, udokumentowanych audytów źródeł i kontroli wizualnej opisanej powyżej. Nie potwierdzono niezależnie pełnego CI całego Atlasu ani renderowania wszystkich rysunków w przeglądarkowym podglądzie aplikacji. Nie uruchamiać od początku szczegółowych audytów tylko z powodu kolejności rozdziałów; ewentualne przyszłe zmiany sprawdzać przyrostowo.
