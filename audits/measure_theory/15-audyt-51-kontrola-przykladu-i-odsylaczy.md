# Audyt LI (51): rozdział 15 — dualność, wypukłość i słaba zbieżność w L^p

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`.

## Zakres

Następna iteracja po audycie L (50) rozdziału 15. Skontrolowano źródło `chapters/pl/measure_theory/15-dualnosc-wypuklosc-i-slaba-zbieznosc-w-przestrzeniach-lp.tex` (przed zmianą blob `d41de3e4f4e7faad473065b3f472e5f6fa95b352`, po zmianie blob `075e6e30bc73a28450b7ffcb6af6b8fe9a76f8ab`). Nie rozpoczynano rozdziału 16.

Sprawdzono twierdzenia i dowody o: izometrycznym zanurzeniu `L^q\to(L^p)^*`, oszacowaniach punktu środkowego (oba zakresy `p`), jednostajnej wypukłości, istnieniu minimizatora przez ciąg Cauchy'ego, reprezentacji dualnej `1<p<\infty` bez sigma-skończoności, reprezentacji `L^1` przy sigma-skończoności, refleksywności, słabej zbieżności, dolnej półciągłości normy, wyborze podciągu w wariancie separowalnym oraz minimalizacji energii.

## Wykryta luka i poprawka

W przykładzie `[Norma funkcjonału całkowego]` wstępne założenie `0<\alpha<1/q` pozostawało w sprzeczności z następnym rozpatrywanym przypadkiem `\alpha q\ge1`. Poprawiono zakres założenia na `\alpha>0` oraz jawnie rozdzielono przypadki.

Niewykazany dotąd brak ograniczoności w przypadku `\alpha q\ge1` otrzymał konstruktywny dowód. Niech `g=x^{-\alpha}`, `g_N=g\chi_{\{g\le N\}}`, `f_N=g_N^{q-1}/\|g_N\|_q^{q-1}`. Wtedy `\|f_N\|_p=1` oraz `\int_0^1 f_Ng\,\mathrm d\lambda_1=\|g_N\|_q\to\infty`. Dzięki ucięciu nośnika w pobliżu zera każda całka jest skończona; zbieżność do nieskończoności wynika z twierdzenia o zbieżności monotonicznej. Nie dodawano nowych twierdzeń ani rozdziałów.

**Commit źródła:** [012d74e64a1566c2ca50fd63fcd582ec12c5b151](https://github.com/dariusz-piekarz/mathematical_scipts/commit/012d74e64a1566c2ca50fd63fcd582ec12c5b151).

## Niezależne kontrole po poprawce

- Ponownie pobrano bezpośrednio z GitHub 15 kanonicznych plików LaTeX rozdziałów 01–15. Zidentyfikowano 343 unikatowe etykiety; 0 duplikatów.
- Rozdział 15: 17 etykiet, 17 odsyłaczy `\ref` lub `\eqref`, 17/17 celów odnalezionych w rzeczywistym zbiorze rozdziałów 01–15.
- Liczniki środowisk rozdziału 15: 8 twierdzeń, 3 lematy, 1 wniosek, 2 definicje, 2 przykłady, 3 uwagi, 12 dowodów, 2 środowiska `equation`, 1 `enumerate`. Każdy licznik `\begin` zgadza się z licznikiem `\end`.
- Brak użycia `\mathbf{1}_A` i `\mathbb{1}_A`; w poprawce użyto wyłącznie `\chi_A`.
- 180 000 deterministycznych obliczeń kontrolnych dla dwóch oszacowań punktu środkowego przy `p\in\{1.1,1.25,1.5,1.9,2,2.5,3,4,8\}`: 0 naruszeń po uwzględnieniu dokładności zmiennoprzecinkowej. Są to kontrole numeryczne, **nie** dowód twierdzeń.
- Zweryfikowano analitycznie normalizację `f_N`, równość `\int f_Ng=\|g_N\|_q` i rozbieżność zarówno dla przypadku granicznego `\alpha q=1`, jak i `\alpha q>1`. Kontrole numeryczne dla przykładowych parametrów potwierdzają tę zależność.

## Stan stabilizacji i blokery

**Rozdział 15 pozostaje w stabilizacji**, ponieważ dokonano zmiany w źródle po audycie L. Wcześniejsze wyniki CI i PDF dotyczą wcześniejszego bloba i nie potwierdzają automatycznie obecnej wersji. Po zmianie nie uzyskano potwierdzenia pełnej kompilacji LaTeX ani oględzin wszystkich stron aktualnego PDF. Odczyt dostępnych legacy statusów commita i workflow ograniczonych do PR zwrócił puste zestawy: nie należy interpretować tego jako sukcesu ani porażki całego CI.

Kolejny krok: niezależny czysty audyt na niezmienionym blobie `075e6e30bc73a28450b7ffcb6af6b8fe9a76f8ab`, pełny aktualny LaTeX/PDF, kontrola wizualna wszystkich stron rozdziału 15, potwierdzone CI; dopiero po spełnieniu kryteriów stabilności można przejść do rozdziału 16.
