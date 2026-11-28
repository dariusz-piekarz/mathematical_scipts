# Algebra liniowa — rozdział 29, audyt III

**Data:** 21 listopada 2026  
**Źródło po II iteracji:** `090817361a87a6d457bb9c2c284ad4d50cf8cddf`.

## Istotne poprawki samodzielności dowodów

1. **Niezdefiniowany język wiązek.** Po przeniesieniu DG-04 zabrakło w samodzielnym skrypcie LA definicji gładkiej wiązki wektorowej, jej rzędu, lokalnej trywializacji, cofnięcia oraz wiązki dualnej. Dodano zwarte definicje przed wiązką tautologiczną.
2. **Wiązka normalna.** Twierdzenie o odwzorowaniu Gaussa wprowadzało `\nu M` bez zdefiniowania; obecnie jawnie określono `TM` i `\nu M`. Uzasadniono też kanoniczne utożsamienie `\R^N/T_pM` z `(T_pM)^\perp` przez rzut ortogonalny i sprawdzono gładką zależność od p.
3. **Hausdorff przestrzeni rzutowej.** Dotąd własność użyta przy dowodzie osadzenia Plückera nie miała lokalnego wyjaśnienia. Dopisano, że `\mathbb P(\Lambda^kV)=\operatorname{Gr}_1(\Lambda^kV)`, stąd korzystamy z dowiedzionej wcześniej własności Hausdorffa grassmannianu.
4. **Gładkie funkcje odcięcia.** Przy konstrukcji uniwersalnej wiązki tautologicznej wskazano jawnie potrzebny standardowy fakt o istnieniu gładkich funkcji odcięcia na rozmaitościach, od którego zależy wybór `\beta_i`.
5. **Terminologia i odsyłacze.** Zachowano poprzednie poprawki `Równanie Plückera` i `iniektywna`; nie zmieniono etykiet ani rysunków.

## Kontrole pozostające
Weryfikacja CI i PDF dla nowego bloba oraz powtórne badanie rachunków współrzędnych Plückera i konstrukcji ilorazowej. Audyt III **nie jest czysty**, gdyż zmienił dowód i jawne założenia.
