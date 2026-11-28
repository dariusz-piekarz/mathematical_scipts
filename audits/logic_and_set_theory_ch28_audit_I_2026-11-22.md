# Rozdział 28 — audyt I: integracja i naprawa podstawowych dowodów

**Data:** 2026-11-22. **Plik:** `chapters/pl/logic_and_set_theory/28-liczby-porzadkowe-i-rekurencja-pozaskonczona.tex`.

## Zakres integracji
Porównano biblioteczny plik `28-ordinals-and-transfinite-recursion.tex` z pełniejszym PDF `logika_teoria_mnogosci_iteracja_79.pdf` (strony 228–232). Zachowano wszystkie podstawowe wyniki, a dodatkowo przywrócono z PDF lemat o granicznych ordynałach jako sumach poprzedników, przykład pustej sumy i supremów, hierarchię von Neumanna, definicję mnożenia ordynałów i przykład jego nieprzemienności. Nie rozszerzano zakresu ponad istniejący materiał.

## Matematyka
1. Rozwinięto **rekursję pozaskończoną na ustalonym ordynale**: poprawne przybliżenia, zgodność przez najmniejszy argument różnicy, przypadek zerowy, następnika i graniczny. Na etapie granicznym użyto schematu zastępowania i lematu `lem:ordinal-limit-union` do wyznaczenia dokładnej dziedziny sumy przybliżeń.
2. Rozpisano **istnienie reprezentanta ordinalnego każdego dobrego porządku**: jednoznaczne przybliżenia na odcinkach `W_{≤w}`, zbiór tych przybliżeń przez zastępowanie, sumę dającą funkcję `r`, iniektywność przez ufundowanie, relację `u≺v ⇔ r(u)∈r(v)`, przechodniość i dobry porządek obrazu `r[W]`.
3. Oddzielono argument w ZF od punktu korzystającego z AC: aksjomat wyboru służy tylko do uzyskania dobrego porządku na dowolnym `A`; konstruowanie jego reprezentanta ordinalnego jest twierdzeniem ZF.
4. Wyodrębniono konstrukcję ordynału początkowego jako minimum niepustego, **ustalonego zbioru** ordynałów równolicznych z `A` przez separację w `α+1`, bez odwoływania się do „zbioru wszystkich ordynałów”.

**Wynik:** istniejące dowody zostały naprawione i uściślone; rozdział wymaga kolejnych iteracji.
