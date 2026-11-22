# Topologia ogólna — rozdział 21, audyt 01

**Data:** 2026-11-22. **Gałąź:** biblioteka-matematyczna-iteracja-6.
**Źródło:** chapters/pl/general_topology/21-topologie-na-rodzinach-podzbiorow.tex.
**Wynik:** NIE CZYSTY. Cztery usterki poprawione; **0/2** czystych audytów po ostatniej modyfikacji.
**Blob po korektach:** b63abaad5fea93f2a5d4317c8be1ada73fcbe1a2.

## Kontrola zakresu

Rozdział 18 dotyczy przestrzeni odwzorowań i topologii zwarto-otwartej;
nowy rozdział 21 dotyczy przestrzeni zbiorów, a więc nie powiela materiału
rozdziału 18 ani twierdzeń z rozdziałów 07 i 14.
Jawnie rozróżniono zbiory zwarte niepuste w Vietorisie
od wszystkich zbiorów domkniętych, łącznie z pustym, w Fellu.

## Kontrola dowodów

1. Podbazowe warunki trafienia i zawierania dla Vietorisa są spójne;
   przedstawiona baza obejmuje także skończone przecięcia tylko warunków
   górnych lub tylko dolnych.
2. Zanurzenie singletonów działa dla dowolnego X; domkniętość singletonów
   i oddzielanie dwóch zwartych podzbiorów wymagają Hausdorffa, co
   zostało poprawnie założone.
3. Indukowane przez ciągłe f odwzorowanie K(f) jest ciągłe;
   sprawdzono oba typy przeciwobrazów podbazowych.
4. Metryka Hausdorffa jest dobrze określona dla niepustych zwartych
   podzbiorów przestrzeni metrycznej, a nierówność trójkąta jest udowodniona.
5. Równość topologii Vietorisa i Hausdorffa wynika z oszacowań:
   trafienie kuli oraz dodatnia odległość zwartego K od domkniętego
   dopełnienia otwartego U; odwrotnie skończone pokrycie K kulami
   o promieniu r/3 i warunki górne r/2 dają metryczną kulę r.
6. Dowód zupełności: jednostajna zbieżność funkcji odległości,
   niepustość zbioru zerowego, konstrukcja łańcuchów o sumowalnych
   przyrostach, całkowita ograniczoność i dopiero następnie
   zwartość K oraz przejście do d_H.
7. Zwartość K(X) dla zwartego metrycznego X wyprowadzono z
   zupełności i skończonych sieci niepustych podzbiorów skończonej sieci X.
   Dla dowolnego zwartego Hausdorffa X podano osobny dowód przez ultrafiltry.
8. Kryterium podbazowe Aleksandra wyprowadzono z charakterystyki
   zwartości przez ultrafiltry, dostępnej w rozdziale 07.
9. Topologia Fella na wszystkich domkniętych podzbiorach X,
   w tym pustym, jest zwarta: dowód z podbazy wykorzystuje
   własność skończonych przecięć w każdym zwartym C_j.
10. Hausdorff Fella dla lokalnie zwartej przestrzeni Hausdorffa
    korzysta z istniejącego lematu o otwartym otoczeniu
    o zwartym domknięciu (rozdział 14).
11. Porównanie w zwartym Hausdorffa X przez dopełnienia
    jest poprawne; przykłady {n} oraz {0,n} w R
    odróżniają zbieżność Fella od zbieżności Vietorisa.

## Znalezione błędy i naprawy

- **Kolizja etykiet**: początkowo jedna etykieta
  thm:topog21-vietoris-hausdorff opisywała dwa różne twierdzenia.
  Korekta rozróżnia etykiety thm:topog21-vietoris-separation
  i thm:topog21-vietoris-hausdorff.
  W CI 45041905480 kolizja spowodowała błąd Duplicate labels.
  Commit poprawki: 763ccd639e39070a0b9b789b3851d241d648439b.
- **Przykład punktowych zbiorów na prostej**:
  zapis z przecinkami dziesiętnymi w jednym zbiorze
  mógł być interpretowany jako cztery elementy zamiast dwóch.
  Użyto dokładnie ułamków 1/5 i 17/10, a wynik 3/10.
  Commit: ba0a6f205c00f4ba58ab8e964beead988ec52567.
- **Kolejność logiczna dowodu zupełności**:
  doprecyzowano, że metrykę Hausdorffa do zbudowanego K
  stosujemy dopiero po wykazaniu jego zwartości.
  Ta sama korekta ba0a6f2.
- **Brak makra LaTeX**: w CI 45042012708 testy rozdziałów 01–21
  przeszły, lecz kompilacja całej książki zatrzymała się na
  Undefined control sequence przy \mathscr U.
  Zastosowano dostępne w amsmath/amssymb oznaczenie \mathcal U.
  Commit: 6245a5997c23cf75ba8adc01cb6f65cec69d94c1.

## Testy i integracja

Dodano osobny punkt wejścia books/pl/general_topology_ch21.tex,
wpis w catalog/books.json, import w books/pl/general_topology.tex,
test tools/tests/test_general_topology_ch21.py oraz test i kompilację
w .github/workflows/general-topology-chapter.yml.

Pierwszy przebieg po naprawie etykiet przeszedł testy rozdziałów
01–21 oraz test katalogu, ale nie zbudował PDF z powodu \mathscr.
Nie jest to zielone CI. Wymagane jest nowoczesne zakończone CI
dla bloba b63abaad... i wizualna inspekcja jego rzeczywistego PDF.

**Status: OTWARTY — 0/2**. Po uzyskaniu kompilacji należy przeprowadzić
dwa czyste audyty tej samej wersji, a następnie audyt nadmiarowy.
