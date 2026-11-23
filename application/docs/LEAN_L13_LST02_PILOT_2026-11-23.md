# L1.3 — iteracja pilotażowa LST-02 (kandydaci do recenzji)

**Zakres:** jeden pakiet czterech mapowań dla kanonicznego
`LST-02`, bez ingerencji w plik LaTeX, starych formalizacji LST-01,
weryfikowany kandydat L1.4.1 ani status tamtego 2+1.

## Odwzorowania

| Oryginalna etykieta LaTeX | Deklaracje Lean | Co należy sprawdzić |
| --- | --- | --- |
| `thm:negation-quantifiers` | `lst02_not_forall`, `lst02_not_exists` | Obie równoważności, klasyczna logika, domena także pusta |
| `thm:same-quantifier-order` | `lst02_swap_forall`, `lst02_swap_exists` | Wymiana obu kwantyfikatorów tego samego typu bez założenia niepustości |
| `thm:swap-mixed` | `lst02_mixed_quantifier_forward`, `lst02_mixed_empty_counterexample` | Tylko poprawny kierunek implikacji; drugi pomocniczy kontrprzykład dla pustych dziedzin |
| `thm:unique-expansion-xli` | `lst02_unique_exists_expansion` | Definicyjne rozwinięcie `∃!` do istnienia i jednoznaczności |

Przepisanie nie wzmacnia hipotez o niepustości, nie wprowadza
nieudowodnionych aksjomatów i nie zmienia kanonicznego tekstu.
Twierdzenie o przeciwprzykładzie jest deklaracją **pomocniczą**,
nie dodatkowym mapowaniem źródłowym.

**Etap oceniania:** `statement_status=needs_review`,
brak `source_document_sha256` i brak `approved`. To celowe:
`formalization_status=draft` nawet przy prawidłowym bieżącym
dokumencie, dopóki nie zostanie wykonana osobna recenzja semantyczna
i przypięty digest oryginału. Sama kompilacja Lean, testy
statyczne i `axiom_check` nie mogą nadać `approved` ani
`certificate=true`.

## Kryteria dalszego odbioru

1. Potwierdzić, że wszystkie cztery etykiety należą do rzeczywistych
   środowisk `twierdzenie` w LST-02 i obejmują całe tezy,
   a status katalogu odróżnia `draft` od `approved`.
2. Uruchomić rzeczywisty Lean 4.26.0 i przypięty Mathlib na nowym
   `LST02_Quantifiers.lean`; skontrolować wszystkie siedem
   `#print axioms`, w szczególności `Classical.choice`
   dla pierwszej negacji. Nie traktować offline mocków jak kompilacji.
3. Sprawdzić negatywne przypadki pustych domen i brak odwrotnej
   implikacji przy mieszanych kwantyfikatorach.
4. Oddzielny recenzent ocenia dokładny zakres matematyczny
   i kwalifikuje mapowania do `approved`. Następnie przypiąć
   SHA256 kanonicznego źródła (bez żadnej edycji TeX) i
   przeprowadzić techniczne 2+1 na niezmiennym SHA.
5. Raportować odrębnie wpisy manifestu, deklaracje rzeczywiście
   kompilowane oraz recenzowane powiązania. Ukończenie całego
   pilotażu 20–30 i LA-01 pozostaje otwarte w issue #11.

**Brak certyfikatu semantycznego:** `certificate=false`.
