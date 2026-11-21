# Algebra liniowa — rozdział 29, audyt V

**Data:** 21 listopada 2026  
**Źródło przed audytem:** `80e8eb081d2d65ae1741ef86c6218be32783b80f`.

## Kontrola matematyczna i precyzja definicji

- Wrócono do przestrzeni rzutowych: równości Gr₁(Rⁿ)=RPⁿ⁻¹ oraz Gr₁(Cⁿ)=CPⁿ⁻¹ wymagają n≥1; dla n=0 takie oznaczenia są nienaturalne. Warunek zapisano jawnie.
- W stwierdzeniu o przestrzeniach ramek ortonormalnych włókno odwzorowania Stiefela do grassmannianu nie jest kanonicznie grupą O(k). Po wyborze ramki jest `O(k)`-torsorem, a jako rozmaitość jest dyfeomorficzne z O(k). Zamieniono nieprecyzyjne „izomorficzne” na „dyfeomorficzne (po wyborze ramki)”.
- Sprawdzono, że przestrzeń ilorazowa O(n)/(O(k)×O(n−k)) jest zgodna z działaniem izometrycznym i że w lokalnym przekroju Gram–Schmidt daje gładkie ramki, bez założenia globalnej trywialności.
- Dodatkowo 40 numerycznych kontroli działania O(2) na ramkach dwóch przestrzeni o tym samym obrazie ortogonalnego rzutowania — PASS.
- Współrzędne Plückera, dowody ciągłości, gładkości, zwartości i opis wiązki normalnej pozostawiono bez zmian.

## CI
[Walidacja audytu III](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44954394507) zakończona SUCCESS i zawierała pełny PDF po dodaniu brakujących definicji.
Nowa wersja wymaga osobnego CI i kontroli PDF.

## Wynik
**Audyt V nie jest czysty**, ponieważ naprawiono dwie nieścisłości założeń i charakteru włókien. Kontynuować niezależne audyty do dwóch czystych iteracji.
