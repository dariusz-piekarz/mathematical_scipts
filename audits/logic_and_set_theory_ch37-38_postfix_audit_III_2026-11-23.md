# Logika matematyczna i teoria mnogości — audyt potwierdzający III rozdziałów 37–38

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Kryterium stabilności:** niezależnie czyste audyty I oraz II na niezmienionych źródłach, niezależne potwierdzenie III, poprawne odsyłacze i rzeczywisty zielony CI po korektach.

## 1. Potwierdzenie niezmienności źródeł

Na koniec audytu pobrano ponownie aktualne pliki z GitHuba, a nie tylko ich wcześniejsze kopie.

| Rozdział | Aktualny blob | Liczba wierszy | Etykiety | Odsyłacze |
|---|---|---:|---:|---:|
| 37 | `6c495beddc92e39b6885171e6415f0efe21d5b59` | 775 | 26 | 18 |
| 38 | `28d73acfcc3a6db9519822df210aa66391c51628` | 640 | 26 | 19 |
| 39 (kontrolnie) | `9d06016d71a4c42434b8f0a58c13f666160a4034` | 949 | 22 | 25 |

W stosunku do audytów I i II **nie zmienił się ani jeden blob źródła rozdziałów 37 i 38**. Rozdział 39 również jest niezmieniony. Nowe zmiany dotyczą wyłącznie części technicznej pliku `books/pl/logic_and_set_theory.tex` i raportów audytu.

## 2. Niezależny przegląd kryteriów i prób obalenia dowodów

- **Model `V_κ` z rozdziału 37:** bez regularności κ nie wystarcza argument o ograniczoności rang obrazu mniejszego zbioru. Regularność i silna graniczność są jednak w przesłankach i wykorzystane w różnych miejscach dowodu.
- **Ultraprodukt i zanurzenie:** twierdzenie Łosia jest formułowane osobno dla każdej ustalonej formuły. Przeliczalna zupełność niegłównej miary chroni przed nieskończonym łańcuchem malejącym, a zbiorolokalność relacji pozwala na kolaps Mostowskiego. Nie korzysta się z fałszywej równości `[id]=κ` dla początkowej nienormalnej miary.
- **Normalność `W`:** regretywność funkcji i punkt krytyczny κ wymuszają `j(f)(κ)<κ`; wynika z tego duże włókno stałej wartości. Lemat o klubach w normalnej mierze w rozdziale 38 korzysta właśnie z tego, a nie z samej zupełności.
- **Mahlo:** stacjonarność `I_κ` jest udowodniona przez wspólny ultrafiltr, a nie wywnioskowana z nieograniczoności. Trzeba tu odróżniać silną nieosiągalność κ wewnątrz M od zewnętrznej; tekst zawiera osobny argument o absolutności w potrzebnym kierunku.
- **Własność drzewa i relacje podziałowe:** przy mierzalnej κ małość każdego poziomu pozwala odzyskać oryginalne węzły z ich obrazów przez j; przy kolorowaniu par poprawnie stosuje się tylko `<κ` przecięć na etapie `ξ<κ`.
- **Język:** korekty rodzaju gramatycznego przy `λ` i formy „nieprzeliczalna regularna liczba kardynalna” w obu źródłach są zachowane. Odrębne nazwy dwóch rodzajów przecięć (zwykłego i diagonalnego) oraz pełna forma „liczba kardynalna” są zgodne ze standardem.

Nowych błędów matematycznych, brakujących założeń ani koniecznych poprawek w skontrolowanych twierdzeniach nie wykryto.

## 3. Kontrola rzeczywistego PDF

Pobrano rzeczywisty artefakt [walidacji 45081007565 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081007565), złożony z `logic_and_set_theory.pdf` oraz logu. Plik ma **337 stron A4**.

Wyrenderowano i przejrzano **wszystkie 17 stron PDF 321–337**: rozdział 37 — strony 321–326 (6 stron), rozdział 38 — strony 327–331 (5 stron), rozdział 39 — strony 332–337 (6 stron). Na montażach sprawdzono początek i koniec każdego rozdziału, oznaczenia środowisk, wzory i układ tekstu. Nie stwierdzono widocznego nakładania się napisów, obciętych wzorów ani pustych artefaktów.

Oglądany artefakt odpowiadał źródłom rozdziałów **po pięciu poprawkach językowych**, lecz plikowi głównemu **przed** naprawą kotwic PDF.

Dodatkowo niezależnie od kroków CI przejrzano log: przed naprawą `hyperref` raportował powtórzenia identyfikatorów stron `page.1`, ..., `page.9`. W pliku głównym dodano `\\frontmatter`; następne CI wykazało spadek liczby ostrzeżeń do powtórzenia `page.i` (strona tytułowa/spis treści). Wprowadzono więc `\\hypersetup{pageanchor=false}` tylko dla strony tytułowej oraz `\\hypersetup{pageanchor=true}` przed spisem treści. Zachowano dotychczasowe `\\mainmatter`, wszystkie rozdziały i etykiety.

Dla ostatecznej naprawy strony tytułowej rozpoczął się [przebieg 45081904405](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45081904405), którego wynik należy potwierdzić przed uznaniem technicznej naprawy za zakończoną. Nie należy utożsamiać sukcesu kompilacji z brakiem wszystkich ostrzeżeń `hyperref`: osobne ostrzeżenia o tokenach w zakładkach PDF są znanym pozostałym zagadnieniem.

## 4. Werdykt

**Audyt I — czysty. Audyt II — czysty. Audyt III — matematycznie i wizualnie czysty dla rozdziałów 37–38. Źródła rozdziałów 37 i 38: stabilne (2/2+1).** Korekty pliku głównego książki mają oddzielny status techniczny i wymagają potwierdzenia najnowszego CI. Kontrola PDF nie oznacza weryfikacji dowodów w Lean.

Nie dodano niezatwierdzonych twierdzeń ani nowych rozdziałów.
