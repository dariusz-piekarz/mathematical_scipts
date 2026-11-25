# Globalna unikatowość etykiet — kontrola niezależna

Stan badany: c7d1f9f0007f3f3fb1cf47dbd0dfad9819f11933 (gałąź biblioteka-matematyczna-iteracja-6).

Odczytano listę inputów i wszystkie 44 źródła przy tym samym SHA. W pięciu partiach wyodrębniono etykiety poza komentarzami i listingami. Każdej etykiecie przypisano deterministyczny 32-bitowy skrót (FNV-1a, operacje na kodach znaków JS). Zestawiono wyniki w Pythonie przez Counter. Liczności partii: 148, 203, 92, 128, 139. Łącznie 710 skrótów, 710 różnych, 0 powtórzeń. Różne skróty implikują różne napisy; kolizja skrótów nie może ukryć powtórzonego napisu. Dane pośrednie przepisano z odpowiedzi odczytów do lokalnego przebiegu Python, z kontrolą liczności.

PASS w zakresie globalnej unikatowości wykrytych etykiet przy ustalonym SHA. Bez zmian w źródłach matematycznych. Nie wykonano pełnego narzędzia --strict ani ponownej kontroli odsyłaczy na tym samym SHA. Nie jest to audyt semantyczny powtarzających się treści. CI oraz wizualna kontrola PDF nadal niepotwierdzone.

Następnie: kontrola powtórzeń treści, pełny --strict, CI i PDF.
