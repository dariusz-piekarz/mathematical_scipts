# Biblioteka matematyczna — audyt odsyłaczy, partia VI (wystąpienia 66–78)

**Data:** 20 listopada 2026. **Podstawa:** raport `reference_provenance_audit_355.json`, obejmujący 355 rozdziałów i 257 nierozwiązanych wystąpień (migawka), oraz odczyt aktualnych kanonicznych plików `chapters/pl/` w gałęzi `biblioteka-matematyczna-iteracja-6`. **Charakter prac:** kontrola semantyczna pochodzenia odsyłaczy, a nie modyfikacja źródeł, scalanie skryptów czy pełny dowód twierdzeń. Oryginalne `\label`, `\ref`, `\eqref`, pozostałe warianty treści i ich pochodzenie pozostają nienaruszone.

## Wyniki przypadków 66–78

| Nr | Cytowanie (wiersz) | Etykieta | Kandydaci w indeksie | Proponowany lokalny właściciel | Sprawdzenie kontekstu i dalsze zastrzeżenia |
|---:|---|---|---|---|---|
| 66 | DG-10:1611 | `ch:homologia-przestrzeni` | DG-08:2; TOP-05:2 | **DG-08** | Fragment porównuje formy z homologią singularną wprowadzoną w rozdziale DG-08; właściwy lokalny cel. |
| 67 | DG-10:1734 | `thm:homotopia-singularna` | DG-08:460; TOP-05:354 | **DG-08** | Twierdzenie daje niezmienniczość homotopijną homologii singularnej i stosuje operator pryzmatowy. Cytowanie wykorzystuje wersję dla homologii i dualnie dla kohomologii; rozszerzenie na *gładkie* sympleksy uzasadniane jest odrębnie w DG-10 i wymaga zachowania kontroli gładkości na brzegu. |
| 68 | DG-10:1859 | `lem:male-lancuchy` | DG-08:714; TOP-05:507 | **DG-08** | Lemat o małych łańcuchach odnosi się do otwartego pokrycia i izomorfizmu homologii. DG-10 rozszerza operator podziału na gładkie sympleksy; **do pogłębienia** zachowanie gładkości i argument przejścia do kochainów przy nieskończonych kompleksach. |
| 69 | DG-10:2127 | `thm:symplicjalna-singularna` | DG-08:1384; TOP-05:1033 | **DG-08** | Twierdzenie DG-08 jest sformułowane dla skończonych kompleksów symplicjalnych (oraz skończonych Δ-kompleksów), podczas gdy DG-10 przechodzi także do lokalnie skończonych triangulacji przez skończone podkompleksy; **do pogłębienia** argument przejścia do granicy i dokładne warunki lokalnej skończoności. Nie przypisywać twierdzeniu szerszej tezy niż podana. |
| 70 | DG-10:2238 | `thm:homologia-char-zero` | DG-06:1795; TOP-03:1512 | **DG-06** | Stwierdzenie mówi wyłącznie o przejściu do `\mathbb Q`, `\mathbb R`, `\mathbb C`. W tekście DG-10 występują dokładnie te współczynniki; przykład modulo 2 nie może być wnioskiem z tego twierdzenia. |
| 71 | DG-10:2241 | `prz:zmiana-wspolczynnikow-rp2-torus` | DG-08:2159; TOP-05:1529 | **DG-08** | Przykład oblicza kompleksy komórkowe torusa i `\mathbb{RP}^2` nad ciałami charakterystyki zero, z dodatkowym kontrastem modulo 2; odpowiednio ilustruje znikanie torsji przy przejściu do `\mathbb Q`, `\mathbb R` lub `\mathbb C`. |
| 72 | DG-10:2271 | `ch:wyzsza-homotopia` | DG-09:2; TOP-06:2 | **DG-09** | Rozdział DG-09 wprowadza grupy wyższej homotopii oraz odwzorowanie Hurewicza `h_k`; lokalny cel jest zgodny. |
| 73 | DG-10:2273 | `thm:hurewicz-h1` | DG-09:887; TOP-06:734 | **DG-09** | Twierdzenie DG-09 wymaga łukowej spójności `X` i utożsamia `\pi_1(X)_{\mathrm{ab}}` z `H_1(X;\mathbb Z)`; DG-10 jawnie pracuje ze składową łukowo spójną, więc założenie jest spełnione. |
| 74 | DG-10:2283 | `thm:hurewicz-wyzszy` | DG-09:1891; TOP-06:1491 | **DG-09** | Twierdzenie wymaga `(k-1)`-spójnego kompleksu CW, `k\ge2`; DG-10 wymienia te założenia i osobno powołuje triangulowalność rozmaitości gładkich. **Do pogłębienia** dokładny zakres twierdzenia o triangulacji, szczególnie przy brzegu i niezwartości. |
| 75 | DG-10:2316 | `prz:pi1-torus-rp2` | DG-07:2269; TOP-04:1493 | **DG-07** | Konstrukcja CW torusa przez doklejenie `2`-komórki według komutatora w DG-07 jest dokładnie modelem użytym po wycięciu dysku w DG-10, dającym retrakcję na bukiet dwóch okręgów. |
| 76 | DG-10:2346 | `prz:rp2-pi2` | DG-09:2344; TOP-06:1901 | **DG-09** | Przykład używa nakrycia `S^2\to\mathbb{RP}^2` i izomorfizmu wyższych grup homotopii dla nakryć, skąd `\pi_2(\mathbb{RP}^2)\simeq\mathbb Z`; lokalny właściciel zgodny. |
| 77 | DG-10:2347 | `prz:homologia-rp2` | DG-08:2060; TOP-05:1476 | **DG-08** | Przykład z `\partial_2=\times2` daje `H_1(\mathbb{RP}^2;\mathbb Z)=\mathbb Z/2`, `H_2=0`; dokładnie te dane są cytowane. |
| 78 | DG-11:371 | `thm:podzial-jednosci-formy` | DG-10:461; TOP-09:389 | **DG-10** | Gładki, lokalnie skończony podział jedności podporządkowany pokryciu przez mapy gwarantuje dodatnio określoną metrykę. DG-11 poprawnie korzysta ze zwartości nośników, lokalnej skończoności i dodatniości; założenia Hausdorffa i przeliczalnej bazy odpowiadają deklaracji w DG-10. |

## Kontrole matematyczne wymagające dalszego pogłębienia

1. **DG-10:1734 i DG-10:1859:** odróżnić kompleks gładkich sympleksów od wszystkich ciągłych sympleksów; wykazać precyzyjnie, że operatory pryzmatowe, barycentryczne i łańcuchowe zachowują przyjętą regularność aż do ścian. Sprawdzić, w jakim sensie dualizacja porównania daje izomorfizmy kohomologii.
2. **DG-10:2127:** twierdzenie porównawcze DG-08 jest w źródle dla skończonych kompleksów; uogólnienie na lokalnie skończone wymaga argumentu filtracyjnego przez skończone podkompleksy i kontroli skończonych nośników cykli oraz ich wypełnień. Fragment DG-10 zawiera szkic tego argumentu, lecz nie stanowi pełnego dowodu bez dodatkowej weryfikacji.
3. **DG-10:2283:** warunek `(k-1)`-spójności i istnienie struktury CW nie mogą być pomijane. Cytowany tekst osobno przywołuje triangulację gładkich rozmaitości; nie jest to konsekwencja twierdzenia Hurewicza.
4. **DG-11:371:** nie mylić podziału jedności podporządkowanego pokryciu z globalną trywializacją wiązki stycznej. Konstrukcja jest sumą lokalnych metryk, a nie globalną identyfikacją `TM\cong M\times\mathbb R^n`.

## Wynik i status

- **13 wystąpień** w tej partii: wszystkie **niejednoznaczne**, każde z **dwoma kandydatami** w migawce. Dla 13 wskazano właściciela z tego samego skryptu; 4 grupy tematów oznaczono do szerszego audytu matematycznego.
- Łącznie po sześciu partiach **78 z 257** wystąpień poddano ręcznemu przeglądowi, **179 pozostaje**. Nie oznacza to usunięcia niejednoznaczności w bazie ani poprawienia plików TeX.
- Nie wykonano zmian w oryginalnych `\label`, `\ref`, `\eqref`, rozdziałach `chapters/pl/` ani w `main`. Nie dokonano scalania skryptów i nie usunięto żadnego wariantu dowodu.
- **Nowa reguła globalna:** wszelki materiał kopiowany z Biblioteki zachowuje dokładnie źródłowe etykiety i odsyłacze; konflikty między skryptami są dokumentowane i rozwiązywane jawnie, nie milczącymi zmianami nazw.

**Następna partia:** wystąpienia 79–91. Dodatkowy priorytet: pogłębiony audyt matematyczny wersji gładkiej lematu o małych łańcuchach i argumentu dla lokalnie skończonych triangulacji.