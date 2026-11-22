# Logika matematyczna i teoria mnogości — rozdział 32, audyt I

**Data:** 22 listopada 2026 r.  
**Gałąź:** `biblioteka-matematyczna-iteracja-6`.  
**Źródło:** `chapters/pl/logic_and_set_theory/32-podstawy-wymuszania-i-modele-generyczne.tex`.  
**Tytuł:** „Podstawy wymuszania i modele generyczne”.

## Cel i zakres

Pierwsza pełna wersja rozdziału wprowadza pojęcia wymuszania, zgodności i antyłańcuchów, filtry i zbiory gęste, generyczność względem tranzytywnego modelu ZFC, lemat Rasiowej–Sikorskiego, dodanie ciągu Cohena, gęste podporządki, hierarchię nazw, interpretację nazw i wstępne własności zbioru $M[G]$. Relacja $p\Vdash\varphi$, lemat prawdy i dowód $M[G]\models\mathrm{ZFC}$ są celowo odłożone do rozdziału 33.

## Kontrola matematyczna i poprawki

1. **Konwencja porządku:** silniejszy warunek jest mniejszy ($q\le p$). Definicja filtru słusznie wymaga domknięcia ku słabszym warunkom i skierowania ku silniejszym. Skontrolowano wszystkie użycia w dowodzie Rasiowej–Sikorskiego i przy przenoszeniu filtru przez gęsty podporządek.
2. **Model wyjściowy:** założono zewnętrznie przeliczalny tranzytywny *zbiorowy* model $M\models\mathrm{ZFC}$. Wyjaśniono, że sama syntaktyczna niesprzeczność ZFC nie uprawnia jeszcze do założenia istnienia takiego modelu. Wnioski o niezależności CH nie są tu przedstawiane jako udowodnione.
3. **Generyczność:** zbiór $D_p=\{q:q\le p\text{ lub }q\perp p\}$ rzeczywiście należy do $M$ i jest gęsty. Dowód rozstrzygania warunku przez filtr nie używa niejawnego wyboru. Podobnie sprawdzono konstrukcję $D^\downarrow$ i właściwy kierunek domknięcia.
4. **Rasiowa–Sikorski:** rekurencja po *ustalonej enumeracji* $\mathbb P$ wyznacza ciąg warunków $p_{n+1}\le p_n$. Filtr jako domknięcie ku słabszym warunkom $\{q:\exists n\ p_n\le q\}$ jest skierowany i spotyka wszystkie $D_n$. Dla zewnętrznie przeliczalnego $M$ można wyliczyć wszystkie gęste zbiory należące do $M$.
5. **Cohen:** zbiór $D_n=\{p:n\in\operatorname{dom}p\}$ jest gęsty i należy do $M$. Zatem $c_G=\bigcup G$ jest funkcją całkowitą. Dla dowolnego $x\in (2^\omega)^M$ zbiór $E_x$ jest gęsty i wymusza różnicę $c_G(n)\ne x(n)$ dla pewnego $n$; dowodzi to $c_G\notin M$. Kontrola skończonych warunków zgodnych/niezgodnych jest w teście regresyjnym.
6. **Gęste podporządki:** dowiedziono, że z generycznego filtru $H$ na $\mathbb Q\subseteq\mathbb P$ otrzymuje się filtr na $\mathbb P$ przez domknięcie ku słabszym warunkom. Podzbiór $D_\mathbb Q$ jest gęsty i należy do $M$. Przykład $2^{<\omega}\subseteq\operatorname{Fn}(\omega,2)$ zawiera konstrukcję przedłużenia do odpowiednio długiego ciągu.
7. **Hierarchia nazw:** rozróżniono hierarchię nazw $N_\alpha$ i zwykłe $V_\alpha$. Interpretacja $\tau^G$ jest uzasadniona rekurencją i schematem zastępowania. Nazwy kanoniczne spełniają $(\check x)^G=x$; standardowa nazwa filtru spełnia $(\dot G)^G=G$.
8. **Zakres $M[G]$:** wykazano istnienie zbioru interpretacji nazw, jego tranzytywność, $M\subseteq M[G]$ oraz $G\in M[G]$. Nie przypisano $M[G]$ aksjomatów ZFC bez lematu prawdy i twierdzenia o wymuszaniu.
9. **Precyzja formalna:** wykryto i poprawiono siedem niedookreślonych sformułowań hipotez, w tym brak kwantyfikacji $p',q'$ w lemacie o zgodności, niewymienione jawnie $M,\mathbb P,G$ w lemacie o rozstrzyganiu, założenia o największym warunku przy nazwach kanonicznych i niepełne założenia twierdzenia o $M[G]$.
10. **LaTeX:** pierwszy przebieg CI wykrył błąd w opcjonalnym tytule twierdzenia `[Pierwsze własności $M[G]$]`: nawias zamykający `]` w zapisie matematycznym był traktowany jako koniec argumentu opcjonalnego. Poprawiono nagłówek na `[Pierwsze własności rozszerzenia generycznego]` bez zmiany etykiety ani tezy.

## Inwentarz i testy

- **8 sekcji; 11 definicji, 7 lematów, 4 twierdzenia, 1 wniosek, 4 przykłady, 4 uwagi, 12 środowisk dowodu, 1 rysunek TikZ.**
- **33 etykiety, 11 odsyłaczy** w rozdziale 32; wszystkie etykiety pozostają niezmienione w audycie I.
- Książka została zarejestrowana w `books/pl/logic_and_set_theory.tex` i `catalog/books.json` jako 32. rozdział.
- Pipeline `.github/workflows/logic-and-set-theory-chapter.yml` obejmuje 32 rozdziały, nowe testy `tools/tests/test_logic_and_set_theory_ch32.py`, bilans **803 etykiet i 590 odsyłaczy** dla pełnej książki.
- [Pierwszy przebieg #45014361647](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45014361647): kontrola rejestracji, odsyłaczy, inwentarzy i testy rozdziału 32 **PASS**; kompilacja PDF **FAIL** z powodu błędu nagłówka wskazanego wyżej.
- [Powtórzony przebieg #45014576177](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45014576177): uruchomiony po poprawce nagłówka. Końcowy status wymaga odczytania po ukończeniu; nie wolno zakładać sukcesu bez wyniku CI.

## Werdykt audytu I

**Wykonano rzeczywiste poprawki matematycznej precyzji i LaTeX.** Główne konstrukcje nie wykazały sprzeczności podczas niniejszego audytu, jednak rozdział pozostaje w fazie audytów, a do potwierdzenia aktualnego stanu technicznego potrzebny jest końcowy wynik nowej kompilacji oraz przegląd stron PDF.
