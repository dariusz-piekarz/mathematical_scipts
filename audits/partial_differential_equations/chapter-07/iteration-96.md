# PDE-07 — iteracja 96: druga lektura sekcji 7.1–7.2

Data: 2026-11-25. Przed zmianami źródło ccabfced1d41d4b25f2853aed43dff90c70b8ea6. Po zmianach commit 1e8d4cb0a2fe54059b76374362ba2d6bec411386, blob 26e76ef3e6d554997e35ee1df3b61900e09ad16b. Zachowano wszystkie 36 etykiet i wszystkie 66 wystąpień odsyłaczy, ich kolejność oraz poprawne zagnieżdżenie środowisk. Pozostałe sekcje niezmienione.

| ID | Wynik drugiej lektury | Uzasadnienie |
|---|---|---|
| PDE-07-001 | PASS | Definicje nośnika, wielowskaźników, półnorm i pustego K spójne. |
| PDE-07-002 | PASS po korekcie | Uzupełniono argument, dlaczego rodzina półnorm rzeczywiście daje najsilniejszą topologię lokalnie wypukłą z ciągłymi włożeniami. |
| PDE-07-003 | PASS po korekcie | Uzasadniono wyczerpanie, zwartość i warunki ostre; ważona półnorma wykrywająca uciekające nośniki pozostaje poprawna. |
| PDE-07-004 | PASS | Pochodne znikają poza nośnikiem, globalne półnormy są ciągłe, redukcja do granicy zero poprawna. |
| PDE-07-005 | PASS | Zwarty nośnik ma dodatni dystans od dopełnienia, przedłużenie zerem jest gładkie. |
| PDE-07-006 | PASS | Rekurencja wielomianów, zanikanie pochodnych i ich ilorazów przez s oraz złożenie z 1 minus kwadrat normy poprawne. |
| PDE-07-007 | PASS | Przesunięcia nie mają wspólnego zwartego nośnika mimo lokalnego zanikania. |
| PDE-07-008 | PASS po korekcie | Zastąpiono nieokreślone supremum po pustym K przez zdefiniowaną półnormę; obie implikacje i skalowanie pozostają poprawne. |
| PDE-07-009 | PASS | Normalizacja zespolonym T(psi_j) jest dopuszczalna, wspólny K i zanik każdej półnormy dają sprzeczność. |
| PDE-07-010 | PASS po korekcie | Podano jawny test o wartości 1 w zerze, odróżniając ją od normalizacji całki; lokalnie skończona suma i skalowanie dowodzą dokładnego rzędu. |
| PDE-07-011 | PASS | Regularne funkcjonały i delta są liniowe bez sprzężenia, oszacowania lokalne poprawne. |
| PDE-07-012 | PASS | Lokalny splot ma testy o zwartym nośniku w większej kuli i znika; obcięcie daje globalne L¹. |
| PDE-07-013 | PASS po korekcie | Zastąpiono ogólne odwołanie do analogii pełnym argumentem gęstości C_c w L¹ przez regularność miary i jawną funkcję odległości. Przesunięcia, Tonelli, majoranta i przeliczalne pokrycie poprawne. |
| PDE-07-014 | PASS | Skalowanie testu i absolutna ciągłość całki dają sprzeczność z działaniem delty. |

Wynik: 9 kryteriów bez korekty, 5 po korekcie, 14/14 zweryfikowanych semantycznie. Wzmocniono istniejące kryteria 002,003,008,010,013 bez zmiany ID; rejestr nadal zawiera 70 kryteriów, commit dce623092ad436676a820fabb3a337e79be872fd, blob 54b7f57288aeb9ea995a461e978a92bb1ffe1b8f. Nie dodawano nowych tematów. Kontrola źródła i rejestru wykonana, nie jest formalizacją Lean.

CI dla commitu rejestru: [{"id":45584928939,"name":"PDE - chapter 07 audit","status":"in_progress","conclusion":null}]. Poprzednie CI 45577455405 odnosiło się do wersji przed korektą; trzeba potwierdzić nowy przebieg i ponownie sprawdzić render. Nie uruchomiono lokalnie testów Python w tej iteracji, pełnej kompilacji tomu ani Lean. Następna iteracja 97: druga lektura sekcji 7.3–7.4, kryteria 015–030. Rozdział pozostaje nieustabilizowany.
