# Biblioteka matematyczna — audyt odsyłaczy, partia 05 (wystąpienia 53–65)

**Data:** 20.11.2026. **Źródła:** `chapters/pl/` na gałęzi `biblioteka-matematyczna-iteracja-6` oraz pełny raport `reference_provenance_audit_355.json` z indeksu 355 rozdziałów. Wystąpienia są liczone w kolejności raportu, nie według numeracji etykiet. **Zakres:** weryfikacja kontekstu użycia i odpowiadających mu deklaracji; bez modyfikowania oryginalnych `\label`, `\ref`, `\eqref`, bez zmian w źródłach i bez scalania książek.

| Nr | Cytujące miejsce | Etykieta | Rzeczywiste cele | Ocena i lokalna propozycja | Status |
|---|---|---|---|---|---|
| 53 | `DG-09:1353` | `thm:homotopia-singularna` | `DG-08:460`, `TOP-05:354` | Poprawnie uzasadnia niezależność `f_*[S^n]` od homotopii reprezentanta. W kontekście `DG-09` preferować `DG-08`. | lokalna propozycja |
| 54 | `DG-09:1440` | `thm:warstwa-komorek` | `DG-08:1498`, `TOP-05:1121` | Wolne generatory względnej homologii `H_n(W,A)` odpowiadają nowym `n`-komórkom. `DG-08` formułuje wynik dla **skończonych** CW; `DG-09:1441` jawnie odwołuje się też do rozszerzenia na pary CW. Preferować `DG-08`, ale osobno zbadać przejście do potencjalnie nieskończonego zbioru komórek. | lokalna propozycja warunkowa |
| 55 | `DG-09:1706` | `eq:formula-komorkowa` | `DG-08:1841`, `TOP-05:1336` | Wzór na współczynniki brzegu komórkowego przez stopnie odwzorowań dołączających odpowiada uzasadnieniu relacji w homologii. Preferować `DG-08`; sprawdzić zgodność orientacji w dalszym dowodzie Hurewicza. | lokalna propozycja |
| 56 | `DG-09:1920` | `thm:homotopia-singularna` | `DG-08:460`, `TOP-05:354` | Teza zapewnia niezmienniczość homologii przy równoważności homotopijnej; drugi odsyłacz dotyczy Whiteheada i nie jest przedmiotem tego konfliktu. Preferować `DG-08`. | lokalna propozycja |
| 57 | `DG-09:1973` | `thm:formula-komorkowa` | `DG-08:1822`, `TOP-05:1318` | Twierdzenie daje dokładnie współczynniki brzegu komórkowego używane do identyfikacji podgrupy relacji. Preferować `DG-08`. | lokalna propozycja |
| 58 | `DG-09:2185` | `thm:homologia-sfer` | `DG-08:1138`, `TOP-05:794` | Homologia sfery i dysku względem brzegu ma odpowiednie grupy `\mathbb Z`, co odpowiada porównaniu z homotopią. Preferować `DG-08`. | lokalna propozycja |
| 59 | `DG-09:2275` | `thm:homologia-sfer` | `DG-08:1138`, `TOP-05:794` | W połączeniu z Hurewiczem daje `\pi_n(S^n)\cong\mathbb Z` dla `n\ge 2`; preferować `DG-08`. | lokalna propozycja |
| 60 | `DG-09:2287` | `def:stopien-sfer` | `DG-08:1777`, `TOP-05:1283` | Definicja stopnia jako działania na `H_n(S^n;\mathbb Z)` jest zgodna z wnioskiem dla `\pi_n`. Preferować `DG-08`. Przypadek opartych i nieopartych odwzorowań wymaga zachowania rozróżnienia w sąsiednim argumencie. | lokalna propozycja |
| 61 | `DG-09:2356` | `prz:homologia-rp2` | `DG-08:2060`, `TOP-05:1476` | Przykład oblicza `H_2(\mathbb{RP}^2;\mathbb Z)=0`, więc ilustruje konieczność założenia jednospójności w twierdzeniu Hurewicza. Preferować `DG-08`. | lokalna propozycja |
| 62 | `DG-10:11` | `ch:homologia-przestrzeni` | `DG-08:2`, `TOP-05:2` | Wprowadzenie do porównania kohomologii de Rhama z homologią singularną cytuje wcześniejszy rozdział tego samego skryptu. Preferować `DG-08`. | lokalna propozycja |
| 63 | `DG-10:1426` | `thm:les-kohomologia` | `DG-06:774`, `TOP-03:646` | Podano stopniowo dokładny krótki ciąg kompleksów kochainowych form, a `DG-06` gwarantuje długi ciąg kohomologii. Preferować `DG-06`. Dodatkowo skontrolować znak w formule homomorfizmu łączącego (zależność od konwencji mapy różnicy). | lokalna propozycja warunkowa |
| 64 | `DG-10:1427` | `ch:algebra-homologiczna` | `DG-06:2`, `TOP-03:2` | Cytowanie wskazuje bezpośrednio na algebraiczną konstrukcję długiego ciągu kohomologii w `DG-06`; preferować `DG-06`. | lokalna propozycja |
| 65 | `DG-10:1600` | `prz:homologia-cw-torus` | `DG-08:2018`, `TOP-05:1448` | Komórkowy rachunek `H^1_{\mathrm{dR}}(T^2)\cong\mathbb R^2`, `H^2_{\mathrm{dR}}(T^2)\cong\mathbb R` opiera się na przykładzie homologii torusa oraz późniejszym twierdzeniu de Rhama. Preferować `DG-08`; nie mieszać grup homologii z grupami de Rhama bez tego twierdzenia. | lokalna propozycja |

## Ustalenia i kwestie do pogłębienia

1. **13/13 to wystąpienia niejednoznaczne**, bez brakujących deklaracji. Wszystkie mają semantycznie odpowiedni lokalny cel w obrębie skryptu geometrii różniczkowej, ale **żaden nie został automatycznie naprawiony**. Kandydat lokalny to propozycja właściciela, nie nowe `\label` ani zmieniony `\ref`.
2. W `DG-09:1440` twierdzenie o względnej homologii warstw dotyczy skończonych CW; zastosowanie do dowolnej liczby komórek wymaga precyzyjnego argumentu przejścia do granicy po skończonych podkompleksach. Nie można tego ukryć samą naprawą odsyłacza.
3. W `DG-09:1706` i `DG-09:1973` należy sprawdzić orientacje i znaki stopni w formule brzegu komórkowego.
4. W `DG-10:1426–1439` sprawdzić dokładność ciągu kompleksów form (rozkład jedności) oraz sign convention mapy `s(\alpha,\beta)=\alpha|_{U\cap V}-\beta|_{U\cap V}` i homomorfizmu łączącego; nie zmieniać konwencji bez śledzenia jej w całym rozdziale.
5. **Stan przeglądu: 65/257 wystąpień z migawki, 192 pozostałe.** To licznik audytu i propozycji, **nie licznik naprawionych odsyłaczy**. Nie wykonano w tej partii pełnej kompilacji `xr-hyper` ani pełnego audytu dowodów.

**Zasada globalna:** przy kopiowaniu materiału z Biblioteki zachowywać wszystkie oryginalne `\label{...}`, odsyłacze (`\ref`, `\eqref`, `\cref`, ...) i ich pochodzenie. Kolizje rejestrować jawnie. Scalanie poszczególnych działów dopiero po ich skompletowaniu, zaczynając od fundamentów matematyki i zachowując wszystkie różne dowody.

**Następna partia:** wystąpienia 66–78; równolegle pogłębiony audyt przejścia od skończonych do dowolnych kompleksów CW i znaków w ciągu Mayera–Vietorisa dla form.