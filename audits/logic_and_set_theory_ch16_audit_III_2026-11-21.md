# Logika matematyczna i teoria mnogości — rozdział 16, audyt III

**Data:** 21 listopada 2026. **Źródło:** `logika_rozdzial_16_audyt_II.tex`.  
**Procedura:** pełna kontrola matematyczna, sformułowań, dowodów, przykładów, struktury, rysunku, LaTeX; bez nowych twierdzeń i lematów.

## Problemy wykryte i naprawione

1. **Założenia twierdzenia o rozpoznawalności dowodliwości (najważniejsze).** Samo „efektywne kodowanie symboli” nie wskazywało jawnie algorytmu rozstrzygającego poprawność kodów symboli, ich rodzaje i arności, ani poprawność składni. Sformułowano pełne wymagania: rozstrzygalność składni i kodów, rozstrzygalność zbioru zdań `T`, algorytmiczne sprawdzanie reguł wraz z warunkami ubocznymi. W dowodzie uporządkowano kolejność postępowania: kontrola kodu wejściowego, wypisanie wszystkich słów binarnych według długości, weryfikacja kodów skończonych drzew. Stwierdzenie nie zostało rozszerzone na teorię z nierozstrzygalnym zbiorem aksjomatów.
2. **Dowód istnienia maszyny uniwersalnej.** Rozpisano skończone operacje symulatora: skanowanie i porównywanie zapisów, aktualizacja komórek, przyrost i ubytek indeksów, przeniesienia/pożyczki, przesuwanie fragmentów zakodowanej listy. Jawnie określono działanie na błędnym kodzie pary lub maszyny. Zapis indeksów całkowitych określono jako kanoniczny kod ze znakiem, bez nieistotnych zer wiodących.
3. **Definicja maszyny Turinga.** Jawnie wymagano niepustości alfabetu wejściowego.

## Kontrola pozostałych twierdzeń

- Lematu o jednoznaczności kodowania par: przeanalizowano przypadki obu słów pustych, długości prefiksu oraz odrzucenia złych kodów; poprawność bez zmian.
- Lematu „rozstrzygalny ⇒ rozpoznawalny”: poprawność bez zmian.
- Twierdzenia o nierozstrzygalności problemu stopu: poprawna konstrukcja diagonalna programu `K`, z wymogiem, że `D` kończy się dla każdego wejścia; poprawność bez zmian.
- Twierdzeń o rozpoznawalności `H` oraz o dwóch rozpoznających: akceptacja, odrzucenie i zapętlenie są rozróżnione, a przeplatanie nie czeka na negatywny certyfikat; poprawność bez zmian.
- Wzorów taśmy dla `L/P/S`: w każdym kroku używany jest symbol **zapisany** `c`, nie symbol odczytany `a`. Puste fragmenty mają długość zero, a długości są jawnie przechowywane; poprzednia poprawka zachowana.

## Walidacja

- Testy regresyjne łącznie: **13/13 PASS**. W tym nowy test 8400 wielokrokowych przejść, również przez komórki o indeksach ujemnych i z zapisem innego symbolu.
- Kompilacja `latexmk` / `pdflatex`: **PASS**. PDF samego rozdziału: **7 stron**.
- **0** `Overfull \\hbox`, **0** `Underfull \\hbox` (w logu lokalnym). Rysunek przekątniowy i wszystkie 7 stron obejrzane.
- Materiał: **5 twierdzeń, 2 lematy, 1 wniosek, 8 dowodów, 5 definicji, 6 przykładów, 4 uwagi, 1 rysunek** — bez zmian inwentarza.
- **13 etykiet, 9 odsyłaczy**; cele istniejące we wcześniejszych rozdziałach potwierdzono na aktualnej gałęzi. `ch:arithmetization` jest planowanym odsyłaczem do przygotowanego rozdziału 17.
- Lokalne starsze kopie rozdziałów generują ostrzeżenia odsyłaczy `ch:zf-axioms` i `thm:ls-second-order-categorical` (poza rozdziałem 16). Na aktualnej gałęzi GitHuba 01–15 brakującym celem był tylko `ch:zf-axioms`.

**Status:** Audyt III zakończony z poprawkami. Wymagana kontrola stabilizacyjna IV przed integracją na GitHubie.