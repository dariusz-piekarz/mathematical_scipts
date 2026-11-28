# AA-X12 — audyt przekrojowy AA-43–AA-45: zależności różniczkowe i integralność odsyłaczy

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**HEAD przed analizą:** `9c909da4e01b098653f8a593870463e4d5b63815`. **HEAD ponownie odczytany przed publikacją:** `612f6e72c79b0a2b8656fe088997b0b5a85bed77`.

## Wybór zakresu i stan źródeł

Drzewo GitHub (rekurencyjne, `truncated=false`) zawiera AA-01–AA-45, ale nie AA-46. AA-43, AA-44 i AA-45 mają już raporty stabilizacyjne III; dlatego nie rozpoczynano ponownie ich numerowanych audytów. Niniejszy nowy audyt przekrojowy dotyczy wyłącznie zależności między trzema zatwierdzonymi rozdziałami.

Źródła i zweryfikowane SHA blobów:
- AA-43: `c6563f402b7890e5e0c8f02796ebf649f4336906`;
- AA-44: `f750ccc0e673e0e7467973d878f75401374813ec`;
- AA-45: `56604f97c634d04423664e53ae9cc6eeca19fc2d`;
- AA-20: `8aa1aedc2c07fe032527d2a0b276cf50b0a6dbfd`;
- AA-23: `69f5f2c35c3e7179055e0acc06fe95e041d0bc24`.

Odczytano również `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`, `catalog/books.json`, `books/pl/abstract_algebra.tex`, plan `docs/pl/plan_algebry_abstrakcyjnej_aa43_plus.md` oraz raporty `ch43_iteration_03.md`, `ch44_iteration_03.md`, `ch45_iteration_03.md` i ostatni raport przekrojowy 11.

## Kontrola odsyłaczy

Z trzech źródeł AA-43–AA-45 odczytano **65 deklaracji `\\label` i 59 wystąpień `\\ref`, `\\eqref`, `\\cref`, `\\autoref`**. W badanym zakresie **0 duplikatów**. Spośród 59 użyć **57** ma cel w AA-43–AA-45. Dwa pozostałe odsyłacze AA-43 sprawdzono w źródłach zewnętrznych:
- `aa:wn:charzero-separable` — definicja celu w AA-20;
- `aa:tw:trace-norm-embeddings` — definicja celu w AA-23.

**Wynik kontroli celów: 59/59 odnalezionych**, przy uwzględnieniu AA-20 i AA-23. Kontrola nie stanowi globalnego skanu wszystkich etykiet całej książki.

## Kontrola matematyczna i niezależne obliczenia

Sprawdzono kierunek zależności: AA-43 wprowadza derywacje i wzory dla śladu/normy; AA-44 używa ich do eliminacji kroków algebraicznych w twierdzeniu Liouville'a; AA-45 redukuje nieelementarność do równań `r'+hr=s` i sprawdza bieguny i stopnie. W odczytanych sformułowaniach AA-45 jawnie występują wymagania przestępności generatora oraz zachowania ciała stałych; nie utożsamiono ich z samym `Dt=ht`. Przy analizie `t^{-1}` osobno przeprowadzono zmianę generatora, nie przyjmując niezależności `t` i `t^{-1}`.

Niezależny test SymPy, uruchomiony w tej iteracji: **6/6 PASS** dla następujących tożsamości: `D sqrt(x²+1)=x/sqrt(x²+1)`, `(1/2)D log(x²+1)=x/(x²+1)`, `D(-e^{-x²}/2)=xe^{-x²}`, `D(e^x/x)=e^x(1/x-1/x²)`, `D(xe^x)=(x+1)e^x`, `D log x=1/x`. Są to testy rachunkowe przykładów, **nie dowody** ogólnych twierdzeń.

**Werdykt matematyczny w wybranym zakresie:** nie wykryto sprzeczności w sprawdzonych zależnościach i sześciu tożsamościach. Nie jest to ponowny pełny audyt każdego twierdzenia w trzech rozdziałach.

## Stan techniczny i decyzja

- Zmiany w źródłach AA-01–AA-45: **0**; nie zmieniono etykiet ani odsyłaczy.
- Kompilacja LaTeX w tej iteracji: **nieuruchomiona** (brak lokalnej kompletnej kopii repozytorium).
- Inspekcja nowego PDF w tej iteracji: **nieprzeprowadzona**.
- GitHub Actions dla tego raportu: **niezweryfikowane**. Wcześniejsze raporty stabilizacyjne zawierają historyczne wyniki CI/PDF, których nie przedstawiamy jako nowe uruchomienia.
- Stabilność: **bez nowego werdyktu**; statusy AA-43–AA-45 wynikają z odrębnych audytów III, nie z tego raportu.
- Kolejny krok: ponownie sprawdzić HEAD i AA-46; jeśli nadal nie istnieje, wybrać inny, niepowtórzony zakres przekrojowy (np. zgodność hipotez w AA-05–AA-08), bez ponawiania X12 dla pozoru.
