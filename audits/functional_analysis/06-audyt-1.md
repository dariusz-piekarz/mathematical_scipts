# Analiza funkcjonalna — rozdział 06 — audyt 01

**Data:** 23 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/functional_analysis/06-twierdzenie-hahna-banacha-i-ciagly-dual.tex.  
**SHA audytowanego źródła po poprawkach:** a7f8b570f38b928257f4d7f3bc0fd20304d2dba6.  
**Wynik:** pierwszy pełny audyt **z poprawkami**, NIE CZYSTY. Rozdział 06 ma obecnie **0/2** czystych audytów i NIE jest stabilny.

## Zakres audytu

Sprawdzono matematycznie wszystkie 17 dowodów i pięć przykładów, założenia formalne, funkcje podliniowe, zastosowanie lematu Kuratowskiego–Zorna, rzeczywistą i zespoloną wersję twierdzenia Hahna–Banacha, ograniczenie przez seminormę, przedłużenia topologiczne, jednoznaczność na gęstej podprzestrzeni, normę funkcjonału, separację domkniętej podprzestrzeni, anihilatory, przestrzeń sprzężoną produktu/ilorazu i wzór na odległość. Kontrola obejmowała przypadki brzegowe oraz właściwą terminologię polską.

## Kontrola dowodów — 17/17

1. **Ciągłość funkcjonału liniowego:** ograniczenie modułu przez 1 na otoczeniu zera i skalowanie przez ε odtwarzają ciągłość w zerze. PASS.
2. **Jednowymiarowe przedłużenie przez funkcję podliniową:** jednoznaczny rozkład m+tx₀ i przedział możliwych wartości a, ograniczony przez L=sup(f(y)-p(y-x₀)) i R=inf(p(z+x₀)-f(z)). Z podaddytywności i dominacji f≤p wynika L≤R, a wartości przy 0 wykluczają nieskończone krańce. PASS.
3. **Rzeczywisty Hahn–Banach:** rozważana rodzina przedłużeń jest zbiorem; łańcuchy mają ograniczenia górne przez zgodne unie; maksymalność i lemat jednowymiarowy dają pełną dziedzinę E. PASS.
4. **Odtwarzanie zespolonego funkcjonału z części rzeczywistej:** wzór G(x)=u(x)-iu(ix) zachowuje mnożenie przez i, więc jest zespolono-liniowy; jednoznaczność z części rzeczywistej. PASS.
5. **Zespolone przedłużenie z dominacją:** rzeczywiste przedłużenie Re f przez p, odtworzenie F i obrót fazy α o module 1 dają |F(x)|≤p(x). PASS.
6. **Kryterium ciągłości przez seminormę:** p=|f| w jedną stronę, w drugą inkluzja poziomic p zapewnia ciągłość f. PASS.
7. **Topologiczny Hahn–Banach:** otwarte absolutnie wypukłe U w X ogranicza moduł f na M∩U, funkcjonał Minkowskiego p_U zapewnia |f(m)|≤p_U(m), a algebraiczne przedłużenie pozostaje ciągłe dzięki p_U. Nie jest potrzebna domkniętość M ani Hausdorff X. PASS.
8. **Jednoznaczność na gęstej podprzestrzeni:** zbiór zerowy ciągłego F₁−F₂ jest domknięty i zawiera gęste M. PASS.
9. **Hahn–Banach z zachowaniem normy:** p(x)=||f||·||x|| i dominacja modułu, wraz z nierównością odwrotną przez ograniczenie do M. PASS.
10. **Funkcjonał normujący wektor:** skonstruowany na \(\K x_0\) funkcjonał ma normę 1, jego przedłużenie osiąga ||x₀||; w przypadku x=0 supremum także jest 0. PASS.
11. **Seminorma jako supremum funkcjonałów:** dla p(x₀)=0 funkcjonał zerowy, w przeciwnym razie przedłużenie z prostej \(\K x_0\); moduł nie przekracza p i górne ograniczenie jest osiągnięte. PASS.
12. **Rozdzielanie punktów:** z lokalnej wypukłości i Hausdorffa istnieje p z p(x−y)>0; dominowany funkcjonał nie zeruje się na różnicy. PASS.
13. **Oddzielanie punktu od domkniętej podprzestrzeni:** z otoczenia W z (x₀+W)∩M=∅ i **symetrycznego** U⊂W poprawnie wyprowadza się x₀−m∉U; następnie p_U(x₀−m)≥1 i zdefiniowane g(m+λx₀)=λ jest dominowane przez p_U. Jawnie uzupełniono brakujące uzasadnienie używające −U=U. PASS po korekcie.
14. **Domknięta podprzestrzeń jako przecięcie jąder:** ciągłość f daje zawieranie cl(M); oddzielanie punktu x₀ spoza cl(M) zapewnia przeciwną inkluzję. PASS.
15. **Przestrzeń sprzężona produktu:** warunek ciągłości na podstawowym otoczeniu produktowym wymusza zależność wyłącznie od skończenie wielu współrzędnych; odwrotna ciągłość skończonych sum rzutów. PASS.
16. **Przestrzeń sprzężona ilorazu:** składanie z rzutowaniem jest liniowe, różnowartościowe i odwzorowuje na anihilator; z definicji topologii ilorazowej każda funkcja wyprowadzona z funkcjonału na X jest ciągła. PASS.
17. **Odległość do domkniętej podprzestrzeni:** oszacowanie przez normę funkcjonału, konstrukcja na M+\(\K x_0\), dopuszczalna dominacja i normowanie do dokładnej wartości odległości. Przypadek x₀∈M oddzielnie. PASS.

## Pięć przykładów — 5/5 skontrolowanych

1. **Nieciągły funkcjonał algebraiczny:** na liniowo niezależnych znormalizowanych e_n wartości f(e_n)=n nie mogą pochodzić z funkcjonału ciągłego; rozszerzenie bazy Hamela wykorzystuje aksjomat wyboru. PASS.
2. **Sumowanie na c₀₀ w ℓ¹:** jednoznaczne przedłużenie sumowania dzięki gęstości, a brak ciągłości tego samego funkcjonału dla normy supremum. PASS.
3. **Ewaluacja pochodnej na C∞([0,1]):** |f^(j)(t₀)|≤p_j(f) zapewnia ciągłość. PASS.
4. **Niejednoznaczne normujące przedłużenia na R² z normą supremum:** F_a(x,y)=ax+(1−a)y, a∈[0,1], zachowują normę 1. PASS.
5. **Brak przedłużenia z prostej w L^p dla 0<p<1:** przestrzeń ma trywialną przestrzeń sprzężoną, ale niezerowy funkcjonał na M=Kχ_[0,1] jest ciągły w topologii podprzestrzeni. PASS.

## Poprawki matematyczno-redakcyjne

1. **Dowód rozdzielania punktu od domkniętej podprzestrzeni:** dopisano rolę symetrii U. Bez tego etap od (x₀+W)∩M=∅ do x₀−m∉U odwracał różnicę bez wyjaśnienia; teraz formalnie z x₀−m∈U wynika m=x₀−(x₀−m)∈x₀+U⊂x₀+W, sprzeczność. Konstrukcja funkcjonału po poprawce nie wymaga dodatkowych założeń.
2. **Globalna terminologia:** zastąpiono rzeczownikowe „dual” przez „przestrzeń sprzężona” oraz „przestrzeń algebraicznie sprzężona” w tytule rozdziału, definicjach, wynikach, przykładzie, anihilatorach i zapowiedzi dystrybucji. Nie zmieniono stabilnych etykiet ani ścieżki pliku, aby nie zrywać odsyłaczy innych rozdziałów.
3. **Funkcja charakterystyczna:** stałą funkcję 1 w przykładzie L^p zapisano zgodnie z konwencją jako χ_[0,1].
4. **Odsyłacz źródłowy:** twierdzenie o zerowości wszystkich ciągłych funkcjonałów na L^p, 0<p<1, ma teraz wskazany rozdział 05, gdzie zostało szczegółowo udowodnione, a nie dawny rozdział 01.
5. Zachowano wszystkie 17 dowodów, 5 przykładów i 22 etykiety; zmiany nie zmieniają treści twierdzeń.

## Regresje i CI

- Dodano tools/tests/test_functional_analysis_ch06.py: **14 testów** obejmujących strukturę tekstu, zgodność etykiet i odsyłaczy, warunek symetrii, model jednowymiarowego przedłużenia rzeczywistego, rekonstrukcję zespoloną, oszacowanie seminormą, rodziny normujących przedłużeń, separację, zbieżność operatorów współrzędnych, anihilator i normę odległości.
- Dodano .github/workflows/functional-analysis-ch06.yml: dedykowane testy i kompilacja LaTeX pełnego kontekstu rozdziałów 01–06, podwójna kontrola odsyłaczy i PDF oraz artefakt.
- [Przebieg 45175593130](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45175593130): etap testów **14/14 PASS**, przygotowanie TeX 01–06 PASS; ostateczny wynik kompilacji i wizualnej kontroli PDF trzeba dopisać po zakończeniu.

## Decyzja

**Audyt 06/01 zakończony z poprawkami — nie jest czysty. Licznik stabilizacji 0/2.** Po pozytywnym CI następny etap to nowy, niezależny audyt 06/02, a po nim kolejny, jeśli również będzie bez dalszych poprawek. Do rozdziału 07 nie przechodzimy przed stabilizacją 06.
