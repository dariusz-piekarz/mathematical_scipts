# AA-X02 — audyt przekrojowy AA-25–AA-27: 90. twierdzenie Hilberta, Kummer, Artin–Schreier

**Data:** 2026-11-23. **Repozytorium:** `dariusz-piekarz/mathematical_scipts`. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**HEAD bezpośrednio przed zapisem:** `53ef10c651ec5c54d7944916e5a221d51edefbf6`.

## Granice kontroli i podstawa

Kontrola dotyczy zgodności wybranych kluczowych hipotez, konstrukcji i klasyfikacji rozszerzeń cyklicznych w trzech istniejących rozdziałach:

- AA-25: `chapters/pl/abstract_algebra/25-twierdzenie-hilberta-90-i-rownania-normowe.tex` (Git blob `2524f56e0a4802d28c441ff932ba5399a10eb61c`).
- AA-26: `chapters/pl/abstract_algebra/26-rozszerzenia-cykliczne-i-teoria-kummera.tex` (Git blob `5bee95fdfedeaaf4fc697dce636e5d82afcd249b`).
- AA-27: `chapters/pl/abstract_algebra/27-teoria-artina-schreiera.tex` (Git blob `628da680adc66f257511a260df4283db8cb9a7d7`).
- Sprawdzono też wspólne założenia i odniesienia do AA-22 i AA-23 (odpowiednio podstawowe twierdzenie Galois oraz formę śladu).

To **nowy audyt przekrojowy**, a nie powtórzenie szczegółowych audytów rozdziałowych ani pełna ponowna lektura wszystkich 42 rozdziałów. W chwili weryfikacji nie istniało źródło AA-43.

## Wynik analizy matematycznej

1. **AA-25: dwie postaci 90. twierdzenia Hilberta.** Dla cyklicznego `L/K` generator `σ` działa w obu formułach dokładnie na tym samym rozszerzeniu. Sprawdzono równoważności `Tr(a)=0 ⇔ a=b−σ(b)` oraz `N(a)=1 ⇔ a=b/σ(b)` na wszystkich elementach badanych ciał i niezależnie konstrukcję niezerowego świadka `B(x)=Σ_j p_j σ^j(x)`. Wśród przypadków są rozszerzenia stopnia 1 oraz `F_4/F_2`, `F_27/F_3`, gdzie charakterystyka dzieli stopień, mimo to funkcjonał śladu nie jest zerowy. Nie wolno wyprowadzać niezerowości śladu z samego `Tr(1)=n`.
2. **AA-26: założenia teorii Kummera.** W `F_7` liczba 3 jest odwracalna i istnieje pierwotny pierwiastek sześcienny z jedynki. W `F_{343}=F_7[α]`, `α^3=2`; `β=α^2` spełnia `β^3=4` i `β^2=2α`, więc `F_7(α)=F_7(β)`, choć klasy `[2]` i `[4]` w `F_7^×/(F_7^×)^3` są różne. Potwierdza to klasyfikację *prostych* w grupie ilorazowej, a nie identyfikację pojedynczych klas. Sprawdzono też przypadek kwadratowy `F_{25}/F_5` oraz nierozdzielność warunków przy naruszeniu hipotez.
3. **AA-27: klasy addytywne.** W `F_{27}=F_3[α]` zachodzi `α^3−α=1`, a Frobenius `σ(α)=α+1`; dla `β=cα+d`, `c∈F_3^×, d∈F_3`, mamy `β^3−β=c`. Analogicznie w `F_4/F_2`. Sprawdzono liczbę pierwiastków `X^p−X−a`, ich położenie w ciele bazowym lub rozszerzeniu i orbity Frobeniusa. Wzory klasyfikacyjne używają `F/\wp(F)`, nie multiplikatywnego `F^×/(F^×)^p`.
4. **Most AA-25 ↔ AA-27.** Jeżeli `σ(α)=α+1` w rozszerzeniu Artina–Schreiera, to przy `b=−α` mamy `1=b−σ(b)` i `Tr(1)=p\cdot1=0`; to konkretny przypadek addytywnej postaci 90. twierdzenia Hilberta.
5. **Wyjątki i kwantyfikatory.** Twierdzenia AA-26 wyraźnie wymagają, aby `n` było odwracalne w ciele i pierwiastki jedności należały do bazy. AA-27 pracuje w charakterystyce `p` i stosuje `X^p−X−a` o pochodnej `−1`. Nie znaleziono błędnego przeniesienia hipotez Kummera do przypadku Artina–Schreiera ani do postaci Hilberta, obowiązujących bez ograniczenia charakterystyki przy rozdzielczym rozszerzeniu Galois.

## Test odtwarzalny — rzeczywiście uruchomiony

Zapisano `tools/tests/test_abstract_algebra_cross_aa25_27.js` (bez dodatkowych bibliotek).
Przeprowadzono **2514 dokładnych kontroli arytmetycznych w JavaScript**, bez użycia tolerancji zmiennoprzecinkowych. Obliczenia na reprezentacjach wielomianowych ciał skończonych operują wyłącznie na małych liczbach całkowitych.

| Rodzaj kontroli | Wynik |
|---|---:|
| Własności modeli ciał, odwrotności, norma i ślad | 1289/1289 |
| Obraz `1−σ` a jądro śladu | 433/433 |
| Obraz `b↦b/σ(b)` a jądro normy | 423/423 |
| Świadkowie, konstrukcja `B(x)`, produkty normowe | 264/264 |
| Równania Artina–Schreiera, klasy, Frobenius | 43/43 |
| Klasyfikacja i pierwiastki Kummera | 60/60 |
| Wspólne świadectwa Artin–Schreier/Hilbert | 2/2 |
| **Łącznie** | **2514/2514** |

Użyto ciał `F_2, F_4, F_8, F_3, F_9, F_27, F_5, F_25, F_7, F_343`. Każde sprawdzenie to jawny warunek programu (nie niezależne twierdzenie matematyczne). W chwili publikacji test uruchomiono bezpośrednio w sesji audytowej, nie w zdalnym runnerze CI. Zachowany plik pozwala odtworzyć go komendą:

```bash
node tools/tests/test_abstract_algebra_cross_aa25_27.js
```

## Spójność odsyłaczy i integracja

Dla AA-25, AA-26 i AA-27 znaleziono odpowiednio **10, 12 i 10 etykiet** oraz **9, 6 i 5 użyć odsyłaczy**. W kontrolowanym zbiorze nie ma powtórzeń etykiet; cele wewnętrzne istnieją, a zewnętrzne, m.in. `aa:tw:fundamental-galois` w AA-22 i `aa:tw:trace-nondegenerate` w AA-23, mają źródłowe definicje. Nie jest to globalne sprawdzenie etykiet całej książki.

Test dodano do workflow `.github/workflows/abstract-algebra-chapter.yml` (Node 22, nowy krok oraz wyzwalacz dla ścieżki testowej). Workflow zmieniono w commicie `8cd2bb3ed85af64e616071d6b81128f75ce7ffba`, a plik testowy dodano w `becf89de78ce0b5a2e39a5bb0bc70d418f959062`.

## Werdykt i ograniczenia

**AA-X02: matematyczna kontrola przekrojowa bez wykrytych uchybień w rozpatrywanych twierdzeniach; 2514/2514 dokładnych sprawdzeń PASS.** Nie zmieniano zatwierdzonych źródeł LaTeX.

**Brak potwierdzenia pełnego GitHub Actions po aktualizacji workflow:** jego sukces musi zostać osobno odczytany z faktycznego przebiegu. W tej iteracji nie wykonywano nowej lokalnej kompilacji książki ani niezależnej inspekcji PDF. Poprzedni udokumentowany sukces CI książki nie jest nowym wynikiem tego audytu. Nie oznaczamy AA-X02 jako finalnie ustabilizowanego, dopóki nie zostanie potwierdzona integracja; wymagany jest też jeden niezależny audyt kontrolny po jej pozytywnym zakończeniu.

**Następny krok:** sprawdzić najnowszy HEAD i przebieg CI dla nowego workflow; wykonać dodatkową niezależną, sceptyczną kontrolę AA-X02 w tej samej bazie źródłowej. Po uzyskaniu stabilności można rozpocząć odmienną kontrolę przekrojową, np. spójności AA-31–AA-36.
