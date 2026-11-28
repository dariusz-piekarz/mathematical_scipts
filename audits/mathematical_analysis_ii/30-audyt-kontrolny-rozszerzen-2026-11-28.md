# AM II 30 — audyt kontrolny rozszerzeń (2026-11-28)

Źródło: `chapters/pl/mathematical_analysis_ii/30-calki-wielokrotne-i-zamiana-zmiennych.tex`, blob `9635193b2892ee8031deb56e73c9ba43f68b076f`.

## Kontrola matematyczna
- Grupowanie sum Riemanna i pola przekrojów bryły pod wykresem z=x+2y; objętość 3/2 w obu kolejnościach.
- Rozróżnienie hipotez Tonellego i Fubiniego, wyjątki dla przekrojów i brak całkowalności bezwzględnej.
- Jakobian jako graniczny stosunek objętości, nieliniowe podstawienie (u,v)→(u,uv), dokładny stosunek pól symetrycznej komórki.
- Dokładne pola i objętości komórek biegunowych, walcowych i sferycznych oraz graniczne czynniki jakobianowe.

## Kontrola statyczna i integracja
- 1501 wierszy LaTeX, 36 etykiet, 8 ilustracji statycznych, 3 zarejestrowane wykresy Plotly.
- 46/46 odsyłaczy lokalnych oraz 15/15 zewnętrznych sprawdzonych względem aktualnych rozdziałów docelowych.
- Brak duplikatów etykiet w sprawdzonych rozdziałach; nawiasy i środowiska poprawne.
- Poprawione proporcje osi komórek przestrzennych w a46b148.

## Odbiór techniczny
- Workflow AM II 46148301607: success, commit 111abce3d77e0b053ff97be455d819fbaee0e5ac, identyczny blob rozdziału 30.
- Artefakt 15264977321: PDF 309 stron, 33 rozdziały, 72/72 ilustracji zweryfikowanych, bez niepowodzeń (audit_output/am2_reader_figures.json).
- Workflow Concept graph backend and browser checks 46148648879: success dla a46b148.
- Workflow Mathematical library application checks 46148648890: cancelled; pełny test przeglądarkowy nowych wykresów pozostaje niepotwierdzony.

Wniosek: kontrola merytoryczna, odsyłacze, kompilacja PDF oraz walidacja ilustracji zakończone. Pełny odbiór aplikacyjny Plotly pozostaje otwarty. Można rozpocząć rozszerzenia rozdziału 31.
