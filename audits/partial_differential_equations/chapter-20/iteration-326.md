# RRC 20 — iteracja 326: trzecia pełna lektura stabilizacyjna

Końcowy commit źródła 48532dc5d2201630255aa83ef3553a0ac43873ff, blob b48423b1c622d03cec34fde45a861f49f7911977. Ponownie odczytano wszystkie osiem sekcji (1222 wiersze przed zmianami).

- Uściślono wybór borelowskiego reprezentanta macierzy A, użycie przeliczalnego zbioru kierunków i wspólnego zbioru czasów. 
- W dowodzie reguły obcięcia najpierw wykazano ciągłość N:V→V, następnie silną mierzalność i przynależność do przestrzeni Bochnera, dopiero potem ciągłość w L²(0,T;V). Sprecyzowano interpretację nieujemności u(t) jako klasy w H dla każdego t.
- We wzorze Duhamela uzasadniono, że skończone rozwiązania są rozwiązaniami słabymi w pełnej przestrzeni V, ponieważ operator zachowuje V_n; uzupełniono hipotezę 0<T<infty. 
- Sprawdzono dokładną tożsamość maksymalnej regularności z 325: poprawna pochodna energii, zbieżność wszystkich składników i oszacowania. Rozbito długi wzór w tezie; zbieżność Lu_n wynika bezpośrednio z tożsamości dla różnic. 
- Uzupełniono hipotezy czasu w twierdzeniu o zwartości i wniosku o przesunięciach oraz poprawiono sformułowanie tezy o eksplozji w określonej klasie regularności. Ponowna kontrola dowodów Galerkina, półgrupy, przesunięć, eksplozji i Eulera nie wykazała nowych błędów rachunkowych.
- Ujednolicono zapis miary Lebesgue'a w całkach. W pierwszym commicie f893df7faf45f265b364eddce550f328dbc80fe4 zamiana tekstowa dotknęła także pięciu mianowników zwykłych pochodnych; natychmiast przywrócono poprawny zapis w końcowym commicie. Sprawdzono brak takiego wzorca w końcowym źródle.

Kontrola końcowego zapisu: 1250 wierszy, 23 zachowane unikatowe etykiety, 41 wystąpień odsyłaczy, 12 różnych celów zewnętrznych. Wszystkie cele jednoznaczne w źródle i rozdziałach 4,9,10,11,15,18, poprawne zagnieżdżenie begin/end i delimiterów matematyki eksponowanej. Dedykowane CI 45994065047 queued; poprzednie runy 45991021945,45991264058,45993650919 oraz końcowy run rozdziału 19 45989522023 przy pierwszym odczycie queued. Brak potwierdzenia aktualnej kompilacji, odbioru wizualnego i globalnego CI.

Następny etap: lektura po korektach do pierwszej iteracji bez nowych usterek, potem pełna lektura kontrolna i odbiór techniczny. Nie deklaruje się stabilizacji.
