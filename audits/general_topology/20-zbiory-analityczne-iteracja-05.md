# Topologia ogólna — rozdział 20, audyt 05 (pierwszy czysty po poprawce)

**Data:** 2026-11-22. **Badany niezmieniony blob:** `2607376331f94935063107dee49148b45cc1679f`.
**Wynik:** **CZYSTY — 1/2** kolejnych czystych kontroli tego samego bloba.
**Źródło:** `chapters/pl/general_topology/20-zbiory-analityczne-i-operacja-suslina.tex`.

## Kontrola matematyczna

Niezależnie od audytu 04 sprawdzono łańcuch wnioskowania:

1. W lemacie o parametryzacji niepustego `X` przez `\mathcal N` przekroje domkniętych kul wyznaczają niepuste domknięte następniki, pokrycie każdego `F_s`, malejące średnice i jednoznaczną granicę na każdej gałęzi; rekurencyjny wybór następników daje surjekcję.
2. Charakterystyka analitycznych przez rzut domkniętego w `X\times\mathcal N` obsługuje przypadek pusty, a graf ciągłego odwzorowania jest domknięty w metryzowalnym produkcie.
3. Domknięte zbiory świadków dla przeliczalnej sumy (rozłączne znaczniki) i przecięcia (produkt świadków) są rzeczywiście domknięte. W przecięciu przeliczalny wybór świadków jest dozwolony w ZFC.
4. Przeciwobraz analitycznego przez ciągłe `f` odtwarza domkniętych świadków przez `(x,u)\mapsto(f(x),u)`. Obrazy używają złożenia.
5. W dowodzie borelowskości `\mathcal D=\{B:B, X\setminus B\text{ analityczne}\}` jest `\sigma`-algebrą; otwarte są typu `F_\sigma` i ich domknięte składowe są analityczne, bez zastosowania dowodzonej tezy.
6. Konstrukcja `e:\mathcal N\to C_\infty\subseteq2^{\mathbb N}` ma jednoznaczne rozdzielanie blokami jedynek, jest homeomorfizmem; `C_\infty` jest `G_\delta`. Osadzenie trójkowe Cantora daje borelowski `E\subseteq\mathbb R` i domknięty względnie obraz `F`, więc rzut borelowskiego zbioru z `\mathbb R^{n+1}` jest równoważny analityczności w `\mathbb R^n`.
7. Operacja Suslina: dla `H_n=\bigcup_{|s|=n}(F_s\times[s])` dopełnienie jest otwarte, `\bigcap H_n` domknięty; w odwrotnej implikacji dla `x\in\bigcap_n\overline{\pi(H\cap(X\times[\alpha|n]))}` świadkowie dążą do `(x,\alpha)\in H`.
8. **Weryfikacja naprawionego lematu uniwersalnego:** każdy kod `c` zawiera wartości `1/2`, a warunek `c_{e(x|n,y|n)}=1` wybiera dokładnie gałęzie drzewa `T_F`. Nawet dla `F=\varnothing`, otrzymujemy `T_F=\varnothing` oraz `U_c=\varnothing`. Dla `F=\mathcal N^2` wszystkie istotne współrzędne są równe 1 i `U_c=\mathcal N`. Dla dowolnego domkniętego `F` zbieżność świadków zgodnych na rosnących prefiksach daje równoważność `H_c=F`.
9. **Przekątna:** gdyby zbiór `D=\{x:(x,x)\notin U\}` był analityczny, universality dawałaby kod `c` z `D=U_c`, a następnie `c\in D\iff c\notin D`. `E=\mathcal N\setminus D` jest analityczny jako przeciwobraz ciągłej przekątnej i nieborelowski, gdyż borelowskość `E` pociągałaby analityczność `D`. Teza jest wyraźnie ograniczona do `\mathcal N`, nie do wszystkich przestrzeni polskich.

Nie znaleziono dalszych błędów, brak niejawnego zastosowania twierdzeń o determinacji, rozdzielaniu albo uniwersalnej mierzalności.

## Skład, integracja i CI

- Aktualny plik ma **859 wierszy**, **23 różne etykiety**, **23 odsyłacze**. Cztery odsyłacze zewnętrzne kierują do rzeczywiście obecnych etykiet rozdziału 19: `ch:topog-polskie-borelowskie`, `ex:topog-polskie-cantor-baire`, `thm:topog-polskie-iloczyn`, `lem:topog-polskie-otwarte-fsigma`. Brak niezrównoważonych środowisk twierdzeń i dowodów. Nie występuje stary predykat `>0` w kodowaniu.
- [GitHub Actions 45040786110](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45040786110) **completed/success** dla commitu `14729987a729b894821bdc0bfbff25f3aa28929c`, zawierającego dokładnie badany blob `26073763...`. Sprawdzono konkretne zakończone kroki: test modelu operacji Suslina i drzewa kodów, kontrola katalogu i odsyłaczy, kompilacja całej książki, samodzielnego rozdziału 20, kontrola logu LaTeX, publikacja artefaktu.
- Pobrano **rzeczywisty artefakt** `general-topology-ch01-ch20`, ID `14761961399`, z tej walidacji. Rozpakowano `general_topology_ch20.pdf` (6 stron A4) i `general_topology_ch20.log`; strony 1–6 wyrenderowano i przejrzano w układzie zbiorczym, strony 5–6, obejmujące poprawiony lemat i przekątniowanie, obejrzano osobno w pełnej rozdzielczości. Nie stwierdzono nakładania się tekstów, uciętych znaków, uszkodzonych wzorów ani problemów łamania stron; brak komunikatów `Overfull`, `Underfull`, `Missing character`, `LaTeX Warning` i niepoprawnych odsyłaczy w logu.

**Status:** **1/2**, po audycie 05 nie zmieniono źródła. Następny audyt 06 musi dotyczyć identycznego bloba, ponownie samodzielnie sprawdzając matematyczną poprawność i testy. Dopiero druga czysta kontrola pozwala uznać rozdział 20 za stabilny.
