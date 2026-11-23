# Topologia ogólna — audyt globalny 64: brakująca samodzielna kompilacja rozdziału 01

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Zakres:** jedna konkretna luka w końcowej walidacji wydawniczej rozdziałów 01–26; bez dodawania nowych rozdziałów i bez zmiany treści matematycznej.

## Weryfikacja stanu wyjściowego

Odczytano bezpośrednio z GitHub API aktualną gałąź, raporty 38, 48, 59, 63, źródła 06 i 21, istniejący punkt wejścia `books/pl/general_topology_ch02.tex` oraz workflow `.github/workflows/general-topology-chapter.yml`. Zweryfikowano [run 45145462325](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45145462325): `completed/success` na commicie `5623a2ce38bfe4ac87e71ef7d0b8735fc12dfed5`, w tym test globalny, kompilację całej książki, samodzielnych rozdziałów **02–26** i kontrolę logu. Artefakt `general-topology-ch01-ch26` (ID `14804570320`, 7608675 bajtów) jest wykazany jako nieprzeterminowany, ale nie pobrano jego zawartości do nowej kontroli wizualnej.

Porównanie commitu raportu 62 `63dc23b870690a55606c574b36efe9172da6b8bf` z bieżącą gałęzią **przed poprawką** wykazało 21 późniejszych commitów, ale jedyną zmianą w ścieżkach topologii był nowy raport globalny 63; brak zmian źródeł rozdziałów. Porównanie od ostatniego zielonego CI `5623a2ce...` wykazało 7 commitów z modyfikacjami innych projektów, bez modyfikacji topologii. Raport 63 potwierdza 325/325 indywidualnie udokumentowanych dowodów we wszystkich 26 rozdziałach i 27 podpisanych ilustracji, lecz otwartą końcową inspekcję wizualną.

**Nowa rzeczywiście wykryta luka:** workflow zawierał kroki `Build standalone Chapter 02 PDF` do `Build standalone Chapter 26 PDF`, lecz **nie** zawierał kroku dla rozdziału 01. Ponadto `books/pl/general_topology_ch01.tex` nie istniał. Zielony CI nie dowodził więc samodzielnej kompilowalności rozdziału 01. Ta luka dotyczy także wymaganego zakresu 01–23.

## Rzeczywista naprawa

1. Utworzono `books/pl/general_topology_ch01.tex` na podstawie istniejącego punktu wejścia rozdziału 02, zachowując pakiety, definicje środowisk i makra, ustawiając `\\setcounter{chapter}{0}` oraz `\\input{../../chapters/pl/general_topology/01-przestrzenie-topologiczne.tex}`. Commit: `08729adced16e8f34ce43375054770301fbe259c`; blob po zapisie: `7c88f711ab11d0dd79951e0908fd4ff16c71bcd0`.
2. Zaktualizowano `.github/workflows/general-topology-chapter.yml`: do obserwowanych ścieżek dodano `books/pl/general_topology_ch01.tex`, a przed krokiem rozdziału 02 dodano `Build standalone Chapter 01 PDF`, uruchamiający `xu-cheng/latex-action@v3` dla `general_topology_ch01.tex` w `books/pl` z tymi samymi argumentami co inne rozdziały. Commit: `c565b358adf52a75d901c88cd2ee75dcff299ee3`; blob workflow: `62066a046238106743902589538ca92443332341`.

Po obu zapisach **ponownie pobrano** plik wejściowy i workflow z GitHub na HEAD `c565b358adf52a75d901c88cd2ee75dcff299ee3`; oba zawierają zamierzone elementy. Pierwsza próba utworzenia pliku zakończyła się `409 Conflict` z powodu równoległego przesunięcia gałęzi; po ponownym odczycie utworzenie powiodło się. Nie nadpisywano cudzych zmian.

## Werdykt i pozostające zadania

**PASS implementacji poprawki strukturalnej**, ale **NIE PASS kompilacji nowego rozdziału 01**: podczas ostatniego odczytu listy przebiegów nowy CI po commicie `c565b358...` nie był jeszcze widoczny. Nie wolno przypisywać sukcesu CI `45145462325` nowemu punktowi wejścia. Potrzebne: rzeczywisty `completed/success` workflow z krokiem `Build standalone Chapter 01 PDF`, weryfikacja jego logów i artefaktu, a po zmianie cykl dwóch niezależnych czystych kontroli i dodatkowe potwierdzenie. **Nie zmieniono żadnego źródła rozdziałów ani matematyki.**

Pozostaje też otwarta końcowa niezależna inspekcja wizualna PDF 188 stron i 27 podpisanych ilustracji **na wersji końcowej**; raport 38 potwierdza wcześniejszy realny przegląd i korekty rysunków 6.1 oraz 21.1, ale nie zastępuje nowej inspekcji końcowego artefaktu. Raporty 39–41 udokumentowały wymagane 2+1 dla zmienionych źródeł 06 i 21.

**Następny krok:** potwierdzić nowy CI na SHA `c565b358...`, sprawdzić samodzielny PDF rozdziału 01 i przeprowadzić niezależny przegląd końcowego wydania. Nie wyłączać automatyzacji przed pełnym zamknięciem.
