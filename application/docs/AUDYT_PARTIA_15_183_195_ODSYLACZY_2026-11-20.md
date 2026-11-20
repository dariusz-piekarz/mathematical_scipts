# Biblioteka matematyczna — audyt odsyłaczy, partia XV (183–195)

Data: 20 listopada 2026 r.  
Gałąź: `biblioteka-matematyczna-iteracja-6`  
Źródło kolejności: `reference_provenance_audit_355.json` (355 rozdziałów; indeksowanie od 1).  
Zakres: 13 wystąpień; **7 błędnie oznaczonych jako `missing` odsyłaczy międzytomowych**, **6 `ambiguous` z lokalnym kandydatem**.

## Mapa rozstrzygnięć

| Nr | Źródło | Oryginalny odsyłacz | Typ | Preferowany cel | Treść |
|---:|---|---|---|---|---|
| 183 | `P4-17:3` | `I-ch:condexp` | międzytomowy (xr-hyper) | P1-10: `ch:condexp` | Warunkowa wartość oczekiwana |
| 184 | `P4-23:3` | `I-ch:lln` | międzytomowy (xr-hyper) | P1-08: `ch:lln` | Prawa wielkich liczb |
| 185 | `P4-23:3` | `I-ch:clt` | międzytomowy (xr-hyper) | P1-09: `ch:clt` | Centralne twierdzenie graniczne |
| 186 | `P4-23:3` | `III-ch:sde-properties` | międzytomowy (xr-hyper) | P3-06: `ch:sde-properties` | Własności i aproksymacje SDE |
| 187 | `P4-24:3` | `I-ch:markov` | międzytomowy (xr-hyper) | P1-12: `ch:markov` | Łańcuchy Markowa w czasie dyskretnym |
| 188 | `P4-24:3` | `II-ch:ctmc` | międzytomowy (xr-hyper) | P2-05: `ch:ctmc` | Łańcuchy Markowa w czasie ciągłym |
| 189 | `P4-30:3` | `II-ch:procesy` | międzytomowy (xr-hyper) | P2-01: `ch:procesy` | Procesy stochastyczne |
| 190 | `TOP-04:4` | `ch:algebra-homologiczna` | kolizja między skryptami | TOP-03: `ch:algebra-homologiczna` | Kompleksy łańcuchowe i homologia |
| 191 | `TOP-04:15` | `def:homotopia-lancuchowa` | kolizja między skryptami | TOP-03: `def:homotopia-lancuchowa` | Homotopia łańcuchowa |
| 192 | `TOP-04:1080` | `def:topologia-ilorazowa` | kolizja między skryptami | TOP-01: `def:topologia-ilorazowa` | Topologia ilorazowa |
| 193 | `TOP-04:1189` | `def:topologia-ilorazowa` | kolizja między skryptami | TOP-01: `def:topologia-ilorazowa` | Topologia ilorazowa |
| 194 | `TOP-04:1540` | `ch:algebra-homologiczna` | kolizja między skryptami | TOP-03: `ch:algebra-homologiczna` | Kompleksy łańcuchowe i homologia |
| 195 | `TOP-05:4` | `ch:algebra-homologiczna` | kolizja między skryptami | TOP-03: `ch:algebra-homologiczna` | Kompleksy łańcuchowe i homologia |

## Kontrola matematyczna i pochodzenie

1. **P4-17, P4-23, P4-24, P4-30, wystąpienia 183–189:** Prefiksy `I-`, `II-`, `III-` należą do przestrzeni etykiet importowanych przez `xr-hyper` w `books/pl/probability_volume_iv.tex`, gdzie istnieją warunkowe `\externaldocument[I-]`, `\externaldocument[II-]` i `\externaldocument[III-]`. Deklaracje w docelowych tomach zachowują oryginalną postać `\label{ch:...}`. Treść cytowań jest zgodna z tematyką rozdziałów: formalne warunkowanie w Bayesie, MPWL i CTG dla Monte Carlo, symulacje SDE, łańcuchy Markowa dla MCMC oraz procesy stochastyczne w pomiarach powtarzanych. To **nie są brakujące rozdziały**.
2. **TOP-04, wystąpienia 190, 191, 194, oraz TOP-05, wystąpienie 195:** Odpowiednim właścicielem `ch:algebra-homologiczna` i `def:homotopia-lancuchowa` jest **TOP-03**; odpowiadające deklaracje w `DG-06` są powtórzeniami pochodzącymi z innego skryptu. `TOP-03` definiuje homotopię łańcuchową formułą `f_n-g_n=∂^D_{n+1}h_n+h_{n-1}∂^C_n`; cytowanie w `TOP-04:15` poprawnie przeciwstawia ją homotopii topologicznej.
3. **TOP-04, wystąpienia 192, 193:** Cel `def:topologia-ilorazowa` jest w **TOP-01**. Dla surjekcji ilorazowej `q:X→X/∼` topologia na ilorazie spełnia `U` otwarty wtedy i tylko wtedy, gdy `q^{-1}(U)` jest otwarty w `X`. Zasada dotyczy zarówno sklejeń sympleksów, jak i dołączania komórek CW; źródłowe przykłady i wykorzystanie własności uniwersalnej są zgodne z definicją `TOP-01:52`. Równoległa deklaracja `DG-01:104` jest znaczeniowo zgodna, ale nie jest właściwym właścicielem dla skryptu `TOP`.

## Status i ograniczenia

- Ustalenie właściciela **nie** jest fizyczną zmianą `\ref`, `\label` czy `\eqref`. W indeksie nadal mogą występować kategorie `missing` i `ambiguous`, dopóki aplikacja nie uzyska mechanizmu rozstrzygania w kontekście tomu oraz właściciela skryptu.
- Niezależna, pełna kompilacja wszystkich czterech tomów z plikami `.aux` nadal wymaga osobnego testu; kontrola źródeł `xr-hyper` nie zastępuje weryfikacji PDF.
- Ustalony zakres **Geometrii różniczkowej: 36 rozdziałów ogółem, pierwsze 20 dodane do repozytorium**. Odsyłacze do sekcji nieobecnych w aktualnym indeksie nie mogą być automatycznie klasyfikowane jako luki pełnego dzieła bez sprawdzenia rozdziałów 21–36.
- Nie zmieniono plików kanonicznych `chapters/pl/`, nie przemianowano etykiet, nie scalano skryptów, nie modyfikowano `main`.

**Łączny postęp: 195/257 wystąpień przejrzanych, 62 pozostają.** Następna partia: 196–208.