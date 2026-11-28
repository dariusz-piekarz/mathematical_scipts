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


## Odporność audytora na Python -O/-OO (2026-11-23)

Dodatkowy audyt narzędzia ujawnił, że **pierwotna wersja**
[`lst02_finite_model_audit.py`](https://github.com/dariusz-piekarz/mathematical_scipts/blob/29cc379f94771393ba15196a938ddf6d07b1c8bd/application/docs/review_evidence/lst02_finite_model_audit.py)
używała instrukcji `assert`, które interpreter usuwa przy `python -O`
lub `python -OO`. W takim trybie wcześniejsza wersja mogła
raportować `PASS` bez kontroli równoważności.

[Commit `75fc7acd`](https://github.com/dariusz-piekarz/mathematical_scipts/commit/75fc7acd8d7c08f6384ad04afd558b6570291a07)
wprowadza `require` i jawny wyjątek `FiniteModelAuditError`
zamiast optymalizowalnych asercji, sprawdza pełne liczby modeli
**31 / 689 / 201** i odrzuca **trzy świadomie fałszywe twierdzenia**
(pozornie wzmocnione prawo de Morgana, zignorowaną jednoznaczność,
fałszywą odwrotność mieszanej implikacji). Dodano **5 testów**
regresyjnych, w tym osobne wykonanie programu w trybach
zwykłym, `-O` i `-OO`.

Zgodność dokładnych bajtów plików w repozytorium z lokalnie
testowanymi potwierdzają bloby Git:
- audytor: `edc49416319d6c105ef76329e3f24f4bbc4667ba`;
- testy: `2c743967697ab30e1a79c5d894ad87ea1c527a18`.

[Osobny workflow CI #45225501675](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45225501675)
`completed/success`: 5/5 testów `PASS` w każdym
z trzech trybów Pythona, identyczne JSON-y, trzy fałszywe
twierdzenia odrzucone i `certificate=false`.
[Artefakt JSON z trzech uruchomień](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45225501675/artifacts/14840744460),
SHA-256 archiwum:
`f3a0adcba6320a935e5b2515f52ffbc8aa6dcc0dc212bd4627a445f890226653`.

Powtórzenie poza CI:

```bash
python -m unittest discover -s application/docs/review_evidence -p 'test_lst02_*.py' -v
python -O application/docs/review_evidence/lst02_finite_model_audit.py
python -OO application/docs/review_evidence/lst02_finite_model_audit.py
```

To wyłącznie diagnostyczny audyt skończonych modeli. **Nie**
zmieniono czterech formalizacji LST-02, ich statusów
`needs_review`, manifestu ani weryfikowanego SHA kodu Lean
`163c8f6415d9d390fc1a737f6954b2865eff6c6e`. Historia 3/3
dla tego SHA nie stanowi aprobaty semantycznej.
