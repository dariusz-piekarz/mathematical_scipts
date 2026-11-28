# PDE I — rozdział 08: stabilizacja

Data: 2026-11-25, audyt 127. **STABILNY w zakresie kontroli rozdziałowej.**

Źródło: chapters/pl/partial_differential_equations/08-transformata-fouriera-i-dystrybucje-temperowane.tex, blob 7e35b139c158ab1a6230fa1c2a7778d14a2743c2.
Rejestr: tests/mathematical/partial_differential_equations/chapter-08/regression.md, blob b26d3381fe6c3f1752b44ce2090650aa8d577939.

## Ostatnia lektura kontrolna — 086–092

| Kryterium | Kontrola matematyczna i szczegółowość | Wynik |
| --- | --- | --- |
| 086 | Funkcja x_j abs(f)^2 należy do S przez iloczyn i mnożenie współrzędniowe; pochodna w L¹, zanik składnika brzegowego R/(1+R)^2, Fubini oraz zbieżność zmajoryzowana na przekrojach, d=1 osobno. Leibniz i Cauchy–Schwarz uzasadniają całkowalność składników. | Bez zmian |
| 087 | Łańcuch od ujemnej części rzeczywistej do modułu i Cauchy'ego–Schwarza, poprawne zniesienie czynników Plancherela, stała 1/2. | Bez zmian |
| 088 | Obie normy dodatnie, kwadrat normy różnicy od rzutu przy iloczynie skalarnym liniowym w pierwszym argumencie; warunek równości wymusza c rzeczywiste ujemne. Ciągłość podnosi równość a.e. do punktowej, czynnik całkujący daje rozwiązanie ODE. | Bez zmian |
| 089 | Ograniczenie do hiperpłaszczyzny zachowuje półnormy z odpowiednimi zerowymi indeksami; odwrotnie półnormy iloczynu Gaussa i g rozdzielają się; niezerowość oraz d=1, przykład ostrości. | Bez zmian |
| 090 | Przesunięcie i modulacja zachowują S; podstawienie y=x+ae_j daje fazę exp(ia(xi_j+b)) i argument xi+be_j; sprawdzono znaki obu przesuniętych norm. | Bez zmian |
| 091 | Dodatnie mianowniki, całkowalność pierwszych momentów przez Cauchy'ego–Schwarza, drugie momenty przez S, miary o masie 1 i poprawne odchylenia standardowe w nieunitarnej konwencji. | Bez zmian |
| 092 | Podsumowanie rozróżnia topologię S i słabą* na S', unitarność po normalizacji, hipotezy mnożników i zakres regularności eliptycznej; kryterium Poissona ograniczone do danych L² i rozwiązań H², bez nieuzasadnionych twierdzeń o problemach brzegowych. | Bez zmian |

## Bilans stabilizacji

- Pierwsza lektura (103–113): 92 kryteria semantyczne w trwałym rejestrze, 11 sekcji merytorycznych i podsumowanie.
- Druga lektura (116–121): 92/92, 42 bez zmian, 50 po uściśleniach.
- Lektura kontrolna (123–127): 92/92 bez zmian; raporty control-001-033.md, control-034-052.md, control-053-068.md, control-069-085.md i powyższa tabela. Brak nowych istotnych błędów i luk dowodowych w kontrolowanym zakresie. Nie jest to recenzja zewnętrzna.
- Łączna kontrola techniczna (122/126, raport ci-second-reading.md): końcowy CI 45595506552 completed/success, job 139140395511, 12/12 testów w 0,052 s, 39 etykiet, 92 rozwiązane wystąpienia odsyłaczy, 92 kotwice. PDF 30 stron A4, kontrola układu wszystkich stron w skali plansz w audycie 126. Brak Overfull/Underfull i krytycznych błędów końcowej kompilacji. Pozostało 21 ostrzeżeń o pustych celach hiperłączy do innych rozdziałów w izolowanym PDF.
- Ponownie porównano 12/12 wejściowych blobów bieżącej gałęzi z drzewem head zaliczonego CI 5864e953691a5cef7da3034a1254cef88ecc4603; wszystkie identyczne. Rejestr zawiera 92 kolejne unikatowe ID z istniejącymi kotwicami. Nie zmieniano źródła, rejestru, testów ani workflow.
- Testy numeryczne są rzeczywiście wykonanymi testami przykładów, a kryteria semantyczne są lekturą matematyczną; nie są formalnymi dowodami Lean. Nie wykonywano formalizacji Lean ani końcowej kompilacji całego tomu.

Artefakt: https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45595506552/artifacts/15014325429, PDF SHA256 455ef0f51648459583d7e4cbee9653597d123bf27cf478f206939d2ae7c50b3f.

Stabilizacja rozdziału 08 zakończona dla wskazanego źródła. Zachować rejestr i testy regresyjne. Następna iteracja 128: pierwsza lektura rozdziału 09 (chapters/pl/partial_differential_equations/09-przestrzenie-sobolewa.tex), rozpoczęta od wprowadzenia i pierwszej sekcji, z możliwością propozycji uzupełnień tylko na etapie pierwszej lektury. Końcową kontrolę struktury, CI i PDF wykonywać łącznie, gdy jest to możliwe.
