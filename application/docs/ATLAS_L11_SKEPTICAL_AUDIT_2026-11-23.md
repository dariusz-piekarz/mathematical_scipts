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
