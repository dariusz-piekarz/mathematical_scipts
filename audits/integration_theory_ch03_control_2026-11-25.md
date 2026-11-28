# IT-03 — niezależna kontrola po poprawkach

Sprawdzone źródło: 9a39741c2269b7969ae2b20fb7fb168700953fad (commit 6a1c0ed613dc22c3adb44a25f8099a325a66bd5b). Testy rozdziału: dd226d7af42b497dc1192c736f868a1b3fedcd08, 9 metod. Kryteria: 416e2f8d8ed9d0da15968f614cb9f4b57c23c62a (12 kryteriów).

Ponowna kontrola matematyczna i szczegółowości:
- Definicja, jednoznaczność, addytywność wahania, przypadki końcowe; oszacowania sum po zagęszczeniu i zupełność R.
- BV bez wspólnych nieciągłości: prawostronna i lewostronna ciągłość V, skończoność D_r, kontrola wariacji na rozłącznych wnętrzach, całkowanie przez części.
- Lokalność, sklejanie przy jednej funkcji ciągłej, kontrprzykład wspólnego skoku.
- Kryterium oscylacyjne: pokrycia otwarte, liczba Lebesgue'a, atomy, końce a i b, uzupełnienie miary, granice funkcji schodkowych. Stałe przedłużenie integratora jest prawostronnie ciągłe i nie generuje atomu w a.
- Jeden skok: wybór u_n,v_n działa również dla t_n=c i c=b. Wzory dla skończonej liczby skoków i oszacowanie kwadratury.
- Podstawienie: usunięcie zerowych komórek, zachowanie znaczników przy odwróceniu, ciągłość odwrotności, addytywność i wariacja G, jednostajna kontrola błędu, zgodność przykładów.

W sprawdzonym zakresie brak nowych istotnych luk i nie zmieniano źródła. Testy automatyczne w CI 45621624236 (job 139231002695, SHA 2018da579299e4861d19f84635ea8b87e7f230ea) mają krok Regression tests SUCCESS, w tym 9 metod IT-03; kompilacja i artefakt w momencie odczytu jeszcze oczekują. Nie przypisujemy aktualnej wersji rezultatu starszego PDF. Lean i kontrola wizualna PDF nie zostały wykonane. Stabilizacja matematyczna: kontrola bez nowych uwag; techniczna pozostaje otwarta do końcowego CI i kontroli wizualnej.
