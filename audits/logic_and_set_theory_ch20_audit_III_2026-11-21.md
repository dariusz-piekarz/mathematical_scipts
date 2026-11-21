# Logika matematyczna i teoria mnogości — rozdział 20, audyt III

Data: 21 listopada 2026 r.  Zakres: **istniejący tekst po audycie II**, bez nowych twierdzeń, lematów i przykładów.

## Wynik: jedna korekta, wymagana niezależna kontrola stabilizacyjna

**Usterka [przykład „Dwie wypowiedzi o liczbie 4”]:** występował predykat `\operatorname{Bew}_T` bez jawnego ustalenia, że $T$ jest efektywnie aksjomatyzowalną teorią rozszerzającą $Q$. Oryginalne sformułowanie dopuszczało błędne odczytanie, że sama dowolna teoria $T\supseteq Q$ automatycznie ma przyjęty wcześniej standardowy arytmetyczny predykat dowodu. Dodano założenie efektywnej aksjomatyzowalności oraz argument: $Q\vdash\overline 2+\overline2=\overline4$, więc dowód jest rzeczywistym skończonym dowodem także w $T$, a w standardowym modelu prawdziwe jest zdanie o jego istnieniu. **Nie zakładamy poprawności semantycznej $T$.**

## Niezależne sprawdzenie istniejących wyników

1. **Tarski semantyczny:** lemat diagonalny w $Q$ daje $L\leftrightarrow\neg\operatorname{Tr}(\overline\ell)$. Ponieważ $\mathfrak N\models Q$, ta równoważność zachodzi w $\mathfrak N$. Definicja pełnej prawdy wymusza przeciwną równoważność dla tego samego $L$. Sprzeczność jest semantyczna, nie wymaga dowolnej teorii $T$.
2. **Tarski syntaktyczny:** niesprzeczność teorii $T\supseteq Q$ wystarcza do sprzeczności dwóch dowodliwych równoważności; efektywna aksjomatyzowalność ani poprawność semantyczna $T$ nie występują w dowodzie.
3. **Nieutożsamianie zdań z ich dowodliwością:** zastosowanie właśnie syntaktycznego Tarskiego do arytmetycznej formuły $\operatorname{Bew}_T$ jest poprawne.
4. **(D1):** przyjęte kodowanie z Lematu `res:7:7`, $\Delta_0$-zupełność $Q$ (Lemat `res:4:7`) i Lemat `lem:incomp-proof-check` uzasadniają każdy krok od konkretnego kodu dowodu do $T\vdash\Box\varphi$.
5. **(D2) i (D3):** nie są przypisywane dowolnemu predykatowi; odesłanie `ch:derivability-proof` rzeczywiście wskazuje przygotowany rozdział 21 i jego twierdzenie `thm:xi-hbl-verified`.
6. **Nieodwracalność (D1):** samo $T\vdash\Box\varphi$ nie gwarantuje standardowego świadka. Argument odwrócenia jest poprawny przy dodatkowym założeniu $\Sigma_1$-poprawności $T$; zwykła niesprzeczność tego nie zastępuje.
7. **Przykład skończonego predykatu prawdy:** poprawny także przy powtórzeniach zdań, ponieważ różne zdania mają różne kody, a identyczne zdanie ma jedną wartość prawdy.
8. **Definiowalność, wyliczalność, rozstrzygalność, przeliczalność:** kwantyfikatory i zakresy są poprawne; przykład nie utożsamia istnienia kodowania z algorytmem rozstrzygającym prawdę.

## Skład i testy

- Zachowane: 3 twierdzenia, 1 lemat, 4 dowody, 3 definicje, 5 przykładów, 7 uwag.
- 8 etykiet, 14 odsyłaczy, wszystkie ich cele są obecne w kompilacyjnym zestawie źródeł.
- 27/27 testów regresyjnych PASS; powtórna kompilacja pełnego lokalnego skryptu PASS.
- PDF rozdziału: 5 stron, bez błędów LaTeX i przepełnień, odsyłacze rozdziału rozwiązane; render wszystkich stron sprawdzony wizualnie.
- Dwa nierozwiązane odsyłacze w **innych** rozdziałach lokalnego zestawu (`ch:zf-axioms`, `ch:axiom-choice`) dotyczą przyszłego materiału; nie występują w rozdziale 20.

Wniosek: korekta jest punktowa, struktura dowodów pozostała bez zmian. Przeprowadzić audyt IV na nowej wersji.