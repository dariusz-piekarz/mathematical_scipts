# Topologia ogólna — globalny audyt 64: przegląd wizualny wszystkich 188 stron i 27 ilustracji

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Charakter:** końcowy, niezależny **audyt wizualny gotowego wydania**, domykający punkt pozostawiony otwarty w [raporcie 63](00-globalny-audyt-63-finalna-macierz-325-dowodow-ci.md). Nie jest to kolejny od podstaw dowód matematyczny 325 twierdzeń — tę dokumentację zawierają wcześniejsze audyty 01–63.

## Materiał źródłowy: faktycznie pobrane pliki PDF

**Nie opierano się na samej deklaracji zielonego CI.** Pobrano i rozpakowano dwa artefakty **`general-topology-ch01-ch26`** bezpośrednio z GitHub Actions:

1. [Workflow 45144859501](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45144859501), commit `63dc23b870690a55606c574b36efe9172da6b8bf`, artefakt **14803448329** — źródłowy PDF do oględzin.
2. [Workflow 45145462325](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45145462325), commit `5623a2ce38bfe4ac87e71ef7d0b8735fc12dfed5`, artefakt **14804570320** — nowszy PDF do niezależnego porównania; potwierdzono bezpośrednio `completed/success`.

W obu archiwach pełny `general_topology.pdf` ma **188 stron A4** i **1 419 603 bajty**. SHA-256 pierwszego PDF: `01416731e2021c913119a2772906f26367a266fe9ca0ff8f8316b15594876542`. SHA-256 nowszego PDF: `9d2b76edaa0726e3fd237725a08d7a614dc1aa3cc31ef61cf6011cb99ce8ae49`. Różnica plików binarnych wynika co najmniej z innego czasu utworzenia w metadanych; **nie wolno utożsamiać ich bajtowo**.

Sprawdzono natomiast rzeczywistą równoważność rezultatów:
- **188/188 stron o dokładnie jednakowym obrazie pikselowym** przy niezależnym rasteryzowaniu każdego PDF w skali 1:1 (72 dpi);
- **188/188 stron o identycznym wyodrębnionym tekście**;
- **188/188 stron o identycznej liczbie obiektów rysunkowych**;
- identyczny spis treści i **440 odsyłaczy PDF** w obu dokumentach.

**Wniosek:** po dopisaniu raportu 63 kompilacja nie wprowadziła regresji widocznego wydania.

## Zakres rzeczywistego oglądania

- Wyrenderowano **wszystkie strony 1–188** w skali ~85 dpi i ułożono je w **10 zestawień po maksymalnie 20 stron**. Każde zestawienie obejrzano wizualnie pod kątem nietypowych przerw, ucięcia wierszy, osieroconych dużych fragmentów, wyraźnych nakładek i położenia rysunków.
- Automatycznie znaleziono **27 podpisów `Rysunek N.M`**, wycięto okolice każdej ilustracji w powiększeniu ~144 dpi i obejrzano wszystkie trzy zestawienia ilustracji.
- Dodatkowo wygenerowano pełnostronicowe, szczegółowe rendery ~158 dpi dla wybranych stron: **50, 86, 96, 170, 180 i 186**; szczególnie sprawdzono rysunki 6.1, 10.1, 12.1, 24.1, 25.1 i 26.1. Kontrola całej książki w zestawieniach jest kontrolą makroukładu; do oceny mniejszych podpisów i szczegółów grafiki wykorzystano rendery powiększone.
- Strony PDF z podpisanymi rysunkami: **9, 15, 20, 33, 34, 39, 41, 43, 46, 48, 50, 52, 59, 64, 69, 73, 79, 81, 86, 92, 96, 144, 150, 160, 170, 180, 186** — dokładnie **27/27** podpisów.
- Tytuł, spis treści (strony 2–7), początki i końce rozdziałów oraz finał rozdziału 26 są widoczne i w logicznej kolejności. Ostatnia strona 188 nie jest pusta ani osierocona.

## Kontrole techniczne PDF

Na faktycznie rozpakowanym PDF wykonano dodatkowo:
- **188 stron A4**, dokument otwieralny i niezaszyfrowany;
- **27 fontów, wszystkie osadzone** (kontrola `pdffonts`, kolumna `emb=yes`);
- **440 aktywnych odsyłaczy**, bez odsyłacza kierującego poza zakres stron 1–188; **178 pozycji struktury zakładek**;
- współrzędne wyodrębnianych fragmentów tekstu we wszystkich 188 stronach: poziomo od **68,74 do 527,27 pt**, pionowo od **34,60 do 803,31 pt** na stronie **595×842 pt** — **0 fragmentów poza stroną i 0 podejrzanych naruszeń przyjętych progów marginesów** (x: 25–570, y: 15–815 pt);
- w **pełnym logu i 25 logach samodzielnych rozdziałów 02–26** stwierdzono **0** wystąpień: `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning`, `Undefined control sequence`, `Fatal error`;
- `pdf_preflight.py` i `pdf_inspect.py` nie zgłosiły problemu uniemożliwiającego odczyt pliku; nie wykryto formularzy ani załączników wymagających osobnej walidacji.

## Werdykt wizualny i uwaga nieblokująca

**PASS — 188/188 stron w oględzinach makroukładu i 27/27 ilustracji w osobnym przeglądzie powiększeń.** Nie stwierdzono uciętych stron, kolizji podpisów z rysunkami, brakujących etykiet na wykresach, nieczytelnych znaków ani błędnych przerw uniemożliwiających publikację. Rozdziały otwierają się regularnie, a podpisy są bezpośrednio powiązane z właściwą grafiką.

**Kosmetyczna obserwacja, nie błąd blokujący:** na schemacie **Rysunek 26.1, PDF s. 186** niebieska droga po poprawce biegnie w wielu miejscach dokładnie po szarej drodze wyjściowej. Ponieważ ta pierwsza została narysowana na wierzchu, szarej linii jest miejscami mało widać. Pętla i sens konstrukcji są wyraźne, podpis jest poprawny, a linie nie kolidują z tekstem. Opcjonalnie można w kolejnej redakcyjnej wersji poprawić kontrast/rysunek; **nie zmieniano źródła tylko z powodu tej uwagi**, co pozwala zachować stabilny blob i ukończony rejestr dowodowy.

## Wynik końcowy

Łącząc [audyt 63](00-globalny-audyt-63-finalna-macierz-325-dowodow-ci.md) i faktyczny przegląd wydania z niniejszego raportu, wszystkie zdefiniowane wcześniej warunki **pełnego audytu „Topologii ogólnej”** są spełnione:

- **26/26 rozdziałów**, każdemu przyporządkowany aktualny stabilny blob;
- **325/325 dowodów** z indywidualną dokumentacją matematyczną i odniesieniem do źródła;
- pełne kontrole globalnych odsyłaczy (810 etykiet, 262 referencje), środowisk i terminologii;
- zielone CI na commicie raportu 63, z faktyczną kompilacją pełnego **188-stronicowego** PDF;
- ukończony przegląd wizualny **188/188 stron** i osobny przegląd **27/27 ilustracji**;
- ponowna weryfikacja, że artefakty PDF z kolejnych dwóch przebiegów są **identyczne wizualnie na 188/188 stronach**.

**Status: FINAL PASS dla wydania kontrolowanego przez workflow 45145462325.** Po opublikowaniu niniejszego raportu 64 zostanie uruchomione osobne CI commitu raportu; jego wynik należy jeszcze odczytać, zanim przypisze się temu późniejszemu commitowi `completed/success`. Nie należy utożsamiać statusu kontrolowanej wersji skryptu ze statusem bieżącego HEAD całej gałęzi, na której mogą trwać równoległe prace niezwiązane z topologią.
