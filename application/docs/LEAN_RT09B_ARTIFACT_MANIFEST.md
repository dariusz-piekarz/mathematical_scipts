# RT-09b — manifest integralności wybranego katalogu artefaktów

Narzędzie `scripts/lean_artifact_manifest.py` tworzy i sprawdza manifest
pełnych SHA-256 wszystkich plików w **jednym wybranym katalogu**, łącznie
z dokładnym wykazem podkatalogów. Niczego nie pobiera, nie rozpakowuje
i nie wykonuje. Istniejący runner Lean pozostaje bez zmian.

## Kryteria odbioru

- Każdy plik ma względną ścieżkę, rozmiar i SHA-256 całej zawartości.
  Dodatkowy, brakujący, przemianowany lub zmieniony plik albo pusty katalog
  powoduje odmowę weryfikacji.
- Manifest zawiera raport źródeł RT-09a: SHA checkoutu, przypięty toolchain,
  rewizję Mathlib, komplet dziewięciu pakietów i skróty manifestów źródłowych.
  Weryfikacja porównuje go z osobno przekazanym raportem; CLI odtwarza raport
  przez rzeczywistą inspekcję checkoutów Git.
- Zaufany skrót SHA-256 manifestu jest wymagany. Powinien pochodzić z osobnego,
  uwierzytelnionego kanału. Plik manifestu i jego skrót przesłane razem przez
  niezaufaną stronę nie ustanawiają zaufania. Sam raport źródeł także nie jest
  podpisem ani certyfikatem.
- Odrzucane są linki symboliczne, hardlinki plików, punkty reparse Windows,
  ścieżki specjalne i nieprzenośne nazwy, kolizje wielkości liter oraz zmiany
  wykryte podczas skanowania/odczytu. Manifest nie steruje otwieraniem ścieżek:
  weryfikator sam wylicza katalog i porównuje cały odtworzony dokument.
- Limity: 20 000 wpisów wraz z korzeniem, 32 poziomy podkatalogów,
  512 MiB na plik, 2 GiB łącznie, 8 MiB JSON, 120 s skanowania i haszowania.
  Odczyt pliku jest ograniczony jego początkowym rozmiarem i jednym bajtem
  kontrolnym. Limit czasu jest kooperatywny; nie ogranicza zawieszonego
  wywołania systemowego ani czasu inspekcji źródeł Git.

## Użycie

Z katalogu `application/`, przy przygotowanym przypiętym Lean/Mathlib:

```powershell
python -m scripts.lean_artifact_manifest create WYBRANY_KATALOG manifest.json --lean-root lean --checkout-sha PELNE_SHA
python -m scripts.lean_artifact_manifest verify WYBRANY_KATALOG manifest.json --lean-root lean --checkout-sha PELNE_SHA --expected-sha256 ZAUFANY_SHA256_MANIFESTU
```

Manifest musi znajdować się poza opisywanym katalogiem; tworzenie nie nadpisuje
istniejącego pliku. CI tworzy manifest rzeczywistych artefaktów katalogu
`Mathlib/Logic` z przypiętego cache, weryfikuje go w tym samym zaufanym zadaniu
i publikuje manifest oraz wynik jako dowody. Skrót wyliczony w tym zadaniu
testuje spójność przebiegu; sam nie stanowi zewnętrznej atestacji producenta.

## Granice wyniku

`selected_artifact_bytes_verified` oznacza zgodność wybranego drzewa z zaufanym
manifestem w czasie odczytu. Nie dowodzi, że pliki są bezpieczne ani że katalog
zawiera pełne domknięcie importów. Zakres `Mathlib/Logic` jest pierwszą próbką
rzeczywistych artefaktów do dalszego przygotowania zaufanego przykładu.
Nie obejmuje binariów Lean/Lake, bibliotek systemowych ani innych pakietów.
Wersja toolchainu jest metadanymi źródeł, a nie pomiarem bajtów jego binariów.

Skan nie jest atomową migawką systemu plików. Wymaga spokojnego katalogu
na zaufanym hoście; nie chroni przed złośliwym kernelem ani celowo
synchronizowanymi podmianami między sprawdzeniami. Windows może zwracać
buforowany czas zmiany przez zapytanie ścieżkowe: tożsamość między ścieżką
a deskryptorem używa czasu utworzenia, a czas zmiany deskryptora porównywany
jest przed odczytem i po nim. SHA-256 zawsze obejmuje całą zawartość.

`offline_ready=false`, `execution_allowed=false`, `certificate=false`.
Dalsze punkty muszą ustalić komplet artefaktów i narzędzi oraz przeprowadzić
rzeczywisty test zaufanego przykładu w izolacji bez sieci. RT-09b nie włącza
wykonywania kandydatów draft. Odbiór techniczny nadal wymaga CI 2+1
na jednym SHA oraz osobnej fazy B.
