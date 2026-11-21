# Global Mathematical Writing Granularity Standard (Polish)

WZORZEC: źródłowy rozdział 01 geometrii i topologii różniczkowej, plik
`rozdzial1_poprawiony.tex` (Biblioteka matematyczna). Po przejrzeniu źródła
zidentyfikowano strukturalny standard: motywacja, każda definicja z jawnymi
obiektami i kwantyfikatorami, rozbicie warunków, przykład/kontrprzykład,
dowód w pełnych krokach, komentarz interpretacyjny, rysunek tam gdzie pomaga.

## Reguła obowiązkowa dla kolejnych iteracji we wszystkich skryptach

1. Zanim użyjesz pojęcia, wyjaśnij problem motywujący i podaj ścisłą definicję.
   Symbolom niestandardowym poświęć lokalne objaśnienia, w tym zakres zmiennych
   i różnicę między obiektami języka a metajęzyka. Przy skomplikowanym wzorze
   rozpisz go na słowa i wyjaśnij kierunek kwantyfikatorów.
2. Każdy nietrywialny dowód rozbij na uzasadnione kroki; nazwij konstrukcję,
   wykaż jej istnienie i dobrze określoność, podaj zakres użytych aksjomatów,
   przeprowadź oba kierunki równoważności osobno. Nie zastępuj dowodów
   zdaniami „oczywiste”, „analogicznie” ani „standardowo” przy istotnych etapach.
3. Po definicji lub nowym twierdzeniu umieść obliczalny ręcznie przykład
   z wyjaśnieniem każdej czynności i przykład graniczny/kontrprzykład tam,
   gdzie ujawnia on konieczność założeń.
4. Odniesienia do wcześniejszych rozdziałów tylko przez poprawne odsyłacze;
   pojęcia jeszcze niewprowadzone trzeba najpierw zdefiniować lub wyraźnie
   odłożyć na później, nie używając ich w dowodzie.
5. Jeśli rysunek pomaga, dodaj go wewnątrz źródła (TikZ), sprawdź podpis
   i brak kolizji po kompilacji. Nie wstawiaj nieistniejących zależności.
6. Audyt obejmuje również poprzednio napisane rozdziały: pisownię,
   poprawność matematyczną, wszystkie kwantyfikatory, ukryte aksjomaty,
   dowody, przykłady, niestandardowe symbole, rysunki i odsyłacze.
7. Format: zwarte składy LaTeX bez pustych stron; nie skracać treści
   celem zaoszczędzenia miejsca. Polski styl: „ciąg”, „ciągowy”, „ciało”,
   „obszar” w znaczeniu open connected domain, `\chi_A` i zestawienie `(f,g)`.
   Zakaz słowa „tensorowanie” oraz jego odmian.

8. **Zachowanie etykiet przy kopiowaniu z Biblioteki:** przenosząc lub kopiując
   fragment, rozdział albo dowód z istniejącego zasobu Biblioteki matematycznej,
   zachowuj bez zmian wszystkie oryginalne deklaracje `\label{...}` oraz
   odpowiadające im odsyłacze (`\ref`, `\eqref`, `\cref` i pokrewne).
   Nie generuj arbitralnie nowych nazw etykiet i nie zastępuj ich przez numery
   rozdziałów. Weryfikuj po skopiowaniu, czy zachowano **dokładnie** zestaw
   etykiet oraz powiązanych odwołań (wraz z wielokrotnością wystąpień),
   i prowadź mapę pochodzenia źródła.
   Jeżeli istnieją kolizje tych samych nazw między niezależnymi skryptami,
   **nie przemianowuj ich po cichu**: odnotuj właścicieli i zakresy,
   zachowaj źródłowe deklaracje, a rozwiązanie zapewnij przez jawnie
   udokumentowane kwalifikowanie celu/aliasy w aplikacji lub zatwierdzony
   etap integracji; nie pozwól, by odsyłacz wskazał przypadkowo cudzy wynik.
   Reguła dotyczy również przyszłych scalanych wersji — różne warianty
   dowodów muszą zachować pochodzenie i działające odsyłacze.

Powyższy standard dotyczy także geometrii, algebry, topologii,
analizy funkcjonalnej, PDE, teorii miary i wszystkich pozostałych
polskojęzycznych tekstów matematycznych.