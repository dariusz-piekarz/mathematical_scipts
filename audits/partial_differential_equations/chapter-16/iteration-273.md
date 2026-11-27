# RRC 16 — iteracja 273: pierwszy audyt 043–052

Źródło przed 536a9ac846f9a9e9f7b30e0b1dc4c9a040638280 (1490 wierszy), po 0070dc03901209545204d40eede4162956a32839 (1604 wiersze), commit 64bed2acdfbae16bf716af8a5637eab05fd7f4e6.

| Kryterium | Wynik i poprawka |
|---|---|
| 043 | Normy skalowane z ustaloną skalą także na mniejszym zbiorze, nierówności iloczynu i kontrakcji; usunięto niejednoznaczność skali. |
| 044 | Zamrożony operator: x=x0+rho S z, S=A0^{1/2}, jawna transformacja Hessianu i laplasjanu, nośniki w ustalonej kuli. |
| 045 | Uzasadniono tożsamość Gamma*(-Delta w)=w dla C_c^{2,alpha} przez wygładzanie i lokalną całkowalność Gamma. Kontrola globalnej półnormy przedłużonego przez zero prawego członu przez punkt przecięcia odcinka ze sferą. Zastosowanie lematu Newtona i transformacja z powrotem. |
| 046 | Interpolacja na całej kuli bez powoływania się na nieudowodnione przedłużenie: przesunięcie x_t=(1-t)x do wnętrza, odcinki długości t/2, oszacowanie G<=C(t^{-1}Y+tH). |
| 047 | Półnormy niższych pochodnych przez minimum oszacowania Lipschitzowskiego i supremum, ważona nierówność Younga i dobór parametrów; mały składnik zawiera wyłącznie supremum Hessianu. |
| 048 | Jawne odcięcie i normy pochodnych do rzędu trzy, kontrola skalowanych półnorm; przedłużenie zerowe eta v w C^{2,alpha}. |
| 049 | Rozpisano wszystkie składniki A0:D²(eta v), w tym znaki niższego rzędu, normy iloczynów, potęgi rho oraz pochłonięcie różnicy A-A0 w normie samej funkcji odciętej. |
| 050 | Po interpolacji uzyskano lokalne oszacowanie z dowolnie małym współczynnikiem przy rho² normy supremum Hessianu na większej kuli. |
| 051 | Zamiast nieudokumentowanego sklejenia ważonych półnorm wystarcza M=sup delta(x)²|D²v(x)|. Lipschitzowskość delta, porównanie delta(y)>=3delta(x)/4, promień 2delta(x), epsilon=1/8; współczynnik epsilon(4/3)²<1/2, więc M jest kontrolowana przez dane. |
| 052 | Na B_r delta>=delta_*>0, ponowne lokalne oszacowanie półnormy dla par bliskich i norma supremum dla par dalekich, interpolacja gradientu, przejście na domknięcie. |

Zachowano wszystkie 30 etykiet. 60/60 odsyłaczy, 38 unikalnych celów; brak brakujących lub wieloznacznych w sprawdzonych plikach. Stos środowisk poprawny przed zapisem. PDF i CI niepotwierdzone. Pierwsza lektura 52/64 z poprawkami. Następna iteracja 274: 053–058 — komutator i regularyzacja w twierdzeniu Schaudera.
