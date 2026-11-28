# Topologia ogólna — rozdział 23, audyt 03 (skład i korekta)

**Data:** 2026-11-22.
**Zakres:** chapters/pl/general_topology/23-wymiar-topologiczny.tex.
**Wynik:** KOREKCYJNY — licznik czystych kontroli 0/2.

## Kontrola rzeczywiście wygenerowanego PDF

CI 45051084818 zakończyło się sukcesem na źródle
c666640268a1a14b813b4e0a1e7744e342cf9fe8.
Pobrano artefakt PDF ID 14765586288 i wydzielono
general_topology_ch23.pdf (10 stron A4), a następnie
wyrenderowano wszystkie 10 stron do obrazów PNG,
obejrzano kontaktowy zestaw wszystkich stron oraz
osobno strony 09 i 10 w wyższej rozdzielczości.

**Ustalenia:**
- 01–09: czytelne wzory, brak wizualnego nakładania się
  tekstu na rysunek i marginesy;
- 09: ostatni właściwy dowód kończy się przed końcem strony;
- 10: tylko krótkie podsumowanie na niemal pustej stronie.
  Jest to realne uchybienie estetyczne, mimo zielonego CI.

## Korekta

W rozdziale 23 skrócono podsumowanie,
zachowując cztery najważniejsze wyniki:
dim C=0, dim[a,b]=1, dim K<=n dla zwartych
K subset R^n, dim[0,1]^n=n; zachowano również
informację o korzystaniu z twierdzenia Brouwera
i niezakończonym porównaniu Ind/ind/dim
w dodatnich wymiarach.
Commit: 16672f16602b27fc08ba96a201c76c001fcf24a8.
Nowy blob rozdziału:
ef9c42ad0b4a423bf85f4cb80939ee9c46b3da96.

Korekta nie zmienia matematycznej treści twierdzeń
ani identyfikatorów etykiet. Zmienia jednak blob źródła,
więc dla wersji poprawionej nie ma jeszcze
dwóch kolejnych czystych audytów.

## Warunki zamknięcia

1. Niezależnie sprawdzić jeszcze raz matematykę i
   spójność odsyłaczy na nowym blobie.
2. Uzyskać 2 czyste audyty i 1 dodatkowy bez kolejnej
   modyfikacji źródła.
3. Pobrać nowy rzeczywisty PDF z zielonego CI,
   wyrenderować wszystkie strony i zweryfikować,
   czy podsumowanie nie zostawia osieroconej strony.
4. Sprawdzić także pełną książkę i logi LaTeX.

**Stan: 0/2; rozdział 23 nadal w audycie.**
