# PDE — rozdział 10 — trwałe kryteria regresyjne

Pierwsza lektura, iteracja 148. Kryteria semantyczne nie są wykonanymi testami automatycznymi ani formalizacją Lean.

| ID | Etykieta | Kryterium | Metoda |
| --- | --- | --- | --- |
| PDE-10-001 | chap:pde-embeddings | Zakres d,p, niepusty zbiór otwarty, funkcje rzeczywiste, rozróżnienie zanurzeń ciągłych i zwartych; norma euklidesowa gradientu a norma składowych z rozdziału 09, również p=infty. | semantyczna |
| PDE-10-002 | lem:pde10-LW | Nieujemne mierzalne funkcje, przypadki całek zerowych i nieskończonych, konwencja iloczynu przez granicę obcięć. | semantyczna |
| PDE-10-003 | lem:pde10-LW | Baza d=2 przez Tonellego; pierwszy Hölder dla d-1 czynników, niezależność G_j od x_j. | semantyczna |
| PDE-10-004 | lem:pde10-LW | Drugi Hölder z wykładnikami d-1 i (d-1)/(d-2), hipoteza indukcyjna, Fubini i poprawne potęgi. | semantyczna |
| PDE-10-005 | lem:pde10-LW | Jawne obcięcia min(F_j,n) na [-n,n]^(d-1), zbieżność monotoniczna także przy całkach 0 i nieskończonych. | semantyczna |
| PDE-10-006 | thm:pde10-Sob1 | Całkowanie od minus nieskończoności dzięki zwartemu nośnikowi, iloczyn d oszacowań, Loomis–Whitney i Tonelli. | semantyczna |
| PDE-10-007 | thm:pde10-Sob1 | Potęga (d-1)/d, średnie geometryczna i arytmetyczna, jawna stała 1/sqrt(d) dla gradientu euklidesowego. | semantyczna |
| PDE-10-008 | thm:pde10-Sobp | Dla 1<p<d gamma>1, abs(t)^gamma klasy C¹ także w zerze, zwarty nośnik v, zastosowanie twierdzenia dla p=1. | semantyczna |
| PDE-10-009 | thm:pde10-Sobp | Hölder z p,p', rachunek gamma*d/(d-1)=p*, (gamma-1)*p'=p*, dzielenie wyłącznie przy u niezerowym. | semantyczna |
| PDE-10-010 | thm:pde10-Sobp | Gęstość z rozdziału 09, Cauchy w L^{p*}, identyfikacja granic przez Czebyszewa także przy nieskończonej mierze; zachowanie stałej. | semantyczna |
| PDE-10-011 | rem:pde10-critical | Zakres 1<=p<d, 1<=q<=infty, skalowanie norm również dla q=infty, ograniczenie W^{1,p}, rozbieżność dla q>p*. | semantyczna |

## Iteracja 148
Źródło przed 22b013b3e972ece5feaa83488df6fdc89a1f3bfe; po 7678d73026ba49e7060cda158e4286c2e559f165, commit e504d11f70adbc028f346cab57807d5ed40c22b8. Przejrzano wstęp, Loomisa–Whitneya, Sobolewa dla p=1 i 1<p<d, skalowanie. Jedenaście zmian źródłowych: hipotezy i norma, przypadki całek 0 i nieskończonych, baza indukcji, obcięcia, całkowanie po prostej, stała gradientowa, regularność potęgi w zerze, wykładniki, identyfikacja granic, hipotezy i ograniczenie norm w skalowaniu. Zachowano kolejność 32 etykiet; stos środowisk poprawny; materiał od definicji obszaru Lipschitzowskiego bez zmian. Dodano trzy odsyłacze do rozdziału 09. Nie uruchamiano testów Python, CI, kompilacji ani Lean w tej iteracji. Pierwsza próba zapisu raportu: konflikt współbieżnej aktualizacji gałęzi, ponowiono zapis. Następny etap: obszary Lipschitzowskie, przedłużanie, gęstość i zanurzenia. Pierwsza lektura otwarta.
