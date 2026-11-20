# Audyt globalny Biblioteki matematycznej: AT–DG–AG — etap I

**Data:** 20 listopada 2026 r.  
**Gałąź robocza:** biblioteka-matematyczna-iteracja-6 (bez dotykania main).  
**Zakres techniczny:** wszystkie aktualnie importowane rozdziały trzech osobnych książek:
- Topologia algebraiczna (AT): 30 rozdziałów 01–30 oraz rozdział wprowadzający AT-00;
- Geometria i topologia różniczkowa (DG): 20 rozdziałów 01–20; cały oryginalny skrypt ma docelowo 36 rozdziałów, a 21–36 jeszcze nie należą do tego importu;
- Geometria algebraiczna (AG): 11 rozdziałów 00–10.

## 1. Sprawdzalne wyniki źródłowego audytu

Rozpisanie rzeczywistego drzewa \input wykonuje:
application/scripts/audit_cross_volume_geometry_topology.py.

Jego wynik po aktualnym stanie repozytorium:

| Wielkość | AT | DG | AG |
|---|---:|---:|---:|
| Matematyczne rozdziały importowane do książki | 30 | 20 | 11 |
| Różne etykiety wewnątrz tomu (włącznie z przydzielonymi modułami wspólnymi) | 624 | 1278 | 404 |
| Użycia zwykłych odsyłaczy w przeglądanym źródle | 443 | 1260 | 166 |
| Zduplikowane etykiety wewnątrz tego samego tomu | 0 | 0 | 0 |
| Nierozwiązane wystąpienia odsyłaczy względem obecnego importu | 0 | 13 | 0 |
| Odsyłacze wskazujące nazwę istniejącą tylko w innym tomie, bez mechanizmu linkowania | 0 | 0 | 0 |

W trzech tomach łącznie są **304 nazwy etykiet mające więcej niż jeden odrębny plik źródłowy**:
- 303 nazwy pojawiają się w różnych rozdziałach AT oraz DG;
- jedna nazwa, **sec:moduly**, ma trzech różnych właścicieli: AT-03, DG-05 i AG-04.

**Nie należy utożsamiać dwóch różnych twierdzeń tylko dlatego, że ich etykiety mają identyczny zapis.** Przed fizycznym połączeniem książek konieczna jest weryfikacja treści każdej kolizji, a następnie ułożenie kanonicznych właścicieli i kontrolowanych aliasów starych etykiet. Nie zmieniono żadnej istniejącej etykiety.

## 2. Trzy poprawnie współdzielone moduły matematyczne

Następujące fizyczne pliki są dołączane do AG i AT bez kopiowania ich dowodów:
- shared/pl/slabe_twierdzenie_lefschetza.tex — dwa historyczne identyfikatory twierdzenia;
- shared/pl/rozdmuchanie_punktu_normalna.tex — wiązka normalna oraz samoprzecięcie dzielnika wyjątkowego;
- shared/pl/rozdmuchanie_punktu_kohomologia.tex — kohomologia rozdmuchania, forma przecięć, Euler i sygnatura.

W obu tomach źródłowy moduł o normalnej dzielnika wyjątkowego występuje **przed** modułem o jego kohomologii. Jest to ważne, gdyż dowód kohomologiczny powołuje się na lemat o normalnej. Wszystkie trzy pliki zachowują ochronę przed podwójnym składem we wspólnej przyszłej książce i historyczne etykiety. **Nie wchodzą w liczbę 304 kolizji nazw.**

Przy scalaniu należy pozostawić pierwotne nazwy etykiet przypisane do wspólnego obiektu; nie duplikować całego twierdzenia przez kopiowanie go do nowego rozdziału. Żaden z tych plików nie odwołuje się do zewnętrznej grafiki ani źródłowego kodu.

## 3. Mapa nakładek — priorytety dalszych audytów

Poniższa tabela zestawia 15 par tematycznych wybranych do **ręcznej oceny**, nie 15 automatycznie wykrytych identycznych tekstów. Współczynnik J oznacza współczynnik Jaccarda **identycznych niebanalnych linii tekstu** po podstawowej normalizacji odstępów; **nie mierzy równoważności matematycznej**. Nazwy kolidujące w tabeli liczymy bez etykiet importowanych z modułów shared.

| Para | J | Wspólne nazwy etykiet | Nazwy tylko po lewej / prawej | Wniosek do scalania |
|---|---:|---:|---:|---|
| AT-02 / DG-05 | 0,000 | 0 | 6 / 53 | Podobne podstawy algebry, ale odrębne opracowania; bez mechanicznego usuwania |
| AT-03 / DG-06 | 0,607 | 62 | 7 / 10 | Silne pokrycie: zachować obie grupy dodatkowych przykładów i kontrprzykładów |
| AT-04 / DG-07 | 0,535 | 44 | 2 / 16 | Nakrycia, van Kampen; odrębne ilustracje i rozbudowane konstrukcje DG |
| AT-05 / DG-08 | 0,572 | 50 | 3 / 16 | Homologia; m.in. zachować przykład butelki Kleina AT |
| AT-06 / DG-09 | 0,427 | 42 | 3 / 0 | Uzupełnienia AT nie mogą zniknąć po użyciu DG jako podstawy |
| AT-09 / DG-10 | 0,714 | 60 | 4 / 1 | **Najpierw** rozstrzygnąć przeniesienie przykładów form i Stokesa |
| AT-11 / DG-17 | 0,564 | 42 | 8 / 10 | Zachować oba zestawy przykładów PD, przecięć i klas SW |
| AT-18 / DG-18 | 0,000 | 0 | 13 / 50 | Wspólny temat, ale odmienne aparaty Morse'a; nie są tekstowymi kopiami |
| AT-28 / AG-10 | 0,002 | 0 | 10 / 27 | Wspólne twierdzenia są w shared; reszta jest istotnie uzupełniająca |
| AT-28 / AG-09 | 0,000 | 0 | 10 / 30 | Topologia/Kähler–Hodge kontra teoria GAGA i analityfikacji |
| AT-28 / AG-06 | 0,001 | 0 | 10 / 35 | Topologiczna formuła rozdmuchania kontra algebraiczne rachunki powierzchni |
| AT-30 / DG-01 | 0,000 | 0 | 5 / 73 | AT-30 to skrócony słownik, nie substytut DG-01 |
| AT-30 / DG-03 | 0,000 | 0 | 5 / 87 | Korzystać z pełnej algebry zewnętrznej DG-03 |
| AT-30 / DG-15 | 0,000 | 0 | 5 / 38 | Słownik Sarda/transwersalności i nowy przykład AT-30 |
| AT-30 / DG-16 | 0,000 | 0 | 5 / 45 | Słownik tubularny i nowy przykład AT-30; nie zastępować DG-16 |

**Ważne konkretne elementy do zachowania:**
- AT-03: prz:redukcja-mod2-trzy-stopnie oraz fig:redukcja-mod2-top; DG-06: prz:mod2-dwa-zrodla i prz:ses-dwa-rozszerzenia.
- AT-04: prz:nakrycie-m-arkuszy i jej rysunek; DG-07: twierdzenie o grupie transformacji nakrycia, praca z grafami i dodatkowe ilustracje.
- AT-05: prz:homologia-butelka-kleina i przykład Mayera–Vietorisa dla dwóch półkul; DG-08: dodatkowe rachunki grafów i homologii lokalnej.
- AT-06: prz:pi1-klein-hurewicz, prz:pi-2-3-komorki i jej diagram.
- AT-09: thm:forma-okresy-pierwotna, prz:stokes-pierscien-dwa-brzegi; DG-10: prz:formy-rachunek-r3.
- AT-11: dualność Alexandera i Poincarégo–Lefschetza w wyróżnionych sekcjach; DG-17: liczne przykłady z torusem, RP², CP² i klasami charakterystycznymi.
- AT-28: pełny rachunek rozdmuchania P³ wzdłuż krzywej eliptycznej; AG-10: rzutowa krzywa węzłowa, Gysin, Chern, liczby Hodge'a i geom. algebraiczna przekrojów.
- AT-30: jawny dyfeomorfizm tubularny okręgu i przykład transwersalności po perturbacji; DG-01/15/16: pełne założenia, warianty dowodów i twierdzenia ogólne.

## 4. Brakujące cele odsyłaczy DG

W **obecnym** DG-01–20 występuje 13 nierozwiązanych użyć odsyłaczy, ale tylko 12 różnych nazw:

| Rozdział | Liczba użyć | Cele nieobecne w imporcie |
|---|---:|---|
| DG-11 | 2 | prz:thur-dop-nil-kontakt; sec:rownanie-diraca |
| DG-12 | 1 | subsec:dirac-koneksja |
| DG-14 | 7 | sec:algebra-liego; cor:bochner-vanishing; cor:hodge-de-rham; ch:chern-weil; prop:euler-identification-26; lem:angular-form-26; thm:CGB-boundary-26 |
| DG-16 | 1 | ch:grafy-wezly-cztery |
| DG-17 | 2 | prz:hodge-dwie-sfery-18; ch:chern-weil |

Nie zamieniono ich na przybliżone matematycznie etykiety z AT lub AG. **Najpierw** należy doimportować DG-21–36 i sprawdzić dokładne oryginalne definicje etykiet oraz ich cele. Pozostałe po tej operacji braki wymagają korekty po ręcznym odczytaniu dowodów.

## 5. Testy i automatyczna ochrona przyszłych iteracji

Wprowadzono:
- application/scripts/audit_cross_volume_geometry_topology.py — rzeczywisty odczyt kanonicznych books/pl i rekurencyjnych wejść, inwentaryzacja źródeł i etykiet, kwalifikacja odsyłaczy, 15 par wraz z metrykami tekstowymi;
- application/tests/test_cross_volume_geometry_topology.py — regresje zakresu importu, obsługi komentarzy TeX, wspólnych źródeł i etykiet, kolejności modułów, zderzenia sec:moduly i znanej listy nierozwiązanych celów DG; testy nie nadpisują historycznych plików ani etykiet;
- .github/workflows/global-geometry-topology-audit.yml — GitHub Actions zapisuje pełny maszynowy manifest JSON jako artefakt CI i sprawdza samodzielną kompilację geometrii algebraicznej z modułami shared.

Dla AT już istnieje kontrola 30-rozdziałowego tomu (ostatni audyt AT-29/30: 295 stron i trzy przebiegi pdflatex). W tej iteracji **nie** deklarujemy pełnego audytu 36 rozdziałów DG, bo 16 z nich nie jest jeszcze zaimportowanych.

## 6. Wnioski i kolejny etap

To jest **globalny audyt struktury oraz wybranych nakładek matematycznych**, nie automatyczna certyfikacja pełnej poprawności wszystkich 61 istniejących rozdziałów. Nie scalano treści, ponieważ bezpośrednie kopiowanie spowodowałoby utratę ważnych odmiennych przykładów i ryzyko mylnego utożsamienia twierdzeń.

Następna rzeczywista iteracja powinna:
1. porównać **tezy, hipotezy i dowody** dla kolizji w AT-09/DG-10 oraz AT-03/DG-06 i dopiero wtedy wyznaczyć kanoniczne właścicielstwo dowodów;
2. odtworzyć cele 13 odsyłaczy DG po zaimportowaniu brakujących źródeł DG-21–36;
3. wykonać tabelę znaczeń etykiet, zwłaszcza sec:moduly, i dopiero na końcu przeprowadzać scalanie bez utraty treści.
