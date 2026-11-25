# CAT-20 — niezależny audyt kontrolny V

Raport IV zapisano w f0a037ab4c8c9aabddbf76eed1559eb75cff6af0. Punkt odniesienia aaccd5717433d0064d25381cd2c3b1c76d6ebd0a: 44 pliki zakresu CI identyczne z e1a3892fadd3a4f675dde79fe272b402e89f2e2b. Źródło 07597d81f8ce78d9b578c719c401a392b60a9b8a, test eade1f51ce7a14ab14b00175c9d2a2000c379eea. Rejestr 8/8 identyfikatorów; 19 etykiet i 17 wystąpień ref/eqref. Ponownie sprawdzono typy i kolejność złożeń w przenoszeniu obu sześciokątów, naturalność, relacje Coxetera, argument reprezentantów warstw i wszystkie przypadki mnożenia przez generator. Sprawdzono przypadki n=0,1, jednostki, powtarzające się obiekty i zakres twierdzeń. Nie wykryto nowej istotnej luki.

Niezależna kontrola JS grafu permutacji: dla wszystkich 127 profili parzystości stopni dla n=0–6 przeprowadzono BFS po wszystkich permutacjach znakowanych pozycji. Sprawdzono 50363 stany oraz 247016 skierowanych krawędzi zamian sąsiadów. Znak otrzymany dowolną drogą zgodny ze znakiem wynikającym z liczby inwersji par nieparzystych; każdy profil ma n! stanów. PASS. Jest to kontrola skończona konkretnego modelu, nie dowód ogólny.

Potwierdzono CI #45651854997 job 139338167329 SUCCESS, 140/140 testów, 8/8 CAT-20. Wykorzystano rzeczywistą kontrolę wizualną stron 80–89 PDF (artefakt 15040062543, 89 stron) z IV; nie powtarzano renderowania i kompilacji, ponieważ zakres CI nie zmienił się. Nie sprawdzano nowego CI aplikacji ani nie uruchamiano Lean.

Wynik: CAT-20 zamknięty w aktualnym zakresie, bez zmian źródła i testów. Koherencja ogólnych kategorii z pleceniem nie jest twierdzeniem dowiedzionym w tym rozdziale. Następny CAT-21: obiekty monoidalne, komonoidy i dualność.
