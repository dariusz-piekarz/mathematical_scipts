# RRC 23 — iteracja 349

Pierwszy audyt szczegółowy sekcji 23.5 (5/8). Commit cfcc1d337d8c2650b330e6d35913e6f74df56fdc, blob 8107e6f3f8249f82cd5bd64e8886f17f510355b2.

Przy rozpoczęciu iteracji stwierdzono równoległe zapisanie #348 (commit f2856668aa8d5c0852e495c18aa23bef631d44de, blob bf75718b1177ce74888dcea1ba0a5a895a34559a). Odczytano i sprawdzono dowód porównania na torusie, warunek jednostajny, funkcje testowe, obie bariery czasowe i kontrakcję; nie nadpisano zmian.

- Doprecyzowano zakres funkcji sprzężonej Legendre'a i założenia lematu o minimalizatorach; określono zwarty zbiór prędkości i stałą R_{H,K}.
- W twierdzeniu Hopfa–Laxa usunięto zbędne założenie ograniczoności g, zachowując globalną lipschitzowskość. Ograniczoność u stwierdzono tylko dla ograniczonych danych na skończonym walcu. Podano jawną stałą czasową i jednostajny szacunek różnicy u(t)-g.
- Uzupełniono dowód zasady programowania dynamicznego w obu kierunkach, osiąganie minimów i przypadek s=0; jawny szacunek łączny względem czasu i przestrzeni.
- Uzasadniono jednostajność reszty różniczkowania funkcji testowej dla ograniczonych prędkości w nierówności nadrozwiązania.
- Rozpisano dowód porównania na całej R^d w klasie ograniczonych globalnie lipschitzowskich funkcji dla lokalnie lipschitzowskiego H(p), z lokalizacją maksimum, wykluczeniem końców czasu, ograniczeniem gradientu testowego i oszacowaniem błędu M beta. Nie rozszerzano tej jednoznaczności na dane nieograniczone.
- Sprawdzono dotychczasowy dowód skończonego obszaru zależności.

Kontrola źródła: 1018 wierszy (888 wcześniej), 25 zachowanych unikatowych etykiet, 28 odsyłaczy, cele zewnętrzne w rozdz. 2 i 24, wszystkie jednoznaczne, brak błędów zagnieżdżenia i delimiterów. Pozostałe sekcje identyczne. Brak potwierdzonej kompilacji rozdziału 23.

Następny etap: sekcja 23.6 (półwklęsłość i przecięte charakterystyki), następnie Burgers i entropia.
