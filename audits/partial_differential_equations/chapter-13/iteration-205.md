# RRC 13 — iteracja 205: inwentaryzacja i pierwsza lektura 001–014

Źródło początkowe 445c73db6542a20399cb9aab7b50b1df1ea7e825 (647 wierszy); po poprawkach 7a36d0c57c8e5b24f0aebe1896536c2eb9e998d5 (735 wierszy), commit 220af8062da8f4fe6bb87e129ade6ad76f20119f. Dziewięć sekcji, 38 etykiet. Odczytano cały rozdział w celu inwentaryzacji; szczegółowo audytowano pierwsze trzy sekcje.

| ID | Zakres i wynik |
|---|---|
| PDE-13-001 | Wspólna własność eliptyczności poza zbiorem miary zero; jawny argument przez wektory wymierne. |
| PDE-13-002 | Część antysymetryczna znika w formie kwadratowej; rozpisano rachunek, poprawiono nieprecyzyjną terminologię dodatniości. |
| PDE-13-003 | Symbol główny zgodny z konwencją -∂i∂j; określono normy współczynników. |
| PDE-13-004 | Reguła Leibniza w postaci dystrybucyjnej przy W^{1,∞} i H²_loc; jawny wzór na zmieniony dryf i ograniczenia dla mierzalnych współczynników. |
| PDE-13-005 | Przykład skokowego współczynnika: obliczono słabą pochodną i ciągły strumień. |
| PDE-13-006 | Obliczono u''=-3δ₀/4; wyjaśniono zależność formalnego iloczynu od reprezentanta i brak H². |
| PDE-13-007 | Rozróżniono pełną normę H¹ od normy gradientu w RRC 11, także normy funkcjonałów. |
| PDE-13-008 | Zdefiniowano formę na całym H¹×H¹, potrzebną później dla niejednorodnego śladu i porównania; jawne oszacowanie M. |
| PDE-13-009 | Ciągłość i iniektywność zanurzenia L² w H⁻¹; odsyłacz do twierdzenia o zerowym śladzie. |
| PDE-13-010 | Uzasadniono utożsamienie H⁻¹ z podprzestrzenią dystrybucji i wszystkie iloczyny L². |
| PDE-13-011 | Rozpisano obie implikacje równoważności słabej i dystrybucyjnej, w tym błąd aproksymacji. |
| PDE-13-012 | Nierówność Gårdinga: poprawiono zapis z całką członu zerowego rzędu, jawnie uzasadniono Younga i wybór parametru. |
| PDE-13-013 | Przesunięta forma: stała ciągłości, koercywność, hipotezy Laxa–Milgrama i oszacowanie. |
| PDE-13-014 | Rozróżniono J:V→V* i I w realizacji L²; udowodniono nierozwiązywalność dla f=sin(πx) przy rezonansie. |

12 zamian blokowych. 38 oryginalnych etykiet zachowanych w kolejności; 43/43 wystąpienia odsyłaczy (27 różnych celów) istnieją jednoznacznie w RRC 07,09,10,11,12,13. Stos środowisk poprawny. Odczytano tezy RRC 07 (Heaviside), 09 (iloczyny), 10 (Poincaré i zerowy ślad), 11 (przestrzeń dualna, Lax–Milgram i człony dolnego rzędu). Brak kompilacji i testów wykonywalnych w tej iteracji.

Plan pozostałych zakresów: Dirichlet (koercywność, niejednorodny ślad, minimum i porównanie), Fredholm (faktoryzacja, transpozycja, refleksywność, rezonans), Neumann (Wirtinger, zgodność i znak strumienia), Robin (nierówność brzegowa i koercywność), transmisja (wyprowadzenie rozwiązania, oba kierunki równoważności, rysunek), podsumowanie. Pełną liczbę kryteriów ustalimy po pierwszej lekturze. W następnej iteracji szczególnie rozdzielić oszacowanie dla b=0,c≥0 od ogólnej koercywności ze stałą α, jawnie użyć twierdzenia o jądrze śladu i sprawdzić aproksymację v² w W^{1,1}. Nie deklarować stabilizacji przed kolejnymi przebiegami i CI/PDF.
