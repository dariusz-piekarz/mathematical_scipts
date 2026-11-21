# Algebra liniowa — rozdział 16, audyt II

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/16-podprzestrzenie-niezmiennicze-i-wielomian-minimalny.tex`  
**Zweryfikowany blob:** `1874f4774a038e32ccc53dec543ce1c2c8b39a28`  
**Poprzedni audyt:** `audits/linear_algebra/ch16_iteration_01.md`.

## Kontrola matematyczna (cały rozdział)

1. Podprzestrzenie niezmiennicze: definicja, jądra i obrazy wielomianów w operatorze, sumy i przecięcia, konstrukcja endomorfizmu na ilorazie, blokowa postać macierzy i iloczyn wielomianów charakterystycznych. Test przypadków `W=0` i `W=V`. Przykład niediagonalizowalnego bloku Jordana wyklucza automatyczne istnienie niezmienniczego dopełnienia.
2. Przestrzenie cykliczne: najmniejszość względem zawierania, stabilizacja potęg, charakterystyka przestrzeni `K(T,v)`, istnienie i podzielność wielomianu minimalnego wektora. Stwierdzono i poprawiono zakres indeksu `1≤j<d` w opisie macierzy przesunięcia. Zastąpiono niejednoznaczny schemat macierzy towarzyszącej precyzyjnym wzorem na `c_ij` dla wszystkich `d≥1`, ze szczególnym sprawdzeniem wymiarów `d=1,2`.
3. Wielomian minimalny operatora: jednoznaczność przez dzielenie wielomianów z resztą, formuła monicznej NWW wielomianów minimalnych wektorów bazowych, przypadek `V=0`. Zbadano, że żaden niezerowy wielomian stopnia mniejszego niż `deg m_T` nie zeruje operatora.
4. Twierdzenie Cayleya–Hamiltona: poprawność rachunku w `M_n(K[t])`, tożsamość dołączonej oraz niezależne porównanie współczynników. Równość `chi_T(T)=0` nie jest wyprowadzana przez niedozwolone podstawienie nieprzemiennej macierzy do tożsamości z centralnym parametrem.
5. Rozkład pierwotny: weryfikacja zastosowań Bézouta i niezmienniczości jąder; doprecyzowano osobno przypadek dokładnie dwóch czynników `r=2`, aby iloczyn pozostałych czynników nie był niejawnie pusty. Przy powtarzaniu lematu na `W=ker g(T)` zachodzi `g(S)=0`, gdzie `S=T|_W`.
6. Uogólnione przestrzenie własne: sprawdzono rosnący ciąg jąder, stabilizację na potędze z `m_T` oraz działanie `T-λI` na `ker g(T)`. W poprzedniej wersji znaleziono **błędny opis kierunku odwrotności**: z `u(T)(T-λI)=I` wynika odwrotność lewa, a po zamianie kolejności czynników także prawa. Skorygowano i uzasadniono obie równości.
7. Kryterium diagonalizowalności: poprawna równoważność rozszczepienia `m_T` na różne czynniki liniowe `nad K` z istnieniem bazy własnej. Kontrprzykład rzeczywistej rotacji jest poprawny; dla `n=0` iloczyn pusty to `1`.
8. Przykłady: poprawność zespolonych i rzeczywistych rozkładów, nilpotentna część bloku Jordana, różnica `m_T` i `χ_T`; usunięto mylące założenie, że skalar `1` może równać się `2=1+1` w niektórych ciałach (w każdym ciele `1≠2`, także w charakterystyce 2).

## Testy regresyjne i spójność

- Istniejące wyczerpujące testy nad `F2,F3` dla macierzy `2x2` zachowano.
- Dodano niezależny zestaw `tools/test_linear_algebra_invariant_3x3.py` obejmujący **wszystkie 512 macierzy 3×3 nad F2**, **500 deterministycznie wybranych macierzy 3×3 nad F3** oraz macierze towarzyszące stopni 1, 2 i 3 nad oboma ciałami. Weryfikowane są: `chi_T(T)=0`, `m_T|χ_T`, kryterium diagonalizowalności przez `m_T`, wymiary uogólnionych przestrzeni własnych w przypadku rozszczepionym oraz wielomiany minimalne macierzy towarzyszących.
- Test zintegrowano z `.github/workflows/linear-algebra-chapter.yml`. Obie regresje (stara i 3×3) zakończyły się poprawnie w przebiegu [44934636481](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44934636481).
- Po korektach źródło zawiera **30 różnych etykiet** i **17 odsyłaczy**. Dalsze sprawdzenie składu PDF i zakończenia workflow jest częścią końcowego audytu stabilizacyjnego.

## Decyzja

**Audyt II wykrył i usunął usterki tekstu, dlatego sam w sobie nie daje jeszcze statusu stabilnego.** Należy wykonać audyt III tej samej wersji, obejmujący całość dowodów, wynik CI i osiem lub więcej stron PDF. Nie należy dopisywać nowych twierdzeń do rozdziału 16.
