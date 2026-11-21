# Algebra liniowa — rozdział 12, audyt II (niezależna kontrola stabilizacyjna)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Plik:** `chapters/pl/linear_algebra/12-przestrzenie-euklidesowe-i-unitarne.tex`  
**Sprawdzony blob:** `f205ea41e5562cc14f13869e0ff17877d2d29079`  
**Poprzedni raport:** `audits/linear_algebra/ch12_iteration_01.md`

## Kontrola matematyczna

Audyt II przeprowadzono na niezmienionym tekście rozdziału 12, niezależnie sprawdzając formalne przesłanki, kroki dowodów, przypadki brzegowe i regułę sprzężenia zespolonego. Nie dodano nowych twierdzeń ani przykładów.

1. **Formy hermitowskie:** poprawna konwencja `h(au,v)=conj(a)h(u,v)` i `h(u,av)=a h(u,v)`. Rzeczywistość `h(v,v)` wynika z hermitowskości bez zakładania dodatniej określoności.
2. **Polaryzacja:** dla `z=h(u,v)`, różnica `q(u+v)-q(u-v)` daje `4 Re(z)`, a `q(u+iv)-q(u-iv)` daje `-4 Im(z)`. Wzór końcowy z minusem przed `i` jest zatem prawidłowy. Przypadek `u=1,v=i` daje `i`.
3. **Macierz Grama:** `G'=P^*GP` i `h(u,v)=X^*GY` odpowiadają dokładnie drugiemu liniowemu argumentowi, także przy zespolonych, niediagonalnych współczynnikach.
4. **Cauchy–Schwarz:** podstawienie `c=h(v,u)/h(v,v)` jest poprawne w przyjętej konwencji i gwarantuje `h(v,u-cv)=0`. Równość występuje dokładnie przy zależności liniowej; osobno rozpatrzono wektor zerowy.
5. **Grama–Schmidta:** `h(e_i,w_j)=0` wynika bezpośrednio z ortonormalności wcześniejszych `e_i`, a `w_j≠0` z niezależności wejściowej rodziny. Na `C²` przykład zawiera rzeczywiste sprzężenia w odpowiednich współczynnikach.
6. **Riesz:** dla liniowego funkcjonału `F` reprezentant `a=Σ conj(F(e_j)) e_j` daje dokładnie `h(a,v)=F(v)`. Jednoznaczność wynika z dodatniej określoności. Sprzężenie liniowość `a↦h(a,·)` jest świadomie odróżniona od liniowości nad `C`.
7. **Parseval i Bessel:** wyodrębnienie współczynników `h(e_j,v)` i reszty ortogonalnej prowadzi do tożsamości Pitagorasa. Równość w nierówności Bessela jest równoważna zniknięciu reszty. Przypadki rodziny pustej i wymiaru zero są poprawne.
8. **Wyznacznik Grama:** dodatnia półokreśloność `G` wynika z `c^*Gc=||Σ c_i v_i||²`. Zależność daje niezerowe jądro, a niezależność rozkład `G=R^*R` z odwracalną górnotrójkątną `R`; wyznacznik jest dodatni. Uwzględniono pustą rodzinę i konwencję `det I_0=1`.
9. **Izometrie i unitarność:** liniowe odwzorowanie zachowuje normę dokładnie wtedy, gdy zachowuje iloczyn skalarny, ponieważ polaryzacja rekonstruuje formę z wartości na przekątnej. W skończonym wymiarze `A^*A=I` daje `A^{-1}=A^*` i `|det A|=1`. Warunek ten charakteryzuje także zmiany między bazami ortonormalnymi.
10. **Oszczędność materiału:** nie powtórzono dowodów ortogonalizacji, rzutowania i rzeczywistego kryterium Sylvestera z rozdziału 09. Materiał geometrii różniczkowej dotyczący rzeczywistej metryki wykorzystano jako źródło interpretacji, bez przenoszenia niepotrzebnych twierdzeń o rozmaitościach.

## Kontrola techniczna i testy

- Rozdział 12: **1065 wierszy**, **36 etykiet** i **9 odsyłaczy**.
- Łącznie rozdziały 01–12: **501 różnych etykiet**, **205 odsyłaczy mających cel**, poprawna kolejność w `catalog/books.json`, wszystkie importy `\\input` oraz zrównoważone środowiska LaTeX.
- `tools/test_linear_algebra_unitary.py`: **1296** polaryzacji, **1296** wyznaczników Grama, **1094** przykładów ortogonalizacji, **1296** testów Riesza/Bessela i **864** kontroli izometrii unitarnych; razem **5846** prób, wszystkie udane.
- [GitHub Actions 44921770596](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44921770596) — `success`, 127 stron PDF, zero ostrzeżeń kompilacji; [CLI 44921770584](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44921770584) i [kontrola rozdziałów logiki 44921770558](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44921770558) również zakończyły się sukcesem.
- Po zapisaniu raportu i statusu książki uruchamiany jest nowy przebieg CI, którego zakończenie należy sprawdzić osobno.

## Decyzja

**Audyt II — czysty.** Nie wykryto kolejnych błędów matematycznych, nieprecyzyjnych założeń ani luk w dowodach. Rozdział 12 pozostawiono bez zmian. Po dwóch kontrolach i udanej kompilacji **rozdziały 01–12 uznajemy za stabilne**. Kolejny rozdział w planie to 13 „Ortogonalność i rzuty”, z wyraźnym unikaniem ponownego powtarzania wyników rzeczywistych z rozdziału 09 i kompleksowych z rozdziału 12.
