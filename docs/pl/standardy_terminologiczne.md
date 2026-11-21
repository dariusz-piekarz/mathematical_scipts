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

## 3. „Przestrzeń dualna”, nie samodzielne angielskie „dual”

- W polskich tekstach matematycznych nie używamy samodzielnego angielskiego rzeczownika „dual”, w szczególności w tytułach twierdzeń i sekcji. Stosujemy „przestrzeń dualna”, „przestrzeń sprzężona” lub „przestrzeń funkcjonałów liniowych”.
- Dopuszczalne są polskie formy przymiotnikowe: „dualny”, „dualna”, „dualne”, np. „odwzorowanie dualne”, „baza dualna”, „przestrzeń dualna”; również „odwzorowanie sprzężone”, gdy odpowiada znaczeniu.
- Zalecane sformułowania: „przestrzeń dualna do ilorazu” i „przestrzeń dualna do sumy prostej”. Nie zmieniamy z tego powodu istniejących etykiet \verb|\label| i odsyłaczy \verb|\ref|.

## Audyty

W każdym audycie sprawdzamy konsekwentnie te terminy w treści, twierdzeniach, przykładach, podpisach rysunków i komentarzach LaTeX, bez naruszania historycznych etykiet odsyłaczy. Terminologia nie może zmieniać poprawnego znaczenia matematycznego.

## 4. „Wielomian rozkłada się na czynniki”, nie „rozszczepia się”

- O wielomianie piszemy **„rozkłada się nad \(K\) na czynniki liniowe”**, **„rozkłada się na czynniki nierozkładalne”**, **„daje się rozłożyć na czynniki liniowe nad \(K\)”** itd. Nie używamy określeń „wielomian rozszczepia się”, „wielomian rozszczepiony” ani „rozszczepienie wielomianu”.
- Zamiast „warunek rozszczepienia \(m_T\)” piszemy **„warunek rozkładu \(m_T\) na czynniki liniowe”**. Zamiast „bez rozszczepienia” — „gdy wielomian nie rozkłada się na czynniki liniowe nad danym ciałem”.
- Rozróżniamy **rozkład na czynniki liniowe nad ustalonym ciałem** od ogólnego **rozkładu na czynniki nierozkładalne**. Sama separowalność ani brak powtórzeń nie oznaczają rozkładu na czynniki liniowe nad tym ciałem.
- Właściwe zastosowania pojęcia **rozszczepienia** w innych kontekstach (np. rozszczepiona dokładna sekwencja, rozszczepienie krótkiego ciągu dokładnego, rozszczepienie morfizmu) nie podlegają tej zamianie. Nie naruszamy nazw stabilnych etykiet LaTeX.

## 5. Angielskie „chart” to „mapa”, nie „karta”

- **Chart (coordinate chart)** na rozmaitości tłumaczymy jako **mapa**, np. „mapa współrzędnych”, „mapa lokalna”, „mapa \((U,\varphi)\)”, „dziedzina mapy”, „odwzorowanie zmiany map”, „atlas map”. Stosujemy poprawne formy odmiany: „mapy”, „mapie”, „mapę”, „mapą”, „map”, „mapami”, „mapach”.
- W znaczeniu *chart* **nie stosujemy** „karta”, „karty”, „karcie”, „kartę”, „kartą”, „kart”, „kartami”, „kartach” itd. Jedynie zwykłe znaczenia niezwiązane z mapą współrzędnych (np. karty do gry) pozostają bez zmian.
- Angielskie **mapping** oraz **map** w znaczeniu funkcji między przestrzeniami tłumaczymy jako **odwzorowanie**. Wyraz „mapa” jest zarezerwowany dla *chart*, a nie używany jako ogólny synonim odwzorowania.
- Zmiany przeprowadzamy kontekstowo, z zachowaniem polskiej gramatyki, definicji matematycznych oraz historycznych etykiet LaTeX; w szczególności nie zmieniamy mechanicznie każdej sylaby „kart” ani nazw \(\backslash\mathrm{label}\) i \(\backslash\mathrm{ref}\).
- Zasada jest **globalna**, dotyczy wszystkich polskojęzycznych skryptów Biblioteki oraz każdego kolejnego audytu i uzupełnienia.

## 6. Pierwszy i drugi aksjomat przeliczalności

- Dla przestrzeni topologicznej \(X\) piszemy **„\(X\) spełnia pierwszy aksjomat przeliczalności”** lub **„\(X\) spełnia drugi aksjomat przeliczalności”**. Dopuszczalne są również odmiany typu „przestrzeń spełniająca drugi aksjomat przeliczalności” i „niespełnianie pierwszego aksjomatu przeliczalności”.
- **Nie używamy** form „pierwszoprzeliczalna”, „pierwszo przeliczalna”, „drugoprzeliczalna”, „drugo przeliczalna” ani analogicznych odmian. W nagłówkach, treści twierdzeń, dowodach i podpisach stosujemy nazwy **„pierwszy aksjomat przeliczalności”** oraz **„drugi aksjomat przeliczalności”**, zamiast określeń „pierwsza/druga przeliczalność”.
- Reguła obowiązuje **globalnie we wszystkich polskojęzycznych skryptach matematycznych**. Zachowujemy stabilne etykiety LaTeX i odsyłacze nawet wtedy, gdy zawierają starsze słownictwo.
