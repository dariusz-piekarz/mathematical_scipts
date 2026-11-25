# CAT-03 — audyt II (stabilizacyjny)

Stan badany: c0972bac19ea2d38aece68e4404f29c3b903dbc3.
Źródło: 7722d3d50755970a91bfac2910a6e037a036a8f8.
Testy CAT-03: a5a9d1042dccab19711abddab838c86e4cc76708.

## Kontrola semantyczna
- Kowariancja i kontrawariancja: identyczności i kolejność składania poprawne. Potęga symetryczna: istnienie przez własność uniwersalną, równość na generatorach. Działania grup: jednostka z F(id), odwrotność z F(g^{-1}), kolejność zgodna z lewym działaniem.
- Składowe spójne: obraz niepustego zbioru spójnego należy do jednej składowej, co daje zgodność składania; dla pustej przestrzeni brak składowych. Przejrzano wszystkie 19 rozdziałów CAT pod kątem pi_0 i składowych; brak innych wystąpień wymagających migracji. Konwencja pi_0 dotyczy klas połączonych drogą, zgodnie z tekstem. Nie jest to przegląd wszystkich tomów biblioteki.
- Wierność i pełność: wierność odzwierciedla mono/epi; pełność wraz z wiernością odzwierciedla izomorfizmy przez podniesienie odwrotności. Kontrprzykłady poprawne. Zachowanie rozszczepień przez funktor wynika z aksjomatów.
- Hom: typy a:A'→A, b:B→B' oraz u:A→B poprawne; złożenie w pierwszym argumencie odwrócone. Identyczności i oba funktory częściowe poprawne.
- Tensor: dwuliniowość nad pierścieniem przemiennym, faktoryzacja przez własność uniwersalną; sprawdzenie na generatorach. Mnożenie przez 2 po tensorze z Z/2 jest zerowe na niezerowym module.
- Spec: kontrakcja ideału pierwszego jest właściwym ideałem pierwszym, ponieważ homomorfizm zachowuje jedynkę; przeciwobraz D(r) to D(phi(r)). Kolejność kontrakcji poprawna. Nie utożsamiono samej przestrzeni topologicznej ze schematem.
- Homologia: morfizm kompleksów zachowuje cykle i brzegi, więc jeśli x-x' jest brzegiem, f_n(x)-f_n(x') jest brzegiem. Działanie na ilorazie zachowuje składanie i identyczność.
- Formy i de Rham: reguła łańcuchowa daje odwróconą kolejność cofnięć; zgodność z różniczką zewnętrzną przywołana z DG-10. Cykle i brzegi zachowane, zatem przejście do kohomologii poprawne.
- Odsyłacz sec:naturalne istnieje w CAT-04. Nie wykryto nowych istotnych usterek; bez zmian źródła i bez rozszerzania zakresu.

## CI
Przebieg https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45577302560, commit 112ede03252d8cb9645b2e844ca35e80e7220f44. Porównanie 25 blobów (19 rozdziałów, książka, 4 zestawy testów, workflow) bez różnic. Krok testów: success (4+5+5+6 metod). Job validate zakończony success, w tym kompilacja, kontrola PDF i odsyłaczy oraz upload.
Nie odczytano pełnych logów ani nie obejrzano PDF. Nie wykonano formalizacji Lean.

## Decyzja
Kontrola matematyczna i regresje zaliczone. Bramka CI zaliczona. Kolejna iteracja: niezależny audyt III i kontrola PDF, przed CAT-04.
