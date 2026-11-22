# Logika matematyczna i teoria mnogości — audyt I rozdziału 39

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/39-slaba-zwartosc-charakterystyki-i-logika-infinitarna.tex.  
**Blob źródła:** 9d06016d71a4c42434b8f0a58c13f666160a4034.  
**Werdykt matematyczno-redakcyjny:** w pierwszym przeglądzie nie znaleziono koniecznej poprawki dowodowej; status **kandydujący do pierwszego czystego audytu**. Techniczna walidacja musi uwzględniać kompilację po najnowszych korektach językowych wcześniejszych rozdziałów.

## 1. Audyt głównych implikacji

**Własność drzewa ⇒ relacja podziałowa z mniej niż κ kolorami.** Dla kolorowania c:[κ]^2→μ, 0<μ<κ, stworzono profile f_α:α→μ i drzewo wszystkich ich ograniczeń. Małość poziomów wynika dokładnie z μ^{|δ|}<κ, co wymaga silnej graniczności. Gałąź b daje dla każdego δ świadka a(δ)≥δ z f_{a(δ)}|δ=b|δ. Na nieograniczonym zbiorze D wartości b(a(δ)) mają jeden kolor i, ponieważ κ jest regularną liczbą kardynalną, a μ<κ. Rekurencja dobiera δ_ξ większe od wszystkich wcześniejszych a(δ_η), co daje jednorodny zbiór o mocy κ. Osobno sprawdzono przypadki μ=1 oraz δ=0.

**Relacja podziałowa ⇒ własność drzewa.** Wybór porządku leksykograficznego na ścieżkach poprzedników zachowuje porządek drzewa i rozdziela stożki dwóch nieporównywalnych węzłów. Kolorowanie porównuje porządek indeksów w enumeracji T z porządkiem leksykograficznym. Dla jednorodnego H zdefiniowano A jako węzły mające κ wielu potomków indeksowanych przez H. Każdy poziom T_δ spotyka A: mniej niż κ wcześniejszych poziomów ma razem moc <κ dzięki regularności, a sam T_δ ma moc <κ. Dwa nieporównywalne s,t∈A dawałyby dwa nieograniczone zbiory indeksów, z których wszystkie elementy jednego musiałyby poprzedzać wszystkie elementy drugiego, co jest niemożliwe. Dlatego A jest gałęzią współkońcową.

**Własność drzewa ⇒ zwartość infinitarnej logiki zdaniowej.** Dla teorii Σ o mocy κ każde T_α składa się z wartościowań v:α→2 spełniających te formuły o indeksach ξ<α, których nośniki mieszczą się w α. Lokalne spełnianie zapewnia niepustość poziomu, silna graniczność jego moc <κ, a ograniczanie wartościowań domyka drzewo na poprzedniki. Gałąź daje pełne wartościowanie. Każdy nośnik ma moc <κ i jest ograniczony w regularnej κ, więc każda formuła w końcu pojawia się w wymaganiach na pewnym poziomie.

**Zwartość zdaniowa ⇒ własność drzewa.** Zmienna p_t koduje wybór węzła, alternatywy po poziomach wymuszają obecność węzła na każdej wysokości, a klauzule zapobiegają wybieraniu dwóch nieporównywalnych węzłów. Teoria ma κ formuł, każda o nośniku mocy <κ. Dowolny podzbiór teorii mocy <κ jest spełniany przez ścieżkę do węzła na poziomie powyżej wszystkich wymienionych wymagań poziomów; regularność κ zapewnia istnienie tego poziomu. Globalne spełnianie daje gałąź współkońcową.

**Relacja podziałowa ⇒ regularność.** W przypadku singularnego κ istnieje podział κ na μ=cf(κ)<κ przedziałów o mocach <κ. Kolorowanie par przez równość indeksu przedziału nie może mieć jednorodnego zbioru mocy κ w żadnym kolorze.

## 2. Zakres i zabezpieczenia

Każda równoważność w rozdziale jest formułowana **dla silnie nieosiągalnej liczby kardynalnej** κ. Nie stwierdzono nieudowodnionej implikacji z samej relacji podziałowej do silnej graniczności. Zasada logiczna dotyczy **infinitarnej logiki zdaniowej z nośnikami mniejszymi niż κ**, a nie bez dodatkowego argumentu pełnej logiki pierwszego rzędu L_{κ,κ}. Rozdział celowo oddziela te zakresy.

Porównano sformułowanie kombinatorycznej równoważności z literaturą: J. Roitman, *Introduction to Modern Set Theory*, Theorem 7.54 (https://math1um.github.io/Teaching/roitman-set-theory.pdf). Właściwe argumenty dla profili i kodowania teorii są samodzielnie przedstawione, a zgodność znanej równoważności nie zastępuje audytu kroków dowodu.

## 3. Inwentarz i regresje

Rozdział 39 ma **949 wierszy, 22 etykiety, 25 odsyłaczy, 4 definicje, 4 lematy, 6 twierdzeń, 2 wnioski, 4 uwagi, 1 przykład i 12 dowodów**. Dodano dziewięć testów: pełna integralność katalogu, parowanie środowisk, rozwiązanie etykiet, globalne sprawdzenie pełnego rzeczownika „liczba kardynalna” w rozdziałach 37–39, skończone profile, leksykograficzne stożki, teorię zdań kodującą gałąź i małe nośniki.

W pierwszym przebiegu **[CI 45070358451](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070358451): SUCCESS** testy i kompilacja rozdziałów 01–39 były poprawne. Nowe korekty wymuszone przez zasady terminologiczne dotyczą też wcześniejszych rozdziałów 34 i 35; po nich należy oddzielnie potwierdzić CI.

## 4. Powiązany audyt terminologii

W źródłach wszystkich 39 rozdziałów skontrolowano wystąpienia skróconego rzeczownika „kardynał”; niepoprawne formy w rozdziałach 34, 35, 37 i 38 zastąpiono pełną nazwą i odpowiednią odmianą. W globalnych dokumentach AGENTS.md i docs/pl/standardy_terminologiczne.md zapisano nową regułę. W historycznych raportach audytowych rozdziałów 37–38 wprowadzono korekty czysto językowe w niniejszym commicie. Istniejące etykiety LaTeX oraz ścieżki plików pozostawiono bez zmian.

## 5. Dalszy tryb pracy

Po potwierdzonym zielonym CI należy wykonać niezależny audyt II na niezmienionym źródle rozdziału 39, a następnie powtórzyć kontrole do uzyskania dwóch czystych audytów i dodatkowego audytu potwierdzającego. Sukces Python i LaTeX nie oznacza weryfikacji dowodów przez jądro Lean.
