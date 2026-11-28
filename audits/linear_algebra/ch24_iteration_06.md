# Algebra liniowa — rozdział 24, audyt VI (stabilizacyjny)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/24-rownania-riccatiego-i-sterowanie-liniowo-kwadratowe.tex`.  
**Kontrolowany blob:** `82b136e5bd2284442a47d1e740207b2ee3bda816`.  
**Historia:** I (korekta matematyczna), II–III (czyste), IV (poprawka składu), V–VI (dwie kolejne czyste kontrole).

## Ostateczny audyt

1. **Założenia.** Wymiary A, B, Q, R, P i K są zgodne; Q i R są hermitowskie dodatnio określone, a stabilność otwartej pętli jest wymagana tylko w twierdzeniach o nieskończonym horyzoncie. Nie użyto nieudowodnionych założeń o sterowalności.
2. **DARE.** Indukcja Bellmana, monotoniczność i ograniczenie macierzy P_N, przejście do algebraicznego równania oraz stabilność sprzężenia zwrotnego wynikają z jawnych argumentów. Poprawiony dowód jednoznaczności dla *dowolnych* hermitowskich rozwiązań stabilizujących wykorzystuje D=A_1*DA_2 i nie wymaga dodatniości M_2.
3. **CARE.** Różniczkowe równanie Riccatiego ma globalne rozwiązanie dzięki lokalnej jednoznaczności oraz oszacowaniu z kosztu sterowania zerowego. Monotoniczna granica przy A Hurwitz jest dodatnio określona i spełnia CARE. Ciągłe twierdzenie Lapunowa dowodzi stabilności zamkniętej pętli.
4. **Koszt i jednoznaczność.** Obie tożsamości uzupełnienia kwadratu mają właściwy znak i poprawne warunki brzegowe; w czasie ciągłym jednoznaczność optymalnego sterowania jest rozumiana prawie wszędzie. Dla sterowania o skończonym koszcie wykazano x_k→0 w czasie dyskretnym oraz x(t)→0 z x,u,x'∈L² w czasie ciągłym.
5. **Przykłady.** Przeliczono dokładne pierwiastki p=1,-7/8 dla DARE i p=1,-3 dla CARE, sprawdzono odpowiednio stabilne oraz niestabilne sprzężenia. Dwuwymiarowe przykłady mają zerowe residua na ułamkach wymiernych.
6. **Skład i referencje.** 26 unikatowych etykiet, 31 odsyłaczy, 8 poprawnie sparowanych środowisk proof, zgodność z `AGENTS.md`. Ostatnia korekta dotyczy wyłącznie krótszego tytułu wniosku „Sterowanie optymalne”; numer i etykieta zachowane.
7. **CI.** [Run 44947590313](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44947590313) **SUCCESS** dla dokładnego bloba po ostatniej poprawce, w tym regresja `tools/test_linear_algebra_riccati.py`, pełna kompilacja, odsyłacze i log bez ostrzeżeń. [Run 44947606263](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44947606263) także **SUCCESS**.
8. **PDF.** Artefakt `linear-algebra-current-chapter` z runu 44947590313 ma **10 stron** i zawiera wyłącznie rozdział 24. Wszystkie strony są niepuste; PyMuPDF wykazał **0 bloków tekstu poza stroną**. Render wszystkich stron został obejrzany: brak widocznych kolizji i ucięć.

## Decyzja

**Audyt VI czysty**, drugi kolejny przebieg bez poprawek po audycie IV. Rozdział 24 uznany za **STABILNY po sześciu audytach**. Łączny status algebry liniowej: **01–24 stabilne**. Nie poszerzono treści wcześniejszych zamkniętych rozdziałów.

**Opcjonalna propozycja na osobny przyszły rozdział:** sterowalność i stabilizowalność, wykrywalność oraz klasyczne uogólnienia teorii Riccatiego poza stabilną otwartą pętlę. Nie dopisano ich do zatwierdzonego rozdziału 24.
