# Wydzielenie geometrii różniczkowej w przestrzeniach funkcyjnych

## Etap 1 — inwentarz i granice zakresu (2026-11-28)

Stan po wydzieleniu teorii dystrybucji: AF ma 26 jednostek, DT 19. Główny workflow AF–DT przeszedł 37 zestawów regresji i kompilację obu książek (run 46136426513). Ostatni dostępny pełny CI aplikacji (46137170416) nadal jest czerwony: 4 niepowodzenia testów dotyczą rozdzielenia logiki i teorii modeli, 2 niepoprawne odsyłacze w całym grafie wymagają identyfikacji. Nie należy deklarować globalnej stabilizacji.

### Materiał przeznaczony do wydzielenia

| Źródło AF | Zakres | Etykiety |
|---|---|---:|
| FA-14 | Pochodne Gâteaux i Frécheta, reguły rachunku, gradient, pochodne słabe krzywych | 36 |
| FA-15 | Pochodne wyższych rzędów, Taylor, twierdzenia o funkcji odwrotnej i uwikłanej, odwracanie i eksponenta operatorowa | 25 |
| FA-16 | Funkcjonały wypukłe, metoda bezpośrednia, subgradient, odwzorowanie proksymalne, zagadnienie brzegowe | 19 |

Łącznie 80 różnych etykiet. FA-14 i FA-15 stanowią podstawę analizy nieliniowej; FA-16 jest częścią wariacyjną nowego skryptu, a nie definicją geometrii różniczkowej. Podział wewnętrzny może się zmienić podczas rozbudowy; etykiety oryginalne muszą pozostać. FA-15A i FA-15B pozostają w analizie funkcjonalnej (całki wektorowe, miary, własność Radona–Nikodyma i wektorowe przestrzenie Sobolewa); w nowym skrypcie wykorzystujemy wyniki przez odsyłacze. FA-26–33 pozostają w AF: geometria liniowa przestrzeni Banacha, bazy, aproksymacja i teoria operatorów nie są geometrią rozmaitości. Abstrakcyjne topologiczne iloczyny tensorowe pozostają obecnie w DT, bez dublowania.

### Zależności zwykłych odsyłaczy

- FA-14 → AF: sec:integral-vector15b.
- FA-15 → brak zewnętrznych zwykłych odsyłaczy w obrębie planowanego wydzielenia.
- FA-16 → AF: cor:weak-convex-closure, thm:orth-decomposition13, thm:krein-milman, cor:bauer9, cor:alaoglu-norm.
- AF-15A → przenoszone: sec:wariacyjny16, sec:gateaux-frechet14.
- AF-15B → przenoszone: sec:wariacyjny16, def:weak-curve-derivative14.
- AF-33 → brak takich zwykłych odsyłaczy.

To inwentarz wymienionych jednostek, nie pełne przeszukanie repozytorium. Przed przełączeniem rozszerzyć o wszystkie pozostające rozdziały i jawne atlasref. Zachować również sześć istniejących atlasref w trzech źródłach (do AM1, LA i DG). Przerywać cykle kompilacji przez jawne odsyłacze między książkami, nie przez kopiowanie dowodów.

## Proponowany układ docelowy

1. Rachunek różniczkowy w przestrzeniach Banacha i Hilberta: materiał FA-14/15, uporządkowanie pojęć i odwołania do całek wektorowych.
2. Rozmaitości modelowane na przestrzeniach Banacha: atlasy i mapy, przestrzenie styczne, różniczki odwzorowań, podrozmaitości rozszczepione, zanurzenia i submersje; warunki istnienia dopełnień.
3. Wiązki wektorowe, pola wektorowe, lokalne potoki, równania różniczkowe na rozmaitościach Banacha; warunki istnienia, jednoznaczności i gładkiej zależności.
4. Przestrzenie odwzorowań i przekrojów: C^k dla zwartej dziedziny, przestrzenie Sobolewa z warunkami na wykładniki, operatory podstawiania, różniczkowalność składania i odwracania; jawne rozróżnienie utraty pochodnych.
5. Geometria rozmaitości Hilberta, metryki silne i słabe, gradienty, połączenia i geodezyjne przy odpowiednich założeniach.
6. Rachunek wariacyjny i optymalizacja: FA-16, warunki stacjonarności, mnożniki Lagrange'a, druga wariacja, przykłady funkcjonałów na przestrzeniach funkcyjnych. Metoda bezpośrednia zależy od AF; zastosowania PDE pozostają w RRC.
7. Rozszerzenie: rozmaitości Frécheta, różniczkowanie Bastiani, kontrprzykłady do klasycznego twierdzenia odwrotnego, wprowadzenie do twierdzenia Nasha–Mosera z warunkami tame. Nie przenosić automatycznie twierdzeń Banacha na przestrzenie Frécheta.

## Kolejność realizacji

- Przygotować mapę etykiet i kopie kandydackie FA-14–16 poza katalogiem kanonicznym; przeprowadzić audyt dowodów i kolejności zależności.
- Dodać brakujące podstawy rozmaitości Banacha i przestrzeni odwzorowań; porównać zakres AM1, AM2 i DG, unikając duplikatów.
- Przenieść istniejące testy oraz przygotować test zachowania wszystkich 80 etykiet, indeksowania, aliasów i kompilacji.
- Przełączyć katalog, źródła i odsyłacze dopiero atomowo; przed usunięciem starych rozdziałów potwierdzić kompletność.
- Używać istniejących workflow, bez dodatkowych automatyzacji. Audyty rozdziałowe do stabilizacji i osobny audyt kontrolny.

Na tym etapie nie przeniesiono żadnego rozdziału i nie dodano nowego aktywnego skryptu.
