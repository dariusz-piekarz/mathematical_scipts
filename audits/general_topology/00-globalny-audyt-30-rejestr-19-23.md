# Topologia ogólna — audyt globalny 30: wersjonowany rejestr 19–23 i odsyłacze między rozdziałami

**Data:** 2026-11-23. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.
**Punkt pomiaru:** `e7ff9254923fd87f9cad05301b15704e7038befd`; wszystkie badane źródła pochodzą z jednego commitu, nie z kolejnych ruchomych głowic.
**Zakres:** inwentarz rozdziałów 19–23, zgodność wersji ze sprawozdaniami globalnymi 21–25 i konkretne kontrole odsyłaczy do wcześniejszych rozdziałów. Nie jest to ponowne niezależne udowodnienie wszystkich twierdzeń.

## Rejestr kodu źródłowego

| Rozdział | Blob źródła | Proof | TikZ | Figure | Labels | Refs | Zgodny pełny audyt |
|---|---|---:|---:|---:|---:|---:|---|
| 19 — Przestrzenie polskie | `dd05dd723a4e92756d1e339309079c68a4580485` | 9 | 0 | 0 | 23 | 1 | Globalny 21 (9/9) |
| 20 — Zbiory analityczne i operacja Suslina | `2607376331f94935063107dee49148b45cc1679f` | 11 | 0 | 0 | 23 | 23 | Globalny 22 (11/11) |
| 21 — Topologie na rodzinach podzbiorów | `a8e0c4dbcf3c3100bf6b3c9e067b6fce0ddaa73b` | 15 | 1 | 1 | 31 | 9 | Globalny 23 (15/15) |
| 22 — Zbieżność Kuratowskiego, Wijsmana i Attoucha–Wetsa | `33765c2bb1b3065f4ad32596795c3d1981b48dda` | 11 | 1 | 1 | 28 | 20 | Globalny 24 (11/11) |
| 23 — Wymiar topologiczny | `9dc1ed4784d929b405d00a3216865418f240a37c` | 20 | 1 | 1 | 40 | 23 | Globalny 25 (20/20) |
| **Razem 19–23** | — | **66** | **3** | **3** | **145** | **76** | **5 zgodnych raportów** |

Dla każdego pliku potwierdzono `begin{proof}=end{proof}`; dla 21–23 również zgodne liczby otwarć i zamknięć `tikzpicture` oraz `figure`. Brak powtórzonych etykiet wewnątrz pojedynczych źródeł i — po uwzględnieniu bloku 13–18 — w łącznym zbiorze **13–23 (264 etykiety i 93 wystąpienia odsyłaczy)**. Nie wykryto dopasowań do pięciu wybranych grup niedozwolonych form: `zwartościowani*`, `zbieżności zwartej`, `pierwszo-przeliczaln*`, `drugoprzeliczaln*`, `sekwencyjn*`.

## Kontrola faktycznych zależności od wcześniejszych rozdziałów

Każdy odsyłacz 19–23 został porównany z etykietami całego bloku 13–23. Jako prawidłowe zewnętrzne zależności wykryto:

- **20 → 19**: `ch:topog-polskie-borelowskie`, `ex:topog-polskie-cantor-baire`, `thm:topog-polskie-iloczyn`, `lem:topog-polskie-otwarte-fsigma`;
- **21 → 18**: `ch:topog-przestrzenie-odwzorowan`; **21 → 14**: `lem:topog-baire-zwarte-domkniecie`;
- **22 → 21**: `ch:topog-hiperprzestrzenie`, dwa odwołania do `def:topog21-fell`, `prop:topog21-fell-nets`; **22 → 14**: `lem:topog-baire-zwarte-domkniecie`.

Pozostały **cztery wystąpienia** odsyłaczy wychodzących poza zakres 13–23: dwukrotne `thm:topog-zwartosc-ultrafiltry` w rozdziale 21 oraz `thm:topog-zwartosc-hausdorff-normalna` i `thm:topog-tychonoff-iloczyny` w rozdziale 23. **Bezpośrednio odczytano aktualny rozdział 07**, blob `0c31028e8fd301d805781b676c6713a2572501cf`: wszystkie trzy etykiety istnieją. Tym samym żaden z odsyłaczy rozdziałów 13–23 nie pozostał nierozwiązany w sprawdzonym zbiorze źródeł.

## Powiązanie z audytami oraz ograniczenia pomiaru

Odczytano pełne raporty globalne 21, 22, 23, 24 i 25. Każdy poświadcza kontrolę **wszystkich** środowisk `proof` swojego rozdziału i odnosi się do bloba identycznego ze źródłem w pomiarze. Odrębnie istnieją lokalne cykle 2+1. Raport ten porządkuje tę dokumentację, nie nalicza tych samych kontroli ponownie i nie ogłasza formalnego dowodu matematycznej poprawności.

Workflow [45129914798](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45129914798) dla pomiarowego commitu zakończył się `completed/success`. W tej iteracji nie pobrano nowego PDF ani nie oglądano ponownie trzech rysunków; ich obecność i sparowanie w LaTeX to kontrola strukturalna, nie wizualna.

**Werdykt: PASS inwentarza 19–23 i zewnętrznych etykiet**. Pełny audyt matematyczno-wydawniczy pozostaje otwarty. Następna kontrola musi zsumować rejestry 01–23 na jednym SHA, rozliczyć historyczne liczby rysunków 24/27 i przeanalizować także źródła 24–26 w kontekście całego wydania.
