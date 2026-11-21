# Logika matematyczna i teoria mnogości — rozdział 15, audyt IV

**Data:** 21 listopada 2026 r.  
**Rozdział:** „Homomorfizmy, izomorfizmy i elementarność struktur”.  
**Podstawa:** wersja `logika_rozdzial_15_audyt_III.tex` po poprawce audytu III.  
**Wynik merytoryczny:** czysty audyt stabilizacyjny; brak dalszych zmian.

## Ponowna kontrola matematyczna

1. **Definicje homomorfizmu i zanurzenia:** homomorfizm zachowuje interpretacje stałych i funkcji, a relacje przenosi w jednym kierunku; zanurzenie jest iniektywne i odzwierciedla relacje. Uzasadnienia przykładów, w tym odwzorowania `n\mapsto 2n`, są poprawne.
2. **Lemat o termach:** każdy krok indukcji uwzględnia zmienne, stałe i termy złożone; kompozycja wartościowania z homomorfizmem jest poprawnie określona.
3. **Dodatnie formuły egzystencjalne:** przypadki atomów równościowych i relacyjnych, koniunkcji, alternatywy oraz `\exists` są pełne. Kontrprzykłady dla `\neg` oraz `\forall` rzeczywiście pokazują konieczność ograniczenia klasy formuł.
4. **Izomorfizmy:** przypadki atomowe, spójniki i kwantyfikatory uzasadniają równoważność spełniania z przeniesieniem wartościowania. Przy odwrotnym kroku egzystencjalnym wykorzystana jest surjektywność.
5. **Podstruktury i uniwersalne zdania:** porównanie funkcji i relacji dla argumentów z mniejszego uniwersum jest poprawne; arność relacji `k` jest odrębna od liczby zmiennych kwantyfikowanych `n`. Przypadek `n=0` jest uwzględniony.
6. **Kryterium Tarskiego–Vaughta:** w obie strony jawnie porównywane są interpretacje formuł z parametrami, a warunek świadków używany jest tylko dla `\exists`. Przypadek `\forall` wynika z klasycznej równoważności z negacją egzystencjalną. Warunki dotyczące wolnych i związanych zmiennych zostały zachowane.
7. **Równoważność elementarna:** `\operatorname{Th}` jest zdefiniowana dla dowolnej struktury; w końcowym dowodzie rozróżniono model rozszerzony `\mathfrak M^+`, redukt `\mathfrak M` oraz element `a=c^{\mathfrak M^+}`, więc symbol `c` nie jest nieuprawnienie użyty w redukcie. Argument `m<m` jest poprawny.

## Kontrole techniczne

- Liczba wyników i przykładów nie zmieniła się względem audytu II.
- Testy: 8/8 PASS (małe struktury + testy integralności źródła).
- LaTeX: kompilacja PASS, brak błędów i przepełnionych wierszy, 5 stron PDF samego rozdziału; obejrzano wszystkie pięć stron.
- 14 unikatowych etykiet, 11 odsyłaczy, wszystkie lokalne cele rozdziału są obecne; cele zewnętrzne należy potwierdzić w aktualnym repozytorium.

## Decyzja

**Tekst rozdziału 15 jest stabilny merytorycznie.** Dopuszcza się integrację z obecną gałęzią `biblioteka-matematyczna-iteracja-6`. Formalne zamknięcie nastąpi dopiero po pozytywnym CI aktualnego commitu. Nie rozpoczynać rozdziału 16 przed zamknięciem rozdziału 15.