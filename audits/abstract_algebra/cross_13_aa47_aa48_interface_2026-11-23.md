# AA — audyt przekrojowy 13: zgodność interfejsu AA-47/AA-48

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**HEAD bezpośrednio przed publikacją:** `4bb2fdfe90e4d1defbffb03877964cbec1d888d3`.  
**Rodzaj:** nowa kontrola przekrojowa; nie jest ponownym audytem stabilizacyjnym AA-48.

## 1. Baza i wybór zakresu
Odczytano AGENTS.md, docs/pl/standardy_terminologiczne.md, application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md, katalog catalog/books.json, książkę books/pl/abstract_algebra.tex, źródła AA-47 i AA-48, raport AA-47 VII oraz AA-48 I–III i plan docs/pl/zakres_aa48_kovacic_wymierny.md. Katalog i książka obejmują AA-01–AA-48; plan AA-48 wskazuje, że AA-49 nie jest otwarty. Sprawdzono brak dwóch przewidywalnych nazw źródła AA-49, lecz nie przeprowadzono pełnego listingu wszystkich możliwych nazw. Z tego względu niniejszy raport nie deklaruje absolutnego braku pliku o nieznanej nazwie.

## 2. Nowa kontrola zgodności matematycznej
Porównano granicę rozstrzygalności twierdzenia `aa:tw:kovacic-polynomial-rational-decision` (AA-47, potencjał wielomianowy) z `aa:tw:kov-rational-complete-algorithm` (AA-48, potencjał wymierny). AA-48 rozszerza **tylko** decyzję o istnieniu rozwiązania `r∈C(x)`, a nie pełną klasyfikację rozwiązań liouvillowskich; oba rozdziały zaznaczają to jawnie. Przy `q∈C[x]` brak skończonych biegunów q, więc w AA-48 `S=∅`, `R=0` i `r=ω+P'/P`; wzór na stopień `n` redukuje się do wzoru z AA-47. W przypadku stałego `q` AA-47 dopuszcza rozwiązanie stałe; AA-48 otrzymuje je z `ω²=q, n=0` lub z gałęzi `q=0, n=0`. Zatem nie ma sprzeczności w przypadkach granicznych.

Niezależnie uruchomiono lokalny SymPy: **6/6** tożsamości `r'+r²=q` (w tym wielomianowe, wymierne z biegunami rzędu 2 i 4 oraz przykład z jednoczesnym biegunem ustalonym i ruchomym), **2/2** tożsamości liniowego równania dla `P`. W przypadku `q=2/x², u=-1/x` obie funkcje `P=x³` i `P=x³+1` spełniają liniowe ODE, lecz pierwsza ma `P(0)=0`, a druga `P(0)=1`. Potwierdza to, że warunek nieznikania `P` na biegunach q jest rzeczywistą osobną bramką i że AA-48 go nie pomija. Testy skończone nie zastępują dowodu ogólnego.

Przejrzano również odsyłacz AA-48 do `aa:ch:risch-kovacic` oraz powiązanie z klasyfikacją `aa:tw:kovacic-classification`; odpowiednie deklaracje występują w AA-47. Historyczne nazwy etykiet pozostawiono bez zmian. Terminologia `ciało`, `odwzorowanie`, `ciąg` oraz opis granic algorytmu są zgodne z regułami w badanym fragmencie.

## 3. Rozdzielone wyniki
| Bramka | Wynik |
|---|---|
| Zgodność matematyczna interfejsu AA-47/AA-48 | Bez sprzeczności w sprawdzonym zakresie |
| Nowe lokalne sprawdzenia SymPy | 8/8 PASS |
| Odsyłacze między AA-47/AA-48 w badanym zakresie | Cele obecne |
| Zmiany źródeł | 0 |
| Nowa kompilacja LaTeX | NIE WYKONANO |
| Nowa wizualna inspekcja PDF | NIE WYKONANO |
| Nowe CI | NIE URUCHAMIANO |
| Historyczny końcowy CI AA-48 | Raport III dokumentuje run 45172784971, success; nie stanowi nowego przebiegu |

**Werdykt:** kontrola przekrojowa 13 zakończona w ograniczonym zakresie, bez korekt źródeł i bez nowego statusu stabilizacji. Dotychczasowy raport AA-48 III dokumentuje jego stabilizację. W tej iteracji nie dodano żadnego twierdzenia ani lematu.

## 4. Następny krok
Ponownie ustalić HEAD i pełne drzewo, sprawdzić AA-49. Jeśli nowego rozdziału nie ma, wybrać inny nieaudytowany przekrojowo obszar (np. hipotezy AA-05–AA-08) i wykonać dokładnie jeden numerowany audyt. W razie zmian źródeł rozpocząć stabilizację od nowa.
