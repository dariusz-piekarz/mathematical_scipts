# Audyt LXVIII (68) — rozdział 19: pierwszy przegląd zastosowań Radona–Nikodyma

Data: 2026-11-23. Repozytorium: dariusz-piekarz/mathematical_scipts.
Istniejąca gałąź: biblioteka-matematyczna-iteracja-6.

## Bramka wejścia

Rozdział 18 zamknięto po audytach LXVI/LXVII dla bloba 6923d52d8e6bf016319465e9f0c18a3470013499. Rzeczywisty przebieg GitHub Actions 45256186337 dał 8/8 regresji rozdziału, 4/4 regresje całej książki i zielone obie kompilacje PDF. Oględziny siedmiu stron zakończono. Zamknięcie utrwalono w raporcie 00-audyt-lxvii-rozdzial-18-zamkniecie-2026-11-23.md, commit 165d15fb474ce2b4fc189aab4a971ae3da5d7736.

## Lektura i przegląd rozdziału 19

Przeczytano cały rozdział: chapters/pl/measure_theory/19-zastosowania-twierdzenia-radona-nikodyma.tex. Objęto kontrolą:
- formułę zmiany miary i jej warunki całkowalności;
- miary obrazowe i utożsamienie pochodnej miary obrazowej z warunkową wartością oczekiwaną;
- obie normalizacje wariacji całkowitej miar probabilistycznych oraz monotoniczność przy przetwarzaniu danych;
- lemat Neymana–Pearsona wraz z progiem, losowaniem i optymalnością dla poziomu alfa;
- wzór Bayesa dla skończonej przestrzeni parametrów;
- wyciąganie czynnika mierzalnego i warunkową nierówność Jensena;
- nieujemność entropii względnej i zasadę przetwarzania danych.

Przy pierwszej kontroli źródła stwierdzono 18 unikalnych etykiet, 14 odsyłaczy, prawidłowe zagnieżdżenie środowisk i brak zakazanych symboli funkcji charakterystycznej.

## Faktyczne uzupełnienie matematyczne

W commicie 5d6b49dc5e04c6593c1e0ed8960a7618a940c43e dodano przykład wyjaśniający losowanie na granicy w lemacie Neymana–Pearsona. Dla X={a,b}, P(a)=7/10, P(b)=3/10, Q(a)=1/5, Q(b)=4/5 i alfa=3/20 stosunek wiarygodności q/p wynosi 2/7 w a oraz 8/3 w b. Przy progu c=8/3 i gamma=1/2 test phi*=1/2 chi_{b} ma poziom 3/20 i moc 2/5, podczas gdy dowolny test deterministyczny o takim poziomie jest zerowy. Dodatek uzasadnia konieczność randomizacji w przypadkach atomowych i nie zmienia wcześniejszych twierdzeń.

Zweryfikowany blob źródła po zmianie: 7ab39bcbc03d32d4533423be39afc58f6bdc500c.

## Trwałe regresje i osobna bramka CI

Utworzono tools/tests/test_measure_theory_ch19.py, osiem przypadków obejmujących zmianę miary, wariację całkowitą i przetwarzanie danych, optymalność testów Neymana–Pearsona, dyskretny wzór Bayesa, warunkową nierówność Jensena i kontrakcję w Lp, entropię względną i integralność LaTeX. Dodanie: commit c4efda09449f1d8185b2874ff88d3d67b4ba9a78. Skorygowano obliczoną sumę ważoną w pierwszym teście (0.85, nie 0.9): commit 7351c08d9288a01e5e06b16f98ff115f4bea90f1. Blob testu: 09120fb3decf47fc13f4276a3f7d769f896dc894.

Nowy .github/workflows/measure-theory-ch19.yml, commit 92d1b4b9e5404a9e0c283968cbe7f6517b7b0948, blob 8ec92c58979ca6eb10a4e12b67e1a9c8f2b1f0f2, uruchamia 8 testów rozdziału i 4 testy globalne książki, pełną kompilację 31 rozdziałów i osobny PDF rozdziału 19, import etykiet z pełnego AUX przez xr-hyper i publikację osobnych statusów measure-theory/ch19-regressions oraz measure-theory/ch19-pdf.

## Aktualny werdykt

Rozdział 19: PIERWSZY PRZEGLĄD WYKONANY, W STABILIZACJI.
W momencie sporządzenia raportu zapytania o statusy CI dla commitu workflow zwracały pustą listę. Nie jest to ani wynik pozytywny, ani porażka. Pełny test 8+4, logi i oględziny rzeczywistych PDF-ów wymagają potwierdzenia. Dopiero po niezależnym drugim audycie, pozytywnym CI i weryfikacji PDF można zamknąć rozdział 19; nie należy rozpoczynać rozdziału 20 wcześniej.
