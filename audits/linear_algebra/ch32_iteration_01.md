# Algebra liniowa — rozdział 32, audyt I: opracowanie autorskie

**Data:** 22 listopada 2026  
**Rozdział:** `chapters/pl/linear_algebra/32-twistory.tex`  
**Źródło:** nowy materiał, nieprzenoszony z DG-04.  
**SHA źródła:** `ca8d2ff97cba8ad3634a2d4884976936108012db`.

## Zakres i sprawdzona spójność
- Model \(V_\C=M_2(\C)\), niezdegenerowana forma \(q=\det\), zachowujące ją działanie \(SL_2(\C)^2\), postać hermitowska sygnatury \((1,3)\).
- Kwadryka Segrego \(\mathbb{CP}^1\times\mathbb{CP}^1\) i dwie rodziny maksymalnych dwuwymiarowych podprzestrzeni izotropowych, z dowodami.
- Zespolone twistory \((\omega,\pi)\) i relacja incydencji; twierdzenie o przecięciu prostych \(\ell_X,\ell_Y\), płaszczyzny \(\alpha\), obliczone przykłady.
- Osadzenie Plückera \(\operatorname{Gr}_2(\C^4)\) w kwadryce Kleina i korespondencja flag, w tym podanie wzorów na wszystkie minory.
- Kwaternionowa antyliniowa struktura \(J^2=-I\), antyholomorficzna bezpunktowa inwolucja \([z]\mapsto[Jz]\); fibracja \(\mathbb{CP}^3\to\mathbb{HP}^1\simeq S^4\) z włóknem \(\mathbb{CP}^1\), jawne trywializacje i stereografia.
- Dwa rysunki TikZ; oba modele twistorowe opisane oddzielnie, bez pomylenia rzeczywistej postaci lorentzowskiej z metryką euklidesową.

## Kontrole przed uruchomieniem CI
- Źródło zawiera 27 etykiet, wszystkie nowe i z prefiksem `lin32-`. Odsyłacze wskazują na siebie albo na stabilne rozdziały LA-29 i LA-31.
- Dodano testy dokładnego równania Plückera, rank-one/Segre, incydencji, lewego mnożenia kwaternionów, struktury \(J\) i postaci hermitowskiej.
- Workflow i katalog przygotowano do rozdziałów 01–32 oraz automatycznego PDF pojedynczego najnowszego rozdziału.

## Status
Audyt I obejmuje wytworzenie rozdziału: **nie jest czysty**. Wymagane dalsze audyty, uruchomienie CI i osobnego PDF oraz dwie następujące po sobie czyste iteracje dla dokładnie tego samego źródła.
