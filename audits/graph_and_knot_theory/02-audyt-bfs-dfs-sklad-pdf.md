# Grafy i węzły — audyt 03: skład, PDF i korekta wzoru \`low\`

Zakres: nowy rozdział algorytmiczny, rozdział 37 w plikach źródłowych, szósty w składzie.

## Rzeczywista kontrola PDF
Wykonano kompilację LaTeX w GitHub Actions:
- workflow: \`Graph and knot theory - algorithms audit\`;
- przebieg: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45137798414;
- zadanie \`finite-models\`: sukces, obejmuje 1099 grafów nieskierowanych i 4165 skierowanych;
- zadanie \`chapter-pdf\`: sukces, powstał 40-stronicowy PDF fragmentu 00–05+37.

Pobrano artefakt PDF z CI i obejrzano strony 37–39, w szczególności cały rysunek BFS, podpis, rozdział DFS oraz formułę \`low\`. Rysunek i podpis nie nachodzą na siebie. Log składu pokazał dokładnie jedno \`Overfull \\hbox\` na linii wzoru \`low\`, 8,82693 pt ponad szerokość kolumny.

## Poprawka
Zapis \`low[v]\` przeniesiono do wielowierszowego środowiska \`aligned\`, nie zmieniając definicji matematycznej. W workflow dołożono twardą kontrolę wykrywania \`Overfull \\hbox\` lub \`Overfull \\vbox\`; teraz nawet poprawna kompilacja nie wystarcza do uznania składu za stabilny.

## Warunki zamknięcia audytu
Sprawdzić ponowną kompilację w świeżym CI, szczególnie brak przepełnień. Po uzyskaniu obu zielonych zadań PDF i testów enumeracyjnych oraz ponownym obejrzeniu stron zawierających wzór \`low\` rozdział można uznać za stabilny na poziomie bieżącego audytu, bez twierdzenia o globalnej stabilności całego 36-rozdziałowego skryptu.
