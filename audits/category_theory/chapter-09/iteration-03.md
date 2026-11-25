# CAT-09 — audyt III (kontrola matematyczna)

Źródło 39d85f65acf13ceb9fc514a5979d6fd810fe8475. Ponownie sprawdzono typy strzałek w obu wariancjach, naturalność i bijektywność, izomorfizmy par reprezentujących, początkowość/końcowość w kategoriach elementów, liniowość i jednoznaczność przedłużenia, rachunki lokalizacji, hipotezy dla iloczynu tensorowego i konstrukcję różniczek Kählera. W ostatniej konstrukcji wszystkie relacje giną pod mapą indukowaną przez derywację, a obrazy generatorów jednoznacznie wyznaczają mapę ilorazową. Kryterium niereprezentowalności oraz przeciwobraz zbioru potęgowego sprawdzono. Nie wykryto nowej istotnej luki; bez rozszerzania zakresu i bez zmian treści.

## Kontrola niezależna

Uruchomiono kod JavaScript (node control.js), zapisany trwale w tests/mathematical/category_theory/chapter-09/control.js. Wyniki {"cov":1544,"contra":1842,"local":12,"der":97,"total":3495}. Liczniki cov i contra oznaczają pary reprezentant–element testowy, local oznacza pierścienie docelowe, der kandydatów na derywację. Kontrole obejmują także nieuniwersalne elementy i przypadki brzegowe. Derywacje liczb dualnych w charakterystyce 2 i 3 sprawdzano przez regułę Leibniza dla wszystkich par elementów. Testy skończone nie zastępują dowodów; Lean nie uruchamiano.

## Walidacja

CI audytu II: 45592327738, commit f61dcab1bd2680510efe229a45158e6cf0ae804b, stan w chwili zapisu: in_progress, conclusion: null. Krok testów regresyjnych zakończony success według odczytu job 139129445260. Porównano 31 plików objętych CI z aktualną głową przed zapisem, identyczne. Kontrola wizualna PDF nie została wykonana; CAT-09 pozostaje otwarty do potwierdzenia finalnej kompilacji, odsyłaczy i PDF. 
