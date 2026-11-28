# Audyt CXXVI (126) — nierówności Sobolewa i izoperymetryczna
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia 29498d55f35be75a4e574fb22c6b818937e4001a, blob 153081cda6ffca637ad064884f1033554611c4a5. Commit źródłowy 1b67227a860b85b6e81c71cc39b0d34e5e9cb14f, blob 5fb52e784907c07cb087b5bb141486f33383d639.
## Wyniki
Dziewięć zastąpień, 2357 -> 2489 wierszy, zachowano wszystkie 37 etykiet w tej samej kolejności.
- Uściślono hipotezy nierówności produktowej, indukcję Höldera i Tonellego, przejście do wykładnika n/(n-1).
- Rozpisano nierówność Poincarégo na kuli jednostkowej z podwójną całką, dwoma zakresami parametru i kontrolą jakobianu. Jawnie sprawdzono skalowanie nierówności dla funkcji gładkich.
- Uzasadniono radialne odbicie przez analizę różniczki, wyznacznika i zamianę zmiennych. Wykazano brak dodatkowej miary na sferze przy sklejaniu ciągłych funkcji kawałkami C^1 (znoszenie wyrazów brzegowych). Splot i Fatou dają nierówność Sobolewa dla przedłużenia.
- Dla funkcji BV użyto przedłużenia zerowego wyłącznie jako funkcji L^1, bez założenia BV poza kulą; lokalne testy splotu mają nośnik wewnątrz kuli. Rozpisano oszacowanie gradientu przez wariację na całej kuli, zbieżność średnich oraz dwa przejścia Fatou. Nie zakładamy zerowej masy wariacji na sferach.
- Względna nierówność izoperymetryczna: osobne przypadki średniej <=1/2 i >=1/2.
- Naprawiono rzeczywistą lukę w dowodzie globalnej nierówności izoperymetrycznej: wygładzenie funkcji charakterystycznej zbioru o skończonej mierze nie musi mieć zwartego nośnika. Dodano odcięcie z błędem ograniczonym przez C*lambda_n(A)/R, następnie przejście R -> nieskończoność i epsilon -> 0.
## Otwarte
Kolejny audyt: lemat o przecięciu z kulą, wspólny zbiór dobrych promieni dla wszystkich testów, polarny Fubini i pochodne objętości, następnie oszacowania gęstości. Kompilacja, regresje i kontrola PDF pozostają otwarte. Stan 28/31.
