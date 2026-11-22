# Logika matematyczna i teoria mnogości — rozdział 27, audyt II

**Data:** 22 listopada 2026 r.  
**Plik:** \`chapters/pl/logic_and_set_theory/27-liczby-kardynalne-i-arytmetyka-mocy.tex\`  
**Cel:** pełna kontrola istniejącej treści, bez nowych twierdzeń.

## Korekty dowodowe

1. **Wzór parowania Cantora:** wcześniejsza argumentacja jedynie deklarowała, że bloki liczb zaczynające się od \`s(s+1)/2\` są rozłączne i pokrywają \`ω\`. Dodano indukcyjny dowód całkowitości liczb trójkątnych \`t_s=s(s+1)/2\`, zależność \`t_{s+1}=t_s+s+1\` oraz ich nieograniczoność. Prawidłowe pokrycie \`ω\` i jednoznaczność odwrotności parowania wynikają teraz z równości kolejnych końców przedziałów.
2. **Podzbiór \`ω\` jest przeliczalny:** wcześniejszy argument używał twierdzenia jako oczywistego. Wyprowadzono enumerację nieskończonego podzbioru \`D⊆ω\` przez kolejne najmniejsze niewypisane elementy, z argumentem dowodzącym surjektywności.
3. **Przeliczalność \`Q\` i moc kontinuum:** nie poprzestano na stwierdzeniu, że \`Q\` „można zakodować”. Skonstruowano iniekcję \`γ:Z→ω\`, użyto jednoznacznego zredukowanego ułamka \`a/b\` z \`b>0\` i parowania Cantora w \`j(a/b)=π(γ(a),b-1)\`. Następnie jawnie wskazano iniekcję zbiorów potęgowych \`S↦j[S]\` i zakończono dowód przez twierdzenie Cantora–Bernsteina.
4. **Wniosek o antysymetrii:** dopisano krótki, lecz jawny dowód wyjaśniający, że dwie nierówności mocy oznaczają dwie iniekcje, na które stosuje się twierdzenie Cantora–Bernsteina.

## Kontrola i testy

Zweryfikowano poprawność przypadków \`A=∅\`, \`B=∅\` w działaniach na mocach i potęgowaniu; konstrukcje funkcji charakterystycznych i diagonalizację; obie jawne funkcje przedziałowe oraz ich odwrotności. Bez nowych definicji, twierdzeń ani przykładów.

- Nowy inwentarz: 4 definicje, 11 twierdzeń, 2 wnioski, 5 przykładów, 6 uwag, 13 dowodów, 1 rysunek.
- 24 etykiety; 14 odsyłaczy; jeden jawny future reference \`ch:ordinals\`.
- Rozszerzone testy arytmetyczne i konstrukcyjne: **PASS**.
- GitHub Actions [45006332785](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45006332785): **SUCCESS**.

**Werdykt:** audyt II usunął luki w uzasadnieniach enumeracji i parowania, dalej audyt III.
