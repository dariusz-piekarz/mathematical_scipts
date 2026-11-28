# IT-07 — całka McShane'a: kryteria regresji

| ID | Etykieta / zakres | Kryterium | Metoda |
|---|---|---|---|
| IT-07-001 | it:def:mcshane, it:thm:mcshane-basic | Wolne znaczniki, Cousin, kryterium Cauchy'ego i jednoznaczność, liniowość, porządek | semantyczna |
| IT-07-002 | Inkluzja Riemann => McShane | Lokalne oscylacje, sumowanie długości przy powtarzanym znaczniku brzegowym, dowolne wolne znaczniki | semantyczna + Python |
| IT-07-003 | it:thm:mcshane-absolute | Wspólne zagęszczenie, obydwa odziedziczone znaczniki dopuszczalne nawet poza przecięciem, wybór maksimum i minimum | semantyczna + Python |
| IT-07-004 | Inkluzje właściwe | Dirichlet, x^(-1/2), pochodna HK bez całkowalności bezwzględnej | semantyczna + Python |
| IT-07-005 | tw:mcshane-indykator, wn:mcshane-proste | Regularność miary, otwarte pokrycie i zwarty rdzeń, komórki pokrywają przedział | semantyczna |
| IT-07-006 | it:cor:mcshane-lattice | Tożsamości części dodatniej i ujemnej oraz max/min | semantyczna |
| IT-07-007 | it:thm:mcshane-equiintegrability, it:cor:mcshane-uniform | Wspólne cechowanie, skończone sumy, zupełność R, bez założenia ograniczoności funkcji | semantyczna |
| IT-07-008 | it:cor:mcshane-lebesgue-consequences | Bezpośrednia lokalność przez Cauchy'ego; ograniczenie cechowania odległością od c i rozcięcie komórki | semantyczna + Python |
| IT-07-009 | it:cor:mcshane-lebesgue-consequences | Wspólny zbiór wyjątkowy, mierzalność granicy, DCT i MCT dla f_n-f_1 | semantyczna |
| IT-07-010 | it:thm:mcshane-lebesgue (IT-11) | Brak koła: krok 1 przez regularność i bezwzględną ciągłość całki Lebesgue'a; krok 2 przez niezależny dowód HK-mierzalności, bezwzględną całkowalność McShane'a, monotoniczność i MCT | semantyczna |

Audyt: commit c6b31f85281d0f644dbd9176494a50b20a4e373f (blob 050e1b309d4e106a5145a1794de1f4d86c990bce). Zachowano 8/8 etykiet i dodano jedną. Środowiska sparowane. Rozpisano definicję, kryterium Cauchy'ego, liniowość, oszacowania inkluzji Riemanna, przykład funkcji nieograniczonej, bezpośrednią lokalność i addytywność oraz mierzalność granicy. Dowód bezwzględnej całkowalności jest niezależny od reprezentacji Lebesgue'a; sprawdzono rzeczywisty dowód IT-11 oraz jego zależności, bez wykrytego koła logicznego. Dodano pięć testów (commit ac8149883c89afd4cf802289b4eb4b9a677105a2). Są to skończone świadectwa algebraiczne, nie dowody ogólne. CI po zmianach jeszcze niepotwierdzone; kontrola wizualna PDF i Lean niewykonane. Następny krok: audyt kontrolny po zmianach.
