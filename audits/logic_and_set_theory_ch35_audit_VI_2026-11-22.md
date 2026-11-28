# Logika matematyczna i teoria mnogości — audyt VI rozdziału 35

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/35-modele-boolowskie-i-wzgledna-niesprzecznosc-ch.tex.  
**Blob wejściowy:** bb799ab39a13d9a577b07caaba24e3e00b6bca7e.  
**Blob po audycie:** 53b8d212d00a6f92e710d91fb35b6a7805eb5388.  
**Werdykt:** audyt VI **nie jest czysty**, gdyż istotnie uzupełniono pominięty atomowy krok dowodu równoważności wymuszania porządkowego i semantyki boolowskiej. Walidacja po zmianach jest zielona. Następny audyt powinien rozpocząć się od nowego bloba źródła.

## 1. Kontrola głównych twierdzeń i zależności

Zweryfikowano ponownie: rekurencję nazw i wartości boolowskich; tożsamości równości i podstawiania; lemat mieszania i pełności; konstruktory aksjomatów ekstensjonalności, pustego zbioru, pary, nieskończoności, sumy, wyróżniania, zbioru potęgowego, zastępowania, ufundowania i wyboru; istnienie ultrafiltru zewnętrznego; poprawność ilorazu i lemat prawdy; wymuszanie CH oraz jego zaprzeczenia; końcowy wniosek o względnej niesprzeczności.

Sprawdzono w szczególności, że w przypadku zbioru potęgowego porównuje się boolowską równość nazw, a nie dosłowną zgodność ich dziedzin; w przypadku ufundowania minimalizuje się rangę po wszystkich nazwach; w przypadku ultrafiltru nie zakłada się zamknięcia na dowolne kresy górne; w dowodzie dla dowolnego modelu ZFC nie korzysta się z istnienia przeliczalnego tranzytywnego modelu.

## 2. Wykryty i uzupełniony skrót dowodowy

W Lemacie **lem:boolean35-poset-truth** tekst audytu V wyprowadzał odwrotny przekład nazw boolowskich, ale atomowy krok dowodu równoważności pozostawał streszczony zdaniem, że „klauzule gęstościowe odpowiadają nierównościom boolowskim”.

Dodano samodzielny dowód kryterium:

  i(p) ≤ b  ⇔  ∀q≤p ∃r≤q (i(r)≤b).

Ważne: z i(t)≤i(p) **nie** wnioskujemy t≤p, tylko zgodność t,p i istnienie ich wspólnego wzmocnienia. Oba kierunki kryterium wynikają z gęstości obrazu i(P) w RO(P)^+ oraz niezerowości i(r).

### Atomowa przynależność

Niech v = ∨_{(π,s)∈τ}(i(s)∧⟦σ^B=π^B⟧). Z klauzuli p⊩σ∈τ i hipotezy indukcyjnej dla r⊩σ=π, r≤s wynika i(r)≤v dla gęsto wielu r≤p, stąd i(p)≤v. Odwrotnie, jeśli i(p)≤v, to dla q≤p rozdzielność daje parę (π,s) z niezerowym i(q)∧i(s)∧⟦σ^B=π^B⟧. Gęstość obrazów oraz **kolejne** wspólne wzmocnienia pozwalają znaleźć r≤q,s z i(r)≤⟦σ^B=π^B⟧. Hipoteza indukcyjna daje r⊩σ=π; to dokładnie klauzula przynależności.

### Atomowa równość

Dla każdej pary (π,s)∈σ warunek i(p)∧i(s)≤⟦π^B∈τ^B⟧ jest równoważny klauzuli: każdy q≤p,s ma dalsze wzmocnienie wymuszające π∈τ. Udowodniono oba kierunki, wykorzystując niezerowy fragment sprzeczny z nierównością w kierunku odwrotnym. Biorąc kres dolny po parach z obu nazw, dostajemy wartość boolowską równości, z uwzględnieniem łączenia powtarzających się argumentów i tożsamości ∧(a_j⇒c)=(∨a_j)⇒c.

Osobno wyjaśniono, dlaczego dowód jest syntaktyczny i można go zinterpretować wewnątrz dowolnego modelu ZFC, mimo że rozdział 33 formułował twierdzenie o definiowalności w modelu tranzytywnym.

**Commity źródła:**
- 55a9db15034faa6e7d7035e2195648c1fa469cf7 — szczegółowy dowód atomowy;
- 59bedf00e40c495056334483e6f14ac08e1491f9 — odsyłacz do gęstości;
- 02bccf894a5ed27bf3ae3fb1e76d3d2bdc498875 — syntaktyczna interpretacja w modelu nietranzytywnym.

## 3. Niezależna regresja semantyki

Dodano metodę **test_atomic_forcing_truth_for_all_small_preorders** w tools/tests/test_logic_and_set_theory_ch35.py, commit **ee0231d423a359967318dc8a1d9864d727ec2238**.

Test implementuje **oddzielnie** rekurencyjne klauzule wymuszania z rozdziału 33 i wartości boolowskie nazw z rozdziału 35. Obejmuje wszystkie **4** preordery na dwóch oraz wszystkie **29** preorderów na trzech oznaczonych elementach (także nierozdzielające) i wybrane nazwy do drugiego poziomu rangi. Przeprowadzono **40 446 porównań** równoważności dla atomów przynależności i równości. Wynik: **wszystkie poprawne**. Liczba metod testowych w rozdziale 35: **19**.

Test nie jest ogólnym dowodem ani formalizacją w Lean, lecz stanowi regresję przeciw błędom w definicji przekładu i semantyki.

## 4. LaTeX, redakcja i wynik CI

Struktura tekstu: 8 definicji, 8 lematów, 6 twierdzeń, 4 uwagi, 1 przykład, 14 dowodów, 28 różnych etykiet, 32 odsyłacze. Bez błędów parowania środowisk, bez powtórzonych etykiet.

**GitHub Actions [45049853786](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45049853786): SUCCESS**, commit 02bccf894a5ed27bf3ae3fb1e76d3d2bdc498875. Przeszły testy całej książki, w tym 19 metod rozdziału 35, kontrola inwentarza, kompilacja LaTeX, walidacja PDF i logu. Faktyczny artefakt z tego przebiegu został pobrany i rozpakowany.

Książka: **309 stron**; rozdział 35 na stronach PDF **296–309**, łącznie **14 stron**. Wszystkie strony rozdziału zostały wyrenderowane i obejrzane. Nowy dowód, szczególnie na stronie 306, nie ma kolizji ani ucięć. Log: **0 overfull**, **1 underfull hbox** w całej książce (poza poprawką audytu), **0 błędów LaTeX**, brak nierozwiązanych odsyłaczy.

## 5. Status i dalszy tryb

Audyt VI nie jest czysty z powodu rzeczywistego uzupełnienia kluczowego argumentu. **Licznik czystych audytów pozostaje 0.** W następnej iteracji (VII) wykonać nową niezależną kontrolę całego rozdziału, ze szczególnym uwzględnieniem nowego kryterium gęstości, translacji nazw w obie strony oraz dowodu ZFC dla dowolnego ultrafiltru. Po uzyskaniu stabilnej wersji należy przeprowadzić jeszcze jeden audyt potwierdzający, bez dodatkowych zmian w źródle. 
