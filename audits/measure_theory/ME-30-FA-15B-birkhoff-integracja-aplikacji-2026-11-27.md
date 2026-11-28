# ME-30 / FA-15B — kontrola integracji aplikacji

Stan wejściowy 2227869ce37a67ec85c563663dd0ed9a0d785267. Integracja źródeł z commitu 45078f91f9068169128edd754cdded16b5d19c4d: terminologia PASS; FA-15B (46073480852) i pełne FA (46073480963) — etap regresji PASS, PDF w toku przy sprawdzaniu; przebieg aplikacji anulowany. Nie uznano go za PASS.

Dodano test rzeczywistych źródeł FA-15B i ME-30, budujący odizolowaną bazę SQLite przez parser aplikacji. Sprawdza cztery kwalifikowane odsyłacze (trzy do ME i jeden odwrotny), status rozwiązania, istnienie encji, zgodność API label_detail z właścicielem i etykietą oraz brak wymuszania importu drugiego rozdziału przy generowaniu skryptu. Nie zmieniano matematyki ani istniejących etykiet. Wyniki nowego testu wymagają potwierdzenia w CI.
