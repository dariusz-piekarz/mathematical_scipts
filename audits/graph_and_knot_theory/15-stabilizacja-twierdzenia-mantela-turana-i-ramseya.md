# Teoria grafów i węzłów — stabilizacja Mantela, Turána i Ramseya

Data: 2026-11-23.

**Status: STABILNY W ZAKRESIE ROZDZIAŁU 41 I JEGO LOKALNEJ INTEGRACJI.**
Nie jest to ocena globalnej stabilności pozostałych rozdziałów całego skryptu.

## Kontrolowane źródła
- Rozdział: \`chapters/pl/graph_and_knot_theory/41-twierdzenia-mantela-turana-i-ramseya.tex\` (blob \`328790f72943ce7c9ffde6a71deeef65cea93192\`).
- Test: \`tools/tests/test_graph_and_knot_extremal.py\` (poprawiona wersja z commita [061fbb2](https://github.com/dariusz-piekarz/mathematical_scipts/commit/061fbb2f940f21743ad00a6e493cb8754aa24b3d)).
- Integracja: książka oraz \`catalog/books.json\`, 42 pliki źródłowe, w tym rozdział 41 bezpośrednio po nowych 37–40.
- Raporty procesu: \`13-extremalna-mantel-turan-ramsey-audyt-wstepny.md\` i \`14-extremalna-niezalezny-audyt-dowodow-testow-i-pdf.md\`.

## Zweryfikowane testy

[GitHub Actions — przebieg 45148475682](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45148475682):
- **finite-models: success**;
- **chapter-pdf: success**.

Niezależne zliczenia:
- 33 868 wszystkich grafów prostych o 0–6 wierzchołkach: maksimum liczby krawędzi grafów bez \`K_{r+1}\` dla \`r=1..5\` dokładnie równe liczbie krawędzi Turána; w szczególności twierdzenie Mantela;
- 10 650 kontroli symetryzacji niepołączonych wierzchołków: zachowanie zakazu kliki i przewidywana zmiana liczby krawędzi;
- 33 792 kolorowania krawędzi \`K_5\` i \`K_6\`: istnienie kolorowania \`K_5\` bez jednobarwnego trójkąta oraz brak takich kolorowań \`K_6\`, zatem \`R(3,3)=6\`;
- zgodność katalogu Atlasu i składni środowisk LaTeX, etykiet i źródeł.
- wszystkie wcześniejsze kontrole BFS/DFS, A*, CH, MST/DSU i przepływów przechodzą w tym samym przebiegu.

Pierwsza iteracja testu poprawnie wykryła błąd jego inicjalizacji tablicy dwumianowej (\`KeyError (2,1)\`). Przyczyną było sprawdzanie symetrii przed wypełnieniem tabeli. Naprawiono, ponowiono cały zestaw; nie było to naruszenie dowodu matematycznego.

## Matematyka i skład

Podczas niezależnego audytu zweryfikowano w szczególności:
- nierówność stopni w grafie bez trójkątów, nierówność Cauchy'ego–Schwarza i przypadki brzegowe;
- operację Zykowa na klasach bliźniaków oraz argument maksymalności przez sumę kwadratów ich liczności;
- wyrównanie części grafu Turána, w tym \`r>n\` i \`n=0\`;
- indukcję Ramseya, granice dwumianowe, przypadek \`R(3,3)\` i twierdzenie wielobarwne.

Wersję PDF z pozytywnego przebiegu CI pobrano i skontrolowano:
- **63 strony A4**, nowy rozdział na stronach PDF 59–63;
- trzy kompilacje \`pdflatex\`, brak ostrzeżeń o niestabilnych/niezdefiniowanych odsyłaczach, brak przepełnień \`Overfull\`;
- obejrzano wszystkie pięć stron nowego rozdziału oraz oba rysunki TikZ (\`K_{3,3}\`, dwukolorowanie \`K_5\`); podpisy i węzły są czytelne.

Pozostałe CI źródłowego commita integracyjnego:
- [Mathematical library application checks, 45148329087](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45148329087): **success**;
- [Polish mathematical terminology, 45148329080](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45148329080): **success**.

## Następny moduł

Rozpocząć osobny rozdział o **grafach losowych i metodzie probabilistycznej**, w tym model \`G(n,p)\`, wartość oczekiwaną, momenty i podstawowe progi, oszacowania dolne dla liczb Ramseya. Dopiero po jego wielokrotnym audycie, pozytywnym CI i stabilizacji przejść do osobnego rozdziału o ekspanderach.
