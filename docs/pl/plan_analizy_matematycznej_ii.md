# Analiza matematyczna II — 47 rozdziałów

Kurs inspirowany wykładami Marka Jarnickiego, rozszerzony o pełny rachunek różniczkowy wielu zmiennych, całki powierzchniowe i całkowanie po podrozmaitościach. Blok rachunku różniczkowego następuje bezpośrednio po rozdziale 10 o ciągłości, różniczkowaniu i całkowaniu granic; rozpoczyna się od granic i ciągłości funkcji wielu zmiennych, a następnie przechodzi do pochodnych i różniczek.

## I. Przestrzenie unormowane, szeregi i zbieżność funkcyjna

01. Przestrzenie unormowane i przestrzenie Banacha (AF 12, AM I 07, AL 12)
02. Szeregi w przestrzeniach Banacha (AM I 09)
03. Zbieżność bezwzględna, warunkowa i bezwarunkowa (AM I 10, AF 27)
04. Iloczyny Cauchy'ego (AM I 11)
05. Iloczyny nieskończone (AM I 12)
06. Rodziny sumowalne i szeregi wielokrotne (AM I, ME)
07. Algebry Banacha i szereg Neumanna (AF 31)
08. Zbieżność punktowa i jednostajna (TO 18)
09. Szeregi funkcyjne (AM I, AF)
10. Ciągłość, różniczkowanie i całkowanie granic (AM I, AF 15A)

## II. Rachunek różniczkowy funkcji wielu zmiennych

11. Funkcje wielu zmiennych: granice i ciągłość, normy w przestrzeniach euklidesowych, granice wzdłuż krzywych, kontrprzykłady (AM I, TO, AF)
12. Pochodne cząstkowe i kierunkowe, gradient i pochodna Gâteaux; zależności i kontrprzykłady (AF 14)
13. Pochodna Frécheta i różniczka zupełna: macierz Jacobiego, reguły różniczkowania, reguła łańcuchowa, interpretacja geometryczna (AF 14, AL)
14. Twierdzenia o wartości średniej, nierówności dla odwzorowań wektorowych, oszacowania przyrostów i lokalne warunki Lipschitza (AF 14, AM I)
15. Pochodne i różniczki wyższych rzędów: twierdzenie Schwarza, wielowskaźniki, symetryczne formy wieloliniowe, macierz Hessego (AF 15)
16. Twierdzenie Taylora dla funkcji wielu zmiennych: wielomiany Taylora, reszty, oszacowania (AF 15, AM I 23)
17. Twierdzenie o funkcji odwrotnej: pełny dowód, lokalna odwracalność, regularność odwrotności i jej pochodna (AF 15, DG 01)
18. Twierdzenie o funkcji uwikłanej: pełny dowód, istnienie, jednoznaczność, regularność, pochodne, przykłady (AF 15, DG 01)
19. Twierdzenia o rzędzie: stały rząd, lokalne postacie odwzorowań, immersje i submersje, poziomice regularne i osobliwe (DG 01, DG 16, AL)
20. Ekstrema swobodne: warunki konieczne i dostateczne, macierz Hessego, przypadki zdegenerowane (AF 15, AL)
21. Ekstrema związane: mnożniki Lagrange'a, więzy regularne, warunki drugiego rzędu; więzy nierównościowe i warunki Karusha–Kuhna–Tuckera z kwalifikacją więzów (AF, AL, DG; uzupełnienia)
22. Podrozmaitości przestrzeni euklidesowej: przestrzenie styczne i normalne, parametryzacje, zanurzenia, regularne poziomice (DG 01, DG 16)
23. Rachunek różniczkowy na podrozmaitościach: różniczka odwzorowania, funkcje gładkie, ekstrema na podrozmaitościach (DG 01, DG 16)

## III. Szeregi potęgowe, funkcje analityczne i aproksymacja

24. Szeregi potęgowe (nowe)
25. Zespolone funkcje elementarne (AM I 18)
26. Funkcje analityczne (nowe, AF 31)
27. Szeregi Taylora (AM I 23)
28. Aproksymacja, Weierstrass i Stone–Weierstrass (AF)

## IV. Rachunek całkowy

29. Całka Riemanna (AM I 29, TC 01–02)
30. Funkcje pierwotne (AM I 28–30)
31. Całki funkcji wektorowych (AF 15A)
32. Całki niewłaściwe (AM I 31)
33. Całki zależne od parametru (AM I 32, ME 11)

## V. Całkowanie wielowymiarowe i na rozmaitościach

34. Krzywe, długość i prostowalność (AM I 33, DG 11)
35. Całki krzywoliniowe obu rodzajów (DG 10–11)
36. Zastosowania geometryczne i fizyczne (AM I 33)
37. Całki wielokrotne i zamiana zmiennych; zastosowania wcześniejszego rachunku różniczkowego (ME 12–13, AF 14–15)
38. Całki powierzchniowe pierwszego rodzaju (DG 11, ME 28)
39. Całki powierzchniowe drugiego rodzaju i strumień (DG 10–11)
40. Całkowanie po podrozmaitościach dowolnego wymiaru, formy, Green, Gauss–Ostrogradski i Stokes (DG 01, 10–11, ME 26–28)

## VI. Analiza Fouriera

41. Układy ortogonalne w przestrzeniach Hilberta (AF 13)
42. Trygonometryczne szeregi Fouriera (PDE 06)
43. Jądro Dirichleta, Riemann–Lebesgue, Dini (nowe)
44. Jądro Fejéra i średnie Cesàro (PDE 06, AM I 13)
45. Zbieżność jednostajna szeregów Fouriera (nowe)
46. Wahanie ograniczone i Dirichlet–Jordan (TC 03, ME 29)
47. Rozbieżność i zjawisko Gibbsa (AF, PDE)

## Migracja już opracowanych rozdziałów

Numeracja powyżej jest docelowa. Rozdziały 01–10 zachowują numery; dotychczasowe 11 (Szeregi potęgowe) i 12 (Zespolone funkcje elementarne) otrzymają docelowo numery 24 i 25. Nie przepisywać zweryfikowanych dowodów ani nie zmieniać etykiet `ma2:*`. Najpierw domknąć otwartą kontrolę wizualną i CI obecnego rozdziału 12, następnie przed utworzeniem nowego rozdziału 11 przeprowadzić spójną migrację nazw plików, raportów audytowych, kolejności `\input`, katalogu, indeksu i odwołań/testów zależnych od numeracji. Nie pozostawiać podwójnych rozdziałów ani pustych zastępczych plików. Zmianę numeracji oddzielić od zmian matematycznych i zweryfikować CI oraz PDF; wyniki poprzednich audytów zachować z informacją o dawnych numerach. W okresie stopniowego uzupełniania bloku różniczkowego można zachować opracowane rozdziały 24–25 jako istniejące źródła bez włączania ich przedwcześnie do kolejności docelowej; sposób włączenia uzgodnić z mechanizmem walidacji katalogu i numeracji. Kolejny nowy rozdział merytoryczny: 11 — Funkcje wielu zmiennych: granice i ciągłość.

Przed całkami krzywoliniowymi, powierzchniowymi i po podrozmaitościach wprowadzić wszystkie potrzebne podstawy: różniczkowanie, parametryzacje, macierze Jacobiego i Grama, orientację, zamianę zmiennych. Nie zakładać nieudowodnionych wyników z przyszłych tomów. Zachować oryginalne etykiety importowanych wyników, nie zmieniać skryptów źródłowych bez potrzeby. Rozdział -> audyty do stabilizacji -> niezależny audyt kontrolny -> kontrola PDF i CI -> kolejny rozdział. W katalogu książek wyłącznie istniejące pliki.

## Zasada ponownego wykorzystania wyników z tomu I

Wynik udowodniony w AM I przytaczamy w AM II z pełnymi potrzebnymi hipotezami i tezą oraz dokładnym odsyłaczem do rozdziału i numeru twierdzenia/lematu/wniosku w tomie I; nie powielamy jego dowodu bez uzasadnionej potrzeby. Zachowujemy oryginalne etykiety importowanych wyników. Jeżeli zmieniono hipotezy, rozszerzono zakres lub sformułowano nowy wynik, podajemy szczegółowy dowód nowej części. Przed zastąpieniem dowodu sprawdzamy faktyczne istnienie i zgodność wyniku oraz dowodu w źródle. Zasadę stosujemy od rozdziału 05; wcześniej ustabilizowanych rozdziałów nie otwieramy ponownie wyłącznie w celu usuwania dowodów.
