# AA-61 — audyt II: hipotezy, dowody i regresje macierzowe

24 listopada 2026 r. Gałąź biblioteka-matematyczna-iteracja-6. Blob przed korektą 959516491b364b5bc5c6ce8b16ef0f7f8740b2a6, po korekcie f99bd1c134fc5fa9a8d7843b58fa2a8c5dc8aae0 (3767716038feb39fe04a91888f9f6da7668a0873).

## Kontrola matematyczna
Ponownie sprawdzono przeniesienie bazy układu do K przez wyznacznik całkowity, odejmowanie korzenia prostego przez dodatni iloczyn skalarny i ciąg korzeniowy, domknięcie i nilpotentność podalgebr przez wysokości, generowanie przez indukcję, relacje Serre'a i dokładność ich wykładników, rozkład ideałów przez projekcje wagowe, komutowanie składowych, domknięcie przy przeciwnych korzeniach, zejście do prostego korzenia oraz propagację po diagramie. Nie stwierdzono fałszywej tezy. Uzupełniono hipotezy, znaczenie dodatniej liczby całkowitej w nieuporządkowanym K, niepustość zbioru dodatnich korzeni, indukcję dla szeregu pochodnego i argument z niezdegenerowanym parowaniem przy przejściu do przeciwnego korzenia. Doprecyzowano sumę mnogościową hiperpłaszczyzn i poprawiono język. Nie rozszerzono zakresu. Audyt zawiera korekty, licznik czystych audytów 0/2.

## Regresje i CI
Dodano tools/tests/test_abstract_algebra_ch61.js w 73f98cbb999c26ea110c9cce4a71cd3d704eb78d. Funkcję uruchomiono bezpośrednio w JavaScript: PASS, 12 modeli A1–A6 i C1–C6, 182 uporządkowane pary generatorów, 280 sprawdzeń minimalnych wykładników Serre'a (160 wykładnik 1, 110 wykładnik 2, 10 wykładnik 3), 24 zerowe nawiasy między składowymi sl2 i sl3. Rachunki na małych całkowitych macierzach, bez przybliżeń. Zaktualizowano 12 starszych testów liczby rozdziałów i globalną bramkę w 5b4f5c50806aece3c09e0a8eb6906f110c82d0fe; workflow w 6f2a71396dd9040cf36ae0c80475091d32e5b42d. Pełny CI jeszcze niepotwierdzony. Drugi niezależny zestaw i PDF pozostają do wykonania.

AA-61 W AUDYCIE, AA-62 nieotwarty.
