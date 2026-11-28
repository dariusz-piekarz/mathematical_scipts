# Audyt IV — rozdział 06 „Relacje porządku: od porównywania do kresów”

**Data:** 21 listopada 2026 r.  
**Źródło:** kanoniczny plik `chapters/pl/logic_and_set_theory/06-relacje-porzadku-od-porownywania-do-kresow.tex` na gałęzi `biblioteka-matematyczna-iteracja-6` po audycie III; blob Git `f5df8706861ef5e9623c0925abc22145fd42747f`.  
**Zakres:** czwarty, niezależny audyt istniejących definicji, twierdzeń, wniosku, dowodów, przykładów, uwag, diagramów i odsyłaczy; bez rozszerzania materiału.

## Dwie poprawki

1. **Dowód leksykograficznego iloczynu dobrych porządków** (`thm:lex-well-orders-xliii`). W tezie relację leksykograficzną zapisano za pomocą `\preceq_P`, ale w dowodzie pojawiało się `p_0\prec_P p` bez jawnego wprowadzenia tego symbolu w samym twierdzeniu. W dowodzie przyjęto wprost alternatywę `p_0\ne p` lub `p_0=p`; w pierwszym przypadku użyto deklarowanej w tezie nierówności `p_0\preceq_P p` oraz definicji porządku leksykograficznego. Argument, teza i logiczny zakres dowodu pozostały niezmienione.
2. **Redakcja uwagi o nierozdzielności krat.** Sformułowanie „trzema parami nieporównywalnymi elementami” zastąpiono precyzyjnym „trzema wzajemnie nieporównywalnymi elementami” `a,b,c` w kracie `M_3`. Wzory i diagram nie uległy zmianie.

Nie dodano ani nie usunięto twierdzeń, wniosków, dowodów, definicji, przykładów, uwag, rysunków ani etykiet. Nie zmieniono żadnej tezy matematycznej.

## Ponowna kontrola matematyczna

Niezależnie od wcześniejszych raportów przeczytano **15 twierdzeń, 1 wniosek, wszystkie 16 dowodów, 12 definicji, 21 przykładów i 7 uwag**. Sprawdzono definicje i korespondencję porządków ostrych i nieostrych, minimalność i najmniejszość (także w skończonych i nieskończonych porządkach), rekonstrukcję z diagramu Hassego, kryteria kresów, kraty i zupełność, przypadki pustych iloczynów i pustych rodzin, porządek współrzędny i leksykograficzny, gęstość, dobre porządki, indukcję, jednoznacznie określoną funkcję wyboru na ustalonym dobrym porządku oraz iloraz preporządku.

Nie znaleziono nowej fałszywej tezy ani błędnego kroku dowodu. Zbadano również, czy istniejące wyniki nie wykorzystują niejawnie aksjomatu wyboru, w szczególności rozważając konstrukcję minimum kolejnych włókien w leksykograficznym iloczynie dobrych porządków.

- Ponownie wykonano pełny niezależny zestaw `independent_check.py`: **30 665/30 665** testów zaliczonych; obejmuje on wszystkie porządki częściowe i preporządki na zbiorach rozmiaru do 4.
- Ponownie wykonano `extra_check.py`: **215 552/215 552** testów zaliczonych; w tym wszystkie porządki współrzędne i leksykograficzne na małych zbiorach oraz wszystkie podzbiory odpowiednich iloczynów.
- Łącznie **246 217/246 217** testów semantycznych. Testy skończone nie zastępują formalnych dowodów dla zbiorów dowolnej wielkości.

## Kompilacja, odsyłacze i rysunki

- Pełny skrypt (44 rozdziały): `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex` — **kod 0, 376 stron**, **1075 unikatowych etykiet**, **869 odsyłaczy**, **0 duplikatów**, **0 nieznanych celów**, **0 ostrzeżeń `Overfull \hbox`**.
- Częściowo zaimportowana książka 01–06: `latexmk` — **kod 0, 62 strony**, bez przepełnionych wierszy. Cztery oczekiwane odsyłacze do jeszcze niezaimportowanych rozdziałów (`ch:functions`, `ch:syntax-fol`, `ch:semantics-fol`, `ch:zf-axioms`) rozwiązują się w pełnym skrypcie. Etykiet nie zmieniano.
- Liczba i kolejność etykiet rozdziału: **42/42** zachowanych. Liczby środowisk: 15 twierdzeń, 1 wniosek, 16 dowodów, 12 definicji, 21 przykładów, 7 uwag.
- Z pełnego PDF wyodrębniono **12 stron rozdziału 06**; wszystkie wyrenderowano i obejrzano, w tym diagramy Hassego i kraty `M_3`. Nie zauważono kolizji rysunków, obciętego tekstu ani innych problemów układu.

## Status

**Audyt IV zakończony: dwie lokalne nieścisłości poprawione i zweryfikowane.** Zgodnie z ustalonym trybem, ponieważ zaszła zmiana tekstu, **rozdział 06 pozostaje otwarty do audytu V**. Jeśli kolejna niezależna iteracja nie wykryje usterek, będzie można go zamknąć. Zmiany opublikować na aktualnej gałęzi po weryfikacji jej stanu; następnie sprawdzić GitHub Actions.
