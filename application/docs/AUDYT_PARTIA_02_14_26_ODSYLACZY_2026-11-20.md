# Biblioteka matematyczna — audyt odsyłaczy, partia 02 (wystąpienia 14–26)

Data: 20 listopada 2026. Źródła: kanoniczne `chapters/pl/` gałęzi `biblioteka-matematyczna-iteracja-6` i `reference_provenance_audit_355.json` (355 rozdziałów, 257 nierozwiązanych wystąpień w migawce). Sprawdzono kontekst 13 cytowań w `DG-07` i `DG-08` oraz numery deklaracji kandydatów w raporcie pochodzenia. Nie zmieniano plików źródłowych. To audyt referencji, nie pełny audyt dowodów ani scalanie.

| Nr | Miejsce | Cytowana etykieta | Kandydaci (wiersze deklaracji) | Ocena kontekstu i rekomendacja | Status |
|---|---|---|---|---|---|
| 14 | DG-07:1385 | `sec:homologia-symplicjalna` | DG-08:30, TOP-05:28 | Zapowiedź definicji łańcuchów i dowodu `∂²=0` w następnym rozdziale DG-08; preferować DG-08. | propozycja lokalna |
| 15 | DG-07:1540 | `def:topologia-ilorazowa` | DG-01:104, TOP-01:52 | Topologia identyfikacji rozłącznej sumy sympleksów; preferować definicję z wcześniejszego DG-01. | propozycja lokalna |
| 16 | DG-07:1903 | `def:topologia-ilorazowa` | DG-01:104, TOP-01:52 | Uniwersalna własność topologii ilorazowej dla doklejanej komórki; preferować DG-01, sprawdzając zgodność przyjętej definicji z użyciem. | propozycja lokalna |
| 17 | DG-07:2319 | `ch:algebra-homologiczna` | DG-06:2, TOP-03:2 | Zapowiedź użycia długich ciągów z wcześniejszego rozdziału; preferować DG-06. | propozycja lokalna |
| 18 | DG-08:4 | `ch:algebra-homologiczna` | DG-06:2, TOP-03:2 | Homologia kompleksów łańcuchowych jest opracowana w DG-06; preferować DG-06. | propozycja lokalna |
| 19 | DG-08:7 | `ch:topologia-algebraiczna-podstawy` | DG-07:2, TOP-04:2 | Sympleksy wprowadzone bezpośrednio w DG-07; preferować DG-07. | propozycja lokalna |
| 20 | DG-08:26 | `thm:homologia-char-zero` | DG-06:1795, TOP-03:1512 | Zapowiedź zmiany współczynników; preferować DG-06, ale **wymaga kontroli matematycznej**, czy twierdzenie o charakterystyce zero rzeczywiście pokrywa ogólną zmianę współczynników, czy tylko szczególny przypadek. | propozycja warunkowa |
| 21 | DG-08:45 | `def:kompleks-symplicjalny` | DG-07:1435, TOP-04:995 | Definicja skończonego kompleksu symplicjalnego potrzebna do konstrukcji grup łańcuchów; preferować DG-07. | propozycja lokalna |
| 22 | DG-08:254 | `def:delta-kompleks` | DG-07:1509, TOP-04:1049 | Opis sympleksów charakterystycznych i identyfikacji ścian; preferować DG-07. | propozycja lokalna |
| 23 | DG-08:518 | `thm:homotopia-homologia` | DG-06:988, TOP-03:839 | W dowodzie skonstruowano homotopię łańcuchową indukowaną przez homotopię topologiczną; odpowiednie twierdzenie algebraiczne należy do DG-06. Preferować DG-06, bez utożsamiania obu rodzajów homotopii. | propozycja lokalna |
| 24 | DG-08:644 | `prop:ses-iloraz` | DG-06:1237, TOP-03:1063 | Krótki ciąg dokładny kompleksów łańcuchowych prowadzi do długiego ciągu dokładnego homologii względnej; preferować DG-06, zweryfikować hipotezy i definicję homomorfizmu łączącego. | propozycja lokalna |
| 25 | DG-08:969 | `lem:pieciu` | DG-06:1996, TOP-03:1705 | Wnioskowanie z diagramu długich ciągów dokładnych; preferować DG-06, pod warunkiem kontroli wymaganych czterech izomorfizmów. | propozycja lokalna |
| 26 | DG-08:1045 | `thm:les-homologia` | DG-06:515, TOP-03:393 | Ciąg Mayera–Vietorisa wyprowadzany z krótkiego ciągu kompleksów; preferować DG-06, sprawdzić dokładność krótkiego ciągu w każdym stopniu. | propozycja lokalna |

## Wynik i ograniczenia

- 13 niejednoznacznych cytowań, 0 brakujących w tej partii; 12 lokalnych propozycji i 1 propozycja warunkowa (`DG-08:26`).
- Po dwóch partiach przeanalizowano 26 z 257 nierozwiązanych wystąpień; pozostaje 231. To licznik **przeglądu**, nie licznik naprawionych odsyłaczy.
- Zweryfikowano w źródłach tekst otaczający każde cytowanie i porównano go z mapą kandydatów. Nie przeprowadzono pełnego przeglądu treści wszystkich twierdzeń kandydackich, kompilacji `xr-hyper` ani testu PDF; propozycje nie są automatycznymi rozstrzygnięciami.
- Przyszłe poprawki muszą zachować odrębne skrypty, wszystkie warianty dowodów, stabilność nazw i mapę pochodzenia. Obecnie **nie rozpoczynać scalania działów**; kolejność docelowego scalania to podstawy matematyki, a potem kolejne gałęzie, po skompletowaniu materiału.
- W pełnym audycie matematycznym wymagać motywacji przed definicją, ścisłych kwantyfikatorów, pełnych nazw obiektów, rozróżnienia modelu od metateorii, dokładnych dowodów i przykładów zgodnie z globalnymi standardami Biblioteki.

## Następny krok

Wystąpienia 27–39 z raportu pochodzenia; osobno pogłębiona kontrola twierdzenia `thm:homologia-char-zero` przed jakąkolwiek zmianą `DG-08:26`. Dopiero po matematycznej weryfikacji konkretnego celu rozważać kontrolowane poprawki lokalnych odsyłaczy z testem regresyjnym i kompilacją.