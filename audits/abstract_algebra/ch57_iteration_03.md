# AA-57 — audyt III: szeregi, derywacje i algebry macierzowe

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6.
Commit źródłowy 8b9b02e4c3eaa41ac8e6096a4df421ba21de6b3d, blob a64577b1841a14ea92d6ed08de7db6248684be76.

## Kontrola i korekty
Sprawdzono komutator i tożsamość Jacobiego, klasyczne algebry (w szczególności warunek blokowy symplektyczny), ilorazy, reprezentacje i derywacje, oba szeregi i przykłady trójkątne. Uściślono ciało i rozmiar macierzy, jawnie wykazano sp2=sl2 i równoważność definicji reprezentacji przez działanie, wskazano normę oraz zupełność przestrzeni operatorów przy eksponencie, rozpisano współczynnik szeregu odwrotnego i cały krok indukcyjny uogólnionej reguły Leibniza. W dowodzie własności szeregów rozpisano zawieranie nawiasu ideałów w ich przecięciu, oba kroki indukcji i zastosowanie Jacobiego dla par (i,j), (i,j+1). Jawnie powiązano szereg pochodny b_n z szeregiem pochodnym n_n. 12 korekt fragmentów, 840 wierszy. Brak nowych tematów. Środowiska zrównoważone.

## Wykonane niezależne regresje
Kod JavaScript na indeksach jednostek macierzowych: dla n=1,...,24 iterowano nawiasy przestrzeni macierzy trójkątnych, korzystając z reguły mnożenia jednostek macierzowych. W nawiasach górnotrójkątnych nie pojawia się niezerowa przekątna; dla każdej pary jednostek niezerowy nawias jest pojedynczą jednostką z ewentualnym znakiem minus. Weryfikowano dokładną równość zbiorów indeksów kolejnych przestrzeni. Dolny szereg centralny n_n ma wyrazy F_k, szereg pochodny b_n ma dla k>=1 wyrazy F_(2^(k-1)). 437/437 porównań wyrazów szeregów. Dodatkowo 65780/65780 sprawdzeń konstrukcji jednostki E_ij w nawiasie [F_r,F_s] jako [E_(i,i+r),E_(i+r,j)] dla j-i>=r+s, r,s>=1. Są to skończone regresje, nie zastępują dowodu ogólnego. Formuła na szereg pochodny i pełna równość filtracji w tym zakresie stanowią niezależne sprawdzenia, nie dodano nowych twierdzeń do rozdziału.

## CI
Run po audycie II 45363333694: in_progress, kroki {"success":35,"in_progress":1,"pending":87}. Nowy run: [{"id":45363665637,"status":"in_progress","conclusion":null}]. Bez oględzin PDF.

## Werdykt
AA-57 W AUDYCIE. Ze względu na korekty III licznik czystych audytów 0/2. Następnie niezależna kontrola derywacji, reprezentacji oraz ponowna kontrola dowodów Engela i Liego. AA-58 nieotwarty.
