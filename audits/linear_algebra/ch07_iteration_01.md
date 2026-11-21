# Algebra liniowa — rozdział 07, audyt 1 (opracowanie i kontrola wstępna)

**Data:** 21 listopada 2026  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`  
**Rozdział:** `chapters/pl/linear_algebra/07-przestrzen-dualna-i-odwzorowania-dualne.tex`

## Zakres

Utworzono rozdział „Przestrzeń dualna i odwzorowania dualne”: dual algebraiczny, dwuliniowość ewaluacji, baza dualna, zmiana baz dualnych, anihilatory, dual ilorazu, rozszerzanie funkcjonałów, dual sumy prostej, odwzorowania dualne i transpozycja macierzy, jądro i obraz odwzorowania dualnego, bidualność, naturalność oraz ślad endomorfizmu. Dołączono samodzielny diagram TikZ ilustrujący zmianę kierunku przez dualizację.

## Pierwsza kontrola matematyczna

1. Ustalono ciało `K`, przestrzenie skończenie wymiarowe (łącznie z wymiarem `0`) i wyjaśniono, gdzie ma zastosowanie uwaga o wymiarze nieskończonym.
2. W konstrukcji bazy dualnej użyto twierdzenia o jednoznacznym przedłużeniu danych z bazy, a nie nieuzasadnionej identyfikacji `V=V*`. Sprawdzono wzory `v=Σ v^i(v)v_i` i `φ=Σ φ(v_i)v^i`.
3. Przy zmianie bazy sprawdzono kierunek: jeśli `[v]_B=P[v]_C`, to `[φ]_{C*}=P^T[φ]_{B*}`, zaś `w^j=Σ_i (P^-1)_{ji}v^i`. Jest to zgodne z użytymi wcześniej konwencjami.
4. Dla anihilatora `U^∘` dowiedziono `dim U^∘=dim V-dim U`, formuł dotyczących sum i przecięć oraz podwójnego anihilatora. Nie użyto niejawnej identyfikacji z przestrzenią zespolenie sprzężoną; wszystko jest algebraiczne.
5. Dla dualu ilorazu poprawnie użyto funkcjonałów stałych na warstwach i wykazano obie inkluzje obrazu `q*`.
6. W przypadku odwzorowania dualnego kolejność składania jest odwrócona: `(S∘T)*=T*∘S*`, a dla baz dualnych macierz jest transpozycją `A^T`.
7. Dla jądra i obrazu `T*` wyraźnie zaznaczono przestrzenie, w których żyją anihilatory. Drugą równość uzasadniono konstrukcją funkcjonału na `im T` i jego rozszerzeniem.
8. W bidualności użyto naturalnej ewaluacji `J_V(v)(φ)=φ(v)` i oddzielono naturalność `V≅V**` od niekanonicznego izomorfizmu `V≅V*`.
9. Ślad zdefiniowano także dla rozmiaru `0×0`. W dowodzie cykliczności potrzebna jest przemienność mnożenia współczynników w ciele; wniosek o niezależności od bazy wynika z podobieństwa macierzy.

## Testy i integracja

Przeprowadzono kontrolę statyczną etykiet, importów, terminologii i środowisk; wyniki potwierdzi przebieg GitHub Actions. Przykłady na `R^2` i `R^3` oraz macierzy transponowanej zostaną ponownie sprawdzone w następnym niezależnym audycie. Plik zawiera `45` etykiet i `15` odsyłaczy.

**Status:** rozdział 07 otwarty po audycie pierwszym; nie zamykać przed niezależną kontrolą II i zielonym CI.
