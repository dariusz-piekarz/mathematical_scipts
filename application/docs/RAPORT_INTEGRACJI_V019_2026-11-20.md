# Biblioteka matematyczna — integracja aplikacji v0.19 z GitHubem

Data: 2026-11-20. Repozytorium: `dariusz-piekarz/mathematical_scipts`, gałąź: `biblioteka-matematyczna-iteracja-6`.

## Rzeczywiste zmiany

1. Zastąpiono niepoprawny `application/backend/generator.py` wersją v0.19 z Biblioteki. Plik na GitHubie przed poprawką zawierał dwie kopie części funkcji; brakowało m.in. analizatora środowisk `theorem_environment_audit`, kontroli wielokrotnych deklaracji i limitów archiwum. Commit `1e68710e78c9ee7e8470152a4d94d72307008b76`.
2. Zaktualizowano testy parsera, API, generatora, workspace oraz testy środowisk i benchmarków do migawki v0.19. Dodano brakujący `application/tests/test_browser_smoke_contract.py`, commit `fbb7f5194d4ee6968c2c511e45d9ce8380680210`.
3. Dodano `/.github/workflows/mathematical-library-app.yml`, commit `5f7552446b5c17962639507efbaa2c1185f8e661`: w GitHub Actions ma odbudować indeks z `chapters/pl/`, uruchomić testy i zachować raport parsera. Nie ma jeszcze potwierdzenia sukcesu workflow.
4. Pozostawiono bez zmian inne pliki backendu, frontend i kanoniczne `chapters/pl/` oraz `main`; wersje `api.py`, `latex_parser.py` i `workspaces.py` odpowiadały archiwum v0.19 (zgodność identyfikatorów blob Git).

## Weryfikacja lokalna

- `python -W default -m unittest discover -s tests -q` na rozpakowanym archiwum v0.19: **84/84, OK**, 4,885 s.
- Osobno wykonano przebudowę bazy za pomocą `python backend/latex_parser.py index --source rozdzialy --db /mnt/data/sync20/rebuilt.db --aliases config/ALIASY_PO_SCALENIACH.json --report /mnt/data/sync20/index_report.json`. Indekser zwrócił kod **2** z powodu zgłoszonych braków/niejednoznaczności odsyłaczy (nie należy utożsamiać tego z sukcesem audytu odsyłaczy).
- Przebudowana migawka: **352 dokumenty**, **15729 obiektów**, **5762 etykiety**, **4453 odwołania**, **4277 rozwiązanych**, **159 niejednoznacznych**, **17 brakujących**; **303 różne nazwy powielonych etykiet**; **0 ostrzeżeń parsera**.
- Zastąpiono testową bazę świeżo wygenerowaną i ponownie uruchomiono testy: **84/84, OK**, 4,332 s. Następnie przywrócono oryginalną bazę w katalogu testowym.

## Ograniczenia — nie uznawać za ukończone

- Weryfikacja 84 testów dotyczy odtworzonej migawki archiwum, nie klona GitHub po integracji, ponieważ środowisko kontenera nie ma dostępu DNS do `github.com`.
- Raport parsera dotyczący repozytorium GitHub musi zostać wygenerowany w CI z bieżącego `chapters/pl/`, a nie z historycznego `rozdzialy/` w archiwum.
- Workflow GitHub Actions jest zapisany, lecz jego zakończenie i status nie zostały jeszcze potwierdzone.
- Testy przeglądarkowe Playwright i pełne testy kompilacji `xr-hyper` na zintegrowanym repozytorium pozostają otwarte.
- Niejednoznacznych etykiet nie wolno masowo przepisywać bez audytu matematycznego i mapy pochodzenia.

## Następny krok

Odczytać wynik workflow GitHub Actions, skontrolować nowy indeks repozytorium i naprawić rzeczywiste regresje po integracji. Następnie wykonać przeglądarkowe testy Explorer/reader/graf oraz kompilację rzeczywistego zestawu międzydziedzinowego `xr-hyper`, po czym dopiero kontynuować przegląd zależności i scalania. Zachowywać globalny standard granularności matematycznych dowodów.