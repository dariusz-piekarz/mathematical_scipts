# AA-50 — audyt V: regresja dla różnych czynników i krotności

Data: 24 listopada 2026 r. Gałąź: biblioteka-matematyczna-iteracja-6.
Źródło odczytane ponownie: blob fcd1dcc205a120df3c9d69b2ae1b04daf5b785b8.
Poprawka IV: 611ac48fbb27eec6529c6dc4ed0d00fd9878b16b.

## Wykonane sprawdzenie
Dla q=2/x², f=T−2/x, g=T+1/x oraz D=∂x+(q−T²)∂T sprawdzono dokładnie Df=−(T+2/x)f i Dg=−(T−1/x)g.
Dla F=u f^m g^n, u∈{x,x²+1,1/x}, (m,n)∈{(1,1),(2,3),(4,1)}, uruchomiono lokalnie SymPy: 9/9 kombinacji PASS. H=DF/F jest wielomianem stopnia 1 w T; H=u'/u+m Df/f+n Dg/g; pominięcie u'/u daje w każdym przypadku fałszywą tożsamość. Niezależnie sprawdzono oba pierwiastki Riccatiego: 2/2 PASS.
Ponowna lektura poprawionego dowodu potwierdza poprawność argumentu w lokalizacji oraz odwracalność krotności w charakterystyce zero.

## Utrwalenie regresji
Próba modyfikacji dotychczasowego testu zakończyła się konfliktem 409. Po ponownym odczycie utworzono osobny test tools/tests/test_abstract_algebra_ch50_nonmonic.py, commit 79f24efd15ca6e33833e392e8cf4aeeaa8d52d87, blob 7ff8ae1933a11768a6dc015db08466bfbce7a4d1. Nie nadpisano istniejących testów. Należy jeszcze potwierdzić, że CI uruchamia nowy plik; nie zakładamy tego z samego faktu zapisu.

## Bramki
Odczyt statusów commitów 92259f4a8b962d42124d7e3fec66d27635a8bdb9 i 79f24efd15ca6e33833e392e8cf4aeeaa8d52d87 zwrócił puste listy. Odczyt workflow powiązanych z 611ac48fbb27eec6529c6dc4ed0d00fd9878b16b (ograniczony przez API do PR) również pusty. Nie jest to dowód braku uruchomienia push CI ani dowód sukcesu. Pełna regresja obu wcześniejszych zestawów i nowe oględziny PDF nie zostały potwierdzone. 

AA-50: W AUDYCIE. AA-51 nieotwarty. Następny krok: uruchomienie nowej regresji w CI, potwierdzenie pełnego wyniku na aktualnym SHA, kontrola artefaktu PDF. Historyczne raporty pozostają bez zmian.
