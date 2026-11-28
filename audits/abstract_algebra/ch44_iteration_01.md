# AA-44 — audyt I: kontrola wstępna

**Data:** 23 listopada 2026 r. **Werdykt: NIE STABILNY.**

Utworzono rozdział na podstawie stabilnego AA-43 i materiału w sources/pl/galois(2).tex. Zawartość: formalna część wielomianowa pochodnej, ślad i norma dla kroku algebraicznego, współczynniki najwyższych potęg dla kroku logarytmicznego, wykluczenie nowych stałych w kroku wykładniczym oraz konstrukcja wieży w dowodzie dostateczności.

**Kontrola logiczna:** (1) D części właściwej funkcji wymiernej jest właściwe dla Dt=a i Dt=ht; (2) pochodne logarytmiczne mają tylko stałą w t część wielomianową; (3) dla stopnia m>=2 w kroku logarytmicznym powstałaby nowa stała; (4) dla dodatniego wykładnika t w kroku wykładniczym powstałaby nowa stała; (5) dostateczność dołącza tylko brakujące funkcje pierwotne, zachowując stałe.

**Integracja:** dwa testy (SymPy i niezależny model Fraction), książka, katalog, bramka 44 rozdziałów i workflow CI. Historyczny przekrojowy audyt 42 rozdziałów pozostaje nienaruszony.

**Otwarte warunki:** rzeczywiste uruchomienie CI; drugi niezależny audyt matematyczny; log LaTeX; PDF i oględziny każdej nowej strony. AA-45 nie rozpoczynać przed formalnym statusem STABILNY AA-44.
