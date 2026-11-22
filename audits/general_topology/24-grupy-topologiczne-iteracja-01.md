# Topologia ogólna — rozdział 24: audyt 01 (korekcyjny)

**Data:** 2026-11-22.
**Źródło:** `chapters/pl/general_topology/24-grupy-topologiczne-i-przestrzenie-jednorodne.tex`.
**Aktualny blob źródła:** `4b72d373d98eab0c1cc4563b72a6bb8fa62170b6`.
**Status:** 0/2 po korektach; wymagane 2 kolejne czyste audyty
na tym samym blobie i jeden dodatkowy, zielony CI oraz inspekcja PDF.

## Kontrola zakresu i powtórzeń

- Podstawowa algebra grup jest już w `abstract_algebra/01–03`;
  w rozdziale 24 zakładamy ją i badamy nowe własności topologiczne.
- Grupy lokalnie zwarte i konstrukcja miary Haara występują
  w `measure_theory/23-miara-haara-na-grupach-lokalnie-zwartych.tex`.
  Nie powtarzamy definicji miary, konstrukcji ani jednoznaczności.
- Otoczenia jednostajne i zbieżność filtrów są w TO-12/13.
  W TO-24 wprowadzono nowe, szczególne struktury jednostajne grup.
- Definicję grupy topologicznej stosujemy z jawnym aksjomatem
  Hausdorffa, co jest zgodne z rozdziałem o mierze Haara.

## Wynik kontroli matematycznej

1. Jedno kryterium ciągłości: mapa \((x,y)\mapsto xy^{-1}\)
   jest ciągła wtedy i tylko wtedy, gdy ciągłe są
   odwracanie i mnożenie. W odwrotnym kierunku
   odwracanie otrzymujemy przez podstawienie \(x=e\),
   a mnożenie po podwójnym odwróceniu.
2. Translacje i sprzężenia są homeomorfizmami
   z jawnymi odwrotnościami; wynika jednorodność G.
3. Dla dowolnego otoczenia U elementu neutralnego
   istnieje symetryczne otwarte V z \(V^k\subseteq U\).
   Wykorzystano ciągłość mnożenia i iteracyjne
   zwężanie otoczeń.
4. Lemat \(\overline V\subseteq V^2\) dla
   symetrycznego otwartego V został sprawdzony:
   jeśli \(x\in\overline V\), to \(xV\cap V\neq\varnothing\),
   więc \(x=wv^{-1}\in V^2\).
   Daje to regularność każdej grupy Hausdorffa.
5. Ciągłość homomorfizmu wystarczy sprawdzić w e,
   gdyż otoczenia punktu x są przesunięciami otoczeń e.
6. Topologia podprzestrzeni H jest topologią grupową;
   domknięcie H jest podgrupą przez ciągłość
   operacji różnicy \(xy^{-1}\);
   dla H normalnej domknięcie jest normalne.
   Podgrupa otwarta jest domknięta jako
   dopełnienie sumy pozostałych warstw.
7. Projekcja \(q:G\to G/H\) jest otwarta,
   bo \(q^{-1}(q(U))=UH\) jest otwarte.
   Dla H domkniętej różne warstwy rozdzielono
   przez \(q(xV)\), \(q(yV)\), używając
   \(V^{-1}x^{-1}yV\cap H=\varnothing\).
   To dowodzi dokładnie równoważności
   \(G/H\) Hausdorffa \(\Leftrightarrow\) H domknięta.
8. Dla N normalnej iloraz ma ciągłe działania:
   \(q\times q\) jest otwartą surjekcją ilorazową;
   ciągłość mnożenia wynika z diagramu
   \(m_N\circ(q\times q)=q\circ m_G\),
   odwracanie z analogicznego diagramu.
9. Izomorfizm topologiczny indukowany przez
   ciągły, otwarty surjektywny homomorfizm
   wymaga jawnie otwartości: kontrprzykład
   to identyczność z dyskretnej prostej
   na prostą z topologią euklidesową.
10. Dla lokalnie zwartej G i zamkniętej H
    obraz zwartego otoczenia e pod otwartym q
    jest zwartym otoczeniem warstwy H,
    a translacje dają lokalną zwartość wszędzie.
11. Składowa spójna G^0 jest domknięta i normalna,
    bo jej produkt z odwrotnością
    oraz obrazy przez sprzężenia są spójne.
    Dla otwartej surjekcji z ciągłymi włóknami
    przeciwobraz spójnego C jest spójny;
    po zastosowaniu do q:G→G/G^0
    dostajemy całkowitą niespójność ilorazu.
12. Relacje \(E_U^L\) i \(E_U^R\) mają
    poprawne własności struktur jednostajnych,
    indukują wyjściową topologię i
    są odpowiednio lewo/prawostronnie
    niezmiennicze. Odwracanie zamienia obie
    struktury; homomorfizmy ciągłe są
    jednostajnie ciągłe dla odpowiednich par.

## Dwie zasadnicze korekty uzupełniające

**A. Birkhoff–Kakutani.** Początkowy szkic
nie zawierał pełnej metryzowalności pierwszoprzeliczalnych
grup. Dopisano twierdzenie w zgodnej terminologii
„spełnia pierwszy aksjomat przeliczalności”.
Zbudowano zstępującą symetryczną bazę U_n
z \(U_{n+1}^3\subseteq U_n\).
Funkcja dyadyczna \(\rho(g)\)
i infimum długości skończonych łańcuchów
definiują metrykę lewostronnie niezmienniczą.
Dowód zawiera indukcję dla iloczynów o małej
sumie wag; jest to kluczowe uzasadnienie
dodatniej określoności metryki i zgodności
jej topologii z topologią G.

**B. Działanie na G/H.** W początkowym
tekście wykazano otwartość q oraz
ciągłość poszczególnych translacji
w przestrzeni warstw, ale nie ciągłość
całego odwzorowania
\(\alpha:G\times G/H\to G/H\).
Dodano niezależne twierdzenie:
\(\mathrm{id}_G\times q\) jest otwartą
surjekcją ilorazową, a
\(\alpha\circ(\mathrm{id}_G\times q)=q\circ m_G\),
więc \(\alpha\) jest ciągłe.
Działanie jest przechodnie, stabilizatorem H jest H.

Dodano również konkretny przykład
\(S_3/\langle(1\,2)\rangle\), w którym
topologia ilorazu jest dyskretna,
ale algebraiczne mnożenie warstw nie
jest dobrze określone, gdyż H nie jest normalna.

## Integracja i dalsze kontrole

Tekst, samodzielny punkt wejścia,
import do książki oraz katalog obejmują
już rozdział 24. Utrzymano status:
01–23 stabilne, 24 w audycie.
Dodano `tools/tests/test_general_topology_ch24.py`
ze skończonymi modelami S3, grup cyklicznych,
orbity warstw oraz konstrukcji metryki
Birkhoffa–Kakutaniego. Rozszerzono workflow
budujący całą książkę i osobny PDF rozdziału 24.

**Ograniczenia:** testy skończone nie dowodzą
twierdzeń dla ogólnych grup topologicznych.
CI/PDF najnowszego bloba wymaga potwierdzenia;
nie oznaczono jeszcze rozdziału jako stabilny.
