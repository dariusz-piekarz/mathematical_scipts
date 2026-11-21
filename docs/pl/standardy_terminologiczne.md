# Globalne standardy terminologiczne — skrypty matematyczne (PL)

Zasady przyjęte 21 listopada 2026 r. Obowiązują przy opracowywaniu **wszystkich** polskojęzycznych skryptów matematycznych Biblioteki, przy tworzeniu nowych rozdziałów, audytach i redagowaniu dowodów. Zachowujemy istniejące stabilne \(\label\) i \(\ref\), gdyż ich zmiana mogłaby zerwać odsyłacze.

## 1. „Suma zbiorów”, nie „unia”

- Dla operacji mnogościowej oznaczanej \(A\cup B\) używamy **„suma zbiorów”** albo, jeśli trzeba odróżnić ją od sumy algebraicznej, **„suma mnogościowa”**.
- Dla rodziny zbiorów \(\bigcup_{i\in I}A_i\) piszemy „suma zbiorów z rodziny”, „suma mnogościowa rodziny” lub po prostu „suma zbiorów”.
- Unikamy słowa „unia” i jego odmian w tekście matematycznym, również w nagłówkach i podpisach. Nie zmieniamy nazw stabilnych etykiet \(\label\), nawet jeśli zawierają ciąg „unia”.
- **Ważne rozróżnienie:** \(A\cup B\) to suma *mnogościowa* zbiorów; \(U+W=\{u+w:u\in U, w\in W\}\) to suma *algebraiczna* podprzestrzeni. Nie należy utożsamiać tych konstrukcji.

## 2. „Warunek niezależności liniowej”, nie „relacja liniowa”

- W dowodach dotyczących liniowej niezależności mówimy **„warunek niezależności liniowej wektorów”**, „równość \(\sum a_iv_i=0\)”, „równanie z definicji niezależności liniowej”, „równość świadcząca o zależności” i podobnie.
- Unikamy określenia „relacja liniowa”, „relacja zależności” oraz samego słowa „relacja” w kontekście równania \(\sum a_iv_i=0\).
- Dokładnie zaznaczamy, co implikuje niezależność: z równości \(\sum_{j=1}^m a_jv_j=0\) dla **parami różnych** wektorów albo różnych indeksów wynika zerowanie wszystkich współczynników. Jeśli istnieje równość z niezerowym współczynnikiem, to mamy świadectwo zależności.
- Określenie „relacja” zachowuje swoje normalne znaczenie przy **relacjach teoriomnogościowych**, relacjach równoważności, porządkach itd.; niniejsza zasada dotyczy tylko języka liniowej niezależności.

## Audyty

W każdym audycie sprawdzamy konsekwentnie te terminy w treści, twierdzeniach, przykładach, podpisach rysunków i komentarzach LaTeX, bez naruszania historycznych etykiet odsyłaczy. Terminologia nie może zmieniać poprawnego znaczenia matematycznego.
