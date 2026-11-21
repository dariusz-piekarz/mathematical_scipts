# Algebra liniowa — rozdział 20, audyt III (matematyczny)

**Data:** 21 listopada 2026  
**Źródło:** \`chapters/pl/linear_algebra/20-dzielniki-elementarne-i-bloki-pierwotne.tex\`.  
**Po korekcie audytu II:** wzór na wielomian minimalny w przykładzie \`diag(1,1,2)\` jest zgodny z czynnikiem \`pq\`.

## Kontrola niezależna po zmianie

1. Konstrukcja i jednoznaczność rozkładu monicznych wielomianów na nierozkładalne wynika z indukcji i lematu Euklidesa w \`K[t]\`; wykorzystanie Bézouta jest poprawne nad każdym ciałem.
2. W CRT \`[g] -> ([g] mod f_i)\` jest poprawnym homomorfizmem modułów; jądro równe zeru wymaga parowej względnej pierwszości, a surjektywność wynika z \`e_i=u_i \prod_{j≠i}f_j\`, które dają właściwe kongruencje. Konstrukcja działa także dla jednego czynnika.
3. Dla czynników Frobeniusa \`f_1|...|f_r\` wykładniki \`v_p(f_i)\` są niemalejące. CRT rozkłada każdy moduł cykliczny, a bazy w jego składnikach odpowiadają blokom \`C(p^a)\`. Przy alternatywnym rozkładzie wyrównanie wykładników zerami z lewej tworzy nowy łańcuch \`g_1|...|g_r\`. Jest on wyznaczony przez moduł, zatem \`g_i=f_i\`, co kończy dowód jednoznaczności.
4. Wzory na \`n,χ_T,m_T\` wynikają z wymiaru składnika, charakterystycznego wielomianu macierzy towarzyszącej i NWW anihilatorów. Przypadek zerowej przestrzeni nie generuje bloków.
5. Filtrację \`D_{p,k}\` sprawdzono osobno dla \`k=0\`, \`0<k<a\` i \`k≥a\`; na innych składnikach mnożenie przez \`p^k\` jest odwracalne z Bézouta. Różnice \`D_{p,k}-D_{p,k-1}\` liczą dokładnie bloki co najmniej długości \`k\`; drugie różnice bloki długości dokładnie \`k\`.
6. Zmiana bazy \`1,t,...,t^{a-1}\` na \`u^{a-1},...,1\`, gdzie \`u=t-λ\`, prowadzi do jedynek na *nadprzekątnej* bloku Jordana, bez dzielenia przez silnie i bez ograniczenia charakterystyki.
7. Wszystkie pięć przykładów zweryfikowano ponownie: nilpotentne \`t,t³\`, diagonalna \`p,p,q\` i \`f_1=p,f_2=pq\`, rzeczywiste \`q,q²\`, ciało \`F2\` i przykład \`J_3⊕J_3\` vs \`J_3⊕J_2⊕J_1\` o tych samych \`χ,m\` lecz różnych jądrach. Poprawione zdanie o \`p²,q\` używa prawidłowych kryteriów podzielności i NWW.

## Wniosek

**Audyt III czysty matematycznie** po ostatniej korekcie audytu II. Nie dodano ani nie zmieniono twierdzeń; pierwszy kolejny czysty przebieg. Kontrola CI dla tej wersji: [44943090831](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44943090831) — **SUCCESS**.
