
# Analiza funkcjonalna — rozdział 10 — audyt 02: niezależny przegląd matematyczny, redakcja i bramka CI

**Data:** 23 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/functional_analysis/10-przestrzenie-beczkowe-i-bornologiczne-twierdzenie-banacha-steinhausa.tex`.  
**Blob źródła przed 10/02:** `bd4797cbc6013f556ef369db918e81a3acaf0e2c`.  
**Blob źródła po 10/02:** `2ea6b36366c8ec4dc1d2ecf8192fae1054c841b0`.  
**Werdykt:** **Z POPRAWKAMI, NIE CZYSTY — 0/2.** Rozdział 11 nie jest dopuszczony do audytu stabilizacyjnego, dopóki rozdział 10 nie osiągnie dwóch kolejnych czystych przeglądów identycznego źródła i zielonego CI.

## Stan wejściowy i wykryta rozbieżność

Zweryfikowano istniejący audyt `10-audyt-1.md`, świeżą wersję rozdziału 10 i bieżące workflow GitHub Actions. **10/01 istniał już w repozytorium i miał status 0/2**, ale końcowy raport błędnie deklarował usunięcie dwóch dubletów: w źródle nadal pozostał zapis rozbity na wiersze `z twierdzenia Mackeya--Arensa (twierdzenie Mackeya--Arensa)`. Pierwszy test 10/01 nie blokował tego wariantu skutecznie. Przegląd 10/02 usunął tę usterkę i wprowadził rzeczywiste odwołanie `Twierdzenia~\\ref{thm:mackey-arens}`, które odsyła do istniejącej etykiety rozdziału 09. W reportażu nie przedstawiamy wcześniejszego błędnego stwierdzenia o usunięciu duplikatu jako faktu.

## Niezależny przegląd 17 dowodów

1. **Polarne i ograniczoność punktowa:** `H°` jest przecięciem domkniętych absolutnie wypukłych przeciwobrazów dysku; pochłanianie jest równoważne ograniczoności punktowej przez skalowanie. Pusta rodzina `H` obsłużona jawnie.
2. **Charakteryzacja beczkowości:** punktowa ograniczoność w `E'` równa się ograniczoności w topologii `σ(E',E)`. W kierunku beczkowość ⇒ równociągłość użyto pochłaniającego `H°`; w kierunku odwrotnym polar `B°`, odwracanie inkluzji i twierdzenie bipolarne z rozdziału 07 dają `U⊂B`.
3. **Twierdzenie Baire'a:** indukcja w zupełnej przestrzeni metrycznej z malejącymi domkniętymi kulami o promieniach `r_n<2^{-n}` daje ciąg Cauchy'ego, którego granica leży w każdym zbiorze otwartym gęstym oraz w początkowym `O`.
4. **Przestrzenie Baire'a są beczkowe:** ponieważ beczka `B` jest pochłaniająca i zrównoważona, `E=∪_{n≥1}nB`; Baire daje wnętrze pewnego `nB`. Użycie zrównoważenia, symetrii i wypukłości sprowadza niepuste wnętrze do otoczenia zera.
5. **Przestrzenie Frécheta i Banacha:** kompletność metryczna tych przestrzeni wraz z punktem 3 i 4 daje beczkowość, bez założenia normowalności przestrzeni Frécheta.
6. **Banach–Steinhaus dla lokalnie wypukłych TVS:** zamknięte absolutnie wypukłe otoczenie `W⊂V` w przestrzeni wartości istnieje dzięki lokalnej wypukłości; `B=∩_{T∈𝒯}T^{-1}(W)` jest beczką z punktowej ograniczoności, więc zawiera otoczenie zera. Nie wymaga zupełności `F`.
7. **Klasyczna zasada jednostajnej ograniczoności:** beczkowość Banacha i równociągłość operatorów przekładają się przez skalowanie na jednakowe oszacowanie norm; potwierdzono brak potrzeby zupełności przestrzeni wartości.
8. **Drugi dowód klasycznego wniosku (Baire):** domknięte zbiory `A_n=\{x: \sup_T||Tx||≤n\}` pokrywają `E`; zbiór o niepustym wnętrzu pozwala oszacować `||Th||≤2N` i jednakowo `||T||≤4N/r`.
9. **Ciągłość punktowej granicy sieci:** liniowość pochodzi z przejścia do granicy. Ponieważ rodzina jest w hipotezie punktowo ograniczona, Banach–Steinhaus daje równociągłość; domknięte `W⊂V` pozwala wywnioskować `T(U)⊂V`. Hipotezy nie da się usunąć dla ogólnych sieci.
10. **Granica ciągu operatorów:** zbieżny ciąg w TVS jest ograniczony jako zbiór wartości, co aktywuje wynik dla sieci bez dodatkowej hipotezy.
11. **Jednostajna zbieżność na zbiorach zwartych:** równociągłość rodziny i ciągłość granicy dają wspólne `U`; pokrycie zwartego `K` skończoną liczbą `x_j+U`, wraz z punktową zbieżnością i rozbiciem na trzy składniki w `W+W+W⊂V`, kończy dowód.
12. **Ograniczoność w topologiach `τ_s` i `τ_b`:** ograniczoność punktowa w `F` implikuje równociągłość operatorów, ta zaś wraz z ograniczonością `B⊂E` daje wspólne pochłanianie `T(B)` przez otoczenia zera.
13. **Funkcjonał Minkowskiego a zbiory pochłaniające ograniczone:** `p_C` jest skończoną seminormą, a ograniczoność `p_C` na `B` daje `B⊂tC` dzięki definicji kresu dolnego i zrównoważeniu `C`; sprawdzono, że nie wymaga się domkniętości `C`.
14. **Kryteria bornologiczności:** (i)⇒(ii) przez jednostkowy podpoziomicowy zbiór seminormy; (ii)⇒(iii) przez ciągłość każdego `q∘T`; (iii)⇒(i) przez identyczność do przestrzeni wyposażonej w seminormy pierwotne oraz `p_C`, która przenosi ograniczone na ograniczone i musi być ciągła.
15. **Przestrzenie unormowane są bornologiczne:** bornivorous `C` pochłania normową kulę jednostkową, zatem zawiera otwartą kulę o promieniu `1/t`. Zupełność nie jest potrzebna.
16. **Przestrzenie beczkowe są przestrzeniami Mackeya:** `ρ⊂τ(E,E')` wynika z twierdzenia Mackeya–Arensa; dla słabo-* zwartego absolutnie wypukłego `K⊂E'` punktowa ograniczoność i beczkowość implikują równociągłość, a więc `p_K` jest `ρ`-ciągła. To zapewnia przeciwną inkluzję.
17. **Topologia Mackeya Banacha:** z beczkowości przestrzeni Banacha i punktu 16 wynika równość topologii Mackeya z normową.

**Wynik:** 17/17 dowodów nie ujawniło nowych kontrprzykładów do twierdzeń ani niejawnych, nieprawdziwych hipotez. Uzupełniono natomiast niżej wskazany przeskok argumentacyjny w przykładzie.

## Przegląd 4 przykładów i uwag

1. **Niezupełne `c_{00}`:** `f_n(x)=nx_n` są punktowo ograniczone na elementach o skończonym nośniku, lecz normy rosną jak `n`; `B=\{x:n|x_n|≤1\}` jest beczką, ale nie otoczeniem zera. Kontrprzykład i wybór `x^{(n)}=n^{-1/2}e_n` są poprawne.
2. **Słaba topologia nieskończenie wymiarowego Banacha:** kula normowa jest słabo domknięta, absolutnie wypukła i pochłaniająca, lecz nie jest słabym otoczeniem zera. **Uzupełniono istotny krok:** bazowe słabe otoczenie zera jest określone skończoną liczbą funkcjonałów `f_1,...,f_m`; ich wspólne jądro ma niezerowy wektor `v`, a cała prosta `Kv` leży w otoczeniu, nie mieszcząc się w ograniczonej kuli.
3. **Bornologiczna, niebeczkowa:** `c_{00}` z normą supremum jest bornologiczna jako przestrzeń unormowana, ale niebeczkowa na podstawie jawnej beczki z przykładu 1; poprawnie obala implikację odwrotną.
4. **Aproksymacja funkcjonału Diraca:** `T_n(φ)=n∫_{[0,1/n]}φ,dλ` ma `|T_n(φ)|≤p_0(φ)`, zatem rodzina jest równociągła i punktowo zbieżna do `φ(0)`. Dla `C^∞([0,1])` (Fréchet) przejście do jednostajnej zbieżności na zbiorach zwartych jest uzasadnione.

W osobnej uwadze o sieciach potwierdzono, że sieć `a_F=0` dla `1∈F` i `a_F=|F|` w przeciwnym razie zbiega do 0, choć zbiór wszystkich jej wartości jest nieograniczony. Zatem dodatkowa hipoteza ograniczoności punktowej w ogólnym twierdzeniu o granicy sieci jest niezbędna.

## Dokonane poprawki

- **Błąd raportu 10/01 a stan faktyczny:** istniejący dublet `twierdzenia Mackeya--Arensa (twierdzenie Mackeya--Arensa)` rzeczywiście usunięto i zastąpiono dokładnym `\\ref{thm:mackey-arens}`. Commit `7d03672b5bf300d2309a4c1e25fd9d69117816da`.
- **Luka wyjaśnienia w przykładzie o słabej topologii Banacha:** uzupełniono konstrukcję niezerowego wektora we wspólnym jądrze skończonej rodziny funkcjonałów i uzasadniono istnienie całej prostej. Commit `c1adfbcc1f75e445b7b5843e9a2c9157e2741a79`.
- **Spójność terminologiczna:** `przestrzeń dualna topologiczna` zastąpiona `przestrzeń sprzężona` w definicjach i zastosowaniach zgodnie z konwencją rozdziału 09.
- **Regresje:** w `tools/tests/test_functional_analysis_ch10.py` poprawiono kontrolę dubletu rozbitego na kilka wierszy, dodano weryfikację 23 etykiet i odsyłaczy w kontekście 01–10, kontrolę parowania środowisk, test skończenie wymiarowego modelu wspólnego jądra oraz sprawdzanie terminologii. Zestaw wzrósł z **7 do 13 testów**, commit `423a3cd8edbeb52c161fa53633e966cf01f3aed5`.
- **CI:** dodano dedykowany workflow `.github/workflows/functional-analysis-ch10.yml` na istniejącej gałęzi. Kompiluje pełny kontekst 01–10 na podstawie `books/pl/functional_analysis.tex`, sprawdza testy, logi LaTeX (m.in. niezdefiniowane odsyłacze, overfull hbox), rozpoznaje kluczowe nagłówki w tekście PDF i publikuje artefakt. Commit po poprawieniu filtrów wyzwalających: `cbc911c72d63865e8f575b380b70bdf94e3d5ca0`.

## Niezależna kontrola strukturalna i zależności

Z odczytu faktycznych plików LaTeX rozdziałów 01–10: **182 etykiety, brak duplikatów**; w samym rozdziale 10: **23 etykiety, 14 odsyłaczy do istniejących celów**. Poprawne parowanie: 5 definicji, 9 twierdzeń, 1 stwierdzenie, 2 lematy, 4 wnioski, **17 środowisk dowodowych**, 4 przykłady, 5 uwag i 2 `enumerate`. Nie znaleziono starych oznaczeń `\\mathbf 1_A`, błędnej „zwartości sekwencyjnej” ani powielonej nazwy twierdzenia Mackeya–Arensa po korekcie.

## Bramka CI i dalsza iteracja

Po wprowadzeniu zmian uruchomił się workflow [Functional analysis — chapter 10 audit #45216752588](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45216752588). **13/13 testów PASS** i przygotowanie kontekstu 01–10 PASS. W chwili zapisu podstawowej wersji tego raportu trwa kompilacja LaTeX i końcowa weryfikacja PDF; wynik należy dopisać po ukończeniu, bez deklarowania PASS przed jego potwierdzeniem. Matematyczne dowody zostały ocenione niezależnie od testów i CI.

**Werdykt 10/02: audyt z korektami, 0/2.** Kolejny krok: po potwierdzeniu zielonego CI niezależny audyt **10/03** na **niezmienionym blob SHA `2ea6b36366c8ec4dc1d2ecf8192fae1054c841b0`**. Rozdział 11 pozostaje poza zakresem.
