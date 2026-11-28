# Topologia algebraiczna — powtórka nocnego audytu i pojednanie wersji TOP-13/TOP-14

**Data:** 21 listopada 2026. **Zakres:** dokładnie dwa rozdziały: TOP-13 i TOP-14. **Status:** `ponowny_audyt` (kontrola rozpoczęta, nie pełne zatwierdzenie wszystkich twierdzeń).

## Skąd pochodziły rozbieżności

1. Repozytorium `dariusz-piekarz/mathematical_scipts`, gałąź `biblioteka-matematyczna-iteracja-6`: `chapters/pl/algebraic_topology/{13-,14-}*.tex`.
2. Biblioteka ChatGPT: `/Biblioteka matematyczna/rozdzialy/TOP-13--*.tex` oraz `TOP-14--*.tex` (wersja 10, modyfikacja około 08:39 UTC).
3. Lokalny archiwalny stan sprzed oraz po porannej powtórce: `TOP_13_14_PONOWNY_NOCNY_PARTIA_01_2026-11-21.zip`, z osobnymi `source/` i `updated/`.
4. Historia iteracji 11–17 oraz raport ponownej kontroli. Automatyzacja audytów topologii algebraicznej jest wyłączona.

GitHub i Biblioteka nie były tożsame. GitHub miał 10 etykiet w TOP-13 i 15 w TOP-14, Biblioteka odpowiednio 7 i 11: różnica to siedem niezależnych przykładów/rysunków. Biblioteka zawierała natomiast nowsze uzupełnienia dowodów (reprezentacja H¹, niezmiennik Hopfa, współczynniki lokalne). Żadnej wersji nie nadpisano drugą bez kontroli.

## Co scalono w tej iteracji

**TOP-13.** Zachowano całe dotychczasowe źródło Biblioteki. Uzupełniono brakujący przykład klasyfikacji rzeczywistych wiązek liniowych nad S¹, wiązki Möbiusa, linii tautologicznej nad RP² i pierwszej klasy Stiefela–Whitneya. Rozszerzono rachunek przestrzeni Moore'a o pełne obliczenia homologii i kohomologii z dowolnymi współczynnikami abelowymi oraz porównanie Hom i Ext; odzyskano diagram różniczek. Pozostawiono istniejący krótki przykład przedłużania map i rozwinięty przykład współczynników lokalnych z monodromią -1. Zachowano stare etykiety i trzy brakujące etykiety GitHuba.

**TOP-14.** Zachowano argument o niezmienniku Hopfa z długiego ciągu fibracji, przykład niejednoznaczności podniesienia i dodatkowe rachunki Steenroda. Przywrócono niezależny przykład przeszkody Whiteheada dla odwzorowania składającego S² ∨ S² → S² wraz z pierścieniowym dowodem przez (x+y)²=2xy i diagramem; przykład CP² z dwiema metodami wykazania niemożliwości podniesienia; przykład RP⁵, w którym Sq¹(t³) i Sq²(t³) nie znikają, a t⁶=0, ze sprawdzeniem Sq¹Sq¹. Zachowano cztery brakujące etykiety GitHuba.

W nowych diagramach zastąpiono nazwy kolorów specyficzne dla dużego dokumentu barwami z podstawowego zestawu TikZ, aby moduły mogły składać się samodzielnie w pomocniczej preambule. Nie zmieniono oryginalnych nazw etykiet. Nie usunięto żadnego wiersza ze źródeł Biblioteki sprzed scalenia, nowe bloki są wyłącznie dodatkami.

## Ponowny audyt merytoryczny — część wykonana

- **TOP-13:** sprawdzono klasyfikację głównych wiązek grupy O(1) przez [X,BO(1)] ≅ H¹(X;Z/2) dla CW-kompleksów, rozróżnienie rzeczywistych i zespolonych linii, opis monodromii Möbiusa, uniwersalny rachunek przestrzeni Moore'a (`A[m]` oraz `A/mA`) i zgodność z warunkiem przedłużenia `ma=0`. Zachowano i ponownie skontrolowano obliczenie skręconego H¹(S¹;L), w którym `t-1` działa jak -2.
- **TOP-14:** zweryfikowano przeszkodę Whiteheada także bez odwoływania się do definicji iloczynu Whiteheada, wykorzystując mnożenie w H*(S²×S²;Z). Sprawdzono przykład CP² przez naturalność iloczynu kubkowego i niezerowość h², wzory dwumianowe dla Sq¹(t³), Sq²(t³), Sq¹Sq¹(t^m) oraz przypadki modulo 2 w relacji Sq²Sq²=Sq³Sq¹. Sprawdzono, że argument o niejednoznaczności podniesienia rozróżnia istnienie od liczby klas podniesień.

Ta kontrola **nie oznacza**, że wszystkie wcześniej cytowane głębokie twierdzenia mają już pełne, samodzielne dowody. Do kolejnych iteracji pozostają: twierdzenie o reprezentacji kohomologii dla wszystkich wariantów, klasyfikacja wiązek głównych z pełnym dowodem jednoznaczności, kołańcuch przeszkód z lokalnymi współczynnikami, konstrukcja wyższych diagonalnych, pełne dowody wzoru Cartana i relacji Adema. Nie należy zamykać statusu `ponowny_audyt` bez niezależnej kontroli tych fragmentów.

## Testy wykonane teraz

- 3/3 przebiegi `pdflatex` w osobnym dokumencie z dwoma aktualnymi modułami: kod wyjścia 0.
- **23 strony PDF**. Log końcowy: **0 Overfull hbox**, 0 ostrzeżeń o niezdefiniowanych referencjach i 0 o powielonych etykietach.
- Sprawdzono 10 etykiet TOP-13 i 15 TOP-14; wszystkie oryginalne etykiety Biblioteki i siedem brakujących etykiet GitHuba są obecne bez duplikatów.
- Zachowanie każdego niepustego wiersza wcześniejszych kanonicznych źródeł Biblioteki; zgodność środowisk `przyklad`, `twierdzenie`, `lemat`, `proof`, `figure`, `tikzpicture`; brak `\input` i `\includegraphics` wewnątrz rozdziałów.
- W Pythonie sprawdzono 200 przypadków arytmetycznych dla `m(m+1)` modulo 2 i 200 przypadków współczynników z relacji `Sq²Sq²=Sq³Sq¹`.
- Obejrzenie arkuszy wszystkich 23 stron pomocniczego PDF, w tym odzyskanych diagramów na stronach 11 i 17. Nie stwierdzono widocznych kolizji napisów na odzyskanych rysunkach.

**Niewykonane w tej iteracji:** pełna kompilacja 31-rozdziałowej kanonicznej książki z GitHuba i audyt wszystkich twierdzeń w TOP-13/TOP-14. Nie należy przenosić statusu pełnej akceptacji.

## Rejestr wersji

- TOP-13: 952 wiersze, 41 778 bajtów UTF-8, SHA-256 `c4bcf2dc8237e60ba5706db00bfcdd31303a12614c91979cdf5855ea05e081fa`.
- TOP-14: 1020 wierszy, 40 874 bajty UTF-8, SHA-256 `d0514247c40dae6f6ea127b99cf2b460d0967e9bd3d52b5a18a53813cd21d3a4`.

Kolejny krok: ponowny, niezależny audyt pozostałych dowodów **tych samych dwóch pełnych rozdziałów**, a dopiero po ich zatwierdzeniu kolejne rozdziały według rzeczywistego stanu raportów. Synchronizacja plików GitHub–Biblioteka została przeprowadzona i zweryfikowana; szczegóły poniżej.

## Potwierdzenie synchronizacji Biblioteka–GitHub

Po przygotowaniu i przetestowaniu scalenia obydwa kanoniczne pliki w `/Biblioteka matematyczna/rozdzialy/` zostały **nadpisane poprawionymi wersjami**, a te same kompletne źródła zapisano na istniejącej gałęzi GitHub `biblioteka-matematyczna-iteracja-6` bez zmiany `main` i bez tworzenia nowej gałęzi.

- TOP-13: commit `6015e0c3121404d1dbece3147093aa5ad1341a6b`; potwierdzona końcowa zawartość ma 952 wiersze i blob `97dfdcf5f4ed9649f85b47be7bd258e5c4516918`.
- TOP-14: końcowy commit `0cde41b0a925deb450febc7fba5bf7e94964babe`; potwierdzona zawartość ma 1020 wierszy i blob `b44c029107e82d39281de7000002b493277216f3`. Poprzedni zapis TOP-14 został natychmiast uzupełniony o końcowe 20 wierszy wykryte przy weryfikacji długości.

Po zapisie ponownie odczytano oba źródła z Biblioteki i GitHuba; porównanie zawartości znak po znaku dało zgodność `true` dla każdego z dwóch plików. Raport i archiwum scalonych źródeł zapisano w katalogu `/Biblioteka matematyczna/iteracje/`. Nadal obowiązuje status `ponowny_audyt` z powodu wskazanych wyżej nierozliczonych twierdzeń.