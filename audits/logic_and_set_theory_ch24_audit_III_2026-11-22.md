# Logika i teoria mnogości — rozdział 24, audyt III

Data: 22 listopada 2026 r.  
Źródło: `chapters/pl/logic_and_set_theory/24-gorne-twierdzenie-lowenheima-skolema-i-paradoks-skolema.tex`  
SHA źródła przy kontroli: `f69a3a237a7641fce84c6e6b5684a9d45ae1d06b`

## Niezależna powtórna kontrola
- Diagram elementarny zawiera pełne zdania rozszerzonego języka, w tym kwantyfikatory i negacje; zachowuje wartości wszystkich formuł z parametrami, nie jedynie relacje atomowe.
- Ponownie rozpisano logikę czterech kroków górnego twierdzenia: skończona spełnialność `ED(M) ∪ {d_i≠d_j}`, zwartość, elementarne zanurzenie `j`, dokładna moc `λ` po użyciu dolnego twierdzenia oraz transport interpretacji dla dosłownego rozszerzenia `M≼N`.
- W lemacie o sumie rosnącego ciągu elementarnego osobno oceniono kierunek od sumy do wcześniejszego etapu przy formule egzystencjalnej. Świadek należy do pewnego skończonego etapu, a przechodniość elementarności umożliwia przeniesienie zdania w dół.
- Sprawdzono, że model `Th(N)∪{n<c}` powstaje z rzeczywistej skończonej spełnialności w standardowych liczbach naturalnych i kompaktności; przeliczalny podmodel jest budowany w języku z nową stałą, zatem zachowuje tę stałą.
- Przy paradoksie Skolema rozdzielono zewnętrznie przeliczalny zbiór elementów `E_r` od braku wewnętrznego obiektu reprezentującego bijekcję. Istnienie modelu ZFC pozostaje jawnie warunkowe.
- Przy kategoryczności arytmetyki Peana drugiego rzędu pełna semantyka pozwala podstawiać `E={S^n(0):n∈N}` do aksjomatu indukcji; tego kroku nie wolno przenieść na arbitralną semantykę Henkina.
- Odsyłacze do zwartości, dolnego twierdzenia i wprowadzenia semantyki są poprawne. Nie znaleziono nowych błędów językowych, niespójności oznaczeń ani ukrytych założeń.

## Walidacja techniczna
18 etykiet, 11 odsyłaczy; 4 twierdzenia, 2 lematy, 1 wniosek, 2 definicje, 2 przykłady, 6 uwag, 7 dowodów. Testy rozdziału 24: 10/10 PASS. Cały skrypt 01–26: 202 strony, GitHub Actions 45003169518: SUCCESS. Pięciostronicowy PDF rozdziału 24 był już sprawdzony wizualnie w poprzedniej iteracji.

**Wynik audytu III: stabilny, brak nowych usterek.** Nie dodawano nowych twierdzeń.
