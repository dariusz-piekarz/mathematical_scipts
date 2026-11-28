# Audyt 228 — drukowany rozdział 25, etap A: Wirtinger, peryferia, Fox, Seifert

Data: 2026-11-25. Kontynuacja 227.
Źródło: chapters/pl/graph_and_knot_theory/18-teoria-wezlow-od-diagramow-do-rozmaitosci-czterowymiarowych.tex.
Blob wejściowy 3a7d3ad29a707ca0d90e3af49f20ac9eae5a108d.

## Kontrola matematyczna
Przeczytano sekcje o prezentacji Wirtingera, strukturze peryferyjnej, kolorowaniach i powierzchniach Seiferta oraz sekcję rachunku Foxa. Algebraiczne podstawienia w przykładzie trójlistnika i abelianizacja poprawne. Konstrukcja sferycznej tożsamości relatorów Wirtingera pozostaje przywołanym standardowym lematem geometrycznym, nie pełnym dowodem własnym.
- Udowodniono jednoznaczność preferowanej długości przez zmianę klasy o wielokrotność meridianu oraz bazowość przez macierz unimodularną. Wyjaśniono wybór kołnierza powierzchni Seiferta w otoczeniu tubularnym.
- W dowodzie o kolorowaniach uzupełniono brakujące uzasadnienie redundancji usuniętego wiersza nad dowolnym modułem n, przez homomorfizm do grupy półprostej z inwolucjami s_a. Argument działa też dla n=2. Rozpisano współczynniki Foxa w t=-1 dla obu rodzajów sprzężenia oraz ich związek z wyznacznikiem węzła.
- Rozpisano rozłączność dysków z kołnierzami przy zagnieżdżeniu okręgów Seiferta, umieszczenie pasm w rozłącznych lokalnych otoczeniach i wygładzenie naroży.
Commit 989472da856a055f986b51708860e1df6d6ddc45, blob 31adff07b54d502f0650ed1c776e1e4d9f4822. 162 poprawnie zagnieżdżone pary środowisk, 21 unikatowych etykiet, 7 odsyłaczy; nowy odsyłacz do sec:kt-fox-calculus istnieje.

## Test
GKT-25-FOX-01: lokalnie wykonano w Pythonie 18495 trójek kolorów dla n=2,...,16; dokładne sprawdzenie równoważności relacji sprzężenia z 2b=a+c oraz inwolutywności. PASS. Kod dodano do tools/tests/test_graph_and_knot_hodge_bass_serre_knot.py, commit 06c432edccb41be153ac33e1a1b186f6fca6fde0, blob ac7b8f5567d6c75c76ffcaeb66c96374278e0eee; potwierdzono wywołanie w __main__. Test skończony, nie formalizacja Lean.

## Rysunek
GKT-25-SEIFERT-FIG-01: wykryto błędną orientację wygładzenia na rysunku. Oba lewe końce pierwotnego skrzyżowania są wejściowe, oba prawe wyjściowe; pionowe wygładzenie łączyło końce o niezgodnych orientacjach. Zastąpiono je dwoma poziomymi łukami skierowanymi w prawo. Commit a4e696ef0c4eac73d8e987909ab3959d338b043c, blob 8aacf564a731d3388e33cb0f773663daef4ccba4 potwierdzony. Trwałe kryterium: zachowanie kierunków na czterech końcach, brak przecięcia łuków i czytelność po renderowaniu. Oględzin nowego PDF jeszcze nie wykonano.

## Bramka i dalszy zakres
Globalny run 45593499698 dla commitu testowego był queued; dla ostatniego commitu rysunku lista przebiegów jeszcze pusta przy odczycie. Poprzedni run 45593225126 nadal niezakończony. Nie deklaruje się PASS zintegrowanego CI ani kompilacji. Następny audyt 229: szczegółowa kontrola macierzy Seiferta, modułu Alexandera i rachunku Foxa; kontynuacja pierwszego przejścia A, bez przedwczesnego zamknięcia. Postęp 24/44.
