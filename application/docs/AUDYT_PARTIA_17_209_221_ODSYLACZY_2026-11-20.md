# Audyt pochodzenia odsyłaczy — partia XVII, wystąpienia 209–221

**Data:** 20 listopada 2026 r.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`, gałąź `biblioteka-matematyczna-iteracja-6`.  
**Źródło numeracji:** tablica `unresolved_references` w `reference_provenance_audit_355.json`, 355 rozdziałów w migawce.

## Wynik

**13/13 odsyłaczy jest niejednoznacznych w globalnym indeksie**: dla każdego istnieje oryginalny właściciel w `TOP` i odpowiednik w `DG`. Kontrola cytowanego twierdzenia/definicji i otaczającego kontekstu wykazała, że wszystkie 13 odsyłaczy z `TOP-05` i `TOP-06` ma właściwy cel w *tym samym skrypcie topologii algebraicznej* (`TOP-03`, `TOP-04`, `TOP-05`). Nie ma tu brakujących deklaracji. Nie zmieniano etykiet.

## Weryfikacja pozycji

| Nr | Wystąpienie źródłowe | Oryginalna etykieta | Właściwy właściciel i wiersz | Kandydaci w indeksie | Ocena treści |
|---:|---|---|---|---|---|
| 209 | `TOP-05:1425` | `prz:cw-s2` | `TOP-04:1344` | DG-07, TOP-04 | model CW sfery S² |
| 210 | `TOP-05:1450` | `prz:pi1-torus-rp2` | `TOP-04:1493` | DG-07, TOP-04 | modele CW torusa i RP² |
| 211 | `TOP-05:1485` | `prz:pi1-torus-rp2` | `TOP-04:1493` | DG-07, TOP-04 | modele CW torusa i RP² |
| 212 | `TOP-05:1507` | `sec:wspolczynniki-euler` | `TOP-03:1362` | DG-06, TOP-03 | torsja i współczynniki |
| 213 | `TOP-05:1557` | `eq:homologia-char-zero` | `TOP-03:1516` | DG-06, TOP-03 | zmiana współczynników na ciało charakterystyki zero |
| 214 | `TOP-05:1579` | `thm:euler-homologia` | `TOP-03:1633` | DG-06, TOP-03 | algebraiczna charakterystyka Eulera |
| 215 | `TOP-06:4` | `ch:topologia-algebraiczna-podstawy` | `TOP-04:2` | DG-07, TOP-04 | podstawy homotopii i CW |
| 216 | `TOP-06:7` | `ch:homologia-przestrzeni` | `TOP-05:2` | DG-08, TOP-05 | homologia przestrzeni |
| 217 | `TOP-06:40` | `def:droga-petla` | `TOP-04:82` | DG-07, TOP-04 | drogi i pętle |
| 218 | `TOP-06:75` | `thm:grupa-podstawowa` | `TOP-04:155` | DG-07, TOP-04 | konstrukcja grupy podstawowej |
| 219 | `TOP-06:442` | `ch:homologia-przestrzeni` | `TOP-05:2` | DG-08, TOP-05 | homologia przestrzeni |
| 220 | `TOP-06:690` | `thm:kryterium-podnoszenia` | `TOP-04:473` | DG-07, TOP-04 | kryterium podnoszenia odwzorowań |
| 221 | `TOP-06:722` | `prz:homologia-cw-torus` | `TOP-05:1448` | DG-08, TOP-05 | obliczenie homologii komórkowej torusa |

## Dodatkowy audyt matematyczny

1. `TOP-05:1425,1450,1485`: obliczenia homologii sfery, torusa i płaszczyzny rzutowej używają dokładnie modeli CW z `TOP-04`. W szczególności torus ma jedną 2-komórkę dołączoną komutatorem, a dla `RP²` 2-komórkę dołączoną z odwzorowaniem stopnia dwa. Oba zastosowania są merytorycznie zgodne z cytowanym przykładem.
2. `TOP-05:1557`: wynik o zmianie współczynników na `Q`, `R` lub `C` z `TOP-03` nie powinien być bezpośrednio stosowany do `Z/2`. Cytujący fragment poprawnie **oddziela** obliczenie w charakterystyce zero od dalszego bezpośredniego rachunku modulo dwa.
3. `TOP-05:1579`: algebraiczny wzór Eulera jest sformułowany dla kompleksów przestrzeni nad ciałem, podczas gdy tekst cytujący zapisuje rangi homologii całkowitej. Krok jest poprawny po przejściu do `Q` i wykorzystaniu `rank H_n(X;Z)=dim_Q H_n(X;Q)`; wskazane jest **jawne dodanie tego przejścia** w przyszłym audycie redakcyjnym.
4. `TOP-06:690`: kryterium podnoszenia dotyczy odwzorowań z przestrzeni łukowo i lokalnie łukowo spójnych oraz warunku grupy podstawowej. Zastosowanie do `S^n` i `S^n × I` przy `n≥2` spełnia te założenia; fragment cytujący uzasadnia także zachowanie punktu bazowego przy podnoszeniu homotopii. Nie należy przenosić tego wniosku na `n=1`.
5. `TOP-06:722`: przywołana homologia `H_2(T²;Z)=Z` wynika z obliczenia komórkowego `TOP-05:1448`, a nie z analogicznego fragmentu w `DG-08`. Semantyczna identyfikacja jest jednoznaczna na poziomie skryptu.

## Zastrzeżenie o geometrii różniczkowej

Pełny skrypt ma **36 rozdziałów**, a do repozytorium wprowadzono obecnie **20**. Wszelkie raportowane wcześniej braki w `DG` odnoszą się do istniejącej migawki, nie do całości oryginalnego skryptu. Oryginalne etykiety kopiowanego materiału mają pozostać zachowane.

## Dalsze działania

Przygotować w aplikacji deterministyczny wybór właściciela na podstawie oryginalnego skryptu, z jawnie pokazywanym konfliktem, gdy brak wystarczającego kontekstu. Sam audyt nie zmienia backendowego statusu `ambiguous` ani testów. Nie wykonywano merge, nie modyfikowano `chapters/pl/` ani `main`.

**Postęp 221/257; pozostało 36 wystąpień. Następna partia: 222–234.**