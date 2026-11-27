# L1.5 — hybrydowa autoformalizacja LaTeX → Lean

Decyzja użytkownika 24.11.2026: własny silnik reguł i parser matematyczny jako podstawa, opcjonalny lokalny model AI oraz możliwość podłączenia zewnętrznych modeli (np. OpenAI/Codex, Anthropic/Claude). Tryb lokalny działa bez kluczy, sieci i opłat API. Zewnętrzne integracje są domyślnie wyłączone; nie ma automatycznego fallbacku do chmury. Decyzja nie jest zgodą na faktyczne płatne wywołanie, przesłanie treści ani wykonanie niezaufanego kodu.

**Aktualny warunek użytkownika, 27.11.2026:** integracja LLM ma być bez
opłat za inferencję zewnętrzną i bez abonamentu wymaganego przez Atlas.
Wyłącznie lokalne wagi na własnym sprzęcie; brak przejścia do płatnej
usługi, zdalnego domyślnego dostawcy i modeli chmurowych. Nie utożsamiać
licencji open source z darmowym dostępem do modelu. Koszt prądu i użycie
własnego sprzętu pozostają lokalne. Ten warunek zastępuje wcześniejszy
opcjonalny zakres płatnych adapterów, dopóki użytkownik go nie zmieni.

## Kolejność po stabilizacji L1.5.2

| Podetap | Zakres i kryterium odbioru |
|---|---|
| L1.5.3 | Kontrakt lokalnego silnika, typowany AST, mała wersjonowana gramatyka, limity rozmiaru/głębokości; unsupported zamiast zgadywania, brak sieci. |
| L1.5.4 | Parser i reguły translacji rachunku zdań, kwantyfikatorów, równości, porównań, prostych działań z jawnymi typami. Kontrola zakresów zmiennych, priorytetów i założeń. |
| L1.5.5 | Wersjonowany słownik pojęć, odpowiedniki Mathlib, kontekst indeksu i zatwierdzonych mapowań. Ślad reguł, testy rzeczywistych obiektów LST/LA. |
| L1.5.6 | Izolowane kandydaty draft, generacja tezy i próba dowodu taktykami Lean. Odrębny zabezpieczony runner niezaufanych kandydatów, jawna zgoda, limity czasu/RAM/procesów/wyjścia/sieci; bez sorry/admit i nowych aksjomatów. |
| L1.5.7 | Ograniczona pętla napraw z diagnostyką Lean, bez cichej zmiany tezy, założeń i AST; limit prób. |
| L1.5.8 | Wspólny interfejs generatorów i lokalny model bez opłat API. Pierwszy warunkowy pilot: LeanFlow + Lemex + lokalny serwer Responses API. Jawna instalacja, licencja, wersja/hash, zasoby, offline; brak modelu nie blokuje reguł. |
| L1.5.9 | Ocena AutoformBot jako alternatywnego procesu wyłącznie po potwierdzeniu lokalnego runtime bez opłat. Adaptery płatne i chmurowe wyłączone z bieżącego zakresu na polecenie użytkownika. |
| L1.5.10 | Integracja przepływu, Chromium, pomiary coverage/unsupported/compiled, niezależny audyt matematyczny próby. |

Każdy podetap: osobne regresje, 2+1 na niezmiennym SHA, sceptyczny audyt i niezależny odbiór zgodnie z głównym planem. Nie zmieniać harmonogramu ani równoległych audytów. L1.5.2 ma własną bieżącą walidację; niniejszy plan nie zmienia kandydata.

## Kontrakt architektury

- Pakiet indeksu → tokenizacja → typowany AST ze śladem źródła → reguły generacji. Nierozpoznany fragment blokuje kompletną tezę; nie wolno pomijać założeń. Pierwszy pilot: proste twierdzenia Prop, jawnie typowane formuły. Transkrypcja tezy i dowodu są odrębne.
- Wspólny interfejs generatorów rules / local_model / external_provider; wybór użytkownika, jawne możliwości, wersja generatora, SHA źródła i diagnostyka. Wynik zawsze niezaufany draft/needs_review; status kompilacji osobno not_run/blocked/failed/compiled. certificate=false. Nie modyfikować kanonicznych TeX/Lean ani manifestu automatycznie. Kompilacja nie potwierdza zgodności znaczenia.
- Nie przekazywać kandydatów istniejącemu runnerowi zarejestrowanych plików. Osobna izolacja, zakaz arbitralnego I/O i metaprogramowania; filtry tekstowe nie są sandboxem. Jeśli odpowiednia izolacja nie jest dostępna, kompilacja blocked. Lokalny model także ograniczony zasobowo i bez sieci. Licencje i wersje komponentów, wag i danych sprawdzać przed integracją; brak automatycznej instalacji.
- Nie obiecywać uniwersalnej transkrypcji dowolnego języka naturalnego.

## Adaptery zewnętrzne

Poniższe historyczne wymagania nie są zadaniem wdrożenia płatnych usług.
Warunek z 27.11.2026 dopuszcza obecnie tylko lokalną inferencję. W razie
braku lokalnego modelu raportować niedostępność i zachować tryb regułowy.

- Panel ustawień: wybór generatora i modelu, konfiguracja/odłączenie dostawcy. Codex i Claude to rodziny planowanych integracji; przed implementacją sprawdzić aktualne oficjalne interfejsy, licencje, warunki, dostępność i ceny. Nie zakładać uprawnień API z abonamentu. CLI tylko w ograniczonym trybie bez agentowego dostępu do repozytorium, terminala i zapisu.
- Klucze tylko w backendzie: systemowy magazyn sekretów lub zmienne środowiskowe; bez kluczy w HTML, localStorage, repozytorium, logach i artefaktach CI. Jawna rotacja i odłączenie, maskowanie sekretów. Kontrolowane adresy dostawców, brak arbitralnych URL z przeglądarki i niezatwierdzonych przekierowań.
- Przed wywołaniem: pokaż dostawcę/model, dokładny zakres źródła i kontekstu, transfer poza komputer, warunki prywatności/licencji, szacowany koszt i maksymalny budżet. Jednorazowa zgoda związana z SHA, zakresem, dostawcą, modelem i limitem. Brak zgody lub nieznane warunki = blocked. Nie wysyłać całego repozytorium, sekretów, innych materiałów ani historii rozmów.
- Budżet per żądanie i sesja, limity wejścia/wyjścia, czasu, prób i równoległości. Rezerwacja przed wywołaniem i rozliczenie udokumentowanego zużycia; ceny z datą i walutą. Szacunek nie jest gwarantowaną kwotą; brak wiarygodnej granicy kosztu blokuje płatne żądanie. Bez automatycznych odpłatnych ponowień przy niejednoznacznym błędzie. Lokalny tryb ma zerowy koszt zewnętrzny.
- Wynik dostawcy to niezaufany kandydat, nie polecenie do wykonania; ta sama ścieżka izolacji i audytu. Żadnych narzędzi agentowych. Ręczny powrót do reguł lokalnych możliwy zawsze.
- Testy atrap transportu: brak sieci w trybie lokalnym, brak klucza/zgody, zmiana źródła/modelu, przekroczenie budżetu, maskowanie sekretów, przekierowania, timeout, niejednoznaczne rozliczenie i błędna odpowiedź. CI nie wysyła płatnych żądań. Rzeczywisty test dostawcy wymaga osobnej zgody i limitu. Nie przedstawiać atrap jako rzeczywistej integracji.

## Stan

27.11.2026: sprawdzono dokumentację i przypięty kod LeanFlow/Lemex.
Konfiguracja lokalnego dostawcy bez klucza jest technicznie możliwa,
ale pełny przebieg lokalnego modelu i narzędzi nie został jeszcze wykonany.
Domyślna konfiguracja Lemex używa zdalnego EPFL RCP; nie używać jej w tym
pilotażu. Wymagane bezstanowe HTTP Responses API, wyłączone WebSockety,
zewnętrzne wyszukiwanie i chmura. Ollama dokumentuje odpowiedni protokół;
zgodność narzędzi oraz jakość formalizacji wymagają rzeczywistego testu.
Przygotowano lokalny pakiet czterech twierdzeń z LST-01/LST-02 przez
istniejące `lean_transcription.prepare`, po sprawdzeniu indeksu względem
źródeł. To dane wejściowe, nie wygenerowane ani udowodnione formalizacje.
Szczegóły i źródła w przeglądzie poniżej. Kolejność ukończenia runnera
L1.5.6 pozostaje obowiązująca; przygotowanie pilota nie włącza jego wykonania.

Aktualizacja kierunku, 26.11.2026: użytkownik wskazał wykorzystanie gotowych
rozwiązań z GitHuba zamiast budowy własnego modelu. Przed wdrożeniem
generatora modelowego ocenić AutoformBot i LeanFlow oraz gotowe wagi
formalizatora; zakres, źródła i kryteria pilotażu zapisano w
[przeglądzie gotowych narzędzi](LATEX_TO_LEAN_EXISTING_TOOLS_REVIEW_2026-11-26.md).
Obecny własny kod to parser, reguły i kontrola pochodzenia, nie trenowany
model. Kolejność odbioru L1.5.6 pozostaje obowiązująca.

L1.5.2: kandydat ac4c30c11378c6a74bbeaf4f57ef5fb09bbc65e3, workflow 45351518032. Ten dokument jest zatwierdzoną decyzją projektową, nie implementacją adapterów. 
