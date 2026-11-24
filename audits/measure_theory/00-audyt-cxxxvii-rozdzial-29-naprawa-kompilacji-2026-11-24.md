# Audyt CXXXVII (137) — naprawa kompilacji rozdziału 29
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia 6135157a4c2f98f7743d8a3ed2ebff42a3982e94; blob 89115c4b293c7c5a9a0ab9b2b16967cf97504d54.
## Wynik poprzedniego CI
Run 45370276374: regresje 12+4 success, PDF failure (job 138362479157), publikacja statusów success. Log wskazuje undefined control sequence w rozdziale 29, wiersz 164, polecenie mathscr. Nie powstał PDF; artefakt 14908922748 zawierał wyłącznie log.
## Naprawa
Commit 192d20d95f527141d75392ab87ee086d3182d8f2; blob 303e077c31f2c4c3c7a144b81e2945a5bbdced4d.
- Zastąpiono sześć wystąpień mathscr S przez mathcal S.
- Porównano środowiska rozdziału z preambułą. Niezdefiniowane stwierdzenie zmieniono na lemat oraz dostosowano jego przywołanie.
- Zachowano 37 etykiet w kolejności; bez zmian preambuły ani matematycznej treści.
- Po konflikcie zapisu raportu ponownie potwierdzono blob źródła.
## Nowy przebieg
Run 45371886126 był w toku podczas kontroli. Kompilacja i rzeczywista kontrola PDF nadal otwarte. Nie zamknięto rozdziału. Stan 28/31.
