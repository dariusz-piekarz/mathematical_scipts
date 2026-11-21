# Algebra liniowa — rozdział 27, audyt II (korekta ścisłości)

**Data:** 21 listopada 2026  
**Źródło:** `chapters/pl/linear_algebra/27-gramiany-obserwowalnosci-i-realizacje-minimalne.tex`  
**Blob po korekcie:** `b2042d62fe076a6efbf3bcbaea6c2b82d058e358`.

## Wykryta luka

W pierwotnym dowodzie Twierdzenia `thm:lin27-minimal-uniqueness` sformułowanie „wspólna ranga odpowiednio dużej macierzy Hankela” nie zawierało jawnego dowodu, że dla *dwóch* realizacji o być może różnych wymiarach można wybrać jedną i tę samą macierz Hankela, której ranga jest jednocześnie ich wymiarem minimalnym. Wymagało to wykazania stabilizacji obrazu `K_N` i jądra `O_N` dla dostatecznie dużego N.

## Poprawka

1. Niech d_1, d_2 oznaczają wymiary dwóch realizacji minimalnych, a `N=max(d_1,d_2,1)`.
2. Dla każdej realizacji dodatniego wymiaru d_i≤N, twierdzenie Cayleya–Hamiltona pokazuje, że `im K_N=R_i` i `ker O_N=N_i`. Z faktoryzacji `H_(N,N)=O_N K_N` i pełnej sterowalności/obserwowalności realizacji minimalnej wynika `rank H_(N,N)=d_i`.
3. Równość wszystkich parametrów Markowa daje identyczne macierze `H_(N,N)`; ich wspólna ranga wymusza `d_1=d_2`.
4. Osobno objaśniono przypadek wymiaru zero. Dopiero po tym kroku buduje się jednoznacznie odwzorowanie T na sumach `A_i^kB_i u_k`.

Pozostałe weryfikowane argumenty: równania gramianów, kryteria Kalmana i PBH używane wyłącznie przez odsyłacze, konstrukcja `R/(R∩N)`, rangowy dowód minimalności, podobieństwo, równoważenie i najmniejsze kwadraty są poprawne.

## Walidacja

Regresja `tools/test_linear_algebra_minimal_realizations.py` przeszła część testową GitHub Actions w przebiegu 44951715486; obejmuje 256 trójek nad F2 i 6561 trójek nad F3, rangi kilku macierzy Hankela oraz wymierne przykłady. Finalny CI dla bloba po korekcie oraz końcowy PDF pozostają do sprawdzenia.

**Decyzja: audyt II wykrył i usunął brakujące uzasadnienie. Nie jest czystym audytem.** Licznik kolejnych czystych audytów resetuje się, a stabilizację uzależniamy od dwóch kolejnych czystych kontroli i zielonego CI/PDF.
