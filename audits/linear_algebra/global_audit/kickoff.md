# Algebra liniowa — globalny audyt, kontrola startowa (nie jest iteracją 01–09)

**Data:** 22 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Źródło repozytorium:** `dariusz-piekarz/mathematical_scipts`  
**Automatyzacja:** 9 cogodzinnych iteracji, 01:00–09:00 czasu `Europe/Warsaw`, 22 listopada 2026.

## Wykonane kontrole
1. Przeczytano katalog `catalog/books.json` i plik główny `books/pl/linear_algebra.tex`: dokładnie **32** wpisy rozdziałów i **32** instrukcje `\input`.
2. Pobrano i automatycznie przeanalizowano źródła **wszystkich 32 rozdziałów**, sprawdzając wystąpienia `\label`, `\ref`, `\eqref`, `\begin{proof}`, `\end{proof}` oraz wybrane wyrażenia terminologiczne. We wszystkich plikach liczby początków i końców środowiska `proof` są równe. Jest to test SKŁADNI, a nie ocena matematycznej kompletności dowodów.
3. W rozdziale 01 osiem wystąpień ciągu `unia` znajduje się w HISTORYCZNYCH etykietach `\label` lub argumentach `\ref`, nie w treści prozy; zgodnie z zasadą zachowania odsyłaczy pozostawiono je bez zmian. Tytuły i zdania używają `suma zbiorów`.
4. W rozdziale 22, w dowodzie równoważności iniektywności, surjektywności i zerowości jądra operatora na przestrzeni skończenie wymiarowej, rzeczywisty błąd pisowni `injektywność` zmieniono na **`iniektywność`**. Nie zmieniono rozumowania matematycznego.
5. Pozostałe przeskanowane fragmenty nie wykazały kolejnych trafień w zbiór zakazanych wyrazów `tensorowani...`, `sekwencj...`, `karta` w kontekście chart, `seskw...` ani `unia` w prozie; wynik nie oznacza jeszcze pełnego audytu językowego.

## Stan CI
Ostatnie potwierdzone przejście workflow `Linear algebra chapter validation` dla źródła skryptu sprzed tej korekty: **SUCCESS**, uruchomienie `44961002573`, commit `d59cf8e1f3de04477beffb4645b7d6c3bb2efd34`.
**Nie deklarujemy** jeszcze wyniku CI dla nowej korekty: wymaga osobnego przebiegu.
Bieżący HEAD może zawierać współbieżne zmiany innych skryptów; każde wypchnięcie wymaga `expected_sha`.

## Status 9 właściwych iteracji audytu
| Iteracja | Rozdziały / zakres | Status po kontroli startowej |
|---|---|---|
| 01 | 01–04 | do szczegółowego audytu |
| 02 | 05–08 | do szczegółowego audytu |
| 03 | 09–12 | do szczegółowego audytu |
| 04 | 13–16 | do szczegółowego audytu |
| 05 | 17–20 | do szczegółowego audytu |
| 06 | 21–24 | do szczegółowego audytu; ch22: korekta językowa do ponownej weryfikacji |
| 07 | 25–28 | do szczegółowego audytu |
| 08 | 29–32 | do szczegółowego audytu |
| 09 | cała książka, zależności i PDF | do końcowego audytu |

Każda iteracja ma rzeczywiście sprawdzić dowody, wzory, przykłady, ilustracje, język, odsyłacze, LaTeX i CI zgodnie z `AGENTS.md` i standardami repozytorium. Sam status wcześniejszych audytów lokalnych **nie** jest równoznaczny z wynikiem tej nowej kontroli globalnej. Globalnego audytu nie uznajemy za zakończony przed wykonaniem wszystkich dziewięciu iteracji i zweryfikowaniem wyników.
