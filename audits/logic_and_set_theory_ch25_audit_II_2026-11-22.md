# Logika matematyczna i teoria mnogości — rozdział 25, audyt II

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/25-aksjomaty-zf-zfc-i-konstrukcje-zbiorowe.tex`  
**Zasada:** wyłącznie audyt rozdziału 25, bez dodawania nowych twierdzeń, lematów i przykładów.

## Wykryte luki i poprawki
1. **Własność dziedzin przybliżeń w rekursji.** W dowodzie lematu o następniku jawnie wykazano przez indukcję $0\in S(n)$ dla każdego $n\in\omega$ oraz przypomniano $n\in S(n)$. Wcześniej definicja $n$-przybliżenia odwoływała się do $f(0)$ bez wykazania, że argument zero należy do dziedziny $S(n)$.
2. **Poprawność konstrukcji przybliżeń.** Dodano uzasadnienie, dlaczego $f_n(n)$ jest określone; doprecyzowano, że przybliżenia istnieją przez separację w $\mathcal P(S(n)\times B)$, a globalna funkcja nie jest zakładana z góry.
3. **Zastępowanie w rekurencji.** Zapisano własność definiującą jedyną wartość $y=f_n(n)$ przez istnienie funkcji $f$ o dziedzinie $S(n)$ spełniającej określone równania, po czym użyto zastępowania do jednoznacznych par $(n,y)$. Wyklucza to nieuzasadniony przeskok od indukcyjnie dowiedzionych przybliżeń do zbioru wykresu.
4. **Zakres indukcji Peana.** Uściślono, że kwantyfikacja po $X\subseteq\omega$ jest wewnętrzna względem ZF. W arbitralnym modelu ZF nie twierdzimy, że obejmuje wszystkie zewnętrzne podzbiory jego interpretacji $\omega$.
5. **Dzielenie z resztą.** W kroku indukcyjnym uzasadniono ścisłą nierówność $t<t+b=a$ przez $0<b$ i wcześniej dowiedzioną monotoniczność dodawania. W dowodzie jednoznaczności wyprowadzono jawnie obie nierówności $bq+b\le bq'$ oraz $bq'\le bq'+r'$.

## Powtórna kontrola
- Zweryfikowano wszystkie dziewięć podstawowych rodzin aksjomatów ZF, schematy separacji i zastępowania oraz rozróżnienie ZF od ZFC.
- Zweryfikowano istnienie iloczynu kartezjańskiego, najmniejszego zbioru indukcyjnego, diagonali Cantora oraz wszystkich przejść w dowodach praw dodawania, mnożenia i potęgowania.
- Sprawdzono niekolisty porządek zależności: konstrukcja $\omega$ → własności następnika → rekurencja → dodawanie → mnożenie → porządek → indukcja silna → dzielenie z resztą.
- Zasady terminologiczne zachowano; nie zmieniono inwentarza: **16 definicji, 14 przykładów, 6 lematów, 11 twierdzeń, 2 wnioski, 5 uwag, 19 dowodów, 1 rysunek**. Pozostało **46 etykiet**, liczba odsyłaczy wzrosła z 23 do **25** przez dodanie uzasadnionych referencji.
- Uaktualniono kontrolę strukturalną CI oraz rozszerzono testy o kontrolę argumentów przybliżeń, zakresu indukcji i nierówności przy dzieleniu.

## Status
Pierwszy przebieg testów po korektach: testy rozdziału 25 **PASS** (workflow 45004356090), pełna kompilacja w toku w momencie sporządzania tego raportu. Kolejny audyt stabilizacyjny musi obejmować gotowy PDF i aktualny log kompilatora.

**Werdykt:** audyt II wykrył i usunął luki w uzasadnieniach; **do audytu III**.
