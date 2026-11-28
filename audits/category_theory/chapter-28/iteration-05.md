# CAT-28 — audyt kontrolny (27.11.2026)

## Tożsamość badanego materiału
- Kandydat CI: `b604a2253f87883373b87b6131d1d0ab1082386b`.
- Blob rozdziału: `86a934bc33ac8bc58a2a594a65d401b3108b741d`; blob dedykowanych testów: `9fa36b84415adb7daec6cb29d390a4737c6f2bb2`. Oba niezmienione względem kandydata podczas kontroli.
- Poprzednie poprawki: 8d0c1043, 9c605d75, d2ecab50, 36c9b08c, e671c6a6, b604a225. Zachowano etykiety.

## Kontrola matematyczna
- Ponownie sprawdzono 13 dowodów, w tym typy morfizmów i kolejność składania dla komonady sprzężenia, koalgebry koswobodnej, ko-Kleisliego, obu funktorów porównawczych, prezentacji kanonicznej i obu implikacji twierdzenia Becka. Sprawdzono użycie epimorficzności rozszczepionej, odzwierciedlania izomorfizmów oraz kryterium równoważności w przyjętym uniwersum.
- Sprawdzono dualizację, przykłady grup, ograniczenia skalarów, kategorii nad zbiorem (również pustym) i kontrprzykłady. Nie znaleziono nowych usterek wymagających zmiany źródła.
- Odrębny test obliczeniowy JS, niekopiujący pięciu istniejących regresji: monada C2 × (-) i jej algebry jako działania grupy C2 na zbiorach 0–3 elementowych. Osiem działań, osiem prezentacji kanonicznych, 615 kandydatów na morfizmy i 159 faktoryzacji; wszystkie sprawdzane równości oraz równoważność warunku morfizmu algebr i koequalizowania spełnione. To test modeli skończonych, nie formalizacja ogólnego dowodu.
- 25 etykiet, 38 wystąpień odsyłaczy, 6 diagramów; poprzednia kontrola odsyłaczy i struktury PASS.

## Walidacja techniczna
- [CI #45966587903](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45966587903) na wskazanym kandydacie: 198 testów teorii kategorii, 5 dedykowanych CAT-28, wszystkie PASS; kompilacja pełnej książki (198 stron) i końcowa bramka odsyłaczy PASS.
- [Artefakt PDF](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45966587903/artifacts/15183445854). Poprzednia iteracja odnotowała kontrolę wizualną stron CAT-28.
- Nie wykonano nowej kompilacji ani niezależnej recenzji człowieka w tej iteracji. Kontrolę wykonał asystent w osobnym przebiegu, nie niezależny recenzent zewnętrzny. Pełne CI aplikacji dla najnowszych zmian pozostaje w toku; nie przypisujemy wyniku innego SHA całemu HEAD.

## Decyzja
Drugi czysty przegląd merytoryczny po ostatniej zmianie. CAT-28 zamknięty w ramach roboczych audytów asystenta; nie jest to certyfikat formalny Lean ani zewnętrzna recenzja. Nie zmieniano źródła ani testów. Następny rozdział zgodnie z kolejką zaawansowanej teorii kategorii; sprawdzić plan przed dodaniem CAT-29.
