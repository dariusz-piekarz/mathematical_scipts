# Zatwierdzone rozszerzenie LA-32 — konstrukcja i transformata Penrose’a

**Decyzja użytkownika (22 listopada 2026):** w trakcie prac nad rozdziałem 32 „Twistory” dodać wcześniej omawiany materiał związany z Rogerem Penrose’em. **Nie rozszerzać w tym celu rozdziałów 28–31 ani nie włączać tego materiału do obecnego audytu 28.** Wprowadzić nową część dopiero przy LA-32 i poddać ją pełnym audytom matematycznym, językowym, odsyłaczy, rysunków, LaTeX oraz CI.

## Stan istniejący w `chapters/pl/linear_algebra/32-twistory.tex`

Jest już relacja incydencji `ω=Xπ` (konwencja z opcjonalnym `i`), korespondencja `X↦ℓ_X⊂CP³`, równoważność `ℓ_X∩ℓ_Y≠∅ ⇔ det(X−Y)=0`, płaszczyzny izotropowe, kwadryka Segrego i Kleina, korespondencja flag oraz kwaternionowa fibracja `CP³→HP¹≃S⁴`. Końcowa uwaga **wymienia transformatę Penrose’a jedynie jako dalszy kierunek**, nie podaje jej wzoru ani dowodu. Nie dublować istniejącej części.

## Treść nowego fragmentu — zatwierdzony zakres

1. **Oryginalna konstrukcja Penrose’a**: wyjaśnić sens korespondencji incydencji `ω=Xπ` (oraz fizycznej konwencji `ω=iXπ`), punktom czterowymiarowej przestrzeni przyporządkować proste `ℓ_X≃CP¹`, a punktom twistorowym odpowiednie izotropowe płaszczyzny `α`. Odwołać się do już udowodnionego twierdzenia o przecięciu prostych; wyraźnie odróżnić zespoloną korespondencję od euklidesowej fibracji nad `S⁴`.
2. **Elementarna lokalna transformata Penrose’a dla skalarnego równania falowego.** Na odpowiednim otwartym obszarze przestrzeni twistorów i dla wybranego holomorficznego reprezentanta `F(ω,π)` jednorodnego stopnia `−2` rozważyć, przy ścisłych warunkach holomorficzności, braku przecinania konturu z biegunami oraz stałego lokalnie typu homologii konturu,
   `Φ(X)=(2πi)^{-1}∮_{Γ_X} F(Xπ,π)(π_0 dπ_1−π_1 dπ_0)`.
   Uzasadnić niezmienniczość całki względem zmiany jednorodnego przedstawiciela `π`, ponieważ `F` ma stopień `−2`, a jednorodna forma stopień `2`.
3. **Dowód równania bezmasowego.** W lokalnych współrzędnych `X=(x_{ij})∈M₂(C)` przyjąć zespolony operator falowy `\Box_{\mathbb C}=∂_{11}∂_{22}−∂_{12}∂_{21}` (zaznaczyć normalizację względem fizycznego operatora Lorentza). Dla `F(Xπ,π)` pochodne dają `∂_{ij}F=π_j∂_{ω_i}F`, więc `(∂_{11}∂_{22}−∂_{12}∂_{21})F(Xπ,π)=0`. Przy założeniach umożliwiających różniczkowanie pod całką otrzymać `\Box_{\mathbb C}Φ=0`. Podać jedno obliczalne, nietrywialne lokalne rozwiązanie jako całkę rezydualną z funkcji wymiernej stopnia `−2`.
4. **Ograniczenia i właściwa wersja kohomologiczna.** Oddzielić reprezentanta konturowego od pełnego twierdzenia Penrose’a z grupami `H¹(PT_U,\mathcal O(-2))` na odpowiednio dobranych **otwartych obszarach**. Nie twierdzić błędnie, że dowolna globalna holomorficzna funkcja na `CP³` reprezentuje niezerową klasę ani że dowolna całka definiuje globalne pole bez dodatkowych hipotez. Zaznaczyć, że pełny izomorfizm kohomologiczny i korespondencja Penrose’a–Warda wymagają dalszych założeń i aparatu snopów, koneksji oraz kohomologii.
5. **Rysunek i integracja.** Dodać lub uzupełnić czytelny schemat podwójnej korespondencji z konturem `Γ_X⊂ℓ_X`; używać istniejącego zestawu TikZ i zachować wszystkie stabilne etykiety. Wprowadzić czytelne odsyłacze do LA-29–31, a opcjonalnie do istniejącej teorii snopów innego skryptu, o ile jej etykiety są rzeczywiście dostępne. Nowe twierdzenia podać z pełnymi, samodzielnymi hipotezami i dowodami.

## Źródła do weryfikacji przy redakcji

- M. Dunajski, *Twistor theory at fifty: from contour integrals to twistor strings*, `https://pmc.ncbi.nlm.nih.gov/articles/PMC5666237/` (przede wszystkim korespondencja, przykład skalarnej transformaty Penrose’a i jej kohomologiczne ograniczenia).
- Podstawowe ujęcie P. Woit, `https://www.math.columbia.edu/~woit/twistorunification/euclidean-twistors.pdf` (rozróżnienie rzeczywistych struktur i korelacja modeli).
- Uzupełniająco literatura klasyczna Penrose’a–Rindlera, *Spinors and Space-Time*, tom 2, dla doboru konwencji spinorowych.

## Kryterium zakończenia

Rozszerzenie Penrose’a zostało **wyraźnie zatwierdzone przez użytkownika**, nie jest luźną propozycją. Wykonać je **gdy kolejka audytów dotrze do LA-32**, sprawdzić rachunki konturowe i równanie falowe niezależnymi testami symbolicznymi, wykonać kompilację LaTeX, audyt graficzny oraz co najmniej dwa kolejne czyste audyty po ostatniej modyfikacji.
