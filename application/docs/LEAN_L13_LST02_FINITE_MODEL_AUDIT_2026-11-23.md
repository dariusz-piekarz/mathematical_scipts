# L1.3 / LST-02 — niezależna metoda kontroli na skończonych modelach

**Data:** 2026-11-23.  
**Kod Lean oceniany osobno:** `163c8f6415d9d390fc1a737f6954b2865eff6c6e`.  
**Narzędzie:** [`review_evidence/lst02_finite_model_audit.py`](review_evidence/lst02_finite_model_audit.py).  
**Zależności:** standardowa biblioteka Pythona, bez zależności od implementacji Lean i jej testów.

## Metoda

Dla każdej dziedziny `D` o liczności 0–4 enumerowano wszystkie
predykaty `P:D→{false,true}`; w sumie **31** przypisań.
Sprawdzono obie równoważności negacji kwantyfikatorów, a także
rozwinięcie `∃!` przez istnienie i warunek jednoznaczności.

Dla każdej pary `D,E` o licznościach 0–3 enumerowano wszystkie
predykaty `P:D×E→{false,true}`; łącznie **689** modeli.
Dla każdego sprawdzono komutację dwóch kwantyfikatorów ogólnych,
komutację dwóch egzystencjalnych i implikację
`(∃y∈E ∀x∈D P(x,y)) → (∀x∈D ∃y∈E P(x,y))`.
Wszystkie predykaty na pustych dziedzinach uwzględniono
z pustą koniunkcją równą `true` i pustą alternatywą
równą `false`.

Dodatkowo policzono modele obalające **niepostulowaną odwrotność**:
w tym zakresie jest ich **201**. Istnieją wśród nich
modele z pustymi dziedzinami oraz modele z obiema
dziedzinami niepustymi. Dla przykładu, przy
`D=E={0,1}` i `P(x,y)≡(x=y)`, zdanie
`∀x∈D ∃y∈E P(x,y)` jest prawdziwe, lecz
`∃y∈E ∀x∈D P(x,y)` jest fałszywe.

## Rzeczywisty wynik wykonania skryptu

```json
{
  "binary": {
    "binary_predicates": 689,
    "domain_sizes": [0, 1, 2, 3],
    "has_empty_empty_counterexample": true,
    "has_nonempty_nonempty_counterexample": true,
    "reverse_mixed_counterexamples": 201
  },
  "certificate": false,
  "scope": "finite Boolean models only; not a semantic certificate",
  "status": "passed",
  "unary": {
    "domain_sizes": [0, 1, 2, 3, 4],
    "unary_predicates": 31
  }
}
```

Uruchomienie przez recenzenta z katalogu głównego repozytorium:

```bash
python application/docs/review_evidence/lst02_finite_model_audit.py
```

## Granice wniosku

To **nie jest dowód dla wszystkich zbiorów, typów lub predykatów**:
weryfikacja obejmuje wyłącznie wymienione rozmiary skończone.
Również klasyczne wartościowanie boolowskie nie pokazuje
konstruktywnej prawdziwości pierwszego prawa negowania
kwantyfikatorów; źródło jawnie wymaga logiki klasycznej.
Algorytm nie kompiluje Lean i nie wystawia poświadczenia
zgodności Lean–LaTeX. Pozostaje użyteczną, odrębną od implementacji
Lean kontrolą próbek, także nieoczywistych przypadków pustych domen.

[CI 2+1 #45208224201](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45208224201)
zakończyło trzy niezależne techniczne rundy `PASS`
dla wskazanego commita, lecz
[issue #11](https://github.com/dariusz-piekarz/mathematical_scipts/issues/11)
nadal wymaga uwierzytelnionej, niezależnej **recenzji semantycznej**
wszystkich czterech mapowań LST-02. Nie zmieniono manifestu:
`needs_review`, `status=stabilizing`, `certificate=false`.
