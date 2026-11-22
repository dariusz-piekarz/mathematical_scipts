# Topologia ogólna — rozdział 20, audyt 06 (drugi czysty, stabilizacja matematyczna)

**Data:** 2026-11-22. **Źródło:** `chapters/pl/general_topology/20-zbiory-analityczne-i-operacja-suslina.tex`.
**Blob źródła, niezmieniony od audytów 04–05:** `2607376331f94935063107dee49148b45cc1679f`.
**Wynik:** **CZYSTY, 2/2**; matematyczne kryterium stabilizacji rozdziału 20 spełnione. Audyt 06 nie zmienia źródła.

## Samodzielny przegląd argumentów inną drogą

1. **Parametryzacja `\mathcal N\to X`.** Zamiast polegać na samej konstrukcji dowodu, zweryfikowano niezależnie jego trzy warunki: (a) `F_s=\bigcup_k F_{s^\frown k}`; (b) `\operatorname{diam} F_{\alpha|n}\to0`; (c) ciąg `x_n\in F_{\alpha|n}` jest Cauchy’ego dla dowolnego wyboru. Dają one odpowiednio surjektywność, jednoznaczność wartości i ciągłość na cylindrach.
2. **Rzuty i działania.** Graf ciągłej funkcji do Hausdorffa jest domknięty; domknięty podzbiór produktu polskich jest polski; kodowanie świadków w sumie rozłącznej i produkcie przeliczalnym zachowuje domkniętość. Pusty zbiór jest osobno obsłużony. W dowodach nie ma założenia kompaktowości rzutowanej przestrzeni.
3. **Borelowskość.** Z `\mathcal D=	ext{analityczne}\cap\text{koanalityczne}` konstruuje się `\sigma`-algebrę; każdy otwarty jest `F_\sigma` w metrycznej `X`, a domknięte w polskiej `X` są polskie. Borelowskie należą do `\mathcal D`.
4. **Rzut borelowski.** Dowiedziony kod blokowy `e` jest homeomorfizmem Baire'a na `G_\delta` Cantora; geometryczne osadzenie w `\mathbb R` jest iniekcją i homeomorfizmem na domknięty obraz. Domkniętość względna obrazu `F` w `\mathbb R^n\times E` implikuje reprezentację jako `H\cap(\mathbb R^n\times E)` z `H` domkniętym w `\mathbb R^{n+1}`, więc wynik jest borelowski.
5. **Operacja Suslina.** Bezpośrednio z cylindrów widać, że `H_n` ma otwarte dopełnienie. Odwrotne zawieranie można traktować jako argument domknięcia: jeżeli `x` należy do domknięć rzutów `H\cap(X\times[\alpha|n])` dla wszystkich `n`, to każde otoczenie `(x,\alpha)` przecina `H`; stąd `(x,\alpha)\in H`. Zgodne z oryginalnym dowodem ciągowym.
6. **Uniwersalne drzewo — alternatywna weryfikacja.** Dla dowolnego domkniętego `F\subseteq\mathcal N^2` zachodzi
   `F=\bigcap_{n\ge1}\bigcup_{(s,t)\in T_F,|s|=|t|=n}([s]\times[t])`.
   Inkluzja w prawo jest oczywista. Gdy `(x,y)\notin F`, otwarte dopełnienie zawiera pewne otoczenie cylindrowe `[x|n]\times[y|n]`, które nie przecina `F`; więc prefiks nie należy do `T_F` i `(x,y)` nie leży po prawej. Kod `1/2` realizuje dokładnie ten przekrój drzewa. Przy `F=\varnothing` warunek akceptacji żadnej gałęzi nie zachodzi.
7. **Przekątna.** Niezależny test logiki: dla rodziny `U_c` obejmującej wszystkie analityczne `A\subseteq\mathcal N`, jej zbiór diagonalnie przeciwstawny `D=\{c:c\notin U_c\}` nie może należeć do tej rodziny. `E=\mathcal N\setminus D` jest analityczny jako przeciwobraz `U` przez ciągłą przekątną, a nieborelowski z uwagi na analityczność borelowskich. Rozróżnienie ścisłości w przestrzeni Baire'a i braku ścisłości dla przeliczalnej dyskretnej pozostaje poprawne.

**Wniosek matematyczny:** brak nowych usterek, niezmieniony poprawiony kod `1/2` wystarcza do uzasadnienia Lematu 20.5.1 i Twierdzenia 20.5.2.

## Język, LaTeX, odniesienia i rzeczywista kompilacja

- Zachowano terminologię: „suma zbiorów” zamiast zakazanego anglicyzmu, brak niepoprawnych form aksjomatów przeliczalności, „uzwarcenie” i pełne założenia w sformułowaniach.
- 23 odrębne etykiety oraz 23 odsyłacze w rozdziale 20. Wszystkie cztery zewnętrzne cele są obecne w rozdziale 19. Liczniki środowisk `twierdzenie`, `lemat`, `definicja`, `stwierdzenie`, `wniosek`, `uwaga`, `przyklad`, `proof` są zrównoważone.
- Dedykowana [walidacja 45040786110](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45040786110) zakończona **success** dla commitu zawierającego badany blob. W jej krokach odnotowano sukces testów rozdziału 20, książki, oddzielnego PDF i kontroli logu LaTeX.
- PDF z artefaktu `general-topology-ch01-ch20` (ID `14761961399`): sześć stron A4, kontrola renderów 1–6, w tym oddzielny przegląd stron 5–6 zawierających poprawiony dowód. Brak nałożeń, ucięć, artefaktów typograficznych i komunikatów o przekroczonym składzie.

## Status

**ROZDZIAŁ 20 STABILNY MATEMATYCZNIE I REDAKCYJNIE (2/2)**. Należy uaktualnić opis wersji książki z „01–19 stabilne; 20 w audycie” na „01–20 stabilne”, następnie wykonać dodatkowy kontrolny audyt 07 bez zmiany źródła, aby spełnić rozszerzoną regułę „stabilność + jeden audyt potwierdzający”. Po nim można przejść do następnego niepowielającego istniejących rozdziałów tematu.
