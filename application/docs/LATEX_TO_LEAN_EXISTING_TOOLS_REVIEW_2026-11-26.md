# Gotowe narzędzia LaTeX → Lean — przegląd z 26 listopada 2026

Na polecenie użytkownika sprawdzono gotowe rozwiązania, aby dalszy rozwój
Atlasu wykorzystywał istniejące modele i narzędzia formalizacji. Obecny
translator Atlasu jest parserem i generatorem regułowym; nie trenujemy
własnego modelu językowego. Poniższa ocena opiera się na dokumentacji
autorów, a nie na wykonanym benchmarku tych narzędzi w naszej bibliotece.

| Rozwiązanie | Udokumentowany zakres | Dopasowanie i ograniczenia |
| --- | --- | --- |
| [AutoformBot, Meta](https://github.com/facebookresearch/autoform-bot) | Plugin dla Codex, Claude Code i Muse: artykuł, rozdział lub notatki → plan zależności → definicje i dowody Lean. Licencja MIT. | Pierwszy kandydat do oceny gotowego procesu. Aktualna dokumentacja wydania 0.7.0 wymaga Lean ≥4.27, a Atlas ma przypięte 4.26. Wymagany osobny projekt pilotażowy; nie aktualizujemy przypięcia Atlasu automatycznie. |
| [LeanFlow, EPFL](https://github.com/epfl-lara/LeanFlow) | LaTeX/PDF → szkic stwierdzeń Lean do przeglądu i późniejszego dowodzenia; osobne tryby dowodzenia i napraw. Apache-2.0. | Alternatywa do porównania. Wykorzystuje istniejący Codex, Claude Code lub Lemex. Dokumentacja wymaga Python ≥3.12; na Windows wskazuje WSL2. WSL2 nie jest zainstalowany w odczytanym lokalnym środowisku. |
| [Goedel-Formalizer-V2-8B](https://huggingface.co/Goedel-LM/Goedel-Formalizer-V2-8B) | Opublikowane wagi modelu przekształcającego nieformalne sformułowanie problemu w stwierdzenie Lean 4. Apache-2.0, 8B, BF16. | Możliwy lokalny generator bez treningu. Nie jest kompletnym procesem formalizacji rozdziału. Konieczne pomiary zasobów, zgodności z naszym Mathlib i jakości na polskim materiale. Karta nie określa minimalnego VRAM; nie deklarujemy, że model zmieści się na bieżącym komputerze. |

Dokumentacja nie dowodzi poprawnego tłumaczenia dowolnego polskiego
manuskryptu. Poprawna kompilacja Lean nie wystarcza do potwierdzenia, że
wygenerowana teza ma dokładnie te same założenia i znaczenie co źródło.
Korzystanie z gotowego procesu nie znosi potrzeby oceny tych warunków.

## Stan Atlasu w chwili przeglądu

- Przypięte Lean 4.26.0 i Mathlib
  `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`; kompilacja i audyt
  aksjomatów zarejestrowanych przykładów są wykonywane w CI.
- `lean_parser` i `lean_draft_generator` obsługują ograniczony język formuł:
  spójniki, kwantyfikatory, równości, porównania, proste działania i jawne
  typy `Prop`, `Nat`, `Int`, `Real`. Nierozpoznane fragmenty są odrzucane.
- Słownik pojęć i kontekst indeksu zapewniają powiązanie ze źródłem.
  Generator zwraca niezrecenzowany szkic; nie tłumaczy swobodnie całego
  polskiego rozdziału i nie uruchamia dowolnego kodu użytkownika.
- Bieżący RT-09c dotyczy zaufanego, stałego przykładu Mathlib offline oraz
  odrzucenia niekompletnego pakietu importów. To nie jest gotowy runner
  niezaufanych wyników modelu. Szczegóły i rzeczywiste wyniki w
  [dzienniku](ATLAS_DEVELOPMENT_PROGRESS.md).

## Kolejny pilot integracyjny

Po zakończeniu bieżącej stabilizacji, w odpowiedniej fazie planu, ocenić
gotowy proces AutoformBot i alternatywę LeanFlow, a następnie wybrać
adapter do Atlasu. Nie budować uniwersalnego translatora ani nie trenować
własnego modelu przed takim porównaniem. Reguły Atlasu zachowują funkcję
kontroli składni, pochodzenia, zakresu i ograniczeń.

1. Użyć odrębnego projektu Lean i przypiąć wersje narzędzia oraz Mathlib.
   Sprawdzić zgodność wersji, licencję i sposób wywoływania istniejącego
   modelu. Nie uruchamiać instalatorów ani agentów w kanonicznym repozytorium.
2. Przygotować wybrane obiekty LST-01 i LST-02 wraz z definicjami,
   założeniami i oryginalnymi etykietami, np. `thm:de-morgan-logic`,
   `thm:negation-quantifiers`, `thm:same-quantifier-order`,
   `thm:swap-mixed`. Dodać osobne przypadki z jawnymi typami i przypadki
   wymagające odmowy. Istniejące mapowania LST-02 mają nadal
   `needs_review`; nie są zatwierdzonym wzorcem semantycznym.
3. Rozdzielnie mierzyć zachowanie wszystkich założeń i znaczenia,
   poprawność składni, kompilację, dowód bez luk, koszty/czas i odmowy.
   Nie zaliczać szkicu ze `sorry` jako gotowego dowodu.
4. Atlas przekazuje wyłącznie wybrany fragment i niezbędny kontekst,
   zachowuje jego skróty i pokazuje wynik jako szkic do przeglądu.
   Generowanie, kompilacja i recenzja znaczenia mają osobne statusy.
5. Wykonanie zewnętrznego dostawcy lub pobranie dużych wag stanowi osobny
   krok wdrożenia. Ten przegląd niczego nie instaluje, nie pobiera wag,
   nie wysyła źródeł do modeli ani nie wykonuje płatnych wywołań.

Ten zapis ustala kierunek oceny gotowych narzędzi. Nie zamyka L1.5.6,
nie przeskakuje do L1.5.7/G2 i nie zastępuje niezależnego odbioru.
