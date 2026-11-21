# Topologia algebraiczna — TOP-23, audyty I–V

**Data:** 21 listopada 2026.  
**Repozytorium:** `dariusz-piekarz/mathematical_scipts`.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6` (bez zmian w `main`).  
**Plik:** `chapters/pl/algebraic_topology/23-kohomologia-snopow-z-nosnikami-i-podstawy-dualnosci-verdiera.tex`.  
**Końcowy blob źródła:** `4a441b1dc247e6c6a3443d516012e989f50d90f6` (**948 wierszy**).  
**Punkt wyjścia:** `TOP_23_24_ITERACJA_22_2026-11-21.md`.  
**Zakres:** wyłącznie istniejące definicje, lematy, twierdzenia, dowody, przykłady i rysunki. Nie dodawano nowych wyników. Zastosowano globalną zasadę **chart = mapa**, **mapping = odwzorowanie**.

## Audyt I — definicje i samodzielność twierdzeń

Przejrzano cały rozdział od definicji snopu przez kohomologię o nośnikach, ciąg Mayera–Vietorisa, kryterium Leraya, de Rhama, kategorię pochodną, dualność Verdiera i lokalizację do kohomologii O(m) na P¹ i parowania Serre’a.

Poprawiono:
- Jawne wprowadzenie przestrzeni X, ciała k, snopu F, pokrycia U i lokalnej mapy współrzędnych w sformułowaniach, gdzie były używane wyłącznie przez kontekst.
- Kryterium Leraya i identyfikację naturalnego izomorfizmu \`Cech H^0(U,F) ≅ F(X)\` zamiast nieobjaśnionej równości obiektów.
- Hipotezy twierdzenia o lokalnym kompleksie dualizującym na drugoprzeliczalnej n-rozmaitości bez brzegu.
- Konsekwentne \`odwzorowanie ograniczenia\`, \`odwzorowanie do punktu\`, \`odwzorowanie porównawcze\`, \`właściwość odwzorowania\`, przy zachowaniu poprawnej \`mapy\` w znaczeniu chart i stabilnych etykiet.
- Odmianę nazwy Borela–Moore’a.

**Commit:** `ebff26e5d83287dc24c03fd2e6a4878760a2a770`.

## Audyt II — krytyczna kontrola funktorów pochodnych

W dowodach Mayera–Vietorisa i lokalizacji wcześniejszy tekst wyprowadzał identyfikację
\[
R\Gamma_c(X,j_!\mathcal G)\simeq R\Gamma_c(U,\mathcal G)
\]
wyłącznie z dokładności j!. Jest to logicznie niewystarczające: dokładność funktora nie zapewnia bez dalszego twierdzenia zgodności z prawym funktorem pochodnym innego funktora.

Poprawiono oba dowody. Zaznaczono, że krótki ciąg dokładny snopów daje trójkąt dokładny i długi ciąg po zastosowaniu RΓ_c, natomiast identyfikacja członów przez j! wymaga osobnego, standardowego twierdzenia o pochodnych sekcjach o nośnikach zwartych (możliwego do wykazania przez odpowiednie rezolucje acykliczne). Dla domkniętego i zastosowano dokładność i_* oraz zachowanie snopów iniektywnych.

Ujednolicono termin **rezolucja** zamiast „rezolwenta” w znaczeniu konstrukcji homologicznej.

**Commit:** `703b704c6b538af7e98722ea0f173ffdcafba661`.  
Dodano niezależne regresje poprawnej zgodności pochodnej, samodzielnych hipotez, terminologii i zagnieżdżenia środowisk — **commit** `24b789453c86b5989de56832b7bbd2a7aad23b1c`.

## Audyt III — snopy rozwiązań operatorów różniczkowych

Ponowna lektura ujawniła pominiętą przesłankę w przykładzie snopu rozwiązań \`Pf=0\`. Sam warunek zgodności P z ograniczeniami nie zapewnia struktury przestrzeni wektorowej rozwiązań: operator P musi być **liniowy**. Sprecyzowano ten warunek i rozróżniono współczynniki rzeczywiste dla funkcji gładkich i form oraz zespolone dla funkcji holomorficznych. Dodano wyjaśnienie, że operator nieliniowy może dawać snop zbiorów bez struktury wektorowej.

**Commity:** `f864913b058716a1ea8e650dfe63404ed8652148` (źródło), `cbed56a1c7c182428c8a3197871fb1c560de58ca` (ochrona testowa). Naprawiono dwa błędy nowych testów: frazę przejętą z poprzedniego rozdziału oraz zbyt wiele ukośników odwrotnych w dosłownych fragmentach LaTeX. **Commity:** `60818993ccb3941fd5cff8f7cc883d54482c1e12`, `c1ee1824a87257b23c67e4e56b067d514bc7162d`. Następne pełne przebiegi regresji zakończyły się sukcesem.

## Audyt IV — diagram parowania i zakres dowodów

Na powiększonym PDF zauważono, że pozioma strzałka w diagramie parowania Serre’a mogła sugerować nieistniejące odwzorowanie \`H¹(P¹,O(-3)) → H⁰(P¹,O(1))\`, zamiast parowania biliniowego dwóch argumentów. Usunięto taką strzałkę, zaznaczając symbol parowania pomiędzy przestrzeniami; obie przekątne prowadzą teraz do jawnych wartości biliniowego parowania. Nie zmieniono wzorów matematycznych ani definicji.

W podsumowaniu skorygowano przesadne sformułowanie o „udowodnieniu warunku snopowego”: warunek ten jest definicją; rzeczywiście wykazano kryterium dokładności na kiełkach i obliczenie Cech H⁰.

**Commity:** `24974f0b5d996d4d94aa7d1b618b95fc4a2c7d52` (źródło), `8fcddb2d3faca0d036dc52c85eef148c0726048a` (test).

## Audyt V — niezależna kontrola końcowa i CI

Na końcowym blobie źródła sprawdzono:
- **22/22 unikalne etykiety**, **11/11 domkniętych odsyłaczy**, **2 rysunki TikZ**, **0** błędów zagnieżdżania środowisk i **0** niedomkniętych środowisk.
- Właściwe rozróżnienie chart=mapa i mapping=odwzorowanie; brak starych form w znaczeniu rezolucji homologicznej.
- Wzory lokalnej kohomologii węzła, przesunięcie \`i^!k_R ≃ k[-1]\`, działanie monodromii na okręgu oraz formułę dualności Verdiera. Istnienie nadzwyczajnych funktorów i twierdzenia porównawcze pozostały jawnie **zewnętrznymi** zależnościami.
- Rachunek kohomologii \`H^q(P¹,O(m))\` i parowania Serre’a: **167 480** sprawdzeń współczynników macierzy parowania dla \`-80≤m≤-2\`, bez niezgodności; ponadto **377** kontroli dokładności mapy diagonalnej na skończonych ciałach.
- Kompilację kontrolną TOP-01–24: końcowy dokument ma **270 stron**, TOP-23 obejmuje strony **251–260**, tj. **10 stron** w wydzielonym PDF. Obejrzano podgląd każdej strony i powiększono obydwa rysunki; brak kolizji, obcięć i nieczytelnych podpisów.
- Końcowy log: **0** błędów LaTeX, **0** nierozwiązanych odsyłaczy, **0** przepełnionych wierszy. Trzy ostrzeżenia Underfull hbox pochodzą z innych rozdziałów.

### Potwierdzone GitHub Actions

- [LaTeX TOP-23/24 z poprzednimi rozdziałami](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44942054200): **completed / success**, SHA `8fcddb2d`.
- [Testy aplikacji, regressje i przeglądarka](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44942054198): **completed / success**, SHA `8fcddb2d`.
- [Kontrola międzytomowa AT–DG–AG](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44942037282): **completed / success**, SHA `24974f0b` — ten sam końcowy stan źródła TOP-23 (późniejszy commit zmienił tylko test).

Jeden wcześniejszy przebieg LaTeX nie rozpoczął kompilacji z powodu chwilowego problemu instalacji pakietów \`lmodern\` i \`poppler-utils\` na runnerze GitHub; **najnowszy przebieg jest zielony**.

**Decyzja:** TOP-23 **STABILNY PO AUDYCIE V**. Zachowano wyniki matematyczne i wszystkie etykiety; poprawiono hipotezy, dwa przejścia pochodne, przykład snopu rozwiązań i diagram biliniowy. Nie dodano nowych twierdzeń ani lematów. Następny etap: **TOP-24**. Automatyzacje pozostają wyłączone.
