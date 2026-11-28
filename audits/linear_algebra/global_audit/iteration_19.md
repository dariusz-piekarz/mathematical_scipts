# Algebra liniowa — audyt globalny, iteracja 19: LA12–13, konwencje zespolone i rzuty

**Data:** 22 listopada 2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`. **Kontynuacja:** [iteracja 18](iteration_18.md).
**Wynik:** **CZYSTY W SKONTROLOWANYM ZAKRESIE**. Odczytano kompletne sformułowania i wszystkie 28 dowodów LA12–13; nie znaleziono koniecznej poprawki w matematycznych plikach źródłowych. Indywidualny przegląd nie jest formalnym certyfikatem Lean.

## 1. Identyfikowalność źródeł

| Rozdział | Blob SHA | Wiersze | Dowody indywidualnie odczytane | Etykiety | Odsyłacze | Rysunki |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| LA12 — przestrzenie euklidesowe i unitarne | `ded0c69dc298d00842d4009073e2444e1037952a` | 1064 | **13/13** | 36 | 9 | 0 |
| LA13 — ortogonalność i rzuty | `cc5d09ff605ccf8bb7572ec56d4cc1f690edf3af` | 1305 | **15/15** | 34 | 18 | 1 |
| **Razem** | | **2369** | **28/28** | **70** | **27** | **1** |

Dla każdego twierdzenia sprawdzono pełne sformułowanie, wszystkie założenia, cały dowód i krytyczne kroki, a nie tylko deklarację istnienia środowiska `proof`. [Per-dowodowy rejestr kontroli](iteration_19_proof_review_12_13.csv) zawiera etykiety, zakresy wierszy i indywidualne adnotacje. Kolumna `Lean_formalization_assessed_here=NIE` rozróżnia audyt matematyczny od rzeczywistej formalizacji.

## 2. Audyt LA12 — 13 dowodów

- **Forma hermitowska i polaryzacja:** dla konwencji `h(u,v)` **antyliniowej w pierwszym argumencie**, liniowej w drugim, z `z=h(u,v)` zachodzi `q(u+iv)-q(u-iv)=-4 Im(z)`. Stąd **właściwy znak** we wzorze jest `-i q(u+iv)+i q(u-iv)`. Nie trzeba zakładać dodatniej określoności do polaryzacji. Sprawdzono również rzeczywistość wartości `h(v,v)` oraz regułę `G_{B'}=P^*G_BP`.
- **Cauchy–Schwarz i ortogonalizacja:** współczynnik w eliminacji ortogonalnej to `c=h(v,u)/h(v,v)` — zeruje `h(v,u-cv)` dokładnie w przyjętej konwencji. W Gramie–Schmidcie poprawnie występuje `h(e_j,v)`, a nie sprzężona wartość; dowód wyklucza zerowe `w_j` dzięki niezależności. Warunki równości w nierówności Cauchy'ego–Schwarza i Bessela są poprawne; zbadano pustą rodzinę.
- **Riesz i współrzędne:** dla liniowego funkcjonału `F`, reprezentujący wektor w bazie ortonormalnej wynosi `a=sum_j conjugate(F(e_j)) e_j`. Odwzorowanie `a ↦ h(a,·)` jest **antyliniowe** dla `K=C`, ale bijektywne, także gdy `dim V=0`; nie myli się go z liniowym odwzorowaniem o innym kierunku konwencji.
- **Grama i izometrie:** dla niezależnej rodziny `G=R^*R`, wyrazy diagonalne `R` są dodatnie i `det G=|det R|²`; dla `m=0` obowiązuje `det I_0=1`. Izometria liniowa zachowująca normę zachowuje iloczyn skalarny przez polaryzację. `A^*A=I` jest równoważne unitarnemu charakterowi macierzy kwadratowej w skończonym wymiarze. Kontrolowano również macierze przejścia między bazami ortonormalnymi i zerowy wymiar.

## 3. Audyt LA13 — 15 dowodów

- **Ortogonalne dopełnienia:** do ogólnych równości `(U_1+U_2)^⊥=U_1^⊥∩U_2^⊥` nie jest potrzebny wymiar skończony. Natomiast `V=U⊕U^⊥` i `U^{⊥⊥}=U` w dowodzie `thm:lin13-rozklad` wymagają **skończenie wymiarowej podprzestrzeni `U`**, nie całego `V`; jest to jawnie zapisane. W końcowej tożsamości `(U∩W)^⊥=U^⊥+W^⊥` poprawnie używa się skończenie wymiarowego `V`.
- **Ortogonalny rzut i najlepsze przybliżenie:** wzór `P_Uv=sum_j h(e_j,v)e_j` zachowuje właściwy kierunek sprzężenia. Sprawdzono `P_U^2=P_U=P_U^*`, `ker P_U=U^⊥`, kontraktywność, jednoznaczność najlepszego przybliżenia i `U={0}`.
- **Operator sprzężony:** w dowodzie istnienia `A^*` funkcjonał `F_w(v)=h_W(w,Av)` jest liniowy w `v`; po użyciu twierdzenia Riesza i sprzężeniu równania otrzymuje się `h_W(Av,w)=h_V(v,A^*w)`. Stąd `A^*` jest liniowe w `w`, ale przyporządkowanie `A ↦ A^*` jest antyliniowe. Weryfikacja obejmuje `(CA)^*=A^*C^*`, `ker(A^*A)=ker A` i równości obrazów z dopełnieniami.
- **Macierz Grama i najmniejsze kwadraty:** przy niezależnych kolumnach `G=B^*B` jest dodatnio określona, a `P=B(B^*B)^{-1}B^*` jest rzutem na ich rozpiętość. Dla `r=0` wszystkie iloczyny mają zgodne zerowe rozmiary. Układ równań normalnych `A^*Ax=A^*y` ma rozwiązania także przy zależnych kolumnach; zbiór rozwiązań to `x_0+ker A`, a jedyne rozwiązanie o najmniejszej normie należy do `(ker A)^⊥`. Sprawdzono `m=0`, `n=0`.
- **Dwa rzuty i przecięcia:** `(PQ)^*=QP` daje równoważność przemienności z samosprzężonością `PQ`. Wtedy `(PQ)^2=PQ` i obraz jest równy `U∩W`, więc `PQ=P_{U∩W}`. Rozważono również ostatnią tożsamość o dopełnieniu przecięcia.

## 4. Kontrola numeryczna niezależna od kodu rozdziałów

Lokalnie wykonano `/mnt/data/linear_algebra_iter19_check.py` (SHA256 `cd8011c9b63b614f8cf91b18eb4b98a44642583588c16a50a7fc8ddf04839219`), wykorzystując deterministyczny generator pseudolosowy i macierze zespolone różnych rozmiarów, w tym `0×n`, `m×0` oraz `0×0`.

**Wynik: 68 090 / 68 090 PASS, 0 FAIL.**

Badano polaryzację zespoloną i półtoraliniowość, Cauchy'ego–Schwarza, wzory Grama–Schmidta i Riesza, kryterium Grama, izometrie unitarne, tożsamość sprzężenia, jądro i rząd, rozwiązania normalne i o najmniejszej normie, równania przy deficycie rzędu, rzuty z macierzy Grama oraz produkty przemiennych rzutów.

Ponadto przygotowano trwały regresyjny [test LA12–13](../../../tools/test_linear_algebra_la12_la13_conventions.py) o analogicznym pokryciu i dodano go do `.github/workflows/linear-algebra-chapter.yml` oraz filtra ścieżek. **Wynik lokalnych 68 090 testów nie jest automatycznie wynikiem nowego kroku CI**; status tego kroku należy odczytać z konkretnego przebiegu.

Testy macierzowe nie weryfikują twierdzeń w pełnej ogólności (np. przestrzeni bez ograniczenia wymiaru). Z tej przyczyny szczegółowy dowód został skontrolowany niezależnie od testów.

## 5. Kontrola redakcyjna, LaTeX i CI

- W obu plikach występuje **70** odrębnych etykiet, **27** odsyłaczy oraz dokładnie **28** poprawnie sparowanych środowisk `proof`. Nie wykryto lokalnie powtórzonych etykiet ani naruszeń terminologii w sprawdzanym zestawie.
- Źródło pojedynczego rysunku TikZ w LA13 (rzut ortogonalny i reszta) jest spójne geometrycznie: wektor od rzutu do `v` jest prostopadły do narysowanej prostej. **Brak nowej bezpośredniej inspekcji wyrenderowanej strony PDF** w tej iteracji.
- [CI 45062408467](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45062408467) dla poprzedniej iteracji 18 zakończył się `completed/success`. Nie stanowi wyniku najnowszego testu LA12–13; jego osobne wykonanie podlega sprawdzeniu.
- **Próba nowego CI:** [run 45064401149](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45064401149) zakończył się `failure` z powodu brakującej zależności `numpy` na runnerze. Dodano instalację `numpy>=2.0,<3` w odrębnym kroku workflow, bez zmian w treści matematycznej. W ponownym [run 45064528288](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45064528288) krok **LA12–LA13 conventions** uzyskał już `success`; w chwili tej aktualizacji kompilacja PDF jeszcze trwała.
- Źródła LA12–13 nie zostały zmienione, wcześniejsza stabilizacja rozdziałów LA12–32 pozostaje zachowana. Nie dopisywano dodatkowego materiału bez zgody.

## 6. Decyzja i dalszy plan

**LA12 13/13 i LA13 15/15 — CZYSTE po indywidualnym audycie.** Po iteracjach 17–19 nowy rejestr pełnego przeglądu obejmuje **110 z 382** środowisk dowodowych, niezależnie od wcześniejszych audytów rozdziałowych i testów CI.

Kolejny etap: poszerzać per-dowodowy rejestr o rozdziały jeszcze nieoznaczone w ten sposób, nie resetując ukończonej stabilizacji. Po 382 indywidualnych kontrolach wykonać **jeszcze jedną sceptyczną iterację audytu** całego skryptu, w tym zamknięcie sprawdzenia PDF/odsyłaczy.