# AA-52 — audyt VI: kontrola szeregów Hilberta niezmienników

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.

## Niezależne dokładne obliczenia
Uruchomiono lokalnie Python/SymPy. Dla generatorów kwaternionowych z AA-52 domknięto grupy przez BFS i mnożenie Hamiltona nad ciałami QQ(sqrt(2)) oraz QQ(sqrt(5)). Otrzymano 24, 48, 120 elementów oraz odpowiednio 5, 7, 9 różnych śladów t=2a. Dla każdej grupy zbudowano histogram liczności N_t. W pierścieniu wielomianowym K[z] utworzono iloczyn D wszystkich różnych mianowników d_t=1-tz+z² i wielomian P=sum_t N_t D/d_t; dzielenie było dokładne (exquo). Sprawdzono równości wielomianów P(1-z^a)(1-z^b)=|G|D(1+z^c) dla trójek (a,b,c)=(6,8,12),(8,12,18),(12,20,30). Wszystkie trzy asercje przeszły. Zatem dokładne szeregi Hilberta dla konkretnych modeli to:
- 2T: (1+z^12)/((1-z^6)(1-z^8));
- 2O: (1+z^18)/((1-z^8)(1-z^12));
- 2I: (1+z^30)/((1-z^12)(1-z^20)).

Uzasadnienie: wartości własne reprezentacji naturalnej to lambda,lambda^(-1). Funkcja tworząca śladów potęg symetrycznych to 1/((1-lambda*z)(1-lambda^(-1)*z))=1/(1-tz+z²). Uśrednienie charakteru po grupie daje wymiar przestrzeni niezmienniczej, ponieważ uśredniona macierz jest rzutem na tę przestrzeń. Zatem P/(|G|D) jest szeregiem Hilberta. Nie wyciągamy z samego szeregu wniosku o konkretnej prezentacji pierścienia niezmienników.

Niezależnie dla d=0,...,60 wyliczono s_d(t) z rekurencji s_0=1, s_1=t, s_d=t*s_(d-1)-s_(d-2), dokładnie uśredniono po grupie i porównano z liczbą rozwiązań d=ai+bj+e dla i,j>=0, e w {0,c}. Każdy stopień przeszedł: 61/61 na grupę, 183/183 łącznie. Kod wyjścia 0. Rachunek potwierdza minimalne dodatnie stopnie 6,8,12 i stanowi dodatkową kontrolę zgodności AA-52. Nie rozszerzono tekstu rozdziału ani zakresu o prezentację pierścienia niezmienników.

## CI i stan
Aktualny blob a151f25b5b4e083cf39621c34fb0bca6af3948fc; run 45304703515, job 138145565432, head 52acf372ac64229c8f13fc20b6f62c88377c5b95. Przy ostatnim odczycie: 107 kroków success, 1 in_progress, 5 pending, brak niepowodzeń i brak artefaktów. Ostatni etap kompilacji/weryfikacji pozostaje niepotwierdzony; PDF nie został obejrzany. Źródło matematyczne i workflow bez zmian. AA-52 W AUDYCIE; AA-53 nieotwarty.
