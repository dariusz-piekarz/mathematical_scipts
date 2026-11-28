# Topologia ogólna — audyt globalny 29: wersjonowany rejestr 13–18

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Zamrożony punkt pomiaru:** commit `e7ff9254923fd87f9cad05301b15704e7038befd`. Wszystkie źródła poniżej pobrano z *tego samego* commitu (nie z ruchomego HEAD).

## Metoda

Bezpośrednio przeczytano źródła sześciu rozdziałów `chapters/pl/general_topology/13-*.tex`–`18-*.tex`. Policzono rozpoczęcia i zakończenia środowisk `proof`, `figure`, `tikzpicture`, komendy `label`, `ref`/`eqref`/`pageref`/`autoref`/`nameref`/`cref`/`Cref`. Porównano powtórzenia etykiet w każdym pliku i w całym pobranym bloku 13–23. Weryfikację terminologii ograniczono do wzorców `zwartościowani*`, `zbieżności zwartej`, `pierwszo-przeliczaln*`, `drugoprzeliczaln*`, `sekwencyjn*`. Odczytano odpowiednie raporty pełnych audytów globalnych i sprawdzono zgodność deklarowanych blobów. **To audyt inwentarza i pochodzenia wcześniejszych sprawdzeń, a nie nowa samodzielna kontrola matematyczna 49 dowodów.**

| Rozdział | Blob źródła | Proof | TikZ | Figure | Labels | Refs | Raport obejmujący wszystkie dowody |
|---|---|---:|---:|---:|---:|---:|---|
| 13 — Zupełność jednostajna | `c9078636452731e42a56196e84b5ed9831120e6b` | 9 | 0 | 0 | 24 | 5 | `13-zupelnosc-jednostajna-iteracja-06.md`, następnie 07–09 (2+1) |
| 14 — Zwartość lokalna | `24ca61f0e19fe6674719fc76e53073aa82cc755c` | 7 | 0 | 0 | 18 | 4 | `00-globalny-audyt-15-rozdzial-14-pelna-kontrola-dowodow.md` |
| 15 — Parazwartość | `82e0fb5be75489017c8ea1844c698c87ce580901` | 7 | 0 | 0 | 21 | 4 | `00-globalny-audyt-16-rozdzial-15-wszystkie-dowody.md` |
| 16 — Funkcje ciągłe i uzwarcenia | `1c2fcb925d62120feaea468400e48842a508a062` | 7 | 0 | 0 | 18 | 0 | `00-globalny-audyt-18-rozdzial-16-wszystkie-dowody.md` |
| 17 — Uzwarcenia Aleksandrowa i Čecha–Stone'a | `6c4e76dd0d2ea1e75a830f858af9d77d163bf7c4` | 10 | 0 | 0 | 20 | 3 | `00-globalny-audyt-19-rozdzial-17-wszystkie-dowody.md` |
| 18 — Przestrzenie odwzorowań | `f7340514548ed3dfb5d98793bf7068fd84276c30` | 9 | 0 | 0 | 18 | 1 | `00-globalny-audyt-20-rozdzial-18-wszystkie-dowody.md` |
| **Razem** | — | **49** | **0** | **0** | **119** | **17** | **6 zgodnych pozycji wersjonowanych** |

## Wyniki kontroli i powiązanie z audytami matematycznymi

1. Wszystkie 49 środowisk `proof` mają sparowane rozpoczęcia i zakończenia. W sześciu plikach nie ma środowisk `tikzpicture` ani `figure`, dlatego nie należy dopisywać im historycznych 27 ilustracji całej książki.
2. Brak powtórzonych etykiet w pojedynczym źródle, a przegląd etykiet wszystkich plików 13–23 potwierdza brak kolizji **w obrębie 13–23**. Wszystkie 17 odsyłaczy z rozdziałów 13–18 rozwiązuje się w swoich rozdziałach.
3. Nie wykryto pięciu wyszukiwanych klas niepożądanych form terminologicznych; nie jest to pełny audyt stylistyczny.
4. **Rozdział 13:** bloby z dokumentacji 06–09 oraz obecnego źródła są identyczne: `c9078636...`. Poprawiona niepustość `B(H,E)` używa symetrycznego `D⊆E` przy odwracaniu relacji `widehat D`. Starszy raport `00-globalny-audyt-09...` ma historyczny blob `33200912...`; **nie** zalicza się go jako audytu po korekcie. Raporty 07–08 i potwierdzający 09 dokumentują osobne 2+1, a workflow `45070070493` dowodzi wykonania nowego testu regresji.
5. **Rozdziały 14–18:** odpowiednio raporty globalne 15, 16, 18, 19, 20 deklarują pełne sprawdzenie 7/7, 7/7, 7/7, 10/10 i 9/9 środowisk `proof`; odczytane w nich bloby odpowiadają dokładnie plikom na zamrożonym commicie. Starsze, węższe audyty wybranych twierdzeń nie są tu błędnie przedstawiane jako audyty całych rozdziałów.
6. Aktualność raportów względem źródeł została w ten sposób uzgodniona, jednak **zgodność wersji oraz licznika nie jest nową niezależną weryfikacją każdego dowodu**.

## CI, zakres i następna iteracja

Dla punktu pomiaru `e7ff9254923fd87f9cad05301b15704e7038befd` workflow [General topology chapter validation #45129914798](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45129914798) ma status `completed/success` (zweryfikowany przez GitHub API).

Nie pobierano ponownie PDF w tym pomiarze; wcześniejsze dokumenty zawierają rzeczywiste kontrole kompilacji, logów i wybranych stron. Zielony CI nie jest sam w sobie niezależnym audytem matematycznym ani wizualnym.

**Wynik tego audytu:** rejestr źródeł 13–18 i powiązanie z raportami pełnych dowodów — **PASS**, bez zmiany LaTeX. **Następny krok:** identyczny inwentarz rozdziałów 19–23 oraz rozliczenie rzeczywistej liczby ilustracji i wszystkich dowodów na jednym commicie. Nie zamykać jeszcze globalnego audytu ani automatyzacji.
