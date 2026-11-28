# Audyt CXXXI (131) — mierzalność obwodów i warstwowanie
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia e5967a0248d59ca40874c4e3407f16fab3ce597a, blob adddd2f23324ad91245942d83cf0926b9489b3bf. Commit źródłowy 9fd255634e3e320a729661baa971f2c7ec027a9e, blob 4404368ad1d1065d06e314a73910fe7ce0d407bb.
## Wyniki
Siedem zastąpień; 3131 -> 3248 wierszy; wszystkie 37 etykiet zachowane w kolejności.
- W lemacie mierzalności jawnie dopuszczono funkcje mierzalne w sensie Lebesgue'a bez całkowalności i obwody nieskończone. Uściślono zbiory nad- i podpoziomicowe, przypadek pustego Omega.
- Zastąpiono szkic konstrukcji gęstych testów pełnym dowodem ośrodkowości: zanurzenie do skończonego produktu przestrzeni C(K_j), Stone–Weierstrass, dziedziczenie drugiego aksjomatu przeliczalności. Rodzina gęsta już w klasie dopuszczalnych testów, symetryczna, zawiera zero; jawne oszacowanie błędu całki i równość przeliczalnego supremum dla dowolnego zbioru.
- Dowód borelowskości przez monotoniczność całek z dodatniej i ujemnej części dywergencji, bez potrzeby zakładania borelowskości u; niezmienniczość wszystkich obwodów po zmianie reprezentanta.
- Ujednolicono nagłówek do terminu koobszar.
- W twierdzeniu o warstwowaniu usunięto redundantne założenie skończoności obwodów prawie wszędzie, wynikające ze skończonej całki. Borelowski reprezentant, punktowe wzory dla części dodatniej i ujemnej, Tonelli i konkretne oszacowanie całki modułu przed Fubinim. Supremum po testach dopiero po uzyskaniu wspólnego oszacowania.
- Dodano równość sumy całek po dodatnich i ujemnych warstwach z całką po całej prostej. Jawnie wykazano przeliczalność wyjątkowych poziomic o dodatniej mierze przez sigma-skończoność, użyto dopełnienia i zamiany zmiennej.
## Otwarte
Następny audyt: aproksymacja ścisła BV na dowolnym otwartym zbiorze (lokalne sploty, podział jedności i błędy gradientów), następnie gładki i pełny wzór koobszaru. Kompilacja, testy i kontrola PDF pozostają otwarte. Stan 28/31.
