# Topologia ogólna — rozdział 21, audyt 04 (drugi czysty, kontrola przypadków brzegowych)

**Data:** 2026-11-22.
**Blob:** a8e0c4dbcf3c3100bf6b3c9e067b6fce0ddaa73b, niezmieniony od audytu 03.
**Wynik:** CZYSTY, **2/2**. Kryterium stabilności matematycznej osiągnięte.

## Alternatywny audyt przez przypadki brzegowe i zależności

1. X pusta: K(X) pusta, definicja Vietorisa i twierdzenia o zwartości oraz zupełności są poprawne w sensie warunków pustych; F(X) zawiera jedynie ∅, co jest zwarta i Hausdorffa.
2. X nie-Hausdorffa: definicje Vietorisa oraz Fella i ich podbazy pozostają określone, natomiast twierdzenia o oddzielaniu przyjmują dokładnie konieczne w dowodach założenia Hausdorffa. Nie ma nieuzasadnionego zastosowania domkniętości zwartych.
3. Singletony: dla dowolnego X punkt {x} jest zwarty; przy Hausdorffie można oddzielić dowolne dwie różne kompaktowe rodziny A,B przez trafienie U i zawieranie V.
4. Przypadki pustych rodzin warunków w bazie Vietorisa: warunki górne można sprowadzić do jednego V, a dolne puste do otoczenia \langle V\rangle. Nie zapomniano o n=0 wewnątrz dowodu bazy, choć sama baza indeksowana jest m≥1.
5. Cauchy'ego w K(X): w dowodzie pełnej zupełności nigdy nie uznano zbioru K za zwarty przed wykazaniem całkowitej ograniczoności. Zastosowanie d_H(A_j,K) następuje dopiero po tym kroku. Pusty zbiór zerowy nie występuje dzięki skonstruowanemu łańcuchowi.
6. W dowodzie zwartości Vietorisa dla X zwartej Hausdorffa, jeśli F (z ultrafiltru) miałby być pusty, skończone podpokrycie X prowadzi do sprzeczności. Jeśli X\V jest pusty, odpowiednie U^+ jest całą K(X), więc automatycznie należy do ultrafiltru; tekstowy dowód obejmuje to jako pusty przypadek skończonego pokrycia.
7. W dowodzie zwartości Fella, jeśli indeksy J są puste, zbiór F=X\setminus\bigcup U_i nadal przeczy hipotetycznemu pokryciu; jeśli C_j=∅ dla jakiegoś j, sam C_j^0 pokrywa całą F(X), więc sprzeczność uzyskuje się natychmiast. Ogólny argument z własności skończonych przecięć obejmuje pozostałe przypadki.
8. Topologia Fella na niepustych zwartych w R jest słabsza od Vietorisa, mimo że cała F(R) jest zwarta: ciąg {n} zbiega w Fellu do ∅, a {0,n} do {0}, podczas gdy żaden z tych efektów nie zachodzi w metryce Hausdorffa.
9. Odsyłacze zewnętrzne są dokładnie do ultrafiltrów (07), lematu otoczeń o zwartym domknięciu (14) i wprowadzenia do przestrzeni odwzorowań (18). Brak nowego powielania tamtego materiału.

## Kontrola języka, rysunku i CI

Rozdział używa „zwartość”, „zbieżność w topologii Vietorisa”,
„zbiory domknięte”, „Hausdorffa”; nie wprowadza zakazanych form
terminologicznych. W przykładzie dwa elementy B są zapisane jako
jednoznaczne ułamki 1/5 i 17/10. Wyskalowany rysunek nie koliduje
z napisami ani opisem osi.

31 różnych etykiet, 9 istniejących odsyłaczy, prawidłowa kolejność
\label i \ref, zrównoważone środowiska. Zielony CI:
[45042413561](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45042413561),
pełna książka, samodzielny PDF i logi. Siedem stron A4 obejrzanych
wizualnie w oryginalnym artefakcie ID 14761939222.

**Rozdział 21: STABILNY MATEMATYCZNIE (2/2)**. Należy przeprowadzić
jeden dodatkowy audyt 05 bez zmian w źródle, a następnie uaktualnić
status rozdziału w książce i ponownie zweryfikować integrację.
