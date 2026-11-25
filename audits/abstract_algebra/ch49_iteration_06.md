# AA-49 — audyt VI: kontrola techniczna i korekta redakcyjna

Stan wejściowy be5bb44433307b419b69f8f3a1f5773bd914b4a6. Źródło przed korektą redakcyjną 27cc7e691df663b74ab1b157982aba48298f70a5, regresja f0aefd798f77345e99291f689a3b0f7bb4dc72ea.

## Kontrole rzeczywiście wykonane
W lokalnym SymPy sprawdzono ogólną tożsamość H'+2theta H+2P L(P)=0 dla symbolicznych funkcji P, theta, q. Dla q=theta=0 i P=x²+a x+b potwierdzono H=a²-4b oraz siedem niezerowych wartości na dziewięciu punktach siatki. Cztery dodatkowe modele niekwadratowe: g=x(x-1), (x-2)/(x+1), (x²+1)/(x-3)², (x-2)³/(x+1)^4. Przy phi=-g'/(2g), q=g+phi'/2+phi²/4 i P=1 sprawdzono L(P)=0, H=4g, H'+2phi H=0, nieparzystą krotność czynnika i oba pierwiastki Riccatiego. Pierwsza próba bezpośredniego uproszczenia wyrażeń z pierwiastkami nie przeszła asercji SymPy; powtórzono rachunek dokładnie w bazie 1,w, w²=g, w'=g'/(2g) w: oba współczynniki wyrażenia r'+r²-q są zerowe dla każdego z ośmiu pierwiastków. PASS. Są to modele tożsamości, nie twierdzenie o pochodzeniu wszystkich danych z list lokalnych.

## CI i PDF
Run 45568093110, head 3a0d92c65ff75f0a61de3828410fcd09303cef35, job 139047732203: completed/success, 151 kroków success. Regresje AA-49 SymPy i Fraction, bramka globalna, latexmk, weryfikacja odsyłaczy, archiwizacja PASS. Pobrano artefakt 15001446403. PDF 444 strony, is_repaired=False. Obejrzano render wszystkich sześciu stron AA-49 (fizyczne 315–320, drukowane 301–306) i stronę tytułową; brak widocznych kolizji lub ucięć. Log bez dopasowań do błędów LaTeX, ostrzeżeń LaTeX i pakietów, Overfull/Underfull oraz undefined references. Nie sprawdzano wizualnie wszystkich pozostałych stron tomu.

## Dwie usterki redakcyjne
Uwaga aa:uw:kov2-computation nadal odwoływała się do eliminacji algebraicznej mimo zmiany dowodu na siatkę. Zastąpiono ją opisem 3^k punktów i zastrzeżeniem dotyczącym wydajności. Ostatnie zdania AA-49 zapowiadały utworzenie rozdziału AA-50, który już istnieje; zastąpiono je aktualnym wskazaniem AA-50. Commit 17d3fdf94bc02fae4800c9bd5755697ecae60510, blob eef209891803f0c33a3e139d4d9b93feecbe0c6c. Bez zmian twierdzeń, dowodów, etykiet i testów. Wcześniejszy PDF i CI nie obejmują tej ostatniej korekty. Nie uruchomiono Lean.

AA-49 pozostaje otwarty do potwierdzenia kompilacji po korekcie redakcyjnej i niezależnego audytu zamykającego. Nie otwierać AA-73.
