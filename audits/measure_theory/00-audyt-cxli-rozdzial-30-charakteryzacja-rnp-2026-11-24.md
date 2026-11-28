# Audyt CXLI (141) — charakteryzacja RNP
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.

Poprzednia iteracja: statusy regresji i PDF success, run 45374982890 (commit a94389b0d5049afdcc4eeae76c6a818195cdac87).

## Korekty
Commit c0d2d388500602b80d0b80cce45edfe4ee6e1ed6, blob 8fcd3bb7856708a01902ead0d3902a406b191aaf, 838 → 942 wiersze, zachowano 28 etykiet.
- Różniczkowanie Bochnera: funkcje przedłużone przez zero, sumowalne zbiory wyjątkowe, jawne oszacowanie limsup i wspólny zbiór pełnej miary.
- Lemat o podziałach: wartości na zerowych komórkach, dowód zbieżności sieci Cauchy'ego przez ciąg i kontrolę ogonów.
- Dzielenie miary bezatomowej: rzeczywisty porządek częściowy na klasach zbiorów, uzasadnienie ograniczenia górnego łańcucha, zastosowanie Zorna.
- RNP: rozkład atomowy z rozłącznymi reprezentantami, jawna konstrukcja gęstości i przypadek zerowej części bezatomowej.
- Kodowanie podziałów: komórki zerowe i końce przedziałów, jawna suma norm, niezależność wyboru poziomu i przedłużenie Lipschitzowskie.
- Kontrakcja średnich: oszacowanie 2 delta + M omega_phi(m_n).

## Regresje
Dodano MT30-006–008 w f27246cd912cf26d3bc7304ca2022d9ce9b2a4e0. Niezależne kontrole JS: 16 podzbiorów w modelu atomowym, 21 bloków przedziałów i 8 warunków źródłowych zaliczone. Wynik nowego CI niepotwierdzony w chwili audytu; nie uruchamiano pliku Python lokalnie. Bez formalnej certyfikacji dowodów.

## Następny krok
Niezależna kontrola twierdzenia o wariacji gęstości Bochnera, jednoznaczności RNP, lematu o całce po krzywej oraz dowodu RNP dla przestrzeni Hilberta (również nieseperowalnych). Weryfikacja najnowszego CI i PDF. Rozdział 30 pozostaje otwarty, stan 29/31.
