# Audyt 227 — drukowany rozdział 25, etap A, diagramy i liczba splecenia

Data: 2026-11-25. Po zamknięciu rozdziału 24 w 226.
Źródło: chapters/pl/graph_and_knot_theory/18-teoria-wezlow-od-diagramow-do-rozmaitosci-czterowymiarowych.tex. Początkowy blob 6c21a214da0c5168a01a3f681612590bebe694ee, 2110 wierszy.

## Zakres i poprawki
Odczytano strukturę całego rozdziału, szczegółowo wiersze 1–385, definicję i konstrukcję powierzchni Seiferta oraz sekcję Jonesa w celu kontroli konwencji znaku. Nie wykonano jeszcze pełnego audytu pozostałych sekcji.
- Poprawiono definicję regularnego diagramu: rzut jest immersją w każdym punkcie dziedziny, punkty podwójne dotyczą obrazu.
- Jawnie ustalono ujemną orientację bazy (x,y,h) względem orientacji S3 przy wysokości h rosnącej do obserwatora. Zachowano dotychczasowy znak det(v_pod,v_nad), zgodny z obliczeniem Jonesa. Nie zmieniano konwencji algebraicznych.
- Zastąpiono skrótowy argument zmiany skrzyżowań dowodem za pomocą zorientowanego cylindra od K1 do poziomu poniżej obu składowych. Dolny brzeg domyka łańcuch płaski, znaki poprzecznych przecięć obliczono wyznacznikiem. Symetria liczby splecenia daje sumę po obu typach skrzyżowań. Niezmienniczość uzasadniono przez jednoczesne przenoszenie powierzchni i krzywej dyfeomorfizmem zachowującym orientację.
- Poprawiono literówkę locally flat embedding oraz dodano odsyłacz do sekcji Seiferta.
Commit f944dcc9b2b2faf3851060da4af94bf0c3bf425f; potwierdzony blob 3a7d3ad29a707ca0d90e3af49f20ac9eae5a108d. Pierwsza próba zapisu napotkała konflikt równoległego przesunięcia gałęzi, po ponownym odczycie źródła zapis się powiódł. Kontrola struktury: 162 poprawnie zagnieżdżone pary środowisk, 21 unikatowych etykiet, 6 odsyłaczy; nowy cel sec:kt-seifert istnieje.

## Regresja
GKT-25-LINK-SIGN-01: 13392 dokładne kontrole całkowitoliczbowe wyznacznika orientacji, wykonane lokalnie w Pythonie, PASS. Test skończonego rachunku znaków, nie formalizacja Lean ani dowód ogólny. Podłączono do istniejącego tools/tests/test_graph_and_knot_hodge_bass_serre_knot.py, commit 3dabf3a8ed08539e2379d1b7be97205af1ad8177, blob 626a574f3428928f5fb02c44cfaabd114e8ee6b9, potwierdzono wywołanie w __main__. Globalny run 45593225126 dla tego SHA był queued przy odczycie. Brak nowej kompilacji PDF i oględzin. Nie deklaruje się wyniku zintegrowanego CI.

## Dalszy zakres
Audyt 228: dalsza pierwsza kontrola rozdziału, w szczególności prezentacja Wirtingera, peryferia, kolorowania Foxa, konstrukcja powierzchni Seiferta; potem macierze Seiferta, Alexander, Conway, Arf, sygnatura, Jones i warkocze. Sprawdzić bramkę CI oraz zgodność orientacji z następnymi rozdziałami. Rozdział 25 niezamknięty; postęp 24/44.
