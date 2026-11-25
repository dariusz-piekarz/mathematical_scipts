# PDE-07 — iteracja 95: CI i kontrola wizualna rozdziału

Data: 2026-11-25. Przebieg 45577455405 (job 139078808544), commit f3e018e1c64efb8abe7700751ee5fe0dc0d60128, status completed/success.

Z rzeczywistych logów: Ran 10 tests in 0.051s, OK; 70 criterion anchors verified (not executed proofs); 36 distinct labels; 66 resolved reference occurrences. Wszystkie kroki workflow zakończone success. Pierwszy przebieg LaTeX zgłaszał nierozwiązane odsyłacze, końcowy log po drugim przebiegu nie zawiera ostrzeżeń o nierozwiązanych odsyłaczach, overfull hbox, missing character ani undefined control sequence. Pozostaje 12 ostrzeżeń hyperref o pustych celach linków, zgodnych z zamierzoną izolacją rozdziału i liczbowymi odsyłaczami zewnętrznymi (bez klikalnych celów w brakujących rozdziałach).

Wygenerowane numery: chap:pde-characteristics=2, chap:pde-laplace=3, eq:pde3-green2=3.8, thm:pde3-phi=3.11, thm:pde3-mean=3.2, thm:pde3-analytic=3.26, thm:pde4-gauss-basic=4.2, chap:pde-fourier-Rd=8, chap:pde-sobolev=9.

Artefakt 15005186364, pde-ch07-audit.zip, SHA256 ac9ebcfdfb9586c8182c6bec3a305091abbe018265f063f61c7e9f27d0ff9e42 zgodny z digest GitHub. Pobrano i rozpakowano rzeczywisty artefakt: PDF 22 strony A4, log, tekst oraz 22 obrazy PNG. Obejrzano przegląd wszystkich 22 stron w czterech planszach oraz stronę 13 w pełnym renderze: rysunek przybliżonych jedynek ma czytelne osie, oznaczenia epsilon=1,2 i granice nośników -2,-1,1,2; proporcje szerokości i wysokości 1:2 i 2:1 zgodne z opisem. Nie zaobserwowano istotnych problemów układu na planszach przeglądowych; to kontrola układu, nie kolejna pełna lektura wzorów.

Porównano bloby aktualnej gałęzi z drzewem commitu CI dla 13 plików: rozdziału 07, rejestru, testów, workflow, pięciu rozdziałów zewnętrznych 02,03,04,08,09, książki, manifestu, listingów, preambuły Atlasu. Wszystkie 13/13 identyczne. Źródło rozdziału ccabfced1d41d4b25f2853aed43dff90c70b8ea6, rejestr fcc405f47ecf73ad1f8e4cdf611fa984a2b3a546, testy 62d0d08e95f35533ba82eb199e8d1e3fdc8fecf6, workflow 27e2b20c2357a473a5ba24a62d91c697ddab2dcd.

Nie zmieniano tekstu rozdziału. Nie wykonano pełnej kompilacji tomu, formalizacji Lean ani drugiej lektury semantycznej. Rozdział nie jest jeszcze ustabilizowany. Kolejna iteracja 96: druga lektura sekcji 7.1–7.2, kryteria PDE-07-001–014; następnie dalsze sekcje i niezależny audyt kontrolny. Każda istotna poprawka ma mieć trwałe kryterium regresyjne, a zmienione źródło wymaga nowego CI.
