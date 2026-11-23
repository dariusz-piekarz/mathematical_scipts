# L1.1 — sceptyczny audyt tożsamości deskryptora `.olean`

**23 listopada 2026 r.** · gałąź `biblioteka-matematyczna-iteracja-6` · zakres: wyłącznie fingerprint instalowanych artefaktów Lake.

## Niezależnie sprawdzona hipoteza

Sukces technicznej serii 2+1 [#45131721594](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45131721594) na SHA `ec591bfdb5923ab09220b2c56bbe64860668da3c` potwierdzał trzy pełne zestawy: aplikacja + Chromium, Linux/Windows i realny Lean+Mathlib; każdy zestaw aplikacji miał 682 testy, 10 sklasyfikowanych pominięć. Raport evidence zakończył się `status=stabilizing`, `skeptical_review=pending`, `certificate=false`.

W sceptycznej inspekcji `application/backend/lean_environment.py` wykryto nowy problem w `_olean_tree`: `artifact.stat()` przed otwarciem, następnie `artifact.open("rb")`, potem `os.fstat(fd).st_size` oraz `artifact.stat()` po odczycie. W poprzedniej implementacji uchwyt odczytu i `artifact` **nie były sprawdzane pod kątem zgodności tożsamości urządzenie/inode**. Przy podstawieniu odczytu z innego zwykłego pliku o identycznej wielkości, a następnie niezmienionym katalogowym `artifact`, metadane ścieżki przed i po są identyczne, a rozmiar deskryptora się zgadza. Fingerprint przypisywałby obce bajty do metadanych oryginalnego artefaktu.

## Usunięcie defektu

- Commit [`8f9ac3fad8850c99afb6bb0b9172e27e2068f9ba`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/8f9ac3fad8850c99afb6bb0b9172e27e2068f9ba): w trakcie otwartego strumienia odczytać jego `os.fstat(fd)`, wymagać zwykłego pliku przez `stat.S_ISREG` oraz zgodności `st_dev` i `st_ino` z wynikiem przed otwarciem. Dodatkowo porównać `st_dev` w `stat` po odczycie. Na Windows zachować porównanie czasów i metadanych ścieżki za pomocą tej samej metody `Path.stat()`, ze względu na różnice semantyki czasu tworzenia dla `fstat`. Bez zmian w serializowanym słowniku i SHA256.
- Commit [`dda19fc9eb8fc274296d8cf15980f52354241301`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/dda19fc9eb8fc274296d8cf15980f52354241301): rzeczywisty deskryptor do innego pliku o tej samej wielkości i niezmieniona ścieżka wyjściowa; niezależnie podmiana deskryptora na `os.devnull`. Oba przypadki muszą zostać odrzucone zamiast zwrócić fingerprint.
- [Szybki Linux/Windows #45133428850](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45133428850): `completed/success`, Linux 140 testów (5 pominiętych), Windows 43 testy (3 pominięte), oba nowe testy wykonane i zakończone sukcesem; to **nie** zastępuje jeszcze pełnego 2+1 i rzeczywistego Lean+Mathlib dla zmodyfikowanego kodu.

## Granice poprawki i kolejne kontrole

- Identyfikatory `st_ino/st_dev` są właściwościami systemu plików; wzorzec nie jest pełnym mechanizmem zapobiegania wszystkim TOCTOU, zwłaszcza na nietypowych FS i przy celowej podmianie treści w tym samym inode. W szczególności nie przeprowadzono eksperymentów dotyczących podmiany po ostatnim `stat`, co do zasady nie jest to objęte punktowym fingerprintem.
- Brak zmiany częstotliwości `before/locked/after`, globalnego budżetu 64 MiB ani granicy 120 000 artefaktów. Żadnych nowych uprawnień runnera ani operacji dowolnego kodu. `certificate=false`; hash zależności nie poświadcza matematycznej równoważności źródła LaTeX i Lean.
- Kandydat do nowego pełnego 2+1: `dda19fc9eb8fc274296d8cf15980f52354241301`. Plik `application/config/atlas_validation_request.json` przypina ten sam commit mimo równoległych zapisów na gałęzi. [Nowa walidacja 2+1 #45133542606](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45133542606). Zaliczać tylko faktycznie zakończone testy, na tym dokładnym SHA.
- **Decyzja audytu:** `needs_revalidation`, **nie `approved`**. Poprzedni techniczny wynik 3/3 na innym SHA jest historycznym dowodem, nie końcowym zamknięciem poprawki. Po nowym pełnym 2+1 potrzeba oddzielnego, zatwierdzonego audytu sceptycznego z informacją o ryzykach i wynikach. Nie publikować samego niesygnowanego `reviewer` jako wiarygodnej tożsamości osoby.


## Rozliczenie pełnej walidacji 2+1 na ostatecznej poprawce

- [Orkiestrator #45133923118](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45133923118): `completed/success` na pełnym `candidate_sha=dda19fc9eb8fc274296d8cf15980f52354241301`. Trzy niezależne pełne rundy: każda po **687 testów aplikacji**, 10 sklasyfikowanych pominięć, zero niesklasyfikowanych; dodatkowo Chromium, natywny Linux/Windows, realny Lean/Mathlib oraz testy sceptyczne kontrolera. Końcowe `ATLAS_STABILIZATION`: `passes=[1,2,3]` / `passed=true`, `problems=[]`, `status=stabilizing`, `skeptical_review=pending`, `certificate=false`.
- W każdej rundzie wymagany Lean 4/Mathlib `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67` zakończył: kompilację wpisów manifestu, audyt aksjomatów, niepominiętą rzeczywistą introspekcję MetaM oraz trzy rzeczywiste, zgodne fingerprinty. Oczekiwane pominięcia cgroup i `pdflatex` dotyczą innych funkcjonalności i nie zostały uznane za zaliczone testy.
- **Technicznie 3/3 na jednym SHA.** Nie jest to potwierdzenie pełnej ochrony przed dowolnym TOCTOU ani matematycznej zgodności LaTeX–Lean. Automatyczna zielona walidacja nie jest dowodem recenzji przez inną, uwierzytelnioną osobę.

## Nowe znalezisko audytowe — nieautentykowany recenzent

- Kontrola `application/scripts/atlas_validation_gate.py` wykazała, że dowolny plik JSON z `decision=approved`, dowolnym `reviewer` i `independent=true` mógł wcześniej nadawać `stable`. Takie pola są jedynie deklaracjami i nie poświadczają, kto zatwierdził recenzję. Jest to defekt mechanizmu audytu, nie zmiana działania `.olean`.
- Poprawka [81095506](https://github.com/dariusz-piekarz/mathematical_scipts/commit/81095506bbdd80e1993741b552742ed2183326aa): poprawnie sformatowana, ale niepoświadczona recenzja ma teraz wyłącznie status `documented_unverified`; **nie nadaje `stable`**. Test [5e6e017a](https://github.com/dariusz-piekarz/mathematical_scipts/commit/5e6e017a7d98ce2dfb384b4e973cce08159be3fc) próbuje sfałszować wpis niezależnego recenzenta, a kandydat o niezgodnym SHA nadal jest blokowany.
- **Warunek formalny pozostaje otwarty:** odrębna recenzja z uwierzytelnionym zatwierdzeniem (np. właściwie skonfigurowana chroniona aprobata GitHub lub podpisana recenzja z zaufanym kluczem). Do jej przyjęcia nie przechodzić do L1.2 ani nie przedstawiać wyników jako `stable`. W tym dokumencie nie podpisano żadnego takiego zatwierdzenia.

**Werdykt technicznej kontroli:** zbadano krytyczne regresje deskryptora i kompletność 3/3; nie znaleziono kolejnego potwierdzonego defektu w implementacji fingerprintu. Ryzyka TOCTOU oraz poświadczenie niezależnego audytu pozostają jawne. **Decyzja końcowa: `pending_authenticated_review`**.


## Audyt raportów CI po pełnym 3/3 — sprawdzanie pochodzenia pominięć

[Atlas #45136597724](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45136597724) zakończył `completed/success` dla `5e6e017a7d98ce2dfb384b4e973cce08159be3fc`. Odczytany bezpośrednio log końcowego joba `evidence` zawiera: `passed=true` w każdym z trzech przebiegów, po 687 testów aplikacji, 10 sklasyfikowanych pominięć, `unreviewed_skips=0`, wszystkie cztery grupy jobów `success`, `problems=[]`, `status=stabilizing`, `skeptical_review=pending`, `certificate=false`. To **3/3 zakończone technicznie**, ale nie poświadczenie recenzenta.

W następującej po nim analizie kodu walidatora wykryto, że `validate_unit_report()` ufał dowolnej niepustej wartości `entry["classification"]`, jeśli tylko nie była równa `unreviewed`; nie weryfikował jej względem faktycznego identyfikatora testu i powodu `reason`. Raport mógł zatem podać `classification="windows_native"` dla nieznanego testu. Ponadto `executed` nie musiało odpowiadać liczbie imiennych `outcomes`. To narusza deklarowaną zasadę **fail-closed dla sfałszowanych artefaktów**. Nie oznacza wykrycia udanego ataku na GitHub Actions ani błędu runnera Lean.

- [Poprawka `51cef7cc`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/51cef7ccb7e8aece049bf9254cca9b01b0627bdf): walidator niezależnie ponownie wywołuje `classify_skip(name, reason)`, odrzuca nieznane lub podmienione kategorie, sprawdza dokładnie typy i liczby `skipped`, `outcome_count`, `executed`.
- [Nowe testy `c3503db4`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/c3503db43bb2bb666baf0f34eb6bcbb3c2f7581b): obca nazwa testu z podrobioną kategorią, fałszywa kategoria dla prawidłowego testu, legalny wyjątek Windows, ukryte brakujące wyniki i nieprawidłowy typ licznika.
- **Stabilizacja:** poprzednie 3/3 pozostaje ważnym historycznym wynikiem dla SHA `5e6e017a`, ale nowe zmiany kodu walidatora/testów wymagają ponownego CI na `c3503db4` i kolejnej serii 2+1 na tym samym nowym SHA. **Nie przenosić licznika 3/3 między commitami.** Bez autentykowanej zewnętrznej recenzji pozostawić `stabilizing` i `certificate=false`.

