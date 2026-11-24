# Audyt CIII (103) — obrazy krytyczne, włókna zerowe i ogólne wzory
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt startowy d260593716579b885811df79c7c1ef35f8a8d60d, blob dc2bb8f2a8d3420721a40779880347158e453bec. Commit źródła 424d89d7588efaad2914ec327e3a5627d69f9f47, blob ca5e9afea0b90d652f62eb3ca94afe5b2fa65f29.

## Zmiany
- Rozpisano pełne oszacowanie obrazu zwartego zbioru o niedostatecznej randze: zwarte otoczenie, całkowa reszta pierwszego rzędu, siatka w obrazie różniczki, liczba kostek, przypadek rangi zero, koszt i kolejność wyboru skali oraz przejścia eta do zera.
- Dla włókien zbioru zerowego jawnie skonstruowano pokrycie kostkami z kalibracji Hausdorffa, w tym pokrycie singletonów i warunek pozostawania w otoczeniu Lipschitzowskim. Rozpisano szacunek średnic, objętości kul i zastosowanie zbieżności monotonicznej oraz przeliczalnej sumy wyjątków po obu parametrach.
- Ponownie sprawdzono argument CII dla krytycznych włókien: dominacja borelowska i miara zewnętrzna omijają nieuzasadnioną mierzalność kosztu przy ustalonej skali.
- Ogólne wzory: jawna definicja sumy po dowolnym włóknie, konwencja zero razy nieskończoność, borelowskość jakobianów. W przypadku coarea dla funkcji mierzalnej w sensie Lebesgue'a ograniczenie do włókna jest mierzalne tylko prawie wszędzie; teza i dowód teraz precyzyjnie to stwierdzają.
- Lemat area dla C^1: jawne zwarte wyczerpanie zbioru krytycznego i mierzalność funkcji wspieranej na zerowym obrazie przez zupełność Hausdorffa.
- W dowodzie ogólnym zastąpiono niepotrzebne odwołanie do Tonellego w potencjalnie niesigma-skończonej przestrzeni przez twierdzenie o zbieżności monotonicznej. Rozpisano rozłączne sumowanie włókien i obraz zbioru wyjątkowego przez przeliczalne pokrycie otoczeniami Lipschitzowskimi.
- Przejście do funkcji mierzalnych: przedłużenie przez zero, borelowski reprezentant, zgodność na włóknach poza zerowym zbiorem parametrów; w coarea również mierzalność ograniczeń dzięki zupełności Hausdorffa. 
- 16 celowanych zamian, wszystkie 28 etykiet zachowane w tej samej kolejności.

## Otwarte
Następna iteracja: kontrola zmian CIII, pełne dowody na rozmaitościach, lokalna identyfikacja miary Hausdorffa i riemannowskiej (w tym odległość zewnętrzna na podrozmaitości), kontrola normalizacji i terminologii. Potem dedykowana bramka testów, kompilacja i oględziny PDF. Nie przeprowadzono kompilacji ani testów w tej iteracji. Rozdział 28 pozostaje nieustabilizowany; stan 27/31. Bez rozszerzania zakresu, nie przechodzić do 29.
