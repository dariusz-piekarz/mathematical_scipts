# Audyt CXXIX (129) — prostowalność i identyfikacja miar
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia e28bc3dea387cff9c69a2b01bb4ddeb694bf7edf, blob 4bbbf3ed6b90d0a296ebc01ca311deb48682a185. Commit źródłowy dce241866079a0e5ac8b0b92f4f5017ef7149d3b, blob f98b7c123d626ce2f54cb8099b365760fe41896d.
## Wyniki
Dziesięć zastąpień, 2879 -> 2995 wierszy, 37 etykiet zachowanych w kolejności.
- W argumencie stożkowym jawny wybór delta=omega_n*(alpha/16)^n/8, oszacowanie odległości od płaszczyzny i sprzeczne ograniczenia objętości V/8 oraz 3V/8. Jawna skala, pokrycie kostkami i iniektywność rzutu.
- Wzmocniono tezę do pokrycia całego brzegu zredukowanego przeliczalną sumą pełnych wykresów Lipschitzowskich. Dokładny wzór przedłużenia McShane'a na dziedzinie rzutu pojedynczego fragmentu, skończoność infimum i dowód własności Lipschitza.
- Naprawiono niesamodzielne założenia lematu identyfikacji miar: samą prostowalność zastąpiono konkretną własnością pokrycia wykresami, rzeczywiście udowodnioną wcześniej. Borelowskość S jest teraz jawnym założeniem, a nie nieuzasadnionym wnioskiem z definicji prostowalności. Rozłączny borelowski podział obejmuje całe S.
- Udowodniono borelowskość warstw jednostajnych oszacowań gęstości, zerową masę singletonów i kontrolę przez pokrycia o małej średnicy.
- Rozpisano gęstość miary Hausdorffa na borelowskim fragmencie wykresu: Rademacher, wzór na pole, porównanie przeciwobrazu kuli z elipsoidami, jawna objętość elipsoidy i błąd o(r^d) w punkcie Lebesgue'a, przeniesienie zbioru wyjątkowego przez odwzorowanie Lipschitzowskie.
- Potwierdzono etykiety thm:rademacher-28 i thm:lipschitz-area-coarea-28 w rozdziale 28.
## Otwarte
Następnie końcowa kontrola identyfikacji miar, przypadek n=1 twierdzenia De Giorgiego (wymaga uzasadnienia reprezentanta jednowymiarowego), dokładne zastosowanie różniczkowania miar i dalsze lematy warstwowania BV. Kompilacja i regresje pozostają do wykonania. Stan 28/31.
