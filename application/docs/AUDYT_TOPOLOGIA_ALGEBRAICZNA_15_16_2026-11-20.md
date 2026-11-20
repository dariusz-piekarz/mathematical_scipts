# Topologia algebraiczna — szczegółowy audyt AT-15 i AT-16

**Data:** 20 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`, bez zmian w `main`.  
**Zakres:** dokładnie dwa kanoniczne pliki `chapters/pl/algebraic_topology/15-operacje-kohomologiczne-naturalnosc-iloczyny-i-relacje.tex` i `16-zawieszenie-twierdzenie-freudenthala-i-homotopia-stabilna.tex`. Poprzednie AT-01–14 stanowią tylko wymagany kontekst matematyczny i źródło celów odsyłaczy.  
**Standard:** szczegółowość dowodów, przykładów i rysunków według pierwszego rozdziału „Geometria różniczkowa”, kontrola hipotez, terminologii, integralności etykiet i kompilacji.

## AT-15 — operacje kohomologiczne

Przeprowadzono kontrolę definicji operacji naturalnych, długich ciągów kohomologii współczynników i homomorfizmu Bocksteina, porównania `Sq¹` z `β₂`, multiplikatywności całkowitego kwadratu, formuły Cartana, relacji Adema, jednomianów dopuszczalnych, operacji na zawieszeniu `ΣCP²` oraz klas Thoma i Stiefela–Whitneya.

1. **Rzeczywisty rachunek Bocksteina:** nowy `prz:bockstein-rp2-komorki-v8` liczy `β₂(t)=t²≠0` z komórkowego kompleksu `RP²`: `∂₂=2`, podniesienie generatora stopnia 1 do `Z/4`, koróżniczka `δã(e²)=2 mod 4`, dzielenie przez 2 i redukcja modulo 2. Dla `RP³` wyjaśnia zarazem `β₂(t²)=0`, nawet przy niezerowej kohomologii stopnia 3. Jest to policzony przykład tożsamości `Sq¹=β₂`, nie zastępnik jej pełnego uniwersalnego dowodu.
2. **Rysunek samodzielny:** `fig:bockstein-rp2-v8` pokazuje kompleksy kołańcuchowe o współczynnikach `Z/4` i `F₂`, redukcje oraz działanie różniczki. Rysunek powstał bez plików zewnętrznych.
3. **Kontrola Adema bez ukrytego lematu:** nowy `prz:adem-rp-niskie-v8` sprawdza `Sq²Sq²=Sq³Sq¹` na każdym jednomianie `t^m` z `H*(RP∞;F₂)`; obie strony wynoszą tam 0. Rozpisano współczynniki `C(m,2)C(m+2,2)` oraz `m C(m+1,3)`. Dowód parzystości jest samodzielny: dla `m=4q+r`, `(1+z)^m=(1+z⁴)^q(1+z)^r` nad `F₂`, a przy parzystym `m+1` `(1+z)^(m+1)` ma tylko parzyste potęgi. **Wyraźnie zaznaczono, że obliczenie na jednym pierścieniu nie dowodzi tożsamości naturalnych operacji na wszystkich przestrzeniach.**
4. **Terminologia:** zastąpiono angielskie `map` tłumaczone jako „mapa” przez „odwzorowanie”, w odpowiednich miejscach: homomorfizm łączący oraz odwzorowanie Hopfa.

## AT-16 — zawieszenie i homotopia stabilna

Skontrolowano definicję zawieszenia zredukowanego, naturalność, warunki spójności, sformułowanie ekscyzji Blakersa–Masseya, zakres Freudenthala, ścisłą nierówność w stabilizacji, obliczenie pierwszego pnia stabilnego, rozszczepienie zawieszenia iloczynu, grupy stabilnych odwzorowań i przykłady widm.

1. **Przypadek niestabilny `q=1` policzony w pełni:** nowy `prz:freudenthal-klein-abel-v8` wychodzi od prezentacji butelki Kleina `π₁(K)=⟨a,b | aba⁻¹=b⁻¹⟩`. Po abelianizacji relacja daje `2[b]=0`, bez relacji na `[a]`, więc `π₁(K)_ab=Z⊕Z/2`. Ponieważ `ΣK` jest jednospójne, Hurewicz i zawieszenie homologii dają `π₂(ΣK)=Z⊕Z/2`. Homomorfizm `E` jest abelianizacją, więc jest surjektywny i nieiniektywny. Wskazano konkretny niezerowy komutator `aba⁻¹b⁻¹=b⁻²` w jądrze, a także kontrast torusa, dla którego abelianizacja jest izomorfizmem.
2. **Jawny układ zawieszeń Hopfa:** nowy `prz:eta-stabilizacja-v8` przeprowadza od `π₃(S²)=Z` przez `π₄(S³)=Z/2` do `π₅(S⁴)=Z/2` i dalszych poziomów. Pierwsza strzałka jest redukcją modulo 2 (`ker E=2Z`), pozostałe od `S³` są izomorfizmami: nierówność Freudenthala `n+1<2n−1` dla `n>2` została sprawdzona jawnie. Odróżniono `π₀^s=Z` i `π₁^s=Z/2`.
3. **Nowy diagram:** `fig:eta-stabilizacja-v8` pokazuje pierwszy surjektywny, lecz nieiniektywny krok oraz następujące izomorfizmy; w pełni osadzony TikZ.
4. **Terminologia:** nazwy `mapa`, `mapy`, `mapę` w znaczeniu odwzorowania zastąpiono właściwymi odmianami „odwzorowanie”; zachowano symbole matematyczne i historyczne etykiety.

## Zastrzeżenia do pełnego zamknięcia luk

- **Cartan (AT-14/15):** AT-15 podaje poprawny rachunkowy dowód postaci multiplikatywnej wzoru *warunkowo* względem twierdzenia o zewnętrznych potęgach kohomologicznych. Nie daje niezależnego dowodu istnienia/normalizacji/multiplikatywności tej operacji z diagonalnych Steenroda. Zastrzeżenie z AT-14 pozostaje otwarte.
- **Adem (AT-14/15):** AT-15 stwierdza i weryfikuje szczególne przypadki, ale nie zawiera pełnej konstrukcji iterowanych diagonalnych ani uniwersalnego dowodu relacji. Szczegółowy przypadek `RP∞` tego nie zastępuje. Zastrzeżenie pozostaje otwarte.
- **Freudenthal (AT-16):** dowód jest poprawny *względem* wcześniej sformułowanego głębokiego twierdzenia Blakersa–Masseya `thm:bm-v8`, któremu w tym rozdziale nie towarzyszy pełny dowód ekscyzji homotopijnej. Pozostała też zależność dowodu niezerowości `Eη` od stabilności kwadratów Steenroda; to twierdzenie zostało przywołane, nie wyprowadzone konstrukcyjnie z diagonalnych.
- Nie należy podawać tych zależności jako nowych, w pełni niezależnych dowodów. Odpowiednie luki powinny pozostać otwartymi pozycjami kolejnych prac.

## Kontrole techniczne

- Wszystkie **11** standardowych wywołań odsyłaczy w AT-15/16 mają etykiety docelowe w AT-01–16. Brak powielonych deklaracji etykiet w tych szesnastu rozdziałach; historycznych `\label` nie usuwano ani nie przemianowywano.
- AT-15 ma **1**, AT-16 **2** rysunki TikZ po zmianach, bez zależności od zewnętrznych obrazów, bibliotek kodu czy danych.
- Dodano `application/tests/test_topology_chapters_15_16.py`: testy integralności książki, odsyłaczy, historycznych etykiet, środowisk TeX, arytmetyki Bocksteina, sprawdzenia Adema, abelianizacji Kleina, zakresów Freudenthala i statusu zależności dowodowych.
- Dodano `.github/workflows/algebraic-topology-audit-ch15-16.yml` z dwukrotną kompilacją AT-01–16 oraz kontrolą brakujących odsyłaczy i przepełnionych wierszy. **Wyniki CI i kontrolę rysunków należy dopisać wyłącznie po ich faktycznym potwierdzeniu**.

## Plan

Po zakończeniu kontroli CI i PDF zarejestrować AT-15 i AT-16 z właściwymi zastrzeżeniami w `application/data/AUDYT_ROZDZIALOW.csv`. Następna para do audytu: **AT-17 i AT-18**. Nie wykonywano żadnego scalania ani zmian na `main`.
