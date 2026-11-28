# Audyt integralności odsyłaczy — partia XVIII, wystąpienia 222–234

**Data:** 20 listopada 2026 r.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło enumeracji:** `reference_provenance_audit_355.json`, 355 rozdziałów, 257 wystąpień problematycznych.

## Wynik

Zweryfikowano **13 niejednoznacznych wystąpień** w kanonicznym `TOP-06`. Każda cytowana nazwa ma dwóch właścicieli — w `TOP` i `DG`. Porównanie sensu cytowania, źródłowej definicji/twierdzenia, dowodów i przykładów pozwala we wszystkich 13 przypadkach przypisać właściciela **z tego samego skryptu topologii algebraicznej**, tj. `TOP-04` albo `TOP-05`. Nie poprawiono indeksu, nie przemianowano deklaracji ani cytowań.

## Tabela rozstrzygnięć

| Nr | Cytujące źródło | Oryginalna etykieta | Właściwy właściciel | Przedmiot porównania |
|---:|---|---|---|---|
| 222 | `TOP-06:760` | `thm:homotopia-singularna` | `TOP-05:354` | Homotopijna niezmienniczość homologii |
| 223 | `TOP-06:845` | `prz:pi1-dwa-okregi` | `TOP-04:840` | Grupa podstawowa bukietu dwóch okręgów |
| 224 | `TOP-06:852` | `prz:homologia-bukiet` | `TOP-05:1567` | Homologia bukietu okręgów |
| 225 | `TOP-06:1118` | `thm:homologia-sfer` | `TOP-05:794` | Homologia sfer i pary dysk–sfera |
| 226 | `TOP-06:1147` | `thm:homotopia-singularna` | `TOP-05:354` | Homotopijna niezmienniczość homologii |
| 227 | `TOP-06:1216` | `thm:warstwa-komorek` | `TOP-05:1121` | Homologia względna warstwy komórek |
| 228 | `TOP-06:1326` | `eq:formula-komorkowa` | `TOP-05:1336` | Współczynniki brzegu komórkowego |
| 229 | `TOP-06:1520` | `thm:homotopia-singularna` | `TOP-05:354` | Homotopijna niezmienniczość homologii |
| 230 | `TOP-06:1573` | `thm:formula-komorkowa` | `TOP-05:1318` | Twierdzenie o współczynnikach brzegu komórkowego |
| 231 | `TOP-06:1754` | `thm:homologia-sfer` | `TOP-05:794` | Homologia sfer i pary dysk–sfera |
| 232 | `TOP-06:1837` | `thm:homologia-sfer` | `TOP-05:794` | Homologia sfer i pary dysk–sfera |
| 233 | `TOP-06:1849` | `def:stopien-sfer` | `TOP-05:1283` | Stopień odwzorowania sfery |
| 234 | `TOP-06:1913` | `prz:homologia-rp2` | `TOP-05:1476` | Homologia płaszczyzny rzutowej |

## Kontrola matematyczna i semantyczna

1. **`TOP-06:760,1147,1520` — `thm:homotopia-singularna`, właściciel `TOP-05:354`.** W trzech miejscach korzysta się z homotopijnej niezmienniczości homologii singularnej. Jest to dokładnie twierdzenie skonstruowane za pomocą operatora pryzmatycznego. Nie należy go utożsamiać wyłącznie z twierdzeniem o homotopii łańcuchowej.
2. **`TOP-06:845,852` — bukiet okręgów.** `TOP-04:840` oblicza \(\pi_1(S^1\vee S^1)=F_2\), zaś `TOP-05:1567` daje \(H_1(\bigvee_{r}S^1)=\mathbb Z^r\). Pierwszy przykład w cytowanym miejscu dotyczy wprost dwóch okręgów, a uogólnienie do dowolnego \(r\) korzysta z van Kampena; porównać to przy późniejszym audycie dydaktycznym.
3. **`TOP-06:1118,1754,1837` — `thm:homologia-sfer`, `TOP-05:794`.** Twierdzenie o homologii sfer jest właściwe dla definicji odwzorowania Hurewicza, względnego generatora \((D^n,S^{n-1})\) oraz pierwszej niezerowej grupy \(\pi_n(S^n)\).
4. **`TOP-06:1216` — `thm:warstwa-komorek`, `TOP-05:1121`.** Twierdzenie cytowane jest pierwotnie dla skończonych CW. `TOP-06` jawnie korzysta z osobnego rozszerzenia na dowolne CW oraz pary CW. **Weryfikacja matematyczna kolejnego audytu** powinna sprawdzić w szczegółach ograniczenie do skończonych podkompleksów i przejście do granicy prostej — nie wolno stosować wersji skończonej bez tego kroku.
5. **`TOP-06:1326,1573` — `eq:formula-komorkowa`, `thm:formula-komorkowa`, `TOP-05:1336,1318`.** Odsyłacze dotyczą tego samego schematu stopni odwzorowań dołączających i współczynników różniczki w kompleksie komórkowym. Rozróżnienie odsyłacza do wzoru i odsyłacza do twierdzenia jest zachowane.
6. **`TOP-06:1849` — `def:stopien-sfer`, `TOP-05:1283`.** Wykorzystanie stopnia sfery jako liczby całkowitej pochodzącej z działania na \(H_n(S^n)\) jest zgodne z definicją.
7. **`TOP-06:1913` — `prz:homologia-rp2`, `TOP-05:1476`.** Zgodne \(H_2(\mathbb{RP}^2;\mathbb Z)=0\) jest zestawiane z \(\pi_2(\mathbb{RP}^2)\cong\mathbb Z\), aby wskazać konieczność hipotezy jednospójności w wyższym twierdzeniu Hurewicza.

**Uwaga dotycząca pełnego skryptu geometrii różniczkowej:** liczy on 36 rozdziałów, a na obecnej gałęzi obecnych jest 20. Nieobecności etykiet w tej niepełnej części nie są jeszcze dowodem nieobecności treści w pełnym skrypcie.

## Rekomendacja implementacyjna

W aplikacji rozwiązywać nieprefiksowaną etykietę najpierw względem skryptu, do którego należy rozdział cytujący, zachowując wszystkie źródłowe wystąpienia i pierwotne `\label`, `\ref`, `\eqref`. Zmiany własności i deduplikacja treści dopiero przy planowanym później scalaniu; obecny audyt nie usuwa kolizji fizycznie.

**Postęp:** 234/257 przejrzanych wystąpień; 23 pozostałe. Następna partia: 235–247. W tej iteracji nie zmieniano `chapters/pl/`, `main`, oryginalnych etykiet ani nie scalano skryptów.