# Algebra liniowa — rozdział 22, audyt IV (kontrola składu)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/22-rownania-sylvestera-i-lapunowa.tex`  
**Wersja po korekcie:** `11aafed28081c5db85005cf235f51b6795710705`  
**Poprzednie iteracje:** I — utworzenie, II — odsyłacze i pozytywność, III — matematycznie czysty.

## Wynik kontroli

1. Nowe testy Sylvestera nad `F2,F3`, w tym porównanie jądra `AX-XB` z sumą NWD czynników niezmienniczych i test zamkniętej formuły, **przeszły** we wszystkich aktualnie uruchomionych kontrolach do etapu kompilacji.
2. Zestaw regresji rozdziałów 01–21 również przeszedł; struktura źródeł i odsyłaczy po korekcie etykiety rozdziału 18 jest spójna.
3. Kompilacja LaTeX była możliwa i dawała PDF, ale kontrola logu odrzucała **Overfull hbox 0.28943 pt** z akapitu wejściowego Twierdzenia o rozwiązaniu przez wielomian charakterystyczny (wiersze 314–319). To rzeczywista usterka składu, nie matematyki.
4. Usunięto nadmiernie długi wiersz, zastępując dwa zapisy typów macierzy krótkim, jednoznacznym opisem: `A` stopnia `n`, `B` stopnia `m`, obie nad `K`, `n,m≥1`, `gcd(chi_A,chi_B)=1`. Wszystkie kwantyfikatory i założenia pozostały jawne.
5. W dowodach i przykładach nie wykryto nowego problemu matematycznego; nie dodawano nowych twierdzeń ani przykładów.

## Decyzja

**Audyt IV wymagał korekty technicznej**; nie uznajemy go za czysty. Konieczne kolejne czyste audyty po pomyślnym końcowym CI z PDF. Aktualny commit poprawy: `d46d8e6299bb1b02daa15d293993390cd6d381bc`.
