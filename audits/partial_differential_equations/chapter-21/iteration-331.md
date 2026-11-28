# RRC 21 — iteracja 331

Commit źródła 72c292acb012ed90b9716a73c576c66ed3b3ce9c, blob 5f9461438fec120a9d6403fde354b6b86a970f2a. Pierwszy audyt szczegółowy sekcji 21.5.

- Uzasadniono komutator pochodnych w H^{-1} i jego przynależność do L² przez regułę Leibniza i aproksymację u w H^s, bez nieuprawnionej aproksymacji współczynników w normie W^{s,∞}. Rozpisano oszacowanie składników.
- Określono normę H^s jako sumę kwadratów norm pochodnych, hipotezy twierdzenia energetycznego, oszacowanie sumy komutatorów i stałą C=M/2+C_0. Wcześniejszą hipotezę globalnego oszacowania energii ograniczono do mierzalności w czasie i jednostajnej przestrzennej regularności W^{1,∞}; dowód nie wymaga pochodnej czasowej współczynników.
- Usunięto istotną lukę w lemacie Friedricha: poprzednia wersja identyfikowała ciągłą funkcję normy jedynie prawie wszędzie, co samo nie wystarcza do silnej ciągłości słabo ciągłego reprezentanta. Nowy dowód konstruuje najpierw reprezentanta w H^{-1} i w każdej chwili identyfikuje go z jednoznacznym elementem H o normie ograniczonej przez normę L∞. Wykazano słabą ciągłość przez gęstość H¹. Rozpisano komutator splotu przez całkowanie przez części, wyzerowanie całki jądra, oszacowanie translacji i zbieżność w L¹ czasu. Dla każdej chwili splot reprezentanta H^{-1} jest równy splotowi właściwego elementu H, co pozwala uzyskać tożsamość energii dla dowolnych końców przedziału. Następnie słaba ciągłość i ciągłość normy dają silną ciągłość.
- Poprawiono notację zamkniętej kuli o zerowym promieniu w sekcji 21.3 (zbiór zadany nierównością zamiast domknięcia pustej kuli).

Kontrola zapisanego źródła: 1042 wiersze (880 wcześniej), 23 zachowane unikatowe etykiety, 48 wystąpień odsyłaczy, dwa różne cele zewnętrzne (rozdziały 5 i 20), wszystkie cele jednoznaczne, brak błędów zagnieżdżenia środowisk i delimiterów. Brak potwierdzonej kompilacji rozdziału 21.

CI rozdziału 19: run 45989522023 zakończony success, commit da99e4b5e7b28193643df991c71dc2b7bbf2d6fc; potwierdzono wszystkie kroki kompilacji, rzeczywiste numery odsyłaczy, diagnostykę, renderowanie i przesłanie artefaktu 15194684382. Nie wykonano jeszcze osobistej kontroli wizualnej stron artefaktu. Rozdział 20: run 45994503573 przy pierwszym odczycie queued.

Postęp pierwszego audytu 5/10 sekcji. Następny etap: sekcja 21.6, konstrukcja istnienia przez regularizację Friedricha, w tym przejście graniczne w H^s, ślad początkowy i oszacowanie bez pomocniczego warunku H^{s+1}; kontrola wizualna artefaktu rozdziału 19.
