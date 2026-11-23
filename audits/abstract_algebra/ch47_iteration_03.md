# AA-47 — audyt III: końcowa stabilizacja algorytmów Rischa i Kovacica

**Data:** 23 listopada 2026 r.
**Werdykt: AA-47 STABILNY w jasno zdefiniowanym zakresie.**
**Gałąź:** biblioteka-matematyczna-iteracja-6.
**Źródło:** chapters/pl/abstract_algebra/47-algorytmy-rischa-i-kovacica.tex.
**Blob SHA źródła:** 1890492adea6acec062972a621b75b00636a6916.
**Blob SHA testów SymPy:** 199d7801ab0d64d7dc9b8e28ca0ce6e224c3f666.
**Blob SHA testów niezależnych Fraction:** 54996a368f37cc5e05e03c34086e7e5a310f5c73.
**Zakres zatwierdzony jako osobny dokument:** docs/pl/zakres_aa47_risch_kovacic.md.

## 1. Kontrola merytoryczna i kompletność dokładnie wyznaczonego zakresu

Wcześniejsze raporty ch47_iteration_01.md i ch47_iteration_02.md dokumentują dwa odrębne przeglądy matematyczne, w tym niezależny audyt kroków decyzyjnych.

1. **Ciało współczynników:** określono warunki efektywnej reprezentacji, dokładnych działań i rozkładu wielomianów. Nie utożsamiono dowolnego elementu C bez reprezentacji z obliczalnym wejściem.
2. **Całkowanie wymierne:** pełny dowód rozkładu f=R'+Σ c_a/(x-a), rachunek części głównych rzędu ≥2, kryterium znikania residuów dla wymiernej funkcji pierwotnej i konstrukcja elementarnej pierwotnej dla każdej funkcji wymiernej.
3. **Rothstein–Trager:** wynik wypadkowy T(z)=Res_x(B,A-zB')=∏_{B(a)=0}(A(a)-z B'(a)), gdy B jest unormowany i bez pierwiastków wielokrotnych; test residuów c_a=A(a)/B'(a); grupowanie czynników przez P_c=gcd(B,A-cB') i pełna rekonstrukcja A/B=Σ_c cP_c'/P_c.
4. **Efektywny szczególny przypadek Rischa:** dla h∈C[x], s∈C(x) dowiedziono konieczności i dostateczności skończonej procedury rozwiązania r'+hr=s. W biegunach s stopnia m≥2 rekurencyjnie wyznaczane są wyrazy części głównej r; biegun prosty jest przeszkodą; po usunięciu biegunów rozstrzyga się skończony liniowy układ dla części wielomianowej. Osobno poprawne są h stałe niezerowe, dodatniego stopnia, S=0, oraz h=0 rozpatrywane przez algorytm wymierny.
5. **Redukcja Kovacica:** przez obliczenie pochodnych dowiedziono, że równanie y''+ay'+by=0 sprowadza się do z''=qz dla q=a'/2+a²/4-b, a następnie do Riccatiego r'+r²=q dla r=z'/z.
6. **Wymierna gałąź Riccatiego dla q wielomianowego:** każdy skończony biegun r jest prosty z residuum 1, zatem r=ω+P'/P. Dla q nieparzystego dodatniego stopnia brak wymiernych rozwiązań, a dla q stopnia 2d≥2 istnieją dokładnie dwa kandydaty ω. Stopień n=deg P wynika z porównania współczynnika przy x^{d-1}; resztę wyznacza skończony liniowy układ dla P. Dowiedziono obu implikacji, w tym braku wielokrotnych pierwiastków P. Przypadki q stałego, w tym q=0, obsłużono.
7. **Granice ogólnego Kovacica:** klasyfikacja przypadków logarytmicznej pochodnej stopnia 1, 2, 4, 6, 12 oraz pełna poprawność algorytmu dla q∈C(x) są wyraźnie cytowane (Kovacic, J. Symbolic Computation 2 (1986), 3–43), a nie przedstawione jako samodzielnie dowiedzione. Kontrprzykład q=x+5/(16x²), r=√x-1/(4x) pokazuje nieadekwatność ograniczenia się do gałęzi wymiernej.
8. **Granice pełnego Rischa:** pełna poprawność ogólnej procedury dla wież elementarnych jest jawnie cytowana (Risch; Bronstein, Symbolic Integration I), nie przypisana do dowiedzionego tylko szczególnego równania r'+hr=s. Nie ma deklaracji, że heurystyczne niepowodzenie CAS dowodzi nieelementarności.
9. **Przykłady:** zweryfikowano pochodne i wszystkie odpowiedzi dodatnie oraz negatywne: wymierna redukcja Hermite'a, wypadkowa dla x²+1, wymierne równanie Rischa, całka Gaussa, q=x²+1, q=x²+3, algebraiczny kontrprzykład stopnia 2 i równanie Airy'ego.

W samym AA-47 występuje **8 bloków dowodu, 7 przykładów i 30 etykiet** (różnica AA-46→AA-47). Testy skończonych modeli nie są przedstawiane jako dowód ogólnego twierdzenia.

## 2. Rzeczywiste poprawki z audytów

Pierwszy przebieg pełnego CI #45159930396 zakończył się niepowodzeniem w kroku ogólnych testów repozytorium z powodu nowej asercji przypadku q=0: SymPy ma deg(0)=-∞, więc implementacja testowego algorytmu błędnie zwracała None. Poprawiono wcześniejszym testem q.is_zero i wynikiem r=0. W tym samym commicie doprecyzowano polskie nazwy oraz usunięto angielski przymiotnik z tekstu.

**Commit poprawki testu i języka:** 5a0cc7b19fc2f6c5834e243b6c5271cf4d696a85.

Dodatkowo audyt końcowy wykrył, że metadane frontowe książki nadal oznaczały AA-47 jako rozdział w audycie mimo zielonego CI. Poprawiono stronę tytułową i komentarz pliku kanonicznego przed końcową ponowną kompilacją.

**Commit poprawki metadanych:** b9be84c91aff3cb203f567edcfb6ee7705295bc9.

## 3. Ostateczny rzeczywisty GitHub Actions

**Przebieg:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45161159035
**Head SHA:** b9be84c91aff3cb203f567edcfb6ee7705295bc9.
**Status:** completed / success, **85/85 zakończonych sukcesem kroków**.

- AA-47 testy symboliczne SymPy: **11/11 PASS**.
- AA-47 niezależny model wymierny Fraction: **10/10 PASS**.
- Pełne testy narzędzi repozytorium: PASS.
- Bramka AA GLOBAL 01–47: PASS, **47 rozdziałów**, 969 unikatowych etykiet, 0 duplikatów, 475 wystąpień odsyłaczy, 298 unikatowych celów, 0 nierozwiązanych; w książce 435 dowodów i 300 przykładów.
- Historyczne audyty przekrojowe AA-01–AA-42: 11 raportów, nie zmieniono ich statusu; AA-43–AA-47 mają oddzielne raporty.
- Kompilacja pełnej książki latexmk: success.
- Weryfikacja PDF, odsyłaczy i archiwizacja artefaktu: success.

## 4. Końcowy artefakt PDF i kontrola stron

**Artefakt z ostatecznego przebiegu:** abstract-algebra-aa01-aa47, **ID 14811666205**.
- Plik abstract_algebra.pdf: **304 strony**, **2 211 999 bajtów**, SHA-256 **aceb8203db99a3c517e0c3681e68670253c31e305f61e0a2e3fae61088528618**.
- Plik abstract_algebra.log: **46 304 bajty**, SHA-256 **245bf09fd9db6041e999706550c39d385ba4eb49dede60442653c3b0d34ef383**.
- Końcowy log: **0** błędów LaTeX, **0** ostrzeżeń LaTeX, **0** ostrzeżeń hyperref, **0** overfull, **0** underfull i **0** unresolved references.
- AA-47 zajmuje **7 stron PDF (298–304)**, drukowane 288–294. Wyrenderowano i obejrzano wszystkie siedem stron w końcowym artefakcie; nie stwierdzono kolizji, obcięć, błędów symboli matematycznych ani niepoprawnych przeniesień.
- W pełnej książce skontrolowano pozycje **156 344 wyrazów**, **0** poza granicami stron.
- Porównanie z pierwszym zielonym przebiegiem AA-47: **303/304 stron identycznych tekstowo**; zmieniła się wyłącznie strona tytułowa, zgodnie z poprawką statusu.
- Porównanie poprzedniej stabilnej książki AA-01–AA-46 (297 stron) z aktualną: **295/297** starych stron występuje bez zmiany tekstu; wyjątki to strona tytułowa i spis treści, zmodyfikowane przez dołączenie nowego rozdziału.

## 5. Werdykt i dalszy plan

**AA-47 STABILNY w przyjętym, jawnym zakresie.** Pełne dowody algorytmiczne obejmują klasy wymienione w dokumencie zakresu, a ogólne klasyfikacje Rischa i Kovacica pozostają jawnie cytowanymi twierdzeniami. Ukończono audyty I–III, rzeczywiste korekty, oba niezależne zestawy regresyjne, pełny zielony CI oraz oględziny każdego arkusza AA-47.

**AA-48 pozostaje NIEOTWARTY**; nie wynika automatycznie z zakończenia AA-47 i wymaga odrębnego ustalenia tematu i zakresu.
