# Logika matematyczna i teoria mnogości — rozdział 28, audyt IV

**Data:** 22 listopada 2026 r.  
**Plik:** `chapters/pl/logic_and_set_theory/28-liczby-porzadkowe-i-rekurencja-pozaskonczona.tex`  
**Zakres:** matematyczny i redakcyjny audyt już istniejącego materiału.

## Znaleziona nieścisłość i poprawka

W przykładzie konstrukcji hierarchii von Neumanna ustalono rodzinę `(V_β)_{β<α}`, ale równanie `V_{β+1}=P(V_β)` zapisano bez warunku `β+1<α`. Dla największego indeksu odcinka następnik mógł więc wykraczać poza określoną dziedzinę funkcji. Skorygowano indeksowanie: osobno `V_0=∅`, `V_{δ+1}=P(V_δ)` dla `δ+1<α` oraz `V_λ=⋃_{β<λ}V_β` dla niezerowych granicznych `λ<α`. Przy `α≥4` wszystkie cztery wskazane poziomy są zdefiniowane. Dodano regresję w `tools/tests/test_logic_and_set_theory_ch28.py`.

## Niezależna kontrola innych partii

Przeanalizowano ponownie:
1. definicję ordynału jako zbioru przechodniego dobrze uporządkowanego przez przynależność;
2. lemat o odcinkach początkowych, w tym dowód, że każdy element ordynału jest ordynałem;
3. trójpodział porównania ordynałów na podstawie identyczności izomorfizmów odcinków;
4. przechodniość, liniowość, dobry porządek i własność najmniejszego ograniczenia górnego sumy ordynałów;
5. rozróżnienie granicznych i następnikowych ordynałów, w szczególności przypadek pustego supremum;
6. indukcję pozaskończoną jako schemat formuł ZF, przy wymaganym zbiorze kontrprzykładów z separacji;
7. rekurencję na ustalonym ordynale, w tym jedyność przybliżeń i zastępowanie na granicznych etapach;
8. rekurencyjne definicje dodawania i mnożenia ordynałów oraz ich nieprzemienność;
9. istnienie i jednoznaczność reprezentanta kardynalnego w ZFC, ze ściśle wydzielonym miejscem użycia AC;
10. brak zbioru wszystkich ordynałów (paradoks Buralego–Fortiego).

Inwentarz bez zmian: **4 definicje, 5 przykładów, 2 lematy, 5 twierdzeń, 1 wniosek, 3 uwagi, 8 dowodów, 17 etykiet i 20 odsyłaczy**. Wszystkie odsyłacze powinny mieć już istniejące cele w rozdziałach 1–28.

## Status

Poprzedni przebieg GitHub Actions **45007737931 — SUCCESS** dla źródła przed doprecyzowaniem indeksów; nowszy przebieg dla bieżącego tekstu i nowego testu został uruchomiony. Aby uznać rozdział za stabilny, należy zakończyć kolejny audyt bez nowych zmian i sprawdzić jego aktualny PDF.

**Werdykt:** poprawiono istniejący przykład, nie dodając twierdzeń; do audytu V stabilizacyjnego.
