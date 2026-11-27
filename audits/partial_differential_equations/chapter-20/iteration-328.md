# RRC 20 — iteracja 328: kontrola stabilizacyjna

Źródło: commit a160cd86d1a9c3c2bf245d5048327b121e2ed9c3, blob 61a8f9cba5782a127d729cd359c7a5956aeaa3db, 1260 wierszy. Potwierdzono zgodność blobu na gałęzi roboczej.

Porównano wszystkie 8 sekcji z wersją po iteracji 326 (48532dc5d2201630255aa83ef3553a0ac43873ff). Sekcje 1, 2 i 8 są identyczne; w sekcjach 3–7 sprawdzono wszystkie różnice wraz z kontekstem. Zapis zmiennej całkowania w dowodzie jednoznaczności jest poprawny. Ograniczenie J do V_n jest klasy C^1, pochodna ograniczona na kuli zawierającej obraz u_n daje lipschitzowskość na tej kuli, stąd absolutna ciągłość złożenia i poprawność reguły łańcuchowej. Równość w H w dowodzie Duhamela zachodzi dla prawie każdego czasu, gdyż obie strony należą do V_n. Kwantyfikacja podciągów w dowodzie zwartości jest poprawna (ciągi indeksów ograniczone mają stały podciąg, a z nieograniczonych można wybrać rosnący podciąg). Definicja F(t) jest zgodna z dowodem eksplozji i dobrze określona na całym przedziale istnienia.

Nie wykryto nowych usterek wymagających zmian. Źródło pozostawiono bez zmian. Jest to kontrola różnic po czterech pełnych lekturach stabilizacyjnych, nie kolejna pełna lektura dowodów.

Kontrola aktualnego źródła i sześciu aktualnych rozdziałów zależnych (4,9,10,11,15,18): 23 unikatowe zachowane etykiety, 41 wystąpień odsyłaczy, 12 różnych celów zewnętrznych, wszystkie cele jednoznaczne, brak błędów zagnieżdżenia środowisk i delimiterów matematyki eksponowanej, brak błędnej notacji pochodnej względem miary.

Runy 45989522023 (rozdział 19), 45994065047 i 45994503573 (rozdział 20) przy odczycie nadal queued. Brak potwierdzenia aktualnej kompilacji, odbioru wizualnego i globalnego CI.

Następny etap: pełny audyt kontrolny wszystkich ośmiu sekcji rozdziału 20. Przy braku nowych usterek można zamknąć stabilizację merytoryczną i rozpocząć następny rozdział, pozostawiając odbiór techniczny otwarty do uzyskania wyników CI.
