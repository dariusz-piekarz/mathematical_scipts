# Moduł 15B — audyt 14 (czysty, 1/2)

Data: 24 listopada 2026. Gałąź: biblioteka-matematyczna-iteracja-6.
Punkt wyjścia: raport 13, commit 59db18da1dc64a0b9c58eead23064ef8f3591806. Odczyt HEAD 3d9d4373b9a1c3e369394912a6dbdf27c752ee7d. Źródło 641dd59fc065281f00dda099123dac99533213cc, testy 5b744df89381f90529f84effdddfdba6a28ac40c: niezmienione od rozszerzenia. Porównanie commitów nie wykazuje zmian w analizie funkcjonalnej.

## Kontrola matematyczna
- Nowy przykład: miara atomowa jest przeliczalnie addytywna, zupełna, o masie 1. Skończone obcięcia są funkcjami prostymi, ich wartości w każdym ustalonym punkcie są od pewnego miejsca dokładnie wartościami f.
- Skalaryzacje: sprawdzono konwencję zespoloną, czynnik sprzężenia, skrócenie 2^n z masą atomu 2^(-n), oszacowanie Cauchy'ego–Schwarza i zbieżność bezwzględną.
- Reprezentacja Pettisa: dla dowolnego A ciąg chi_A(n)/n należy do l2, jego parowanie z każdym funkcjonałem daje całkę skalarną; jednoznaczność z poprzedniej definicji. W szczególności całka po S jest (1,1/2,1/3,...).
- Brak Bochnera: całka normy jest dokładnie szeregiem harmonicznym. Porównanie z poprzednim przykładem nieośrodkowym trafnie rozdziela dwie przeszkody. Nie ma potrzeby korekty.
- Poprzednia treść zachowana; dodanie przykładu nie zmienia założeń twierdzeń. Odsyłacz do poprzedniego przykładu działa w kontekście. Pięć przykładów, 11 dowodów, 24 etykiety. Bez zmian źródła ani testów.

## Technika
CI https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45348120866, commit raportu 13, job 138287558247: completed/success, 9/9 kroków. Log potwierdza Ran 12 tests, OK. Trzy przebiegi pdflatex; PDF kontekstowy 01–17 ma 113 stron. Automatyczna kontrola treści i odsyłaczy zaliczona. Artefakt 14898728595 pobrano, rozpakowano, odczytano końcowy log. Brak niezdefiniowanych odsyłaczy, overfull hbox, missing character, undefined control sequence. Jedno znane underfull hbox (badness 1127) nie blokuje.
Wyrenderowano strony 95–104, obejrzano układ stron 95–99 i 101–104 oraz stronę 100 w pełnej rozdzielczości renderu. Nowy przykład 15B.13 mieści się w całości na stronie 100, wzory i akapity czytelne, odsyłacz widoczny, brak kolizji i obcięcia. Przejście do rozdziału 16 na stronie 103 poprawne.

## Propozycje opcjonalne
Z audytu 12 pozostają diagram hierarchii i pozytywne wyniki RNP. Dodatkowa wartościowa obserwacja po nowym przykładzie: jego miara Pettisa A -> (chi_A(n)/n) jest przeliczalnie addytywna w normie l2, ale ma nieskończoną całkowitą wariację (podziały na pierwsze N singletonów i ogon). Łączy przykład z dalszą częścią o miarach wektorowych. Nie dodawano bez akceptacji.

## Decyzja
Pierwszy czysty audyt rozszerzonego modułu: 1/2. Kolejny audyt 15 niezmienionej wersji, potem rozdział 16 po zaliczeniu drugiego czystego audytu.
