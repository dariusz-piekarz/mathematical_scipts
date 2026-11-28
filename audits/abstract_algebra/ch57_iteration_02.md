# AA-57 — audyt II: indukcja Engela i Liego

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Commit źródłowy 2dd51b38a9e6426235758b94d22ae033ff65893e, blob 99abd725f79020a085ccbddad170f9afbc145332.

## Kontrola dowodów
Przejrzano dowód Engela: indukcja po wymiarze algebry operatorów, wybór maksymalnej właściwej podalgebry, działanie na ilorazie przestrzeni wektorowych (przed wykazaniem własności ideału), nilpotentność operatorów indukowanych, normalizator, kowymiar jeden, niezerowe wspólne jądro. Uzupełniono dobrze określone działanie i jawne sprawdzenie warunku reprezentacji, wzór na potęgę operatora indukowanego, argument maksymalności normalizatora oraz przypadek zerowy i indukcję w abstrakcyjnym twierdzeniu. Sformułowanie wniosku o fladze zawiera teraz jawne założenia, także dla V=0.

W dowodzie Liego sprawdzono wybór ideału kowymiaru jeden, indukcję dla wszystkich elementów tego ideału, przestrzeń cykliczną, ślad ograniczenia komutatora i dzielenie przez dodatni wymiar w charakterystyce zero. Rozpisano drugi składnik indukcji i niezmienniczość przestrzeni cyklicznej względem T. Jawnie wykazano, że funkcjonał wspólnego wektora własnego znika na algebrze pochodnej, co jest konieczną własnością reprezentacji jednowymiarowej. Uściślono założenia wniosku o trójkątności i zastosowanie do reprezentacji dołączonej. W kontrprzykładzie w dodatniej charakterystyce rozpisano zamkniętość i dokładną algebrę pochodną. Łącznie 13 korekt fragmentów, 796 wierszy. Nie zmieniono zakresu ani innych rozdziałów.

## Niezależna regresja
Kod JavaScript z BigInt: dla standardowego nilpotentnego bloku Jordana X rozmiaru n=1,...,10 sprawdzono (ad_X)^(2n-1)(E_ij)=0 na wszystkich jednostkach macierzowych, 385/385 przypadków. Dla p=2,3,5,7,11,13,17,19,23,29,31 wygenerowano macierze mnożenia przez t i różniczkowania na K[t]/(t^p), sprawdzono [Y,X]=I modulo p, 11/11 przypadków. To kontrola wzoru i kontrprzykładu, nie zastępuje dowodów twierdzeń.

## Integralność i CI
Wszystkie 13 wystąpienia odsyłaczy do 11 różnych celów jednoznaczne w AA-56–57, środowiska zrównoważone. Pierwszy CI 45362612008: completed, kroki {"success":124}. CI po korektach: [{"id":45363333694,"status":"in_progress","conclusion":null}]. Nie oglądano PDF.

## Werdykt
AA-57 W AUDYCIE. Czyste niezależne audyty po II: 0/2. Następnie niezależna kontrola szeregów, klasycznych algebr, reprezentacji i derywacji. AA-58 nieotwarty.
