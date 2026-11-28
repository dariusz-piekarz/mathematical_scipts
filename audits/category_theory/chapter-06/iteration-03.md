# CAT-06 — audyt III (kontrolny)

Stan badany 74c5971f06d86a2d071028fece6da6fa0cd837bf, źródło d080944ade403fc3ee859b37547611610ff150ca. Porównano 28 blobów z CI 45587939637 (94899205a11064f1db6b4672fd0dc2dc7530862f); brak różnic.

## Kontrola matematyczna
Ponowna kontrola definicji i dowodów z audytu II: rzutowanie i ograniczanie do składników wyznaczają odpowiednie strzałki jednoznacznie, w tym dla rodziny pustej. Konstrukcja iloczynu wolnego przez normalne domknięcie relacji mnożenia jest poprawna: homomorfizm z grupy wolnej zeruje relacje, a normalność jądra zapewnia faktoryzację; lewostronne odwrotności zanurzeń pochodzą z własności uniwersalnej. W przykładzie C2*C2 komutator jest niejednostkowy przez obraz w S3. Topologia iloczynu jest generowana przez podbazę rzutów, topologia sumy rozłącznej przez warunek otwartości ograniczeń. W module sumy prostej skończony nośnik umożliwia skończoną sumę obrazów. Naturalność bijekcji Hom i izomorfizmów łączności, symetrii i jednostki ma poprawne typy i kierunki. Nie utożsamiono dowolnego koproduktu z iloczynem ani nie przypisano dodawania morfizmów ogólnej kategorii z zerami. Brak nowych istotnych usterek, bez zmian tekstu. 

## Niezależne kontrole rzeczywiście uruchomione lokalnie
Python, tests/mathematical/category_theory/chapter-06/control.py, commit c00f6146b9402c09f4ec2d26a0e006d5f0a21e6f.
- 1273 funkcje: równoważność ciągłości do iloczynu i ciągłości składowych, wszystkie topologie na oznaczonych zbiorach mocy 0–2.
- 1481 funkcji: równoważność ciągłości z sumy topologicznej i ciągłości ograniczeń, te same przestrzenie.
- 2032 przypadki: zachowanie wartości słów w C2*C2 po redukcji przy wszystkich parach elementów S3 o kwadracie równym jedynce, słowa długości do 6.
- 15376 przypadków: zachowanie mnożenia po redukcji i obliczeniu obrazów par słów długości do 4.
- 279620 przypadków: jednorodność wzoru sumy obrazów w modelu skończonych sum Z/4, do czterech składników. Nie jest to osobny test addytywności.
Łącznie 299782 przypadki PASS. Skrypt ręczny poza discovery CI. Modele skończone nie zastępują dowodów ogólnych. Nie uruchamiano Lean.

## CI i PDF
Job validate: wszystkie osiem kroków success, 38 metod testowych. Artefakt 15009472622 pobrany i rozpakowany. pdfinfo: 46 stron; pdftotext -layout: CAT-06 od strony 23 do strony 28 włącznie. Log bez dopasowań Warning, Overfull i ^!. Render pdftoppm 115 dpi stron 23–28 obejrzano w montażu; nie zauważono obcięć, kolizji ani problemów z diagramami. Nie oceniano wizualnie reszty tomu.

## Werdykt
CAT-06 zamknięty. Kolejny CAT-07: equalizatory, koequalizatory i kwadraty kartezjańskie; pierwszy audyt i rozszerzenia.
