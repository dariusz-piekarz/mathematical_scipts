# Biblioteka matematyczna — audyt odsyłaczy, partia XIV (170–182)

Data: 20 listopada 2026. Zakres: 13 kolejnych wystąpień ze źródłowego raportu `reference_provenance_audit_355.json` (355 dokumentów, 257 nierozstrzygniętych wystąpień). **Nie zmieniono** tekstów matematycznych, oryginalnych etykiet, odsyłaczy ani wariantów dowodów.

## Stan wejściowy, zależności i kryterium akceptacji

Odczytano aktualny dziennik `/Biblioteka matematyczna/aplikacja/ROADMAP_I_DZIENNIK.md`, globalny standard granularności, poprzedni raport partii XIII i indeks 355 rozdziałów. Dziennik potwierdza audyt 169/257. Kanoniczne pliki sprawdzano na gałęzi `biblioteka-matematyczna-iteracja-6` repozytorium `dariusz-piekarz/mathematical_scipts`, a nie na równolegle edytowanych skryptach w Bibliotece.

Zależności: rozdziały tomu IV cytują 12 etykiet tomów I–III, importowanych z `.aux` przez `xr-hyper` w `books/pl/probability_volume_iv.tex`, za pomocą prefiksów `I-`, `II-`, `III-`. W docelowych rozdziałach etykiety zachowują oryginalne nazwy `ch:...`; prefiks należy do mechanizmu importu, nie do deklaracji `\label`.

Kryteria: (1) ustalić rzeczywisty cytujący plik i numer wiersza dla wszystkich 13 wystąpień; (2) odczytać odpowiadającą deklarację w źródłowym rozdziale docelowym; (3) zweryfikować zgodność znaczeniową; (4) nie wprowadzać atrap etykiet; (5) oddzielić potwierdzoną obecność deklaracji od jeszcze niesprawdzonego działania linku w PDF.

## Wyniki kontroli

| Pozycja | Źródło i wiersz | Cytowana etykieta | Cel potwierdzony w kanonicznym pliku |
|---:|---|---|---|
| 170 | P4-00:18 | `III-ch:path-integrals` | III/15 — całki po trajektoriach; `\label{ch:path-integrals}` |
| 171 | P4-01:3 | `I-ch:probability` | I/02 — przestrzeń probabilistyczna; `\label{ch:probability}` |
| 172 | P4-01:3 | `I-ch:random-variables` | I/04 — zmienne losowe; `\label{ch:random-variables}` |
| 173 | P4-01:3 | `II-ch:procesy` | II/01 — procesy stochastyczne; `\label{ch:procesy}` |
| 174 | P4-02:3 | `I-ch:distributions` | I/06 — rodziny rozkładów; `\label{ch:distributions}` |
| 175 | P4-02:3 | `I-ch:expectation` | I/05 — wartość oczekiwana; `\label{ch:expectation}` |
| 176 | P4-02:3 | `I-ch:convergence` | I/07 — zbieżność zmiennych losowych; `\label{ch:convergence}` |
| 177 | P4-02:3 | `I-ch:clt` | I/09 — centralne twierdzenie graniczne; `\label{ch:clt}` |
| 178 | P4-03:3 | `I-ch:condexp` | I/10 — warunkowa wartość oczekiwana; `\label{ch:condexp}` |
| 179 | P4-08:3 | `I-ch:lln` | I/08 — prawa wielkich liczb; `\label{ch:lln}` |
| 180 | P4-08:3 | `I-ch:clt` | I/09 — centralne twierdzenie graniczne; `\label{ch:clt}` |
| 181 | P4-16:3 | `II-ch:ctmc` | II/05 — łańcuchy Markowa w czasie ciągłym; `\label{ch:ctmc}` |
| 182 | P4-16:3 | `II-ch:gauss` | II/06 — procesy gaussowskie; `\label{ch:gauss}` |

**Wniosek:** 13/13 odsyłaczy posiada istniejący, semantycznie zgodny rozdział docelowy; występuje 12 różnych etykiet. Wszystkie 13 są w indeksie oznaczone jako `missing`, ale dla tych konkretnych cytowań diagnoza „brak rozdziału” jest niepoprawna. Odpowiedni przyszły status aplikacji: `external_resolved` po weryfikacji konfiguracji i `.aux`. Nie należy usuwać prefiksów ani przemianowywać oryginalnych etykiet.

## Kontrola matematyczna i redakcyjna

W P4-01 cytowanie podstaw przestrzeni probabilistycznej i zmiennych losowych odpowiada definicji eksperymentu statystycznego; rozdział II/01 dostarcza modelu obserwacji zależnych w czasie. W P4-02 rodziny rozkładów, wartość oczekiwana, rodzaje zbieżności i centralne twierdzenie graniczne są właściwym zapleczem dla statystyk z próby. W P4-03 odsyłacz do warunkowej wartości oczekiwanej ma właściwy zakres. W P4-08 prawa wielkich liczb i centralne twierdzenie graniczne są prawidłowym punktem odniesienia dla asymptotycznej estymacji, lecz **nie wystarczają same** do każdego twierdzenia o asymptotycznej normalności estymatora MLE: potrzebne są dalsze hipotezy regularności i identyfikowalności, które należy audytować oddzielnie. W P4-16 odsyłacze do łańcuchów Markowa i procesów gaussowskich odpowiadają wymienionym klasom procesów, ale **same nie są ogólnym twierdzeniem o stacjonarności**; jej hipotezy należy kontrolować lokalnie w tym rozdziale. W P4-00 odsyłacz do całek po trajektoriach prowadzi do faktycznie istniejącego rozdziału III/15.

Kontrola krytyczna: powyższe sprawdza **zgodność cytowanych tematów**, nie poprawność wszystkich dowodów w tych rozdziałach; nie przypisuje odsyłaczom mocy silniejszej niż wynika z ich treści. Nie dokonywano skrótowego przepisywania definicji ani dowodów. Obowiązują globalne zasady pełnych nazw obiektów, w szczególności „liczba kardynalna”, oraz standard motywacji, kwantyfikatorów i szczegółowych uzasadnień.

## Testy i ograniczenia

Wykonano skrypt `verify_batch14.py` na odczytanym pliku JSON: sześć kontroli strukturalnych zaliczonych (liczba, kolejność, status, tom cytujący, unikalność celów, zapis wyniku). Wynik maszynowy: `PROVENANCE_BATCH_170_182.json`, z SHA-256 wejściowego indeksu. Ręcznie odczytano wszystkie 12 kanonicznych plików celowych i sześć plików cytujących na GitHubie. **Nie wykonano** kompilacji TeX, kontroli PDF/`.aux`, testów przeglądarkowych ani przebudowy indeksu; brak podstaw do deklarowania naprawienia tych 13 pozycji w działającej aplikacji. Nie modyfikowano `main`, `chapters/pl/` ani katalogu wspólnych rozdziałów.

## Stan i następny krok

Audyt odsyłaczy: **182/257 przejrzanych, 75 pozostałych**. Nie jest to liczba naprawionych linków. Kolejna partia: **183–195**. Równoległy etap techniczny: implementacja jawnego rozpoznawania prefiksów `xr-hyper`, testy `.aux` i poprawne rozróżnienie `missing` od `external_resolved`, bez zmiany oryginalnych `\label` i `\ref`.