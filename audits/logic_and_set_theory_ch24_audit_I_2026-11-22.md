# Logika matematyczna i teoria mnogości — rozdział 24, audyt I

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/24-gorne-twierdzenie-lowenheima-skolema-i-paradoks-skolema.tex`.  
**Źródło:** wcześniejsze opracowanie rozdziału 24 w pełnym skrypcie rozdziałów 01–44.

## Kontrola matematyczna
1. **Diagram elementarny:** wyraźnie odróżniono pełny diagram od diagramu atomowego. Wszystkie prawdziwe formuły i negacje fałszywych formuł gwarantują zachowanie wartości logicznej dla dowolnej krotki parametrów, a nie tylko równań i relacji atomowych.
2. **Zanurzenie:** pokazano iniektywność funkcji `a↦c_a^B`, zachowanie symboli funkcyjnych i relacyjnych oraz równoważność wszystkich formuł.
3. **Górne twierdzenie:** cztery etapy: (i) skończona spełnialność diagramu z `λ` różnymi stałymi; (ii) elementarne zanurzenie pierwotnego modelu; (iii) ograniczenie mocy przez dolne twierdzenie; (iv) przeniesienie struktury przez bijekcję tak, aby uzyskać dosłowne zawieranie, nie tylko izomorficzną kopię.
4. **Łańcuchy elementarne:** w dowodzie sumy sprawdzono zgodność interpretacji na skończonych krotkach oraz oba kierunki przypadku egzystencjalnego. W kierunku od sumy do etapu użyto późniejszego świadka i przechodniości elementarności.
5. **Prawdziwa arytmetyka:** skończone fragmenty teorii `Th(N)∪{n<c:n∈N}` mają standardowe modele; zwartość i dolne twierdzenie dają model przeliczalny z elementem większym od wszystkich standardowych numerałów. Nie mylimy elementu modelu z liczbą standardową.
6. **Paradoks Skolema:** odróżniono zewnętrzne wyliczenie `E_r` od istnienia wewnętrznie reprezentowanej bijekcji i odróżniono moc zewnętrzną zbioru od mocy w interpretacji modelu ZFC.
7. **Drugi rząd:** kategoryczność standardowej arytmetyki wymaga pełnej semantyki, tj. kwantyfikacji po wszystkich zewnętrznych podzbiorach. W semantyce Henkina krok indukcyjny na zewnętrznym `E` jest niedostępny bez dodatkowych założeń.

## Korekty
- Odsyłacz do twierdzenia o zwartości poprawiono na rzeczywistą etykietę `thm:compactness`.
- Poprawiono fleksję w sformułowaniu „przeliczalne uniwersum”.
- W testach regresyjnych poprawiono błędną kontrolę wielkości litery w frazie „Zewnętrzne wyliczenie”; nie był to błąd matematyczny rozdziału.

## Inwentarz i status
4 twierdzenia, 2 lematy, 1 wniosek, 2 definicje, 2 przykłady, 6 uwag, 7 dowodów; 18 etykiet, 11 odsyłaczy.

Przebieg GitHub Actions `44962281632`: struktura, numeracja, odsyłacze i 9/10 testów rozdziału 24 PASS; jeden test zakończył się niepowodzeniem z powodu czułości na wielkość liter. Test poprawiono w commicie `773a8f89ffc77e4f8dad588f85eee18428889f4a`; wymagane jest potwierdzenie pełnego powtórzenia CI i oględziny PDF.

**Werdykt:** wykonano pierwszą iterację audytu, bez nowych twierdzeń; rozdział oczekuje powtórnej czystej iteracji.
