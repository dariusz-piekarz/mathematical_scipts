# PDE I — rozdział 08: kontrola techniczna po pierwszej lekturze

Data: 2026-11-25. Iteracje 114–115. **CI PASS; rozdział jeszcze niestabilizowany semantycznie.**

- Przebieg [45591751805](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45591751805), job 139127445348, head e75499b8ec4461b0fc6d18fb2a88461b3f3de1d3, status completed/success.
- Testy wykonywalne: 12/12 OK (0,077 s w logu CI). Ponowny lokalny przebieg identycznego pliku (git hash-object a70c18b1384563d26c1a7ac8894ebd52fec27164) również 12/12 OK. To skończone testy numeryczne, nie dowody.
- Kontrola struktury: 92/92 kotwic kryteriów, 39 unikatowych etykiet, 83 wystąpienia odsyłaczy, 10 zewnętrznych celów. Numeracja zewnętrzna: rozdziały 4, 5, 6, 7; sekcje 7.1, 7.4, 7.5; twierdzenia 7.4, 7.19, 7.20.
- Kompilacja izolowanego rozdziału z kanoniczną preambułą: PASS, PDF A4, 26 stron, 480911 bajtów; brak krytycznych diagnostyk objętych workflow.
- Artefakt 15010878908, ZIP 7539955 bajtów, SHA-256 b35105cdfcf929e788cbdc40efd74bb6883134ecd7b6d798cc803edba0edabcd — pobrany plik zgodny z digest GitHub. PDF SHA-256 0fa1b28f90b7a08229d0ba81fa330f004a7090328de3d7462f14c49787c2b231.
- Obejrzano miniatury wszystkich 26 renderów 120 dpi w pięciu arkuszach kontaktowych: brak widocznych obcięć, nachodzenia bloków lub pustych stron. Kontrola układu na miniaturach, nie ponowny audyt każdej formuły w pełnej rozdzielczości.
- Log zawiera 19 ostrzeżeń hyperref o pustym celu odsyłacza (odsyłacze zewnętrzne w izolowanym PDF mają wyłącznie numery, bez aktywnego celu) i 1 Underfull hbox (badness 3029, akapit w twierdzeniu Plancherela, linie 719–727). Nie są to błędy kompilacji; akapit należy ponownie ocenić podczas drugiej lektury.
- Porównano drzewa gałęzi i head CI: 12/12 identycznych blobów wejściowych, tj. rozdziały 04–08, rejestr i testy 08, workflow, książka, manifest, wspólne listingi i preambuła Atlasu.
- Źródło 08: 4932d4f62e2813e57717d90f6161015187ceaac0; rejestr: f2f20552009d2b9a1b6c0cbb363a36fd30e44713; workflow: 04a701ed95cdc9a588a86a51d473eaf7b5b96a61.

Nie zmieniano źródła, testów ani workflow w iteracji 115. Nie kompilowano całego tomu i nie uruchomiono formalizacji Lean. Następna iteracja 116: druga lektura sekcji 8.1–8.2, kryteria 001–016; bez poszerzania zakresu. Po usunięciu ewentualnych usterek ponowna kontrola CI i niezależny audyt przed stabilizacją.
