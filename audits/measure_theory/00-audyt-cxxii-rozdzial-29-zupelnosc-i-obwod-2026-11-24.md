# Audyt CXXII (122) — zupełność BV i pierwsze przykłady obwodu
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia 73184e4908898b9b0b9a3953db20edc1cd5583e9, blob rozdziału 20d154bdb2450fcc067c22dbaa11fa5fb52ecf1f.
Commit źródłowy f9e1eb3f005ca2d2bcdc609b8330f89b103e5514, blob f641b77ccbb70df1684b33091ae1b4a85f8f5a77.
## Wyniki
Dziewięć zastąpień; 1904 -> 1995 wierszy; wszystkie 37 etykiet zachowane w tej samej kolejności.
- Sprawdzono liniowość przestrzeni BV, jednorodność, nierówność trójkąta, określoność normy na klasach równoważności.
- Wyprowadzono równoważność normy wariacji miary wektorowej i sumy wariacji składowych, korzystając z poprzednio udowodnionego wzoru podziałowego. Rozpisano zbieżność składowych, oszacowania obu całek testowych, wykazanie skończoności wariacji granicy przed zastosowaniem twierdzenia reprezentacyjnego.
- Doprecyzowano dziedzinę całki w definicji obwodu i równoważność lokalnego skończonego obwodu z BV_loc funkcji charakterystycznej.
- Uzasadniono przykład półprzestrzeni, znak pochodnej, różnicę między obwodem globalnym w wymiarach n=1 i n>=2, konwencję miary w wymiarze zero.
- W przykładzie kostki jawnie zapisano miarę wektorową z właściwymi znakami na dolnych i górnych ścianach, wyprowadzono skończoność wariacji, wartość obwodu i osobny przypadek przedziału.
- Uzupełniono hipotezy lematu o dopełnieniu i równości prawie wszędzie.
## Otwarte
Następna kontrola: twierdzenie o brzegu C^1, dowód dywergencji w lokalnych współrzędnych, półciągłość obwodu, oszacowania translacji i zwartość BV. Sprawdzić rysunek prostokąta w PDF. Nie uruchomiono kompilacji ani regresji w tej iteracji. Stan 28/31; rozdział 29 otwarty.
