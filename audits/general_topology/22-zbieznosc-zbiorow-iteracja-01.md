# Topologia ogólna — rozdział 22, audyt 01

**Data:** 2026-11-22.
**Gałąź:** biblioteka-matematyczna-iteracja-6.
**Źródło:** chapters/pl/general_topology/22-zbieznosc-kuratowskiego-wijsman-attouch-wets.tex.
**Wersja wprowadzająca:** commit 377277abbe023fadea2917276189cc608bc8f0bc.
**Wersja po korekcie:** commit d162dc918d46baae12d2f56384d8ece28f7bfb31, blob 33765c2bb1b3065f4ad32596795c3d1981b48dda.
**Wynik:** NIE CZYSTY (modyfikacje matematyczne i redakcyjne); **0/2** czystych audytów po korekcie.

## Kontrola poprawności matematycznej

1. Definicje Li i Ls Kuratowskiego mają wszystkie kwantyfikatory. W przestrzeni metrycznej kwantyfikatory trafiania kul są równoważne d(x,F_n)→0 oraz liminf d(x,F_n)=0 (odpowiednio), przy konwencji d(x,∅)=∞.
2. Obie granice są domknięte, nawet gdy F_n nie są domknięte. Sprawdzono dowody bez ukrytego założenia o zwartości lub kompletności.
3. Przy naprzemiennych singletonach {0},{1} w R granica dolna jest pusta, a górna to {0,1}; dla {0,n} obie granice są równe {0} i brak zbieżności w d_H.
4. Zbiory dopuszczalne w topologii Wijsmana i Attoucha–Wetsa są niepuste i domknięte, zatem ich funkcje odległości są rzeczywiste i 1-lipschitzowskie. Dowód metryzowalności Wijsmana dla ośrodkowego X poprawnie wykorzystuje gęstą przeliczalną rodzinę oraz ograniczenie sumy szeregu.
5. Jeśli d(x,F_n)→d(x,F) dla każdego x, to F⊆Li F_n i Ls F_n⊆F. Potrzebna jest domkniętość F, aby d(x,F)>0 dla x poza F.
6. Metryka Attoucha–Wetsa jest dobrze określona bez właściwości X: funkcje odległości są ograniczone na każdej ograniczonej kuli; Delta_m jest skończona i spełnia nierówność trójkąta. Zbieżność w tej metryce oznacza jednostajną zbieżność na każdym niepustym ograniczonym podzbiorze.
7. Dla dowolnego metrycznego X Attouch–Wets ma topologię silniejszą niż Wijsman. Na ograniczonej nieskończonej dyskretnej przestrzeni X, F_n=X\{n} punktowo daje d(x,F_n)→0, lecz supremum po X pozostaje 1, co dowodzi ścisłości.
8. Przy właściwości X każda domknięta kula jest zwarta. Dla rodziny 1-lipschitzowskich funkcji zbieżność punktowa jest na tej kuli jednostajna, dzięki skończonej sieci punktów; argument działa również dla sieci. Stąd zgodność topologii Wijsmana i Attoucha–Wetsa.
9. Dla lokalnie zwartej metrycznej X zbieżność Fella jest równoważna zbieżności Kuratowskiego dla ciągów domkniętych podzbiorów, również pustych. W kierunku przeciwnym do Fella użyto zwartości metrycznej do wybrania zbieżnego podciągu punktów z hipotetycznie nieskończonej liczby trafień zbioru zwartego.
10. W przestrzeni właściwej przy niepustej granicy F, założenie Li=Ls=F wymusza zbieżność odległości. Istnienie zbyt małych odległości d(x,F_n) prowadzi do zbieżnego podciągu z zwartej kuli i punktu granicy górnej sprzecznego z definicją d(x,F).
11. Kontrprzykład X={p,q}∪{y_n} z d(p,q)=2 i wszystkimi innymi odległościami między różnymi punktami równymi 1 jest poprawną zupełną, lokalnie zwartą, ale niewłaściwą przestrzenią metryczną. Ciąg F_n={p,y_n} zbiega do {p} w Fellu i w sensie Kuratowskiego, lecz d(q,F_n)=1 zamiast d(q,{p})=2.

## Uzupełnienie z zakresu głównych twierdzeń

Pierwsza wersja zawierała łańcuch implikacji Attouch–Wets⇒Wijsman⇒Kuratowski
oraz zgodność Fella i Kuratowskiego przy lokalnej zwartości,
ale brakowało bezpośredniego, ogólnego porównania topologii Fella i Wijsmana.

Wprowadzono i udowodniono Stwierdzenie prop:topog22-wijsman-fell:
dla dowolnej przestrzeni metrycznej topologia Wijsmana na niepustych
domkniętych zbiorach jest silniejsza od indukowanej topologii Fella.
Otwartość warunku trafienia wynika z ciągłości ewaluacji odległości.
Warunek ominięcia C zwartego otrzymuje otoczenie przez dodatnie
minimum odległości C od F i skończoną sieć punktów w C.
To ważne rozróżnienie nie wymaga właściwości X.

Doprecyzowano w twierdzeniu o Attouchu–Wetsie,
że supremum w charakterystyce zbieżności rozważamy
dla niepustych ograniczonych B, aby uniknąć niejawnej konwencji
dotyczącej supremum po zbiorze pustym.

## LaTeX, integracja i rzeczywisty PDF

- Rozdział został dodany do książki, katalogu i osobnego pliku wejściowego.
  Test rozdziału 22 obejmuje skończone modele liminf/limsup, dyskretne
  kontrprzykłady, nierówność trójkąta w przykładowej przestrzeni
  niewłaściwej, odsyłacze oraz poprawność struktury LaTeX.
- Dedykowany [CI 45046808669](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45046808669)
  zakończył się completed/success dla wstępnego rozdziału i testów:
  przeszło sprawdzanie plików, kompilacja książki oraz osobnego rozdziału.
- Rzeczywisty PDF pierwszej wersji miał 7 stron A4. Strony 1–6
  były poprawnie złożone, bez nakładek, błędnych odsyłaczy ani
  ostrzeżeń kompilatora; jednak na stronie 7 znajdował się wyłącznie
  czterowierszowy ostatni akapit podsumowania.
  Wprowadzony dowód porównania Wijsmana i Fella zmienia paginację;
  dla nowego bloba trzeba wykonać nowy przegląd PDF.
- Pierwsze zielone CI i jego wizualna inspekcja NIE weryfikują
  bloba po nowej edycji. Następne CI musi dotyczyć aktualnego
  bloba 33765c2... i udostępnić nowy artefakt PDF.

## Status

**Rozdział 22: OTWARTY, 0/2** po edycji. Należy ponownie zbadać
pełny tekst matematyczny, sprawdzić wszystkie odsyłacze
i nowy PDF. Stabilność dopiero po dwóch czystych audytach tego samego bloba
oraz dodatkowym audycie potwierdzającym, zgodnie z przyjętym standardem.
