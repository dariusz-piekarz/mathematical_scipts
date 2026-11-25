# RRC 12 — iteracja 189, pierwsza lektura
Data: 2026-11-25. Początkowy blob f5da77cc4350e0e0557bc36002aad8a12ab41f98, końcowy f9fc2266096a37bbd73d0c2e0f1dc48b443c9e00. Commity f87db26638d0c3b6c5b1dd52d9d1a907bc29aa72 i 366d470b1cc67ea824e531f04f82d334c6cd4776.

| ID | Kotwica | Kryterium i wynik pierwszej lektury |
|---|---|---|
| PDE-12-001 | def:pde12-operator | Liniowość wykresu, domkniętość, kryterium domykalności i minimalne domknięte rozszerzenie — uzupełniono. |
| PDE-12-002 | lem:pde12-graph | Kryterium ciągowe, izometria, iloczyn skalarny i równoważność zupełności — uzupełniono. |
| PDE-12-003 | ex:pde12-derivative | Gęstość dziedziny, domkniętość i symetria pochodnej — uzupełniono. |
| PDE-12-004 | ex:pde12-derivative | Obie inkluzje dziedziny sprzężenia, znak zespolony i przejście przez gęstość — uzupełniono. |
| PDE-12-005 | def:pde12-adjoint | Jednoznaczność, liniowość, domkniętość sprzężenia i różnica symetrii oraz samosprzężoności — uzupełniono. |
| PDE-12-006 | thm:pde12-resolvent | Zupełność przestrzeni formy, Lax–Milgram, przypadek zerowy, liniowość i oszacowania — uzupełniono. |
| PDE-12-007 | thm:pde12-resolvent | Zwartość przez Rellicha–Kondrachova — poprawne, nie utożsamiać z ograniczonością. |
| PDE-12-008 | thm:pde12-resolvent | Samosprzężoność, dodatniość, jądro i gęstość obrazu — uzupełniono. |
| PDE-12-009 | def:pde12-laplacian | Jednoznaczność reprezentanta, oba kierunki charakterystyki dystrybucyjnej i zerowy ślad — uzupełniono. |
| PDE-12-010 | thm:pde12-A-selfadjoint | D(A)=Ran B, nieujemność, obie inkluzje dziedzin sprzężonych, domkniętość — uzupełniono. |
| PDE-12-011 | rem:pde12-corners | D(A)=H²∩H_0¹ dla C^{1,1}; obie inkluzje, odwołanie do rozdziału 15, brak zależności dowodu samosprzężoności od regularności — uzupełniono. |
| PDE-12-012 | rem:pde12-corners | Sektor wklęsły: harmoniczność, całkowalność, ślad przez odcięcie, laplasjan w L² i rozbieżność kwadratu drugiej pochodnej — pełne rozwinięcie dowodu. |

Zachowano 33 etykiety w tej samej kolejności; 27 wystąpień odsyłaczy (19 różnych) rozwiązanych w rozdziałach 09, 10, 11, 12, 15. Obie kotwice atlasref w AF 30 i 33 istnieją w źródłach. W sprawdzonych plikach brak powtórzeń etykiet; poprawny stos środowisk rozdziału 12. Poprawiono także tytuł „Obszar formowa” na „Dziedzina formy”. Nie wykonano testów, dedykowanego CI, kompilacji PDF ani Lean. Nie deklaruje się stabilizacji. Kolejny etap pierwszej lektury: twierdzenia spektralne dla operatorów zwartych, baza własna laplasjanu i dziedzina formy. Liczba końcowa kryteriów rozdziału jeszcze nieustalona.
