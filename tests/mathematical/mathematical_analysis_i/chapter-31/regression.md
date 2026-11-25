# MA1-31 — trwałe kryteria regresyjne
Testy Python sprawdzają skończone świadki, dokładne tożsamości i oszacowania; nie zastępują dowodów granicznych.
| ID | Etykieta | Kryterium | Metoda |
|---|---|---|---|
| MA1-31-001 | ma1:def:improper-infinite | Całkowalność obcięć, granica skończona, oba końce nieskończone | semantyczna |
| MA1-31-002 | ma1:def:improper-finite | Granica jednostronna, zgodność z Riemannem przy całkowalnym przedłużeniu | semantyczna |
| MA1-31-003 | ma1:def:improper-splitting | Niezależne granice, podział przy wszystkich osobliwościach, odbicie sum Riemanna również dla nieciągłej f | semantyczna + Python |
| MA1-31-004 | ma1:thm:improper-cauchy | Oba kierunki, zupełność, dowolny argument, skończony lub nieskończony koniec | semantyczna + Python |
| MA1-31-005 | ma1:thm:improper-positive | Supremum, monotoniczność i rozbieżność do +infty | semantyczna |
| MA1-31-006 | ma1:thm:improper-comparison | Nieujemność na końcowym odcinku i dwa kierunki implikacji | semantyczna + Python |
| MA1-31-007 | ma1:cor:improper-limit-comparison | L dodatnie skończone, L=0 oraz L=+infty | semantyczna |
| MA1-31-008 | ma1:ex:improper-p-integrals | p=1 osobno, przeciwne progi przy zerze i nieskończoności | semantyczna + Python |
| MA1-31-009 | ma1:ex:improper-log-test | Podstawienie na obcięciach, próg p>1 | semantyczna + Python |
| MA1-31-010 | ma1:def:improper-absolute, ma1:thm:improper-absolute-convergence | Cauchy dla modułu, nierówność trójkąta, kilka osobliwości | semantyczna + Python |
| MA1-31-011 | ma1:thm:improper-dirichlet | Ciągłość f, monotoniczne C1 g, oba znaki, oszacowanie 2M abs(g(u)) | semantyczna + Python |
| MA1-31-012 | ma1:thm:improper-abel | Skończona granica g, rozkład g-L, ograniczona funkcja całki częściowej | semantyczna + Python |
| MA1-31-013 | ma1:ex:improper-sinx-over-x | Zbieżność Dirichleta i rozbieżność modułu przez szereg harmoniczny | semantyczna + Python |
| MA1-31-014 | ma1:def:cauchy-principal-value | Niezależne granice a zsynchronizowane obcięcia, całkowalność obcięć, skończona granica | semantyczna |
| MA1-31-015 | ma1:ex:principal-value-counterexamples | PV zero, rozbieżność obu części, zależność log(k) od obcięcia | semantyczna + Python |
| MA1-31-016 | ma1:thm:improper-substitution | Obcięcia, ciągłe przedłużenie przy a, dojście do końca, odwrotny kierunek przez wartość pośrednią, dopuszczalny odcinek stałości | semantyczna + Python |
| MA1-31-017 | ma1:thm:improper-parts, ma1:ex:improper-parts-exp | Skończona granica iloczynu, zbieżność jednej całki, przykład exp | semantyczna + Python |
| MA1-31-018 | ma1:ch:improper-integrals | Czytelność wykresu x^-1 i x^-2, poprawne pole obcięte | Python + PDF |
