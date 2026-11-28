# Lean 4 — LST-01 `thm:equiv-test`: audyt dowodu i pochodzenia logu CI

**Etap:** stabilizacja istniejącej formalizacji `LST-01:thm:equiv-test`; bez przejścia do nowej etykiety.  
**Data:** 2026-11-22.  
**HEAD bezpośrednio przed zapisem:** `107661b5484b9a7e24cb0186589cafdd6186b593`. W czasie odczytów HEAD zmienił się z `d5575aced5df606924c366c630432acd7971d469`; porównanie wskazało tylko `chapters/pl/general_topology/25-continua-i-ich-struktura.tex`, poza zakresem.  
**Odczytano:** `AGENTS.md`, `application/docs/LEAN_FORMALIZATION_PLAN.md`, `application/ROADMAP_I_DZIENNIK.md`, `application/lean/manifest.json`, `application/lean/src/LST01_SyntaxValuations.lean`, kanoniczny `chapters/pl/logic_and_set_theory/01-zdania-i-spojniki-logiczne.tex` oraz rzeczywisty log zadania CI.

## Porównanie twierdzenia z oryginałem

Oryginał: `\\label{thm:equiv-test}`: dla dowolnych formuł zdaniowych `φ, ψ`, semantyczna równoważność `φ ≡ ψ` zachodzi wtedy i tylko wtedy, gdy formuła `φ ⇔ ψ` jest tautologią. Definicja poprzedzająca twierdzenie wymaga wspólnego wartościowania **wszystkich** liter obu formuł.

Lean: `LST01.Formula` jest typem indukcyjnym z `atom : Nat → Formula` i konstruktorami pięciu spójników; `Valuation := Nat → Bool`; `equivalent p q := ∀ ν, eval ν p = eval ν q`; `tautology p := ∀ ν, eval ν p = true`. Deklaracja `lst01_syntax_equivalence_test (p q : LST01.Formula) : LST01.equivalent p q ↔ LST01.tautology (.iff p q)` zachowuje oba kierunki, wspólne wartościowanie, powtórzone litery i odróżnienie składni od `Prop`. Semantycznie zgodna z odczytanym źródłem; brak dodatkowych hipotez. Nie dokonano zmian w kodzie.

## Nowy dowód wykonania: pobrany surowy log CI

Pobrano **rzeczywistą treść** logu joba `137212099319`, a nie tylko status kroków, z przebiegu [45023719378](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45023719378) (22.11.2026, 12:43–12:47 UTC). Log zawiera:
- `Lean (version 4.26.0, x86_64-unknown-linux-gnu, commit d8204c9fd894f91bbb2cdfec5912ec8196fd8562, Release)`;
- `Mathlib revision: 2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`;
- rzeczywiste wywołanie `lake env lean "$file" > "$log" 2>&1`;
- `'lst01_syntax_equivalence_test' depends on axioms: [propext]`;
- pomyślnie zakończone kroki kompilacji z kontrolą aksjomatów i inspekcji Lean MetaM; wynik joba `completed/success`.

`propext` jest standardowym aksjomatem Lean, nie `sorryAx`; w kontrolowanym logu nie ma dodatkowych aksjomatów dla tej deklaracji. Weryfikacja logu potwierdza rzeczywistą **historyczną** kompilację, nie nowe lokalne uruchomienie. Lokalnie `lake` i `lean` nie występują w PATH: `toolchain_unavailable`. W tym przebiegu audytu nie wykonano świeżego `lake env lean`.

## Integralność i rygor stabilizacji

Porównanie GitHub `422ee039d4097b78660832423eefd8953b1a5cbf...biblioteka-matematyczna-iteracja-6` nie wykazało zmian `application/lean/src/LST01_SyntaxValuations.lean` ani kanonicznego `01-zdania-i-spojniki-logiczne.tex`; zmieniono jedynie raporty Lean w tym obszarze. Odczytane SHA blobów Git: Lean `71f5206b8642f53c45d28004ced57d02e0ebe984`, TeX `03f0971888288934e47c3453fd8f0de0a2c71469`. Manifest podaje SHA256 dokumentu `9b5cbe26dee8ed5bc437cb3a0d19638eafc5d9ae178a3caa545b8bcf5842b8d0`; nie przeliczono go niezależnie z bajtów w tym środowisku (Git blob SHA-1 **nie jest** SHA256). Nie zaliczać pełnego testu integralności.

**Kontrole od ostatniej zmiany formalizacji:** jedna nowa kontrola krytyczna źródła i logu w tej iteracji; wcześniejsze raporty są historyczne, nie doliczono ich automatycznie do licznika stabilizacji. **Oddzielny końcowy audyt stabilizacyjny:** niezaliczony — brak nowej kompilacji i niezależnego SHA256. **Status etapu:** nie deklarować nowej stabilności ani certyfikatu aplikacji.

**Korpus:** 5/20–30 etykiet z mapowaniem i zatwierdzonym statusem semantycznym; 5/5 występuje w niezmienionym module historycznie skompilowanym w CI (przy czym dla bieżącej iteracji 0 nowych uruchomień Lean i 0 nowych formalizacji). `certificate=false` pozostaje odrębne od sukcesu CI.

**Następny krok tego samego etapu:** przeliczyć SHA256 kanonicznego TeX-a, zestawić dokładny commit przebiegu CI z niezmienionymi bajtami źródeł i ponownie wykonać `lake env lean` oraz `#print axioms` na aktualnym HEAD; następnie czyste kontrole i dodatkowy niezależny audyt końcowy. Nie modyfikowano innych ścieżek.
