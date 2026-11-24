# AA-53 — audyt VI: monomy wiodące i integracja tomu

Data: 24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Źródło: blob 5675bf04c336a76e6424eeca337f24b5f211aeb5, bez zmian.

## Niezależny argument i wykonane obliczenia
Dla u=x²y², v=x^(2n)+y^(2n), w=xy(x^(2n)-y^(2n)) monom wiodący u^i v^j w^e w porządku leksykograficznym x>y to x^(2i+2nj+(2n+1)e)y^(2i+e), ze współczynnikiem 1. Parzystość wykładnika y wyznacza e=0 lub 1, następnie ten wykładnik wyznacza i, a wykładnik x wyznacza j. Monomy wiodące są więc różne, co daje niezależny dowód liniowej niezależności tej rodziny (w skończonej kombinacji największy monom nie może się skrócić). Wykonano test JavaScript/BigInt z dokładnym rozwijaniem dwumianów dla n=2,...,30 i d=0,...,100: 2929 przestrzeni jednorodnych, 3946 rozwiniętych wielomianów; sprawdzono współczynnik i wykładnik wiodący oraz brak powtórzeń w każdej przestrzeni. Wszystkie asercje prawdziwe. To alternatywna kontrola dowodu, bez zmiany zakresu rozdziału.

## Integracja
Porównano rzeczywisty katalog plików, uporządkowaną listę input w książce i listę chapters w catalog/books.json: 53/53/53, dokładna zgodność kolejności i ścieżek. Sprawdzono bramkę integralności: numeracja 1–53, osobne audyty AA-43–53, zachowane historyczne pokrycie AA-01–42. Workflow zawiera oba moduły testów AA-53 w filtrze ścieżek i osobnych krokach wykonania, kompilację pełnego tomu i archiwizację PDF/log.

## CI
Run 45348236656, job 138287946248, head 3d9d4373b9a1c3e369394912a6dbdf27c752ee7d: in_progress, conclusion brak, kroki {"success":81,"in_progress":1,"pending":33}. Artefakty: brak. Nie przypisano nieodbytych oględzin PDF.

## Werdykt
AA-53 matematycznie bez nowych usterek, technicznie W AUDYCIE do zakończenia CI i kontroli PDF. AA-54 nieotwarty. Nie zmieniano źródła, workflow ani innych rozdziałów.
