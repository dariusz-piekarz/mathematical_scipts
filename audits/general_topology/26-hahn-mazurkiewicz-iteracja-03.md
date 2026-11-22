# Topologia ogólna — rozdział 26, audyt 03 (korekcyjny skład)

**Data:** 2026-11-22.
**Źródło po korekcie:** `9f1ea17248b4df5805c025ba7bb47219c1dd4562`.
**Status:** 0/2 — audyt 02 był czysty na starszym blobie,
ale wskutek poprawy składu rozpoczęto liczenie audytów od nowa.

## Wynik kontroli pierwszego rzeczywistego PDF

W zakończonym sukcesem
[CI 45061818656](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45061818656)
zbudowano pełną książkę (191 stron)
i osobny rozdział 26 (7 stron).
Pobrano artefakt `general-topology-ch01-ch26`
ID 14769359991 i zweryfikowano logi:
brak Overfull, Underfull, Missing character
i LaTeX Warning.

Wyrenderowano i obejrzano **wszystkie siedem stron**
samodzielnego rozdziału.
Rysunek schematycznej pętli na stronie 4
jest czytelny, bez nakładających się opisów,
ale ostatnia strona zawierała jedynie końcowe
zdania przykładu o przestrzeni Sierpińskiego
i podsumowanie. To niepotrzebna, prawie pusta
strona wydawnicza.

**Korekta:** skrócono wyłącznie sekcję 26.6
(wniosek, przykłady, uwagę i podsumowanie).
Zachowano wszystkie twierdzenia,
dowody i ich hipotezy oraz etykiety LaTeX.
Przykłady nadal obejmują solenoid
bez lokalnej spójności, dwupunktową przestrzeń
dyskretną, zbiór Cantora, grafy i sześciany
oraz przestrzeń Sierpińskiego z jawną
ciągłą surjekcją z [0,1].
Wcześniejsza konieczna poprawka
pojęciowa o spójnych podzbiorach Cantora
pozostała zachowana.

Ponieważ źródło zmieniło się względem
bloba audytu 02, nie przenosimy
jego czystego statusu na nowy blob.
Po nowym renderowaniu PDF wykonamy
dwa czyste audyty matematyczno-redakcyjne
na niezmienionym źródle i jeden
dodatkowy audyt potwierdzający.

**Wynik:** korekcyjny — 0/2.
