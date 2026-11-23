# Algebra abstrakcyjna — audyt przekrojowy 05: 90. twierdzenie Hilberta, Kummer, Artin–Schreier

Data: 2026-11-23. Gałąź: `biblioteka-matematyczna-iteracja-6`. HEAD bezpośrednio przed zapisem: `12f5683f51c31a19922cae15403983eb4d0ea88b`.

## Zakres
Nowa, odrębna kontrola AA-25–AA-27 (niepowtarzająca przekrojowych 01–04). Katalog `catalog/books.json` wymienia AA-01–AA-42 i nie zawiera AA-43; nie jest to dowód braku każdego możliwego nieujętego w katalogu pliku. Odczytano `AGENTS.md`, `docs/pl/standardy_terminologiczne.md`, `application/docs/MATHEMATICAL_WRITING_GRANULARITY_STANDARD.md`, katalog i wcześniejszy raport przekrojowy 03.

Źródła (bloby): AA-25 `2524f56e0a4802d28c441ff932ba5399a10eb61c`, AA-26 `5bee95fdfedeaaf4fc697dce636e5d82afcd249b`, AA-27 `628da680adc66f257511a260df4283db8cb9a7d7`.

## Kontrola matematyczna
1. AA-25: multiplikatywne 90. twierdzenie Hilberta używa cykliczności i normy 1; w konstrukcji `B(x)` poprawnie wykorzystano niezależność automorfizmów i `p_n=1`. Postać addytywna nie zakłada błędnie, że ślad jedynki jest niezerowy w charakterystyce dzielącej stopień; używa niezdegenerowania formy śladu. Przypadek stopnia 1 i kontrprzykład dla grupy niecyklicznej są uwzględnione.
2. AA-26: założenia Kummera jawnie wymagają charakterystyki niedzielącej wykładnika i obecności pierwiastków z jedynki; w klasyfikacji stopnia pierwszego `p` używa się niezerowych klas w `F^×/(F^×)^p`. Różne klasy mogą generować tę samą prostą i to samo rozszerzenie.
3. AA-27: w charakterystyce `p` pochodna `X^p-X-a` wynosi `-1`, a pierwiastki mają postać `α+c` dla `c∈F_p`; klasyfikacja dotyczy jednowymiarowych podprzestrzeni `F/\wp(F)`. W dowodzie odwrotnym niezerowość śladu wynika z rozdzielczości, nie z `Tr(1)=p`.
4. Spójność AA-25/AA-26/AA-27: konstrukcje Kummera i Artina–Schreiera dotyczą rozłącznych warunków na charakterystykę, natomiast 90. twierdzenie Hilberta działa także w charakterystyce dodatniej. Nie stwierdzono sprzeczności w skontrolowanych fragmentach.

## Testy niezależne
Lokalnie wykonano 11 asercji Pythona: arytmetyka `F_4`, rząd Frobeniusa, obraz śladu, norma, równanie Hilberta 90, obraz Artina–Schreiera nad `F_2`, pierwotny pierwiastek trzeciego stopnia w `F_7`, sześciany i klasy Kummera. Wynik **11/11 PASS**. Pierwszy prototyp testu miał błąd implementacji mnożenia w `F_4`; poprawiono sam test i uruchomiono cały zestaw ponownie z wynikiem 11/11. Nie jest to błąd źródła LaTeX.

## Ograniczenia
Kontrola przekrojowa, nie pełny ponowny audyt każdego dowodu w trzech rozdziałach. Brak zmian w źródłach i etykietach. Nie wykonano kompilacji LaTeX ani wizualnej inspekcji PDF (brak lokalnej kompletnej książki). Nie uruchomiono ani nie zweryfikowano GitHub Actions; **CI PASS niepotwierdzony**. Stabilność wszystkich rozdziałów nie wynika z tej kontroli.

## Następny krok
Ponownie odczytać HEAD, sprawdzić dostępność AA-43 i niepublikowany raport przekrojowy 04; jeżeli brak nowego rozdziału, wykonać nowy niezależny zakres przekrojowy, bez powtarzania 01–05.
