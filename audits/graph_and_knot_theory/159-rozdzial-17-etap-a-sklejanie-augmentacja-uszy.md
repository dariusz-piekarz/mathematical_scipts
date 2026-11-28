# Audyt 159 — drukowany rozdział 17, etap A (kontynuacja)

Data: 2026-11-24. Plan: 118-plan-cykl-dwuetapowy.md. Poprzedni raport: 158.
Źródło: `chapters/pl/graph_and_knot_theory/10-kryteria-planarnosci-podzialy-krawedzi-i-kolorowanie.tex`.
Commit źródłowy: a167d620743db38d0334f6e96a441a96e4add813.
Blob: 14a33f8e3d74e752fd2d51129cef7de296a02c4b.
Commit regresji: 8f050a2e056372186cb24c59088f456487387f11.

## Zmiany
- Sklejanie przy jednym wierzchołku: konstrukcja przez dwa dyski styczne, z uzasadnieniem umieszczenia wspólnego wierzchołka na brzegu.
- Uzupełnianie grafu zewnętrznie planarnego: wybór przejścia między składowymi G-v w cyklicznym obchodzie, brak istniejącej krawędzi ab, zachowanie zewnętrznej ściany oraz ściśle malejący potencjał sumy liczby składowych po usunięciu wierzchołków minus jeden.
- Dowód istnienia wierzchołka stopnia co najwyżej dwa: jawne wyliczenie wierzchołków i krawędzi grafu pomocniczego oraz uzasadnienie braku dodatkowej przekątnej przy uchu.
- Nie dodawano nowych twierdzeń; 22 etykiety zachowane. Sprawdzone parowanie 57 środowisk LaTeX. Ponowny odczyt źródła z gałęzi potwierdził cztery poprawki.

## Regresja
GKT-17-OUTER-01 — test_gkt17_outerplanar.py; trwały test kombinatoryczny.
Uruchomiono lokalnie równoważny kod testu Python: PASS graphs=3288, triangulations=22, potential_drops=2650. Zakres: wszystkie nieprzecinające się podzbiory krawędzi wielokąta dla n=3..6; kontrola ograniczenia liczby krawędzi, małego stopnia, co najmniej dwóch uszu triangulacji i monotoniczności potencjału przy dołączaniu brakujących boków. Nie jest to formalizacja Lean ani dowód topologicznej konstrukcji.

## Bramka stabilizacji
CI: dla commitu źródłowego brak zwróconych statusów i przebiegów w dostępnych zapytaniach; nie potwierdzono sukcesu. PDF: lokalne pdflatex jest dostępne, lecz git ls-remote nie rozwiązuje hosta github.com; pełna kompilacja i oględziny PDF nie zostały wykonane. Etap A pozostaje OTWARTY.
Punkt wznowienia: potwierdzić CI i rzeczywisty PDF, sprawdzić pozostałe dowody i rysunek pięciokolorowalności; następnie zamknąć A wyłącznie po pełnej stabilizacji i wykonać niezależne B tego samego rozdziału.
