# Audyt 222 — drukowany rozdział 24, niezależna kontrola B

Data: 2026-11-25. Kontynuacja 221, bez rozszerzania zakresu.
Źródło: chapters/pl/graph_and_knot_theory/17-grafy-cayleya-dzialania-na-drzewach-i-teoria-bassa-serre-a.tex.
Odczytana gałąź biblioteka-matematyczna-iteracja-6, blob 6aaca3436174ab0b28de4f43218d2c2f8dd0a830, zgodny z wersją źródłową 6c9722cee627b211ac5b4a5aa35df48560ce1a73 z audytu 221.

## Niezależna kontrola matematyczna
- Graf Cayleya: dla symetrycznego zbioru generatorów bez jedności różni generatorzy dają różnych sąsiadów; dla inwolucji krawędź liczona jednokrotnie. W grupie wolnej cykl prosty daje niepuste słowo zredukowane reprezentujące jedność.
- Działanie: bez inwersji stabilizator krawędzi jest przecięciem stabilizatorów końców; swoboda na wierzchołkach daje injektywność mapy gwiazd. Surjektywność wynika z przeniesienia reprezentanta półkrawędzi. Otwarte gwiazdy są równomiernie nakryte także dla nieskończonej walencji w słabej topologii CW.
- Prosta spójność drzewa: zwarty obraz pętli mieści się w skończonym podkompleksie; dołączenie dróg do korzenia daje skończone poddrzewo. Dla nieskończonego ilorazu argument skończonych podkompleksów obejmuje także homotopie relacji. Drzewo rozpinające istnieje na mocy lematu Zorna.
- HNN: przy składaniu dróg od lewej do prawej t = [p_+ gamma^(-1) p_-^(-1)] daje t iota_-(c) t^(-1) = iota_+(c). Zmiana ścieżek bazowych przez u_-, u_+ daje t' = u_+ t u_-^(-1). Pokrycie podwójnego cylindra ma dokładnie dwie składowe przecięcia. Ciągłość homotopii kołnierza korzysta z iloczynu mapy ilorazowej z identycznością lokalnie zwartego przedziału.
- Klasy boczne: dla relacji t_e iota_-(c) t_e^(-1) = iota_+(c) koniec półkrawędzi g iota_-(G_e) to g t_e^(-1) G_t. Zmiana reprezentanta pozostawia końce niezmienione. Odwrócenie stosowane dwukrotnie daje pierwotną klasę; typy krawędzi pozostają rozróżnione. Dla pętli oba indeksy są liczone oddzielnie.
- Przykłady F2, torus, C2*C3, BS(1,2) zgodne z prezentacją i wzorem stopni. Fundamentalne twierdzenie Bassa–Serre'a oraz acykliczność ogólnego modelu pozostają wynikiem z literatury.
- Sprawdzono w źródle 07 wszystkie cztery różne cele pięciu odsyłaczy: ch:tg-topology, thm:tg-wedge, thm:tg-free-pi1, lem:tg-collapse-CW. Nie wykryto nowej istotnej usterki; źródło bez zmian. Nie proponuje się koniecznych nowych rysunków ani twierdzeń.

## Niezależna regresja GKT-24-BS12-PY-01
Wykonano w procesie Python z Fraction, nie w izolacie JS. Afiniczna para (r,k) reprezentuje x -> 2^k x+r. Wierzchołek ma klucz (r mod 2^k,k). Poniższy kod odtwarza test.

```python
from fractions import Fraction as Q
from itertools import product
from collections import deque

def p(k): return Q(2)**k
def mul(g,h):
    r,k=g; s,l=h
    return r+p(k)*s,k+l
def cos(g,m=1):
    r,k=g
    return r%(m*p(k)),k
def edge(g,sgn):
    return cos(g),cos(mul(g,(Q(0),-sgn)))
def rev(g,sgn):
    return mul(g,(Q(0),-sgn)),-sgn

samples=[(Q(i,8),k) for i in range(-16,17) for k in range(-4,5)]
translations=[(Q(i,4),k) for i in range(-4,5) for k in range(-2,3)]
counts=dict(representatives=0,reversals=0,translations=0,incidences=0)
for g,sgn in product(samples,[1,-1]):
    m=1 if sgn==1 else 2
    a,b=edge(g,sgn)
    for n in range(-5,6):
        h=mul(g,(Q(m*n),0))
        assert cos(h,m)==cos(g,m)
        assert edge(h,sgn)==(a,b)
        counts['representatives']+=1
    h,t=rev(g,sgn)
    assert edge(h,t)==(b,a)
    assert rev(h,t)==(g,sgn)
    counts['reversals']+=1
    for u in translations:
        assert edge(mul(u,g),sgn)==(cos(mul(u,a)),cos(mul(u,b)))
        counts['translations']+=1

def nbr(v):
    r,k=v
    return {cos((r,k-1)),cos((r,k+1)),cos((r+p(k),k+1))}
root=(Q(0),0); d={root:0}; q=deque([root]); edges=set()
while q:
    v=q.popleft(); ns=nbr(v)
    assert len(ns)==3
    for w in ns:
        assert v in nbr(w)
        counts['incidences']+=1
        if d[v]<9 and w not in d:
            d[w]=d[v]+1; q.append(w)
        if w in d: edges.add(frozenset([v,w]))
assert len(d)==1+3*(2**9-1)
assert len(edges)==len(d)-1
print(counts, 'vertices',len(d),'edges',len(edges),'PASS')
```

Wynik: 6534 kontroli reprezentantów, 594 odwrócenia, 26730 translacji, 4602 incydencje; 1534 wierzchołki i 1533 krawędzie. PASS. Liczniki oznaczają iteracje kontrolne, nie liczbę pojedynczych instrukcji assert. Test ograniczony do modelu afinicznego i skończonej kuli; nie dowodzi wierności reprezentacji ani twierdzenia ogólnego. Kod zapisany w raporcie, nie zintegrowany z CI, nie formalizacja Lean.

## CI, PDF, decyzja
Ponownie odczytano przez API GitHub wszystkie cztery przebiegi dla 6c9722ce: 45589293161, 45589292932, 45589292978, 45589292943 — completed/success i zgodne SHA. Raport 221 dokumentuje oględziny PDF (354 strony, 7 stron rozdziału). W tej sesji nie wykonano nowej kompilacji ani nowych oględzin PDF; git ls-remote w środowisku wykonawczym nie działa z powodu DNS. Nie przypisuje się PASS nowemu SHA całej gałęzi. Etap B pozostaje otwarty do końcowej kontroli niezależnej, potwierdzenia bramki dla aktualnego stanu i zamknięcia. Postęp 23/44.
