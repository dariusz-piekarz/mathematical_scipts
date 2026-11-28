# Algebra liniowa — rozdział 29, audyt IV

**Data:** 21 listopada 2026  
**Sprawdzony rozdział:** `chapters/pl/linear_algebra/29-grassmanniany.tex`, poprzedni blob `6fa53e87002405678321fca7c4317dd83a0b4452`.

## Kontrola
- Sprawdzono wymiar `Gr_k(K^n)`, wzory na przejścia między mapami, rzut ortogonalny na wykres, tożsamość stycznej z `Hom(L,V/L)`, lokalną trywializację wiązki tautologicznej i ilorazowej oraz faktoryzację Plückera.
- SymPy: **227** niezależnych przypadków dokładnych Gr(2,5), pięć relacji kwadratowych dla wszystkich 4-elementowych podzbiorów indeksów i niezmienniczość współrzędnych rzutowych przy zmianie bazy o wyznaczniku różnym od zera — PASS.
- W rozdziale 29 obecne są wszystkie 19 własnych etykiet, a zewnętrzne odsyłacze wskazują wcześniejsze LA-10 i LA-11.
- Weryfikacja poprzedniego bloba po audycie II przeszła CI (workflow 44954261674, SUCCESS), a 7-stronicowy PDF po audycie II ma na każdej stronie tekst i nie zawiera bloków poza formatem strony. Obejrzano montaż zawierający oba diagramy TikZ; brak widocznych kolizji.
- **Poprawka redakcyjno-definicyjna IV.1:** usunięto przecinek rozpoczynający nowy wiersz po równości Gr₁(Rⁿ)=RPⁿ⁻¹ i jawnie objaśniono zarówno rzeczywistą, jak i zespoloną przestrzeń rzutową. Nie zmieniono żadnego wzoru, dowodu ani etykiety.

## Decyzja
Ponieważ wprowadzono poprawkę IV.1, **audyt IV nie jest czysty**. Dalsze niezależne kontrole muszą być wykonane na aktualnym blobie; potrzebne będą dwie kolejne czyste iteracje, z końcowym zielonym CI i PDF.
