# CAT-10 — regresje

| ID | Kryterium | Metoda |
|---|---|---|
| CAT-10-001 | Ewaluacja kowariantna | Enumeracja skończonych reprezentowalnych funktorów |
| CAT-10-002 | Ewaluacja kontrawariantna | Enumeracja rodzin |
| CAT-10-003 | Naturalność w obiekcie | Kompozycje map |
| CAT-10-004 | Naturalność w funktorze | Kompozycje map |
| CAT-10-005 | Operacje na krotkach | Enumeracja wyboru współrzędnych |
| CAT-10-006 | Funktor potęgowy | Obrazy singletonów i zbioru pustego |
| CAT-10-007 | Operacje grupowe | S3 i sprzężenia |
| CAT-10-008 | Struktura | Etykiety i środowiska |
| CAT-10-009 | Wszystkie rodziny naturalne dla kategorii jednej strzałki | Enumeracja dowolnych składowych i filtracja naturalności |
| CAT-10-010 | Yoneda dla dowolnych działań monoidu idempotentnego | Enumeracja wszystkich funkcji i działań |
| CAT-10-011 | Klasyfikacja operacji binarnych | Enumeracja wszystkich funkcji na dwuelementowym zbiorze |

python3 -m unittest discover -s tools/tests -p 'test_category_theory_ch*.py' -v. Testy skończone nie zastępują dowodów.
