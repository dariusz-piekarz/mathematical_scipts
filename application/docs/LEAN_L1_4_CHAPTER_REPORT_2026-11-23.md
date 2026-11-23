# Atlas / Lean — L1.4.1: diagnostyczny raport rozdziałowy

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Aktualny stan: 3/3 techniczne PASS; `stabilizing`, oczekuje na niezależny odbiór.**

## Zakres pierwszej zmiany L1.4

- Odczytowy `GET /api/lean/chapter-report?module_id=LST-01` pokazuje wersjonowany raport (schemat 1) dla istniejącego rozdziału indeksu, listę zarejestrowanych formalizacji i rozdzielne liczniki `ready/draft/stale` oraz `statement_approved`.
- Sprawdzane są bajty tekstu z indeksu wobec zapisanego SHA256. Powiązania, etykiety i kanoniczny plik TeX są weryfikowane przez istniejący `lean_catalog`. Uszkodzony indeks zeruje pozytywne deklaracje. Nieznany rozdział to HTTP 404, błędne ID to HTTP 400.
- Raport nie odczytuje plików historii uruchomień, nie uruchamia Lean, nie oblicza kosztownego fingerprintu i nie aktywuje nowego cache. `run_history_checked=false`, `dependency_fingerprint_checked=false`, `proof_status_included=false`, `certificate=false`. Stan `ready` nie oznacza `compiled` ani równoważności Lean–LaTeX.
- Moduł agregujący jest ograniczony wcześniejszym limitem katalogu (250 wpisów). Nie jest atomowym snapshotem równoczesnych zmian plików/katalogu i indeksu SQLite. Nie służy do poświadczania pochodzenia wyników wykonania Lean.

## Kryteria akceptacji i stabilizacja

1. Testy jednostkowe: gotowe i puste rozdziały, błędne identyfikatory, uszkodzony SHA i zastąpiony TeX, niedostępność historii/fingerprintu oraz brak fałszywych pozytywnych statusów.
2. Test HTTP dla rzeczywistego LST-01; brak `proof_status` i dowolnych certyfikatów.
3. Po zmianie: natywne Linux/Windows, pełne CI aplikacji z Chromium, przypięty Lean 4.26.0/Mathlib i osobny sceptyczny audyt, a następnie 2+1 na dokładnie jednym SHA. Zmiana kodu resetuje licznik.
4. Dopiero po stabilizacji tej jednostki rozważyć następny fragment: strategię cache zależności i miarodajny pomiar narzutu pełnego fingerprintu na rzeczywistym Mathlib — bez ograniczania istniejących kontroli `before/locked/after`.

**Granice:** kompilacja i kontrola aksjomatów to diagnostyka wykonania Lean. Nawet poprawne SHA, `statement_status=approved` i `compiled` nie stanowią automatycznego poświadczenia zgodności twierdzeń z LaTeX-em. Zachować `certificate=false`.

**Uwaga do planu:** w dokumentacji historycznej oznaczenie L1.3 użyto także dla pilotażu 20–30 formalizacji. Zamknięty techniczny L1.3 dotyczył odczytu lokalnych rekordów; przejście do tego podetapu architektury nie jest deklaracją ukończenia całego pilotażu.

## Wewnętrzny przegląd sceptyczny przed stabilizacją

Przegląd odkrył potencjalny wyciek przyszłych pól historii: naiwny raport przekazywał całą strukturę z katalogu, a więc przyszłe rozszerzenie katalogu mogłoby wprowadzić do raportu `proof_status` mimo `proof_status_included=false`. Zastosowano ścisłą projekcję pól i regresję z podrobionym `compiled`, logiem i `certificate=true`. Wynik 2+1 trzeba liczyć od **nowego** commita, bez zaliczania wcześniejszego CI.

## Usterka wykryta podczas kolejnego przeglądu sceptycznego

Dwa odrębne odczyty SQLite (początkowy `documents` i późniejszy
`lean_catalog.list_formalizations`) mogły należeć do różnych generacji
indeksu. W szczególności katalog mógł zwrócić status `ready` ze
starszego punktu kontrolnego, a dokument mógł już mieć inne bajty i
inny, spójny SHA256. Dodano końcowe ponowne sprawdzenie
`documents.sha256` i całego `documents.content`. Wykryta podmiana
ustawia `source_index_status=changed_during_report`, wszystkie
powiązania jako `stale`, `statement_status=needs_review` i zeruje
`statement_approved`, bez zwracania poprzedniego SHA jako aktualnego.
Test regresyjny wstrzykuje taką zmianę pomiędzy odczytami i sprawdza
odmowę podniesienia statusu. Nie oznacza to atomowego snapshotu przy
dowolnej późniejszej zmianie ani bezpieczeństwa nieufnego drzewa plików.
Kandydat sprzed tej poprawki nie może otrzymać końcowego odbioru L1.4.1.

## Kolejny sceptyczny audyt: kanoniczny plik LaTeX

Wykryto możliwy fałszywie dodatni status `ready`: starszy katalog
akceptował wpis z przypiętym SHA256, ale bez podanej fizycznej ścieżki
kanonicznego pliku `.tex`; nie miał wtedy czego weryfikować na dysku.
Raport L1.4.1 wymaga teraz jawnej ścieżki i ponownie sprawdza treść
kanonicznego pliku **po** odczycie katalogu. Zmiana manifestu między
odczytami lub brak możliwości potwierdzenia ścieżki powoduje
`unverifiable_canonical_source`, `stale`, `needs_review`,
bez zatwierdzenia. Dodano dwie regresje negatywne: manifest bez ścieżki
oraz zmiana bajtów kanonicznego TeX po odczycie katalogu. Nie jest to
pełna migawka atomowa ani formalna certyfikacja zgodności twierdzeń;
`certificate=false`. Rygor 2+1 liczyć od nowego SHA tej poprawki.

## Rozliczenie stabilizacji — 2026-11-23, 13:00 Europe/Warsaw

Kandydat `1c4b89b1a9ef8affe95e3073739d99bc1c57aa2d`.
[GitHub Actions 2+1 #45160961943](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45160961943)
wykonał wszystkie trzy rundy i zakończył się `success`:
`application=success`, `linux_windows=success`,
`pinned_lean_mathlib=success`, `skeptical_regression_suite=success`.
Każda runda zawiera 729 testów jednostkowych, 10 uprzednio
sklasyfikowanych pominięć i 0 nierozliczonych. Wszystkie 10 testów
L1.4.1 zostało ponownie potwierdzonych w osobnym pełnym CI;
przypięty Lean/Mathlib w każdej rundzie skompilował 4 pliki i 18 twierdzeń
z `axiom_check=passed`. [Artefakt decyzji
walidacyjnej](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45160961943/artifacts/14814696978)
zawiera `problems=[]` i **`status=stabilizing`,
`skeptical_review=pending`, `certificate=false`**.

Jedynym brakującym formalnym warunkiem awansu jest zewnętrzna,
uwierzytelniona decyzja recenzenta, niezależna od autora zmian
i od automatycznych testów. Zgłoszenie do odbioru:
[issue #8](https://github.com/dariusz-piekarz/mathematical_scipts/issues/8).
Nie tworzyć deklaracji `stable` ani niesygnowanego pozornego
zatwierdzenia. Po aprobacie trzeba zachować SHA i powiązać decyzję
z tą wersją; zmiana produkcyjna wymaga nowego 2+1.

## Niezależna analiza bramki po 3/3: wycofanie aprobaty w trakcie raportu

Przy odbiorze technicznym `1c4b89b1` wykryto kolejny rzeczywisty
przypadek niespójności: status `statement_status` z pierwszego
manifestu Lean nie był ponownie porównywany po odczycie katalogu.
Podmiana `approved` na `needs_review` mogła pozostawić pozytywne
`statement_approved` w raporcie. Podobnie można było dopisać lub
usunąć wpisy manifestu albo przenieść etykietę w SQLite bez zmiany
`documents.sha256`, podczas gdy katalog raportował poprzedni stan.

Nowa poprawka:
- porównuje zestawy identyfikatorów formalizacji w całym rozdziale;
- sprawdza ponownie `statement_status` i podstawowe pola wiązania;
- ponownie rozstrzyga właściciela etykiety na aktualnym indeksie;
- przy rozbieżności ustawia odpowiednio
  `changed_manifest_during_report` albo `changed_index_binding`
  oraz obniża status do `stale/needs_review`;
- utrzymuje limit 250 wpisów także dla drugiego odczytu.

Trzy niezależne negatywne regresje wstrzykują wymienione zmiany
dokładnie pomiędzy odczytami. To nadal kontrola diagnostyczna, a nie
atomowa migawka ani certyfikat Lean–LaTeX. **Wynik 3/3 dla
`1c4b89b1` pozostaje prawdziwym historycznym dowodem, ale
nie może zostać przypisany nowemu kandydatowi.** Ponowne 2+1
obowiązkowe na nowym SHA. `certificate=false`.

## Techniczna stabilizacja poprawionego L1.4.1 — wynik 3/3

Nowy kandydat `a1f93d985778492082a66db3975d05e9d73ed763`
(oddzielny od wcześniej rozliczonego `1c4b89b1`) otrzymał
[3/3 pełnych PASS w workflow #45175198218](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45175198218)
zakończonym 2026-11-23 12:49 UTC. W każdej rundzie jest `732` testów
Pythona, `10` sklasyfikowanych pominięć i `0` nierozliczonych.
Prawdziwy Lean 4.26.0/Mathlib o commicie
`2df2f0150c275ad53cb3c90f7c98ec15a56a1a67` skompilował
`4` pliki / `18` twierdzeń przy `axiom_check=passed`.
Windows i Chromium, testy regresyjne, sceptyczny kontrakt oraz
agregacja końcowa również zakończyły się sukcesem.

[Artefakt `atlas-validation-status`](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45175198218/artifacts/14820217988)
jawnie zapisuje `problems=[]`, `status=stabilizing`,
`skeptical_review=pending` oraz `certificate=false`.
Zgłoszono [wniosek o niezależny odbiór #9](https://github.com/dariusz-piekarz/mathematical_scipts/issues/9).
Formalnego statusu `stable` **nie nadano**, dopóki nie ma osobno
uwierzytelnionej aprobaty recenzenta dla dokładnie tego SHA.
Zmiana kodu resetuje cały 2+1. Nie rozpoczęto L1.4.2.
