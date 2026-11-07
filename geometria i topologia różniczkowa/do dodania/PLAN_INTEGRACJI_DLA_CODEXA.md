# Precyzyjny plan integracji: geometrie Thurstona bez dublowania

## Zakres i pochodzenie

Plan powstał po przeczytaniu przesłanych plików:
`05-algebra-abstrakcyjna.tex`, `11-metryka-dlugosc-miara.tex`,
`12-koneksje.tex`, `13-geodezyjne.tex`, `14-krzywizna.tex`,
`29-grupy-liego.tex`, `29a-geometria-kleina.tex`,
`30a-poincare-trzy.tex`, `30b-geometrizacja-thurstona.tex`
oraz pracy S. A. Pinillos Prado, *Geometric Structures on 3-Dimensional
Manifolds* (2021). Zostały sprawdzone **dostarczone kopie**, a nie
najnowszy stan repozytorium na GitHubie. Gdy Codex pracuje na `review`,
MUSI sprawdzić, czy aktualne pliki nadal mają te same nagłówki i etykiety.

**Główna korekta wcześniejszego planu:** w `30b-geometrizacja-thurstona.tex`
już istnieje pełna lista ośmiu geometrii, podstawowe metryki,
zwarty iloraz Nil, Sol jako torus odwzorowania, tabela Seiferta,
orbifoldy, JSJ i geometryzacja. Nie dodawaj osobnego rozdziału,
ani nie włączaj w całości `geometrie_thurstona_3rozmaitosci.tex`.

## Co jest już napisane — i czego NIE powtarzać

- `05`: elementarna algebra abstrakcyjna; nie wprowadzać ponownie grup,
  produktów półprostych ani fundamentalnej teorii grup w nowym rozdziale.
- `11`: metryki Euklidesa, sfery, trzy izometryczne modele H^n, forma
  objętości i teoria długości. Nie powtarzać definicji tych modeli.
- `12`: definicja koneksji, twierdzenie Leviego-Civity, wzór Koszula
  (`eq:koszul`), wzór na symbole Christoffela, geometrii sfery i H^n.
- `13`: geodezyjne euklidesowe, sferyczne i hiperboliczne,
  Hopf--Rinow, pełne rozważania FLRW. Nie kopiować żadnego z nich.
- `14`: algebraiczne symetrie Riemanna, Ricci, skalar, stała krzywizna,
  pełna sekcja **holonomii koneksji**, de Rham, płaskości. Istnieje
  `cor:ricci-plaskosc-3d` z dowodem `Ric=0 => Rm=0` w 3D.
  Nie wprowadzać tego po raz drugi.
- `29`: definicje grup/algebr Liego, eksponenta, Ad, SU(2). Zachować.
- `29a`: działania, stabilizatory, uśrednianie metryki, właściwość,
  dyskretne swobodne ilorazy, orbifoldy i geometria Kleinowska.
  Nie przepisywać lematów `prop:klein-zwarty-stabilizator-metryka` ani
  `prop:klein-dyskretny-iloraz`.
- `30a`: równania potoku Ricciego, odzyskiwanie krzywizn sekcyjnych
  z wartości własnych Ricciego w wymiarze 3 (`prop:poincare3-ricci-sekcje`),
  chirurgia i szkic dowodu Poincarégo. Bez zmian.
- `30b`: wszystkie osiem modeli, podstawowe formuły dla Nil, Sol,
  \widetilde{SL}_2, przykłady zwartych ilorazów, tabela Seiferta,
  podstawy geometryzacji. Dodaj tylko **uzasadnienia i nowe konstrukcje**.

## Pliki dopisków i dokładne miejsca wstawienia

| Dopisek (nowy plik) | Plik docelowy | Kotwica: wstaw BEZPOŚREDNIO PRZED | Zawartość nowa |
|---|---|---|---|
| `11-uzupelnienie.tex` | `11-metryka-dlugosc-miara.tex` | `\section{Metryki lorentzowskie: Schwarzschild, Kerr i FLRW}` | Macierze i objętość Nil/Sol, anizotropia i brak związku det G z płaskością |
| `12-uzupelnienie.tex` | `12-koneksje.tex` | `\section{Pochodna kowariantna i transport wzdłuż krzywej}` | Wzór Koszula dla ramy nieholonomicznej i wszystkie pochodne kowariantne w Nil |
| `13-uzupelnienie.tex` | `13-geodezyjne.tex` | `\section{Twierdzenie Hopfa--Rinowa}` | Dwa momenty i potencjał efektywny Sol; krzywe rzutowane geodezyjnych Nil |
| `14-uzupelnienie.tex` | `14-krzywizna.tex` | `\section{Krzywizna Minkowskiego i modelu FLRW}` | NOWE rachunki z koneksji: krzywizny, Ricci i skalar Nil/Sol |
| `29a-uzupelnienie.tex` | `29a-geometria-kleina.tex` | `\section{Przestrzeń euklidesowa i afiniczna}` | Atlasy (G,X), rozwinięcie, reprezentacja holonomii, kompletność i kontrprzykład |
| `30b-tildeSL.tex` | `30b-geometrizacja-thurstona.tex` | `\textbf{Geometria $\mathrm{Nil}$.}` | Jawna metryka Sasakiego na U H², forma koneksji i jej krzywizna |
| `30b-kontakt-nil.tex` | `30b-geometrizacja-thurstona.tex` | `\textbf{Geometria $\mathrm{Sol}$.}` | Forma kontaktowa, brak całkowalności, holonomia pola powierzchni |
| `30b-seifert-euler.tex` | `30b-geometrizacja-thurstona.tex` | `\section{Twierdzenie geometryzacyjne}` (przed dołączeniem kolejnego dopisku) | Wyprowadzenie e(UΣ)=χ(Σ) z koneksji i Gaussa--Bonneta |
| `30b-hiperboliczne.tex` | `30b-geometrizacja-thurstona.tex` | `\section{Twierdzenie geometryzacyjne}` (PO dopisku o Eulerze) | Nowa sekcja: wielościany, Gieseking, ósemka, Seifert--Weber, Mostow--Prasad, Dehn, H1 |

**Uwaga o kolejności:** w `30b` wstaw `30b-tildeSL.tex` przed opisem Nil,
`30b-kontakt-nil.tex` po opisie Nil i przed opisem Sol, potem
`30b-seifert-euler.tex` i `30b-hiperboliczne.tex` w tej kolejności
pomiędzy sekcją Seiferta a twierdzeniem geometryzacyjnym.
Wszystkie dopiski są **fragmentami**, nie mają `\documentclass`.
Nie dodawaj ich jako osobnych rozdziałów. Możesz wkleić treść do
odpowiedniego miejsca lub użyć `\input` z nowej podścieżki, zgodnie
z praktyką projektu; nie mieszaj obu sposobów jednocześnie.

## Dlaczego tak rozdzieliliśmy materiał

1. **Metryka (11):** tylko własności macierzy metrycznej i miary.
   Grupa Liego i zwarte ilorazy pozostają w `30b`.
2. **Koneksja (12):** pełen rachunek Levi-Civity Nil jest tylko tutaj.
3. **Geodezyjne (13):** tylko dynamika równań ODE, nie ogólna
   teoria zupełności ani ponowne modele hiperboliczne.
4. **Krzywizna (14):** wyliczamy z już uzyskanej koneksji Nil
   oraz krótkiego obliczenia koneksji Sol. W `30b` pozostają
   podane wcześniej wartości liczbowe, z odsyłaczem do obliczeń.
5. **Geometria Kleina (29a):** holonomia struktury `(G,X)` jest
   homomorfizmem `π1 -> G`; holonomia Levi-Civity jest grupą
   transportów na `T_pM`. Torus płaski rozdziela te pojęcia.
6. **Geometryzacja (30b):** formy połączenia i głębsze przykłady
   hiperboliczne, bez ponownej klasyfikacji ośmiu modeli.

## Dodatkowe, bardzo krótkie odsyłacze (bez nowych fragmentów teorii)

- W `30b`, po wyniku `K(X,Y)=-3/4` w części Nil, odwołaj się
  do `\ref{prz:thur-dop-krzywizna-nil}`.
- W `30b`, po wyniku `K(X,Y)=1` w części Sol, odwołaj się
  do `\ref{prz:thur-dop-krzywizna-sol}` i
  `\ref{prz:thur-dop-geodezyjne-sol}`.
- W `30b`, przy `U\Sigma_g` i liczbie Eulera, odwołaj się do
  `\ref{prz:thur-dop-seifert-euler}` oraz do jawnej metryki
  `\ref{prz:thur-dop-tilde-sl-metryka}`.
- W `30b`, na początku sekcji `sec:thurston-model`, jeden odsyłacz
  do `\ref{sec:thur-dop-struktury-gx}`. Nie powtarzaj jej definicji.
- W `14` nie powtarzaj `cor:ricci-plaskosc-3d`, a w `30a`
  nie powtarzaj `prop:poincare3-ricci-sekcje`.
- Możesz dodać 1--2 zdania po wzmiance o hiperbolicznych
  wypełnieniach Dehna w `30b`, odsyłające do nowej sekcji
  `sec:thur-dop-hiperboliczne`, ale nie kopiuj twierdzenia dwa razy.

## Wymagania wykonawcze dla Codexa

1. Sprawdź gałąź `review`, `git status --short`, makra, środowiska,
   docelowy plik główny, aktualne `\label` oraz dokładne kotwice.
   Nie usuwaj ani nie nadpisuj cudzych niezacommitowanych zmian.
2. Dla każdej kotwicy sprawdź, czy istnieje dokładnie raz i czy
   odpowiedni dopisek nie jest już obecny (sprawdź prefiks etykiet
   `thur-dop`). W razie rozbieżności **nie wstawiaj na ślepo**.
3. Wprowadź dziewięć dopisków w odpowiednich miejscach.
   Zostaw dotychczasowe treści w spokoju, dopisując tylko odsyłacze.
4. Sprawdź spójność notacji: `R(X,Y)Z`, znaki `K`, definicję
   `\dd`, zapis `\R`, konwencję orientacji w klasie Eulera,
   `X/Γ` vs `Γ\backslash X`, numery i nazwy środowisk.
5. Zastosuj styl oryginału: język polski, **mapa** zamiast *karta*,
   bez `\boxed`, przewaga wzorów w tekście, dowody wyjaśniające
   istotne przejścia. W razie potrzeby skróć dwa powtarzające się
   zdania w sąsiadujących sekcjach.
6. Uruchom kompilację wszystkich dotkniętych tomów **dwukrotnie**,
   sprawdź undefined/duplicate labels, hyperref i ostrzeżenia.
   Raportuj `git diff --stat` i wynik testów; nie rób push ani merge.
7. Osobno przeprowadź review równań geodezyjnych (zwłaszcza
   znaki przy `w` w Nil i `p_x,p_y` w Sol), obliczeń Ricciego,
   znaku formy koneksji na `U H²`, skręcenia Nil oraz postaci
   relacji grupowej po wypełnieniu Dehna.

## Zweryfikowane lokalnie

Fragmenty dopisków kompilują się w samodzielnym dokumencie
kontrolnym z `pdflatex` (14 stron, brak błędów). W tych kontrolnych
wydrukach odsyłacze do oryginalnych rozdziałów mogą pozostawać
niezdefiniowane: pełne linkowanie trzeba sprawdzić po dołączeniu
do właściwego projektu. Etykiety porównano z dostarczonymi
plikami: nie ma kolizji, a wszystkie użyte `\ref` i `\eqref`
mają cele w istniejących lub nowych fragmentach.

## Tematy świadomie odłożone poza te dopiski

- Pełny dowód klasyfikacji wszystkich 3D algebr Liego.
- Pełne warunki i dowód twierdzenia Poincarégo o wielościanach,
  wraz z obrazkami wszystkich sklejeń i prezentacjami grup.
- Szczegółowa klasyfikacja wszystkich torusowych nakryć i operacji JSJ.
- Dowód twierdzenia Mostowa--Prasada, twierdzenia Thurstona o
  wypełnieniach hiperbolicznych i samej geometryzacji (wyniki głębokie).
- Rozszerzenie na nieorientowalne bazy Seiferta.

To nie są niedostrzeżone luki, tylko obszary wymagające osobnego,
znacznie większego opracowania, którego nie należy „udawać” w
krótkim wstrzyknięciu do istniejącego skryptu.
