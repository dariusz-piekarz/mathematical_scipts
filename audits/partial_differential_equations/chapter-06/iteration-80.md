# PDE-06 — iteracja 80: druga lektura 6.3–6.4

Data: 2026-11-25. Źródło 4adf037b29fc0e09a95fb435557bde958b761d09, rejestr 6293e2798c2b66b9a7fd126670bea0988b76ba00, testy ccbb8b39902904365b1403df5eefa10ff40d2134. Druga kontrola semantyczna, bez rozszerzania materiału.

| ID | Wynik | Uzasadnienie |
|---|---|---|
| PDE-06-011 | PASS | Nietrywialny iloczyn zapewnia istnienie osobnych punktów niezerowych, równanie dla X i T obowiązuje również w zerach; Dirichlet wymusza dodatnie lambda_n. |
| PDE-06-012 | PASS | Nieparzyste okresowe przedłużenie ciągłe dzięki obu zerowym końcom. Masa Gaussa 1, parzystość i okresowość dają zerowanie w 0,L; ogon po skalowaniu zmierza do zera z całkowalności. |
| PDE-06-013 | PASS | Na pełnym okresie przesunięcia mają dolną granicę odległości (2 abs(j)-1)L, więc majoranta jest sumowalna. Współczynnik jądra znormalizowany przez 2L, splot bez tej normalizacji; Fubini uzasadniony. Różniczkowanie transformaty Gaussa i całkowanie przez części dają znak minus i czynnik 2 kappa t xi. |
| PDE-06-014 | PASS | Pochodne r przestrzenne i s czasowe mają majorantę stała razy n^(r+2s) exp(-a n² delta), sumowalną dla delta>0. Identyfikacja współczynników, zupełność i ciągłość dają u=Q_tg. Granica jednostajna i ciągłość g dają ciągłość łączną przy t=0. Jednoznaczność wynika z thm:pde4-max dla części rzeczywistej i urojonej; można stosować na dowolnym skończonym cylindrze. |
| PDE-06-015 | PASS | Norma kwadratowa szeregu sinusowego zawiera L/2; wyjęcie czynnika dla najmniejszej lambda i pierwiastkowanie dają właściwy wykładnik. Pierwszy sinus osiąga równość. |
| PDE-06-016 | PASS | Dwa mnożniki dla nieujemnych czasów należą do [0,1], więc ich różnica w module jest co najwyżej 1; Parseval i sumowalna majoranta dają ciągłość L². Cauchy–Schwarz daje wspólną majorantę na t≥delta, obejmując wszystkie pochodne i sam szereg. Nie przypisuje się wartości punktowych danym w t=0. |
| PDE-06-017 | PASS | Równanie oscylatora po wyborze niezerowej wartości funkcji przestrzennej; omega_n>0, pochodna składnika sinusowego w t=0 daje b_n. |
| PDE-06-018 | PASS | Wspólny zanik przy końcach zapewnia gładkość przedłużeń; zanikanie współczynników z lem:pde6-decay, majoranta n^(r+s-m), zbieżność jednostajna. Dane początkowe z identyfikacji granic w L² i ciągłości. |
| PDE-06-019 | PASS | Różniczkowanie kwadratów modułów daje części rzeczywiste; wyrazy objętościowe znoszą się przez sprzężenie i równość pochodnych mieszanych. U_t=0 na brzegu, strumień zerowy. Zerowa energia różnicy i zerowy brzeg dają jednoznaczność w klasie C². |
| PDE-06-020 | PASS | Ortogonalność sinusów i kosinusów dla skończonych sum daje L/4, przejście przez jednostajną zbieżność pochodnych. Wyrazy mieszane w energii oscylatora znoszą się; pozostają kwadraty modułów z właściwą wagą omega_n². |
| PDE-06-021 | PASS | Pojedynczy sinus spełnia równania i warunki bez użycia założenia o zwartym nośniku. Przy t=2L/c argument kosinusa jest 2 pi n; kontrast z zanikiem gaussowskim dotyczy ewolucji, nie twierdzenia o regularności dla każdej pojedynczej chwili. |

Nie wykryto nowych błędów matematycznych ani istotnych luk w 6.3–6.4. Nie zmieniono źródła, rejestru ani testów. Zweryfikowano również treść zasady maksimum thm:pde4-max w rozdziale 04; stosowana klasa rozwiązań jest odpowiednia na skończonym cylindrze.

Po korekcie Markdown z iteracji 79 przebieg 45572681202 dla commitu ddbeb74dd3a8c5e6154095ecd04aa9750cf261af: completed/success, job 139062917083. Log: Ran 10 tests in 0.176s, OK; 42 criterion anchors verified (not executed proofs); 38 distinct labels; 52 resolved reference occurrences; 16 stron. Wszystkie kroki kompilacji, diagnostyki, renderowania i publikacji zaliczone. Artefakt 15002034381. Nie wykonano ponownych ręcznych oględzin tego artefaktu; wcześniejsze oględziny w iteracji 78 dotyczą identycznego źródła TeX. Nie wykonano Lean ani kompilacji całego tomu.

Druga lektura 4/9 sekcji, 21/42 kryteriów (łącznie z iteracją 79). Następna iteracja 81: 6.5–6.6, Duhamel oraz regularne zagadnienie Sturma–Liouville'a. Stabilizacja i niezależny audyt kontrolny nadal otwarte.
