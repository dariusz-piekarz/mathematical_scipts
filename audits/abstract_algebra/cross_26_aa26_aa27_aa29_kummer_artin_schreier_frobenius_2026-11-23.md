# AA-X26 — audyt przekrojowy AA-26 × AA-27 × AA-29: Kummer, Artin–Schreier i Frobenius nad ciałami skończonymi

**Data:** 23 listopada 2026 r. **Gałąź:** biblioteka-matematyczna-iteracja-6. **Poprzedni etap:** AA-X25 stabilny po 8/8 testach i 103/103 krokach CI. **Badane źródła:** AA-26 (blob 5bee95fdfedeaaf4fc697dce636e5d82afcd249b), AA-27 (628da680adc66f257511a260df4283db8cb9a7d7), AA-29 (9cefafacbb9b857af9ebfa90af25462680a02f07).

AA-X26 nie powtarza AA-X11 (istnienie i liczenie wielomianów nierozkładalnych nad ciałami skończonymi), AA-X22 (cykle Frobeniusa dla wielomianów całkowitych) ani AA-X24 (redukcje wielomianów cyklotomicznych). Bada **jeden interfejs**: multiplicatywną konstrukcję Kummera i addytywną konstrukcję Artina–Schreiera nad tym samym ciałem skończonym, wraz z wyznaczaniem stopnia i rozkładu ich wielomianów za pomocą Frobeniusa. Rozdziały AA-01–AA-50 pozostają w tej iteracji niezmienione.

## 1. Twierdzenie przekrojowe: dokładny stopień i typ rozkładu Kummera

**Twierdzenie.** Niech \(p\) będzie liczbą pierwszą, \(m\ge1\), \(q=p^m\), a \(n\ge2\) dodatnią liczbą całkowitą dzielącą \(q-1\). Niech \(F=\mathbb F_q\), \(a\in F^\times\), \(\alpha\in\overline F\) takie, że \(\alpha^n=a\), oraz
\[
\lambda=a^{(q-1)/n}\in F^\times,\qquad d=\operatorname{ord}_{F^\times}(\lambda).
\]
Wtedy \(d\mid n\), \([F(\alpha):F]=d\), grupa Galois \(F(\alpha)/F\) jest cykliczna rzędu \(d\), a **wszystkie** moniczne nierozkładalne czynniki \(X^n-a\in F[X]\) mają stopień \(d\) i występuje ich dokładnie \(n/d\), bez krotności. W szczególności \(X^n-a\) jest nierozkładalny nad \(F\) dokładnie wtedy, gdy \(\lambda\) ma rząd \(n\). Rząd \(d\) jest też rzędem klasy \(a(F^\times)^n\) w \(F^\times/(F^\times)^n\).

**Dowód.** Grupa \(F^\times\) ma rząd \(q-1\) i jest cykliczna na mocy AA-26. Założenie \(n\mid(q-1)\) daje \(p\nmid n\) i zawieranie \(\mu_n(F)\) wszystkich \(n\) pierwiastków z jedynki w \(F\). Niezerowy wielomian \(X^n-a\) jest zatem rozdzielczy i wszystkie jego pierwiastki są postaci \(\zeta\alpha\), \(\zeta\in\mu_n(F)\). Dla automorfizmu Frobeniusa \(\mathrm{Fr}_q:z\mapsto z^q\) otrzymujemy, ponieważ \(\alpha\ne0\),
\[
\mathrm{Fr}_q(\alpha)=\alpha^q
=\alpha\,\alpha^{q-1}
=\alpha(\alpha^n)^{(q-1)/n}
=\lambda\alpha.
\]
Element \(\lambda\in F\) jest ustalany przez \(\mathrm{Fr}_q\), stąd indukcyjnie \(\mathrm{Fr}_q^k(\alpha)=\lambda^k\alpha\), a najmniejsze dodatnie \(k\), dla którego \(\alpha^{q^k}=\alpha\), jest równe \(d=\operatorname{ord}(\lambda)\). W AA-29 wykazano, że minimalny okres Frobeniusa jest stopniem minimalnego wielomianu \(\alpha\) nad \(F\); zatem \([F(\alpha):F]=d\). Ponadto \(\lambda^n=a^{q-1}=1\), więc \(d\mid n\). Rozszerzenie jest skończone, rozdzielcze i normalne (zawiera wszystkie \(\zeta\alpha\)); jego grupa Galois jest cykliczna i generowana przez \(\mathrm{Fr}_q|_{F(\alpha)}\).

Dla każdego innego pierwiastka \(\beta=\zeta\alpha\) mamy \(\beta^{q^k}=\zeta\lambda^k\alpha=\lambda^k\beta\), gdyż \(\zeta\in F\). Zatem wszystkie \(n\) różnych pierwiastków rozkładają się na orbity Frobeniusa długości \(d\); każda orbita stanowi zbiór pierwiastków jednego monicznego nierozkładalnego czynnika. Występuje dokładnie \(n/d\) takich czynników, a każdy ma stopień \(d\).

Wreszcie odwzorowanie grup \(F^\times\to\mu_n(F)\), \(x\mapsto x^{(q-1)/n}\), jest surjektywne (sprawdzamy na generatorze cyklicznej grupy \(F^\times\) rzędu \(q-1\)), a jego jądrem jest podgrupa \(n\)-tych potęg \((F^\times)^n\). Pierwsze twierdzenie o izomorfizmie utożsamia więc klasę \(a(F^\times)^n\) z \(\lambda\), zachowując jej rząd. **Koniec dowodu.**

**Różnica między „nie jest potęgą” a nierozkładalnością.** W \(\mathbb F_{13}\), dla \(n=4\), element \(a=2\) daje \(\lambda=2^3=8\) rzędu \(4\), zatem \(X^4-2\) jest nierozkładalny. Dla \(a=4\) mamy \(\lambda=4^3=-1\) rzędu \(2\), więc \(4\) nie jest czwartą potęgą, ale \(X^4-4=(X^2-2)(X^2+2)\) ma dwa różne nierozkładalne czynniki stopnia \(2\). Zgodnie z AA-26 kryterium samo w sobie nie wymusza stopnia \(n\) przy złożonym \(n\).

## 2. Twierdzenie przekrojowe: ślad i Artin–Schreier

**Twierdzenie.** Niech \(p\) będzie liczbą pierwszą, \(m\ge1\), \(q=p^m\), \(F=\mathbb F_q\) i niech \(\operatorname{Tr}_{F/\mathbb F_p}(a)=\sum_{j=0}^{m-1}a^{p^j}\in\mathbb F_p\). Wtedy:
1. \(\wp_F(F)=\{x^p-x:x\in F\}=\ker\operatorname{Tr}_{F/\mathbb F_p}\), więc \(|\wp_F(F)|=q/p\), a iloraz addytywny \(F/\wp_F(F)\) ma wymiar \(1\) nad \(\mathbb F_p\).
2. Dla \(a\in F\) i \(\alpha^p-\alpha=a\) zachodzi
   \[
   \alpha^q=\alpha+\operatorname{Tr}_{F/\mathbb F_p}(a).
   \]
3. Jeżeli \(\operatorname{Tr}_{F/\mathbb F_p}(a)=0\), to \(X^p-X-a\) rozkłada się w \(F[X]\) na dokładnie \(p\) różnych czynników liniowych. Jeżeli ślad jest niezerowy, \(X^p-X-a\) jest **nierozkładalny stopnia \(p\)**, \(F(\alpha)=\mathbb F_{q^p}\) w ustalonym domknięciu algebraicznym, a jego grupa Galois nad \(F\) jest cykliczna rzędu \(p\).

**Dowód.** Odwzorowanie \(\wp_F(x)=x^p-x\) jest liniowe nad \(\mathbb F_p\), a jego jądro jest równe \(\mathbb F_p\) (AA-27). Zatem z twierdzenia o jądrze i obrazie \(|\wp_F(F)|=q/p\). Na mocy teleskopowego sumowania
\[
\operatorname{Tr}(\wp_F(x))
=\sum_{j=0}^{m-1}(x^{p^{j+1}}-x^{p^j})
=x^{p^m}-x=x^q-x=0,
\]
czyli \(\wp_F(F)\subseteq\ker\operatorname{Tr}\). Odwzorowanie \(\operatorname{Tr}:F\to\mathbb F_p\) jest \(\mathbb F_p\)-liniowe i **niezerowe**: gdyby znikało na wszystkich \(q\) elementach \(F\), niezerowy wielomian \(T(X)=X+X^p+\cdots+X^{p^{m-1}}\) stopnia \(p^{m-1}<q\) miałby \(q\) różnych pierwiastków, co jest niemożliwe nad ciałem. Jego obraz jest więc całym jednowymiarowym ciałem \(\mathbb F_p\), skąd \(|\ker\operatorname{Tr}|=q/p\). Równość liczności i zawieranie dają \(\wp_F(F)=\ker\operatorname{Tr}\).

Jeśli \(\alpha^p-\alpha=a\), sumowanie \(\alpha^{p^{j+1}}-\alpha^{p^j}=a^{p^j}\) dla \(j=0,\ldots,m-1\) daje \(\alpha^q-\alpha=\operatorname{Tr}(a)\). Wszystkie pierwiastki \(X^p-X-a\) są postaci \(\alpha+c\), \(c\in\mathbb F_p\), i są różne, gdyż pochodna wielomianu wynosi \(-1\). Niech \(t=\operatorname{Tr}(a)\). Ponieważ \(t\in\mathbb F_p\), iterując \(\mathrm{Fr}_q\), otrzymujemy \(\mathrm{Fr}_q^k(\alpha)=\alpha+kt\). Jeśli \(t=0\), już \(\alpha^q=\alpha\), zatem \(\alpha\in F\) i tak samo wszystkie \(\alpha+c\). Jeśli \(t\ne0\), najmniejszy dodatni okres Frobeniusa wynosi \(p\). Z twierdzenia AA-29 o stopniu i okresie Frobeniusa wynika \([F(\alpha):F]=p\), więc wielomian \(X^p-X-a\) jest minimalny i nierozkładalny. Jego wszystkie pierwiastki \(\alpha+\mathbb F_p\) należą do \(F(\alpha)\), co daje galoisowskość, a \(\mathrm{Fr}_q\) działa jako przesunięcie przez \(t\ne0\), będące generatorem addytywnej grupy \(\mathbb F_p\). Jedyność podciała domknięcia algebraicznego z \(q^p\) elementami daje \(F(\alpha)=\mathbb F_{q^p}\). **Koniec dowodu.**

**Przykład graniczny.** W \(F=\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)\) mamy \(\operatorname{Tr}_{F/\mathbb F_2}(1)=1+1^2=0\); wielomian \(X^2+X+1\), nierozkładalny nad \(\mathbb F_2\), rozkłada się na dwa czynniki liniowe nad \(F\). Natomiast \(\operatorname{Tr}(u)=u+u^2=1\), więc \(X^2+X+u\) jest nierozkładalny nad \(F\) i definiuje cykliczne rozszerzenie stopnia \(2\).

## 3. Zgodność hipotez obu konstrukcji

Kummer nad \(F_q\): \(n\mid(q-1)\), \(a\in F_q^\times\), \(\lambda=a^{(q-1)/n}\), a Frobenius działa **multiplikatywnie** według \(\alpha\mapsto\lambda\alpha\). Stopień to \(\operatorname{ord}(\lambda)\mid n\); czynniki \(X^n-a\) mają jednakowy stopień.

Artin–Schreier nad \(F_q\): charakterystyka \(p\), \(a\in F_q\), ślad \(t=\operatorname{Tr}(a)\), a Frobenius działa **addytywnie** według \(\alpha\mapsto\alpha+t\). Stopień wynosi \(1\) przy \(t=0\) i \(p\) przy \(t\ne0\); wielomian \(X^p-X-a\) rozkłada się na \(p\) czynników liniowych albo jest nierozkładalny.

Nie można zamienić warunków obu teorii: \(p\nmid(q-1)\), więc nie istnieje nietrywialny \(p\)-ty pierwiastek z jedynki w \(F_q\). Ponadto każde \(a\in F_q\) jest \(p\)-tą potęgą (Frobenius jest bijekcją), zatem \(X^p-a=(X-b)^p\) dla pewnego \(b\in F_q\) i wielomian ten jest nierozdzielczy. Natomiast \(X^p-X-a\) ma zawsze pochodną \(-1\).

## 4. Trwałe testy i granice walidacji

Nowy plik tools/tests/test_abstract_algebra_cross_aa26_27_29.py zawiera **8 niezależnych funkcji testowych**. Zastosowano elementarną implementację \(\mathbb F_{p^m}\) poprzez wielomiany modulo ustalone moniczne wielomiany nierozkładalne; dane obejmują \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11},\mathbb F_{13},\mathbb F_{17},\mathbb F_4,\mathbb F_8,\mathbb F_{16},\mathbb F_9,\mathbb F_{27},\mathbb F_{25}\). Sprawdzane są:
- tożsamości potęgowania, rzędów i automorfizmu Frobeniusa w każdym modelu;
- dokładna równość obrazu Artina–Schreiera i jądra śladu, wraz z liczbą pierwiastków każdego równania;
- **niezależne od faktoryzacji** stopnie NWD \(\deg\gcd(f,X^{q^k}-X)\) dla wielomianów Artina–Schreiera i Kummera w wielu charakterystykach;
- równoważność n-tych potęg i jądra homomorfizmu klas Kummera oraz jednowymiarowość ilorazu addytywnego;
- jawne przykłady \(\mathbb F_{13}\) (stopnie 4 i 2 dla \(n=4\)), \(\mathbb F_4\), \(\mathbb F_9\) i nieodwracalność pochodnej dla \(X^p-a\);
- **niezależna faktoryzacja SymPy** dla ciał o pierwszej liczbie elementów, porównana z przewidywaniami własnego algorytmu przez NWD;
- 50 plików źródłowych, unikatowość globalnych etykiet oraz **33 etykiety i 16 odsyłaczy** z kontrolowanej trójki AA-26/AA-27/AA-29.

Nie zakładamy, że testy przykładów dowodzą ogólnych twierdzeń; argumenty ogólne zostały zapisane osobno w punktach 1–3. Testy nie stanowią formalizacji Lean. Nowy moduł dodano do wyzwalacza i kroku Run AA-X26 Kummer Artin-Schreier finite-field bridge checks w .github/workflows/abstract-algebra-chapter.yml. Commit workflow **47dbe4e023f9c82daa1238ba1abba3e2f62d1d7e**.

**Stan przy sporządzeniu raportu: W STABILIZACJI.** Do zamknięcia wymagane są 8/8 testów jako ok w rzeczywistym logu, ukończony zielony workflow, kompilacja AA-01–AA-50 i kontrola PDF oraz wszystkich odsyłaczy. Osobny wizualny przegląd wszystkich stron PDF nie jest wykonany. Nie zmieniono zatwierdzonych rozdziałów. Proponowane jako **opcjonalne rozszerzenie**, wymagające osobnej zgody: krótka tabela zestawiająca oba mechanizmy Frobeniusa w AA-27 lub AA-29; nie jest to poprawka obowiązkowa.
