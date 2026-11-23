# Teoria grafów i węzłów — stabilizacja algorytmów przepływowych

Data: 2026-11-23.

## Werdykt

**STABILNY W ZAKRESIE NOWEGO ROZDZIAŁU 40 I JEGO LOKALNEJ INTEGRACJI**.

Ten status dotyczy \`chapters/pl/graph_and_knot_theory/40-algorytmy-przeplywowe-ford-fulkerson-edmonds-karp-dinic.tex\` oraz współpracy z wcześniejszym rozdziałem 04. Nie oznacza zakończenia audytów wszystkich wcześniejszych rozdziałów ani formalizacji matematycznej w Lean.

## Kontrolowana wersja

Commit źródeł: [5b838e2626fe350d6a2eb362f3a1bccf9fd9d0eb](https://github.com/dariusz-piekarz/mathematical_scipts/commit/5b838e2626fe350d6a2eb362f3a1bccf9fd9d0eb).

Potwierdzone wyniki GitHub Actions:
- [Graph and knot theory - algorithms audit, 45146125420](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45146125420) — \`finite-models\` **success**, \`chapter-pdf\` **success**.
- [Mathematical library application checks, 45146125433](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45146125433) — **success**.
- [Polish mathematical terminology, 45146125449](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45146125449) — **success**.

## Rygor matematyczny

Rozdział wykorzystuje istniejące w rozdziale \`04-spojnosc-przekroje-i-twierdzenie-mengera.tex\` definicje przepływu, pojemności resztowej i przekroju. Ujęto:

1. Niezmiennik dopuszczalności przepływu przy powiększaniu; rozróżnienie łuków oryginalnych, przejść wstecznych i przejść równoległych.
2. Równoważność: przepływ maksymalny, brak ścieżki resztowej, osiągnięcie pojemności przekroju; wynik obejmuje rzeczywiste nieujemne przepustowości.
3. Istnienie maksimum dla rzeczywistych przepustowości przez zwartość zbioru dopuszczalnych przepływów.
4. Ford--Fulkerson: zakończenie dla przepustowości całkowitych i ostrożne omówienie niekończących się wyborów ścieżek przy pewnych przepustowościach niewymiernych.
5. Edmonds--Karp: niemalejące odległości resztowe, ograniczenie powtórnych nasyceń i wielomianowość.
6. Dinic: sieć warstwowa, przepływ blokujący, przyrost odległości do ujścia, oszacowanie \`O(n^2(m+1))\`.
7. Certyfikat minimalnego przekroju i przykłady przepływu z anulowaniem części wcześniej przesłanej jednostki.

## Niezależna walidacja obliczeniowa

\`tools/tests/test_graph_and_knot_flow.py\` zakończył się sukcesem:
- **1467** wyczerpująco wygenerowanych małych sieci skierowanych;
- **1050** deterministycznych dodatkowych sieci z łukami przeciwnymi lub równoległymi;
- **680** sieci o dokładnych wymiernych przepustowościach.

W każdym przypadku wartości Forda--Fulkersona (dla przepustowości całkowitych), Edmondsa--Karpa i Dinica sprawdzano względem **niezależnie wyliczonego minimum po wszystkich przekrojach \`s,t\`**, a nie tylko względem siebie nawzajem. Testy dodatkowo kontrolują bilanse, ograniczenia, odległości resztowe i konstrukcję przekroju. Przeszły także wcześniej wprowadzone regresje BFS/DFS, A*, CH, Prima, Kruskala i DSU.

## Rzeczywisty skład PDF

- PDF fragmentu książki \`00–05+37+38+39+40\`: **58 stron A4**.
- Trzy zakończone sukcesem przebiegi \`pdflatex\`; na końcowym przebiegu **brak ostrzeżeń LaTeX o referencjach** i **brak przepełnień \`Overfull\`**. Workflow odtąd wymaga stabilności odsyłaczy i kończy się błędem w razie braku stabilizacji.
- Obejrzano obie ilustracje sieci przepływowych oraz końcowy skład nowego rozdziału.
- Zidentyfikowana wcześniej bliskość pionowej granicy przekroju i etykiet pojemności \`2\`, \`3\` została naprawiona przez przesunięcie linii granicy; w końcowym PDF linia nie koliduje z oznaczeniami.
- Katalog Atlasu i główny plik książki zawierają identyczną kolejność **41** plików źródłowych.

## Następny etap

Rozbudowa algorytmicznej części teorii grafów jest gotowa na poziomie rozdziałów **37–40** (BFS/DFS; drogi ważone i A* wraz z CH; MST/DSU; algorytmy przepływowe). Kolejny moduł z zatwierdzonego planu: **teoria grafów ekstremalna i probabilistyczna**, w tym Turán, Ramsey i grafy losowe, a następnie expandery. Zachować zasadę: tworzyć jeden rozdział, niezależnie go audytować, weryfikować na prawdziwym CI i stabilizować przed przejściem dalej.
