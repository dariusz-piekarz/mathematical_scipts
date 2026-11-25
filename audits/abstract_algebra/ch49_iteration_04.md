# AA-49 — audyt IV: stabilizacja po korekcie przekrojowej

Stan wejściowy e9bfc9a46c4430a0fa470f30da227460a218939e. Źródło 27cc7e691df663b74ab1b157982aba48298f70a5, test SymPy f0aefd798f77345e99291f689a3b0f7bb4dc72ea. Zakres: poprawiony dowód aa:tw:kov2-algorithm i regresja AA-49-FINAL-01.

## Kontrola dowodu

Ponownie odczytano pełny dowód algorytmu. Dla q=0 różniczkowanie 1/r dla r niezerowego daje 1; stałe algebraicznego rozszerzenia C(x) należą do C, więc nie ma ściśle kwadratowych rozwiązań. Dla q niezerowego klasyczne listy lokalne są skończone; odrzucenie ujemnego lub niecałkowitego stopnia jest poprawne. Układ liniowy na współczynniki unormowanego P jest skończony i nie dopuszcza P=0. Parametryzację przestrzeni rozwiązań można wyznaczyć eliminacją Gaussa nad efektywnym ciałem, a jej rozszerzenie skalarów do C opisuje wszystkie zespolone rozwiązania.

Ponownie rozwinięto H=P²(4q-2phi'-phi²) z phi=theta+P'/P. Wszystkie składniki podanego wzoru mają prawidłowe znaki. Równanie śladu daje H'=-2theta H; iloraz dwóch niezerowych H jest stałą w C(x), a więc niezerowym elementem C. Kwadratowość niezerowych wyróżników jest niezmienna w obrębie ustalonej kombinacji danych lokalnych. Nie stosuje się dzielenia przez zerowy H. Parametry afiniczne nie są zmiennymi różniczkowania względem x. H jest wielomianem łącznego stopnia najwyżej dwa, w szczególności stopnia najwyżej dwa w każdej zmiennej; dowód indukcyjny siatki {0,1,2}^k jest poprawny także dla k=0. Test siatki wykrywa świadek niezerowości, a nie bezpośrednio kwadratowość. Po znalezieniu świadka rozkład zredukowanego licznika i mianownika rozstrzyga kwadratowość nad C(x). Konieczność pozostaje uzależniona od jawnie cytowanego twierdzenia lokalnego. Nie znaleziono nowych usterek.

## Rzeczywiście wykonane kontrole lokalne

W Python/SymPy odtworzono rachunki i asercje testu test_14_finite_witness_and_square_class: PASS. Model q=2/x², theta=-2/x, P=x^6+a x³+b spełnia równanie liniowe; H=9x^4(a²-4b), dwa zera i siedem niezerowych wartości na dziewięciopunktowej siatce. Wszystkie siedem ma stały niezerowy iloraz względem x^4. Model q=(4x+5)/(16x²), theta=-1/(2x), P=x-1: H=x, stopień nieparzysty, transport PASS.

Niezależnie sprawdzono ogólną tożsamość H'+2theta H=-2P L(P), gdzie L jest operatorem liniowym z aa:eq:kov2-P-equation, dla dowolnych symbolicznych funkcji P(x), theta(x), q(x), bez zakładania równania L(P)=0. SymPy expand lewej strony po przeniesieniu składników dało dokładnie zero. Dwa przypadki kontrolne jednoelementowej przestrzeni z H=0: (q,theta,P)=(1,2,1) oraz (2/x²,4/x,1); w obu L(P)=0 i H=0. Są to modele tożsamości, nie twierdzenie, że obie trójki pochodzą z list lokalnych. Nie uruchomiono lokalnie pełnego pliku unittest z drzewa repozytorium; odtworzono jego nowy test i dodatkowe obliczenia. Nie dodawano redundantnego testu do CI, istniejąca regresja pozostaje wersjonowana.

## CI i werdykt

Run 45568011888: 37 kroków success, 1 aktywny, 112 pending; run 45568064133: 35 success, 1 aktywny, 114 pending. W obu bramka globalna, regresje AA-49 i kompilacja jeszcze oczekują. Nie zweryfikowano nowego PDF i nie uruchomiono Lean. Bez zmian matematycznego źródła i testów w tej iteracji.

Audyt IV czysty w badanym zakresie, ale AA-49 nie jest jeszcze zamknięty. Następny etap: potwierdzić CI aktualnej regresji, obejrzeć wszystkie strony AA-49 nowego PDF, wykonać niezależny audyt kontrolny. Nie kontynuować rozbudowy ani otwierać AA-73. Audyt przekrojowy całego tomu pozostaje otwarty.
