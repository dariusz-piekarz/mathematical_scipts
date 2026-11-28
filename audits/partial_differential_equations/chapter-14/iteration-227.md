# RRC 14 — iteracja 227: druga lektura 021–032

Źródło przed f8d608fbb8c50561f060c95700c27b1e1f3714de, po e1e17ce02ad6bbe611591b156c3acb872d95975a (be1c642aa9d9b1c5faddfb9cfa38330ea5a7c337), następnie 7c52d4faadd3b91ba04397b6cc5d3c0ec90095b8 (7f7c4a2503ebce7f1493987220b491e3b3ba9be3). Przejrzano sekcje 4–5 i rzeczywiste tezy RRC 03 o Poissonie, Harnacku, gradiencie i Liouville'u.

| Kryterium | Druga lektura |
|---|---|
| 021 | Jawny warunek R>0 i zgodność normalizacji z RRC 03. |
| 022 | Reprezentacja z danych brzegowych przez jednoznaczność — poprawna. |
| 023 | Osłabiono zbędne założenie harmoniczności poza domkniętą kulą do ciągłości na domknięciu; jawnie uzasadniono nieujemność danych. Iloraz i monotoniczność stałych poprawne. |
| 024 | Stała ((R+r)/(R-r))^d i przypadek u=0 bez dzielenia przez u — poprawne. |
| 025 | Przejście przez mniejsze kule, granica samych stałych — poprawne; dostosowano sformułowanie uwagi do nowej tezy. |
| 026 | Spójność łamaną przez lokalną wypukłość kul i zbiór otwarty/domknięty — poprawne. |
| 027 | Odległość od dopełnienia, przypadek całej przestrzeni i podział parametru łamanej — poprawne. |
| 028 | Jawna translacja Harnacka i przynależność obu punktów do kuli wewnętrznej; skończone podpokrycie i niezależność od u poprawne. |
| 029 | Rozpisano granicę obu stałych Liouville'a w postaci bezwymiarowej. |
| 030 | Zbieżność zmajoryzowana, różniczkowanie jądra i rachunek gradientu poprawne. |
| 031 | Osłabiono hipotezę gradientową do ciągłości na domknięciu; przeniesiono mocniejszą stałą d/(R-r) do tezy, rozpisano geometrię kuli o promieniu R-r. |
| 032 | Przeniesiono oszacowanie pochodnych dowolnego rzędu do tezy, zdefiniowano kolejność różniczkowania, jawnie zapisano każdy krok iteracji. |

10 zamian blokowych w części matematycznej oraz jedna zmiana rysunku. 1270 → 1290 wierszy, 34 etykiety zachowane, stos środowisk poprawny; 66/66 odsyłaczy (41 celów) jednoznacznie rozwiązanych w dziewięciu rozdziałach RRC na przypiętym commicie. Pierwsza lektura 64/64, druga 32/64 (nieczysta).

Rysunek Hopfa: dokładny blok TikZ z repozytorium skompilowano lokalnie w samodzielnej otoczce standalone z arrows.meta za pomocą pdflatex, następnie wyrenderowano PDF do PNG i sprawdzono wizualnie. Etykieta R/2 stykała się z wewnętrznym okręgiem; zmieniono położenie na pos=0.42 i font=small, ponownie skompilowano i obejrzano render bez tego nakładania. To nie jest kompilacja całego skryptu ani potwierdzenie działania backendu aplikacji. Rysunek RRC 02 pozostaje do kontroli.

CI dla wcześniejszego commitu 9df3a04660a931e9f074ac0ab05319b879549ba6: wszystkie pięć zwróconych przebiegów zakończone success (45719021210, 45719021101, 45719013749, 45719013504, 45719013432); workflow PDE dotyczy rozdziału 13, nie dedykowanej walidacji 14. Dla aktualnego commitu 7f7c4a2503ebce7f1493987220b491e3b3ba9be3 pięć przebiegów oczekuje na wykonanie; pełnego PASS dla obecnej wersji nie potwierdzono.

Następna iteracja 228: druga lektura 033–044 (subharmoniczność, Hopf dla superharmonicznych, Caccioppoli). Dalsza stabilizacja i audyt kontrolny, pełna kompilacja oraz kontrola aplikacji pozostają otwarte.
