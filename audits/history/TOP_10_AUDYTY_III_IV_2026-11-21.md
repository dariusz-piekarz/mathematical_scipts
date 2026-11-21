# Topologia algebraiczna — TOP-10, audyty III–IV (drugi cykl)

**Data:** 2026-11-21  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/algebraic_topology/10-homologia-i-kohomologia-c-echa-od-pokryc-do-granic-przestrzeni.tex`.

## Audyt III: twierdzenie o kohomologii Čecha przez otoczenia

Po audycie II zweryfikowano dokładnie przejście od nerwów pokryć zwartego $A\subset S^n$ do kohomologii singularnej jego otwartych otoczeń. Poprzednie ujęcie nie wyjaśniało dostatecznie kompatybilności nerwów dla dzikich zbiorów zwartych.

Poprawiono **dowód istniejącego twierdzenia**, bez dodawania nowego twierdzenia/lematu: dla skończonego pokrycia $\mathcal U=(U_i)$ zbioru $A$ wybrano zwarte $K_i\subset U_i$ pokrywające $A$, a przez dodanie punktów świadczących o niepustych przecięciach otrzymano równość nerwów. Dla dostatecznie małego $\varepsilon>0$ otwarte $\varepsilon$-otoczenia $V_i$ mają te same wzorce niepustych przecięć co $U_i$, pokrywają otwarte otoczenie $N$ zbioru $A$, i po ograniczeniu do $A$ tworzą rozdrobnienie oryginalnego pokrycia. Pokazano, dlaczego tak dobrane przedłużenia umożliwiają surjektywność i iniektywność w granicy prostej. Na otwartych podzbiorach sfery cohomologia Čecha zgadza się z singularną dzięki kofinalnym dobrym pokryciom z otwartych kul geodezyjnie wypukłych i lematowi o nerwie. Uściślono wykorzystanie tego faktu, nie utożsamiając automatycznie nerwów dowolnego pokrycia otoczenia i jego śladów na $A$.

**Commit źródła:** `df4c0cd4ee3e49981ae7315b403d22f1bea79ab9`; **test regresyjny:** `43052666869195beea1d7ea2726d43065dcd36b6`.

## Audyt IV: przypadki graniczne i redakcja

Dopisano oddzielny przypadek $n=0$ w opisie przez otoczenia: $S^0$ jest dyskretny, a grupy wynoszą $G^{|A|}$ w stopniu zero i 0 w pozostałych. Pominięto puste składniki pokrycia $\mathcal U$, co zapewnia poprawność definicji metrycznych $\varepsilon$-otoczeń zwartych $K_i$. Poprawiono określenie „otwarte zsumowanie” na „otwarta suma”.

**Commity źródła:** `4cf3fd3becd4176c8479aa56b1add78823b6e550`, `7f6e955688e2bc0b32ecf7b2dbfdf97e2e1a376a`.

## Weryfikacja wersji na GitHubie

- Po audycie III sprawdzono źródło udostępnione przez GitHub: rozdział ma **11 unikalnych etykiet**. Nie ma brakujących ukośników w makrach $\Sigma_p,\pi_j,\sqcup$ ani dawnej literówki „rozdrobnienień”.
- Dla commita audytu III `df4c0cd4` trzy workflowy zakończyły się statusem **success**:
  - [TOP-09–10 TeX](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44922847512);
  - [aplikacja i testy](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44922847524);
  - [odsyłacze międzytomowe](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44922847532).
- Dla ostatniego commita `7f6e9556` uruchomienia CI pozostawały w toku podczas sporządzania tego raportu; ich wyniku nie deklarujemy z góry.

**Stan:** Audyty I–IV wykonane, poprawki opublikowane; następny audyt powinien być niezależnym czystym przeglądem finalnego źródła i wyniku CI na najnowszym commicie. Do tego momentu nie nadajemy rozdziałowi oznaczenia „stabilny”. Nie dodano tematów, twierdzeń ani lematów. Automatyzacje pozostają wyłączone.
