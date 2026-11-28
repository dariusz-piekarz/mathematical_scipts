# Logika matematyczna i teoria mnogości — rozdział 27, audyt III

**Data:** 22 listopada 2026 r.  
**Plik:** \`chapters/pl/logic_and_set_theory/27-liczby-kardynalne-i-arytmetyka-mocy.tex\`

## Ponowny audyt matematyczny

1. **Niezależność działań na mocach od reprezentantów.** Pierwotna definicja tylko zapewniała słownie, że zastąpienie zbiorów przez równoliczne nie zmienia sum, iloczynów i potęg mocy. Dopisano trzy konkretne bijekcje: zamianę znaczników sumy, odwzorowanie produktu przez parę bijekcji oraz korespondencję funkcji \`h ↦ β∘h∘α⁻¹\` i jej odwrotność \`k ↦ β⁻¹∘k∘α\`.
2. **Istnienie \`B^A\` w ZF.** Jawnie wskazano zbiór ograniczający \`P(A×B)\` oraz separację formułą „wykres funkcji z \`A\` do \`B\`”, bez postulatu wyboru.
3. **Narożny przypadek \`s=0\` w parowaniu.** Zapis trójkątnych liczb zastąpiono skończoną sumą po elementach naturalnej liczby von Neumanna \`s\`: \`t_s=Σ_{k∈s}(k+1)\`. Uniknięto nieokreślonej operacji \`s-1\` w \`ω\` przy \`s=0\`.
4. **Dowód, że każdy podzbiór \`ω\` jest przeliczalny.** Uzasadniono istnienie kolejnych minimów przez wcześniej dowiedziony dobry porządek \`ω\` (\`thm:zf-wellordered-omega\`). Rekursję zrealizowano na zbiorze stanów \`P(D)\`, z uzupełnieniem reguły do funkcji całkowitej w hipotetycznym stanie wyczerpanym. Indukcja z nieskończoności \`D\` gwarantuje, że taki stan na rozważanej orbicie nie występuje. Przywołano \`thm:zf-omega-recursion\`, zamiast pozostawiać twierdzenie bez wskazania podstawy.
5. **Weryfikacja granic AC.** W twierdzeniu Cantora–Bernsteina, konstrukcji parowania Cantora, enumeracji podzbiorów \`ω\` i kodowaniu \`Q\` nie użyto nieskończonego wyboru. Wartości wybierane w rekurencji są jednoznaczne, co dopuszcza ZF.

## Zakres i testy

Bez nowych definicji, twierdzeń i przykładów. Inwentarz: **4 definicje, 11 twierdzeń, 2 wnioski, 5 przykładów, 6 uwag, 13 dowodów i 1 rysunek**. **24 etykiety, 16 odsyłaczy**, z jedynym oznaczonym odesłaniem przyszłym \`ch:ordinals\`.

Dodano testy dotyczące jawnej korespondencji zbiorów funkcji, konstrukcji minimum oraz rekurencji na \`P(D)\`; rozbudowana regresja rozdziału 27: **PASS**. GitHub Actions [45006494130](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45006494130): **SUCCESS** dla tego wariantu źródłowego.

**Werdykt:** usunięto kolejne luki w uzasadnieniach; potrzebny audyt IV i niezależny czysty audyt stabilizacyjny.
