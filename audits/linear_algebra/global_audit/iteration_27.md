# Algebra liniowa — globalny audyt 27: rozdział LA29

**Data:** 22 listopada 2026. **Gałąź:** biblioteka-matematyczna-iteracja-6.
**Etap:** LA29 — Grassmanniany i współrzędne Plückera.
**Bazowy blob:** 55fc55e2ff1b95838e0b2ca1c4ec0a6018af64dd; **bazowy HEAD:** 31f65e151d9d8fa557947feee3cbbee6c6c101b2.
**Werdykt:** pełna lektura 6 dowodów, jedna korekta precyzji matematycznej w przykładzie; licznik czystych kontroli nowego źródła 0/2, oddzielny kontrolny audyt +1 oczekuje.

## 1. Konstruktywny i krytyczny przegląd całego rozdziału

Odczytano cały plik 743 wierszy (przed korektą), 4 twierdzenia, 2 stwierdzenia, 2 definicje, 6 dowodów, 6 przykładów, 2 uwagi i 2 rysunki. Każdy dowód oceniono także sceptycznie pod kątem hipotez i przypadków brzegowych:

1. Atlas Grassmannianu: poprawna identyfikacja L=Gamma(A), gładkość przejść, holomorficzność w przypadku zespolonym, zwartość przez idempotenty samosprzężone oraz oddzielność i drugi aksjomat przeliczalności. Przypadki k=0 i k=n są jednoelementowe; nie wymagają osobnej poprawki.
2. T_L Gr_k(V) jako Hom(L,V/L): niezależność przedłużenia v(t), przejście do wykresu, iniektywność i surjektywność, niezależność od dopełnienia.
3. Wiązka tautologiczna i ilorazowa: jawne lokalne trywializacje, dokładność ciągu, ortogonalna identyfikacja z dopełnieniem.
4. Stiefel i ilorazy grup: transytywność O(n)/U(n), stabilizatory blokowe, gładkość sekcji przez ortonormalizację.
5. Osadzenie Plückera: jednorodność minora i zmiana bazy, wzór L={w:w∧ξ=0}, odzyskiwanie współrzędnych macierzy przez mniejsze minory, immersja i osadzenie. Sprawdzono dokładnie znaki w równaniu p12 p34−p13 p24+p14 p23=0.
6. Odwzorowanie Gaussa: lokalna postać A=D_Q F(D_P F)^(-1), własność gładkości, cofnięcie wiązek stycznej i normalnej.

Przykłady: dwie mapy RP^1, styczna do prostych, Möbius, orientacja płaszczyzn w R^3, Plücker Gr_2(R^4), parabola; sprawdzono też konstrukcję uniwersalnej wiązki przez funkcje odcięcia.

**Wykryta i poprawiona nieprecyzyjność w przykładzie paraboli:** całe dG_p ma typ T_pM→T_{G(p)}Gr_1(R^2), a dopiero dG_p(e1) jest utożsamiane przez twierdzenie o stycznej z D∈Hom(T_pM,R²/T_pM), D(e1)=2[e2]. Wcześniejsza fraza myliła te dwa poziomy odwzorowania. Nie zmieniano wyników, wzorów, etykiet ani zakresu tematycznego.

## 2. Testy niezależne

Przeprowadzono lokalnie skrypt /mnt/data/la29_global27_regressions.py, NumPy, seed 20261122. Wynik: **10 501/10 501 PASS**:
- 5400 kontroli rzutowania ortogonalnego (symetria, idempotencja, niezmienniczość wykresu);
- 1800 rekonstrukcji współrzędnych wykresu z rzutowania;
- 1800 testów niezanikania minorów Plückera;
- 1000 sprawdzeń równania Plückera Gr_2(R^4);
- jeden jawny test wielowektora nieskładalnego;
- 500 sprawdzeń pochodnej Gaussa paraboli.

To kontrole numeryczne, nie formalny dowód ogólnego twierdzenia. Kontrola statyczna oryginału: 19 unikalnych etykiet bez duplikatów; 20 odsyłaczy bez brakujących lokalnych celów; 6 par proof, 2 pary figure, 2 pary tikzpicture. Zmiana nie dotyka żadnego z tych znaczników.

## 3. PDF, CI i ograniczenia

Pobrano rzeczywisty ZIP artefaktu 14772992061 z [CI 45070637516](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070637516) (completed/success, commit 817e90c82388160253cbc4f8b99a81cc6e570986). PDF miał 320 stron A4. LA29 zajmował strony PDF 287–294; wyrenderowano i wzrokowo oceniono wszystkie 8 stron. Nie widać nakładania etykiet, rysunków, podpisów ani obcięcia tekstu. Log tego CI: 0 błędów LaTeX, 0 ostrzeżeń LaTeX, 0 overfull, 0 underfull, 0 niezdefiniowanych poleceń i 0 brakujących znaków.

**Te wyniki dotyczą poprzedniej wersji LaTeX.** Poprawka niniejszej iteracji wymaga aktualnego CI, dwóch nowych przebiegów kompilacji i wizualnej kontroli nowego PDF przed uznaniem stabilności. Próba lokalnego klonowania repozytorium nie powiodła się wskutek błędu DNS github.com. Nie deklarujemy wykonania nowej kompilacji na zmienionym źródle.

## 4. Stan kolejki

Po audycie 6 dowodów LA29 globalny rejestr indywidualnie przeanalizowanych dowodów wynosi **363/382**. Pozostało 19: LA30 (3), LA31 (6), LA32 (10).

Ponieważ zmieniono źródło LA29, rozdział jest **ponownie otwarty do stabilizacji, 0/2 czystych audytów po zmianie**. Najpierw dwa niezależne czyste przebiegi aktualnego pliku, CI/PDF, a następnie osobny sceptyczny audyt +1. Dopiero potem LA30. Historyczna zamknięta sekwencja audytów LA12–32 nie jest uruchamiana od nowa.

Raport jest zapisem kontroli, nie potwierdzeniem wyniku przyszłego workflow CI commitu z tym raportem.
