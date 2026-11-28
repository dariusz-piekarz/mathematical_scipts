# Topologia algebraiczna — TOP-22, audyty stabilizacyjne I–IV

**Data:** 21 listopada 2026 r.  
**Repozytorium:** dariusz-piekarz/mathematical_scipts  
**Gałąź:** biblioteka-matematyczna-iteracja-6 — bez zmian w main.  
**Źródło:** chapters/pl/algebraic_topology/22-kohomologia-z-nosnikami-zwartymi-i-homologia-borel-moore-a.tex.  
**Końcowy blob:** d2b5aa8c3167f6007582da0e6645b49eaa934165, **642 wiersze**.  
**Punkt wyjścia:** audits/history/TOP_21_22_ITERACJA_21_2026-11-21.md.  
**Standard:** bez dodawania nowych twierdzeń ani lematów. Pełna kontrola poprawności matematycznej, hipotez, przejść dowodowych, przykładów, języka, rysunków, etykiet, odsyłaczy, PDF i CI; ponowienie audytu aż do braku usterek.

## Audyt I — hipotezy, notacja i terminologia

Przeczytano cały rozdział: definicję H_c przez granicę prostą par, funkcjonalność dla odwzorowań właściwych, kompleks form o nośniku zwartym, operator całkowania po włóknie, kompleks lokalnie skończonych łańcuchów singularnych, dualność Poincarégo dla rozmaitości niezwartych, przykłady jednopunktowego uzwarcenia i sumy prostych.

Wprowadzono 21 korekt:
- Uzupełniono warunek „bez brzegu” w odwołaniu do zwykłej dualności zwartej rozmaitości na początku rozdziału.
- W stwierdzeniach o naturalności H_c oraz właściwym odwzorowaniu w homologii BM jawnie określono X, Y, współczynniki w grupie abelowej G i stopień k.
- W definicji łańcuchów lokalnie skończonych zlikwidowano lukę: grupa współczynników G i stopień k nie były wcześniej zadane.
- Funkcjonał całkowania na prostej ma teraz określoną dziedzinę Omega_c^1(R), a jego argument postać f dx z f∈C_c^\infty(R).
- Uzupełniono kwantyfikator k∈Z w twierdzeniu o H_c^k(R^n).
- Twierdzenie de Rhama z nośnikami zwartymi sformułowano dla gładkich rozmaitości **bez brzegu**, zgodnie z przedstawioną argumentacją opartą na otwartych kulach współrzędnych; nie podsuwamy nieudowodnionego przypadku brzegowego jako konsekwencji tej samej lokalnej konstrukcji.
- „Otwarty zbiór współrzędnych” zastąpiono „otwartą kulą współrzędnych”, dla której lokalny rachunek jest dokładnie właściwy.
- Wyrażenie „rezolwenty snopowe” zastąpiono prawidłowym terminem „rezolucje snopowe”.
- Zmieniono terminologię **mapping = odwzorowanie** („odwzorowanie właściwe”, „odwzorowanie par”, „odwzorowanie łańcuchowe”, „odwzorowanie stałe”), zachowując **chart = mapa**, np. „przy przejściu między mapami”.
- W przykładzie właściwego włożenia prostej w R² użyto dokładniejszego terminu „osadzenie”.
- Ujednolicono odmianę nazwisk w „homologia Borela–Moore’a”.
- W przykładzie M=int W zadano jawnie grupę współczynników G.
- Definicję klasy fundamentalnej BM rozszerzono w ramach istniejącej teorii także na rozmaitość **niekoniecznie spójną**, zgodnie z zakresem późniejszego twierdzenia.

**Commit:** 09e9044652a857d80fd4d3706da32bb6e65018a7.

## Audyt II — krytyczna korekta stopniowania w dowodzie dualności

W drugim czytaniu stwierdzono rzeczywisty błąd matematyczny w porównaniu kompleksu kołańcuchów triangulacji z łańcuchami bloków dualnych. Pierwotna wersja zestawiała współczynnik D(τ) w ∂D(σ) ze **współczynnikiem σ w δτ**, który ma niepoprawny stopień przy k-simpleksie σ i (k+1)-simpleksie τ.

Właściwy rachunek brzegu i kobrzegu — przy zgodnie ustalonych orientacjach — jest:

\[
[D(\tau)]\,\partial D(\sigma)
=[\tau^*]\,\delta(\sigma^*)
=[\sigma]\,\partial\tau,\qquad
\dim D(\tau)=n-k-1.
\]

Poprawiono tekst dowodu, wskazując jawnie wymiary σ, τ, D(σ), D(τ) i definicję kobrzegu. Doprecyzowano również globalną lokalnie skończoną klasę fundamentalną w przypadku nieskończenie wielu składowych spójnych. Termin „mapy łączące” jako mapping zastąpiono „odwzorowaniami łączącymi”, podczas gdy „mapy” w znaczeniu chart pozostały bez zmiany.

**Commit źródła:** 7560cf6f1d4b13e8964b2f3ef42caaba93a472e9.

W regresjach application/tests/test_topology_chapters_21_22.py dodano testy poprawnego indeksowania δ(σ*) i ∂τ, zgodności incydencji na zorientowanym 2-sympleksie, samodzielności założeń i terminologii mapa/odwzorowanie.

**Commit testu:** 98cb801cb70b5060b0a3e395cf9aae629b7bf161.

## Audyt III — funkcjonał całkowania i niezależne rachunki

Ponowna lektura poprawiła precyzję lematu na prostej: funkcjonał całkowania indukuje **jeden** izomorfizm H_{c,dR}^1(R)≅R, natomiast zanik H_{c,dR}^0(R) jest osobną własnością, a nie kolejnym izomorfizmem indukowanym przez ten sam funkcjonał.

**Commit:** f2c2291c123d3d3038b5241b54c7cb2872bf0fbf.

Niezależnie zweryfikowano:
- kierunek morfizmów w układzie skierowanym H^k(X,X\K), dla K⊂L;
- znaki I d = -d_x I i d s = -s d_x w rozkładzie omega=alpha+dt∧beta;
- tożsamość dH+Hd=id-sI dla jawnego operatora Pbeta;
- indeksowanie brzegów dualnych i operatorów kobrzegu;
- zachowanie lokalnej skończoności przez odwzorowanie właściwe i różniczkę brzegową;
- H_0^{BM}(N;Z)=∏Z, a H_0(N;Z)=⊕Z, wraz z odrębnością od H_0(N^+,{∞};Z);
- zerowy homomorfizm BM wywołany właściwym osadzeniem R→R²;
- iloczyn H_1^{BM}(⊔_j R_j;Z)=∏_j Z versus sumę prostą H_c^1(⊔_j R_j;Z)=⊕_j Z;
- właściwe f₂(x)=x² i f₃(x)=x³ na H_c^1(R;R): działanie odpowiednio zero i identyczność. Dla znormalizowanej gładkiej funkcji próbnej o zwartym nośniku w [-1,1] całki pullbacków dla potęg 2,3,4,5 wyniosły numerycznie ~0, ~1, ~0, ~1 (odchylenie <2×10⁻¹³ dla 3 i 5).

Nie wprowadzano nowych twierdzeń. Utrzymano jawny charakter **zewnętrznych** twierdzeń używanych w globalnym dowodzie porównania de Rhama i komórkowo-singularnym dowodzie dualności.

## Audyt IV — kontrola końcowa

Na końcowym blobie źródła wykonano niezależną kontrolę strukturalną i wizualną:

- **14/14 etykiet** jest unikalnych i zachowanych;
- **7/7 odsyłaczy** prowadzi do istniejących celów w TOP-21–23;
- **0** błędów zagnieżdżania i niedomkniętych środowisk;
- **2** rysunki TikZ — oba zachowane;
- **0** błędnych użyć „karta” jako chart oraz „mapa” jako mapping;
- **0** wystąpień starego błędnego wyrażenia σ w δτ;
- kompilacja kontrolna TOP-01–23 daje **259 stron**; TOP-22 zajmuje **strony 243–249**;
- utworzono siedmiostronicowy PDF zawierający **tylko** TOP-22. Obejrzano kontaktowy podgląd wszystkich stron i sprawdzono brak treści poza obszarem stron. Oba rysunki są czytelne, bez kolizji podpisów i obcięć;
- drugi przebieg LaTeX: **0** błędów, **0** nierozwiązanych odsyłaczy i **0** przepełnień Overfull hbox. Trzy ostrzeżenia Underfull hbox pochodzą z innych rozdziałów niż TOP-22.

### GitHub Actions — wszystkie PASS dla końcowego źródła f2c2291c

1. [TOP-21/22 — LaTeX z rozdziałami zależnymi TOP-01–23](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44940774002): **completed / success**.
2. [Aplikacja, skan globalnej terminologii, regresje i testy przeglądarkowe](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44940774039): **completed / success**.
3. [AT–DG–AG — zależności i kompilacja](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44940773998): **completed / success**.

**Decyzja:** **TOP-22 STABILNY PO AUDYCIE IV** (plus wcześniejszy audyt pary TOP-21/22). Zachowano cały materiał, wszystkie etykiety, przykłady i rysunki; nie dodano nowych twierdzeń ani lematów. Następny etap według przyjętej kolejności: **TOP-23**. Automatyzacji nie uruchamiano.
