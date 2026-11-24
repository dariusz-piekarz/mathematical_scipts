# AA-57 — audyt IV: niezależna kontrola derywacji i ponowny audyt twierdzeń

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Źródło: blob a64577b1841a14ea92d6ed08de7db6248684be76, commit 8b9b02e4c3eaa41ac8e6096a4df421ba21de6b3d.

## Wykonane obliczenia
Niezależny kod JavaScript BigInt dla algebry Heisenberga w bazie x,y,z, [x,y]=z. Macierze derywacji wprowadzono przez sześć parametrów całkowitych: D(x)=a x+b y+c z, D(y)=d x+e y+f z, D(z)=(a+e)z. Dla sześciu macierzy bazowych i wszystkich par ich komutatorów sprawdzono warunek derywacji na dziewięciu parach wektorów bazowych: 378/378 kontroli (54 dla samych macierzy bazowych, 324 dla komutatorów). Wszystkie 36 komutatorów są derywacjami. Dla każdej z sześciu macierzy i trzech wektorów bazowych sprawdzono [D,ad_x]=ad_(Dx): 18/18. Następnie dla 75 macierzy z parametrami a,b w {-2,-1,0,1,2}, c w {-1,0,1}, d=b-1,e=a+1,f=-c sprawdzono niezależnie przez iterowane potęgowanie D uogólnioną regułę Leibniza dla k=0,...,8 i wszystkich dziewięciu par bazowych: 6075/6075. Wszystko dokładne, bez arytmetyki zmiennoprzecinkowej. Kontrole nie są dowodem ogólnym ani deklaracją dodania klasyfikacji derywacji Heisenberga do tekstu.

## Kontrola dowodów
Ponownie prześledzono argument Engela: poprawna indukcja jednocześnie dla wszystkich przestrzeni, działanie mniejszej algebry na niezerowym ilorazie przestrzeni liniowych, normalizator, własność ideału i kowymiar jeden, niezerowe wspólne jądro, niezmienniczość i nilpotentność ograniczenia. Flaga wynika przez indukcję po wymiarze reprezentacji, twierdzenie abstrakcyjne przez ograniczenie kolejnych wyrazów szeregu centralnego. W dowodzie Liego sprawdzono ideał kowymiaru jeden, przestrzenie W_j, równoczesną indukcję dla wszystkich y w ideale, bazę przestrzeni cyklicznej, ślad komutatora ograniczeń, wykorzystanie charakterystyki zero i algebraicznej domkniętości w odpowiednich miejscach, działanie na U i końcowy funkcjonał. Ponowne sprawdzenie reprezentacji dołączonej, derywacji i dowodu eksponenty nie ujawniło nowej luki. Zakres bez zmian. Wszystkie 13 odsyłacze jednoznaczne w AA-56–57; środowiska zrównoważone.

## CI
Run 45363665637, job 138339753759, in_progress, kroki {"success":7,"in_progress":1,"pending":115}. Bez oględzin PDF w tej iteracji.

## Werdykt
Pierwszy czysty audyt po korektach III: 1/2. AA-57 W AUDYCIE. Następna iteracja: kontrola przykładów klasycznych, przypadków brzegowych i języka, pełne CI oraz PDF jeśli dostępny. AA-58 nieotwarty.
