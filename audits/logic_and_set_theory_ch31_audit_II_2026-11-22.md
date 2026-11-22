# Logika matematyczna i teoria mnogości — rozdział 31, audyt II

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/31-uniwersum-konstruowalne-i-modele-wewnetrzne.tex`.

## Rozwinięcie dowodu wewnętrznej poprawności ZF

W Twierdzeniu `thm:l-model-zf` występowały dwa matematycznie ważne skróty. Zamiast jedynie stwierdzać `L_α∩Ord=α`, rozwinięto pełną indukcję po ordynałach. Predykat bycia ordynałem ma w ZF równoważne sformułowanie `x` jest przechodni i każdy element `x` jest przechodni. Jest to warunek z kwantyfikatorami ograniczonymi, a więc **absolutny dla zbiorów przechodnich**. Dzięki temu `α` jest definiowalnym podzbiorem `L_α` i należy do `L_{α+1}`; z drugiej strony każdy ordynał `γ∈L_{α+1}` spełnia `γ⊆L_α`, stąd `γ⊆α`, zatem nie pojawia się za wcześnie. Na etapach granicznych wniosek wynika z monotoniczności poziomów.

Drugi skrót `L_n=V_n` dla każdego skończonego `n` rozpisano indukcyjnie. Ponieważ `L_n=V_n` jest skończony, każdy jego podzbiór jest definiowalny nad `L_n` przy pomocy skończonej alternatywy równości do parametrów z podzbioru; pustemu zbiorowi odpowiada formuła `x≠x`. Dlatego `Def(L_n)=P(L_n)=V_{n+1}`, z uwzględnieniem konwencji `Def(∅)={∅}` przy `n=0`. Uzyskano `L_ω=V_ω`, co uzasadnia wewnętrzny aksjomat nieskończoności.

## Pozostałe kontrole

Sprawdzono bez dodatkowych zmian: relatywizację formuł w definicji `Def(M)`, tranzytywność, dobry porządek elementów `L`, oddzielność wewnętrznego zbioru potęgowego od `P(a)` w metateorii, zastępowanie zewnętrzne i wewnętrzne, dziedziczenie ufundowania, oraz poprawne rozdzielenie założeń ZF/ZFC przy GCH. Odsyłacz do `thm:delta0-absolute` dodano w dowodzie, aby wzór nie pozostał bez uzasadnienia.

**Stan:** struktura bez zmian, 68 etykiet, 87 odsyłaczy. Tekst wymaga kolejnego audytu.
