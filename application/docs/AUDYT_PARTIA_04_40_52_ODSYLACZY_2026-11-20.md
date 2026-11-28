# Biblioteka matematyczna — audyt integralności odsyłaczy, partia IV (40–52)

**Data:** 20 listopada 2026. **Stan źródłowy:** `chapters/pl/` gałęzi `biblioteka-matematyczna-iteracja-6` repozytorium `dariusz-piekarz/mathematical_scipts`; indeks i mapa pochodzenia z audytu 355 rozdziałów. Ustalenia odnoszą się do 13 kolejnych rekordów `unresolved_references`, liczonych od 1. Potwierdzono tekst źródłowy miejsc cytujących i przywoływanych deklaracji. Nie zmieniono żadnego pliku TeX, `\label` ani `\ref`.

**Reguła zachowania materiału z Biblioteki:** przy kopiowaniu bezwarunkowo zachować oryginalne nazwy i liczby wystąpień `\label{...}` oraz powiązane komendy `\ref`, `\eqref`, `\cref`. Rozstrzygnięcie właściciela w mapie odsyłaczy nie jest przemianowaniem deklaracji, scalaniem rozdziałów ani uzasadnieniem do usunięcia alternatywnych dowodów. Właścicieli wybieramy na podstawie faktycznego zakresu twierdzenia i skryptu cytującego.

## Wyniki indywidualne

| Nr | Cytowanie | Etykieta | Preferowany właściciel | Inny właściciel | Ocena matematyczna | Status |
|---:|---|---|---|---|---|---|
| 40 | `DG-09:5` | `ch:topologia-algebraiczna-podstawy` | `DG-07:2` | `TOP-04:2` | Przywołany rozdział definiuje drogi, pętle i grupę podstawową. DG-07 jest poprzedzającym rozdziałem tego samego skryptu; jego § o grupie podstawowej realizuje opisywany zakres. | lokalne |
| 41 | `DG-09:8` | `ch:homologia-przestrzeni` | `DG-08:2` | `TOP-05:2` | Mowa o homologii cykli przypisanych przestrzeni, nie o samej homologii kompleksu abstrakcyjnego. DG-08 konstruuje homologię symplicjalną, singularną i komórkową. | lokalne |
| 42 | `DG-09:53` | `def:droga-petla` | `DG-07:130` | `TOP-04:82` | Dla n=1 homotopia opartych odwzorowań (I,∂I)→(X,x₀) jest relacją homotopii pętli względem końców z DG-07. Nie wolno utożsamiać definicji tylko na podstawie nazwy bez warunku stałości na brzegu. | lokalne |
| 43 | `DG-09:88` | `thm:grupa-podstawowa` | `DG-07:227` | `TOP-04:155` | Łączność składania n-kostek jest wywiedziona przez reparametryzację i odsyła do argumentu grupowego dla pętli. Twierdzenie DG-07 podaje działanie, neutralność, odwrotność i dowód. | lokalne |
| 44 | `DG-09:236` | `thm:grupa-podstawowa` | `DG-07:227` | `TOP-04:155` | Anulowanie przejścia wzdłuż drogi i drogi odwrotnej przy zmianie punktu bazowego powtarza mechanizm homotopii pętli z DG-07; to zgodność mechanizmu, nie nowe twierdzenie o strukturze grupy. | lokalne |
| 45 | `DG-09:261` | `cor:pi1-homotopia` | `DG-07:353` | `TOP-04:240` | Użyta jest niezmienniczość π₁ przy homotopii wraz ze zmianą punktu bazowego. DG-07 jawnie podaje g_* = b_u ∘ f_* i wyjaśnia znaczenie ścieżki bazowej. | lokalne |
| 46 | `DG-09:544` | `ch:homologia-przestrzeni` | `DG-08:2` | `TOP-05:2` | Tekst przedłuża homologię komórkową ze skończonych CW na ogólne CW i pary CW. DG-08 jest miejscem konstrukcji skończonego kompleksu komórkowego; dalszy argument w DG-09 jest rozszerzeniem, nie kopią wcześniejszego wyniku. | lokalne; kontrola dowodu |
| 47 | `DG-09:839` | `thm:kryterium-podnoszenia` | `DG-07:644` | `TOP-04:473` | Dla n≥2 Sⁿ jest łukowo i lokalnie łukowo spójna oraz jednospójna; stąd f_*π₁=0⊆p_*π₁. To dokładnie kryterium istnienia podniesienia z DG-07, z ustalonym punktem bazowym. Analogicznie dla homotopii Sⁿ×I. | lokalne; założenia sprawdzone |
| 48 | `DG-09:874` | `prz:homologia-cw-torus` | `DG-08:2018` | `TOP-05:1448` | W DG-09 kontrast π₂(T²)=0 z H₂(T²;ℤ)=ℤ. DG-08 liczy komórkowo H₂ torusa za pomocą jednej 2-komórki i zerowego ∂₂, więc odpowiada wskazanemu użyciu. | lokalne |
| 49 | `DG-09:925` | `thm:homotopia-singularna` | `DG-08:460` | `TOP-05:354` | Dwa homotopijne odwzorowania dają ten sam homomorfizm w homologii; dowód DG-08 używa operatora pryzmatycznego. To zapewnia niezależność klasy 1-cyklu od reprezentanta homotopii pętli. | lokalne |
| 50 | `DG-09:1008` | `prz:pi1-dwa-okregi` | `DG-07:1169` | `TOP-04:840` | Przykład DG-07 dla dwóch okręgów daje F₂=ℤ*ℤ. DG-09 rozszerza ten rachunek do bukietu r okręgów; odsyłacz uzasadnia bazowy przypadek r=2, nie stanowi samodzielnego dowodu dla r>2. | lokalne; zakres przykładu |
| 51 | `DG-09:1018` | `prz:homologia-bukiet` | `DG-08:2206` | `TOP-05:1567` | DG-08 wylicza H₁ bukietu r okręgów jako ℤʳ z kompleksu komórkowego; zgodne z abelianizacją F_r w DG-09. | lokalne |
| 52 | `DG-09:1324` | `thm:homologia-sfer` | `DG-08:1138` | `TOP-05:794` | Konstrukcja odwzorowania Hurewicza korzysta z H_n(Sⁿ;ℤ)≅ℤ dla n≥2. DG-08 zawiera mocniejszą wersję o homologii zredukowanej sfer i względnej homologii dysku. | lokalne; warunki spełnione |

## Kontrola założeń i granic zastosowania

1. **DG-09:53:** utożsamienie π₁ z klasami pętli wymaga odwzorowań opartych i homotopii względnych względem brzegu kostki; jest zgodne z definicją `def:droga-petla` w DG-07, ale nie wystarczy sama zbieżność nazw.
2. **DG-09:839:** kryterium podnoszenia zakłada łukową i lokalną łukową spójność przestrzeni źródłowej. Dla Sⁿ, n≥2, obie zachodzą, a π₁(Sⁿ)=0. Dla Sⁿ×I analogicznie z powodu retrakcji na Sⁿ. Jednoznaczność podniesienia wymaga wyboru punktu w odpowiednim włóknie i spójności źródła. Te warunki są jawnie uwzględnione w DG-09.
3. **DG-09:874 i 1324:** homologia torusa i sfery jest całkowitoliczbowa; nie należy wnioskować tych twierdzeń z samych wzorów na homologię nad dowolnym ciałem. W DG-08 są odpowiednie rachunki nad ℤ.
4. **DG-09:1008:** lokalny przykład z DG-07 dowodzi przypadku dwóch okręgów; dla dowolnego r wymagana jest dodatkowa iteracja argumentu van Kampena (lub bezpośrednia konstrukcja grafowa). Tekst DG-09 poprawnie wskazuje, że `r=2` policzono wcześniej, ale pełny audyt dowodu dla r>2 pozostaje odrębnym zadaniem.
5. **DG-09:544:** rozszerzenie ze skończonych na dowolne CW wykorzystuje skończoność nośnika łańcuchów singularnych oraz zawieranie obrazu zwartej przestrzeni w skończonym podkompleksie CW; przesłanki tych kroków wymagają osobnego szczegółowego audytu przy przyszłym matematycznym przeglądzie rozdziału. Nie jest to wada samego cytowania rozdziału DG-08.

## Wynik i dalsze kroki

- W tej partii: **13 niejednoznacznych wystąpień**, wszystkie mają tekstowo i matematycznie uzasadnionego kandydata lokalnego (`DG-07` lub `DG-08`); **0 brakujących etykiet** w tej partii.
- Łącznie z partiami I–III: **52/257** wystąpień objęto audytem; **205** pozostaje do przeglądu w tej samej migawce. Jest to licznik **przeglądów, nie naprawionych odsyłaczy**.
- **Następna partia:** 53–65. Nie dokonywać automatycznego przemianowania etykiet w źródłach ani cichej zmiany docelowego rozdziału. Ewentualny rejestr rozstrzygnięć lokalnych musi przechowywać nazwę oryginalną, lokalizację cytowania, wszystkich kandydatów i uzasadniony wybór.
- Zachować nadrzędny plan: najpierw skompletować niezależne działy matematyki od podstaw, następnie rozbudowywać gałęzie, a scalanie materiałów prowadzić dopiero po skompletowaniu zakresów, z zachowaniem sumy treści i dowodów.

**Zakres weryfikacji:** sprawdzono konkretne miejsca użycia i fragmenty definicji/twierdzeń właścicieli; nie jest to pełny audyt wszystkich dowodów w rozdziałach, a sam protokół nie jest wynikiem kompilacji `xr-hyper`.