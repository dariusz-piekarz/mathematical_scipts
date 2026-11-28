# Geometria algebraiczna — audyt globalny I (2026-11-22)

## Zakres

Kanoniczne rozdziały ALG-00–ALG-10, trzy moduły wspólne, książka modułowa i historyczny monolit `sources/pl/geometria_algebraiczna(1).tex`. Rozpoczęto po zamknięciu ALG-10/VI; bez dodawania fikcyjnego ALG-11. Źródłowa migawka przed naprawą: `dfcc10cf9f13a26ff7ca4a3f2497e4d70e59188c`.

## Usterka G-01: monolit zawierał starsze wersje pięciu rozdziałów

Ścisłe porównanie tekstu każdego rozdziału od nagłówka `\chapter` wykazało rozbieżności w ALG-00–04; ALG-05–10 były zgodne znakowo. W monolicie brakowało m.in. doprecyzowania przykładu modulo 8, znajdowały się starsze podpisy TikZ, dawny układ współrzędnych rzutowych, słabsze rozróżnienie normalizacji afinicznej i rzutowej oraz stara nazwa „Tensorowanie”. To nie były wyłącznie różnice typograficzne.

**Naprawiono** przez zastąpienie dokładnie fragmentów ALG-00–04 treścią zatwierdzonych plików kanonicznych, bez zmiany żadnego źródła rozdziałowego oraz bez ingerencji w ALG-05–10. Nowy monolit ma 11 rozdziałów i poprawne zakończenie dokumentu.

Commit naprawy: https://github.com/dariusz-piekarz/mathematical_scipts/commit/fe5646f7273e219d5795adf35d30012c43e7fbc9

## Kontrola przekrojowa

- 400 etykiet w 11 rozdziałach oraz 6 w trzech wspólnych plikach = **406 unikalnych etykiet**. Odsyłacze do `tw:ga10-weak` i `thm:xvii-blowup` są poprawne po uwzględnieniu plików współdzielonych; brak duplikatów lub niewyjaśnionych odsyłaczy w badanym zbiorze.
- Sprawdzono zgodność deklaracji słabego Lefschetza (izomorfizmy w stopniach `q<n-1`, monomorfizm przy `q=n-1`), kohomologii rozdmuchania punktu (`H²` zwiększa się o klasę `e`, `e²=-1`) i wzorów Cherna dla hiperpowierzchni z późniejszym zastosowaniem Chern–Gauss–Bonnet.
- Niezależne rachunki dla **250 stopni** `d=1,...,250`: `12(1+p_g)=d(d-4)²+d(d²-4d+6)` oraz `h^{1,1}=d(d²-4d+6)-2-2p_g >=0`, przy `p_g=0` dla `d<=3` oraz `p_g=(d-1)(d-2)(d-3)/6` dla `d>=4`. Wszystkie próby rachunkowe spełniają tożsamości. Przeliczenia nie dowodzą zewnętrznych twierdzeń Hodge'a, Kodairy, Lefschetza, GAGA czy HRR.

## Nowa bramka integracyjna

`tools/tests/test_algebraic_geometry_monolith_sync.py` sprawdza tożsamość rozdziałów, ich kolejność, etykiety i odsyłacze wraz z modułami współdzielonymi. `.github/workflows/algebraic-geometry-global-audit.yml` uruchamia wszystkie istniejące regresje ALG oraz niezależnie kompiluje książkę modułową i monolit, zapisując dwa PDF i logi.

**Wynik I: USTERKA ZNALEZIONA I NAPRAWIONA; STATUS GLOBALNY OTWARTY** do faktycznego odbioru nowego CI, PDF i osobnego bezusterkowego audytu globalnego II (+ dodatkowego audytu kontrolnego). Nie utożsamiać poprawnej kompilacji z dowodem matematycznym.
