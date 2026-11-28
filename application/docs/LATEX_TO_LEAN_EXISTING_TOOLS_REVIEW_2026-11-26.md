# Gotowe narzędzia LaTeX → Lean — przegląd z 26 listopada 2026

## Aktualizacja 27.11.2026 — warunek braku opłat

Użytkownik uzależnił integrację od braku opłat za inferencję. Licencje
MIT/Apache-2.0 dotyczą programu lub wag, nie finansują wywołań dostawcy.
Domyślne uruchomienie AutoformBot lub LeanFlow nie daje gwarancji darmowej
inferencji. Aktualna decyzja: lokalne wagi, zero opłat zewnętrznych,
bez wymaganego abonamentu i bez automatycznej zmiany dostawcy na chmurowego.
Pozostają zużycie sprzętu i energii; nie obiecujemy zerowego kosztu prądu.

Zweryfikowane źródła i ograniczenia:

- [LeanFlow, przypięty kod dostawcy](https://github.com/epfl-lara/LeanFlow/blob/9a2b6b47ac0b54c2478088a4f6bfb44130f1d650/leanflow_cli/runtime/runtime_provider.py): obsługuje Codex, Claude i Lemex; niestandardowe endpointy kieruje do Lemex. Nie traktować domyślnego backendu jako darmowego modelu.
- [Lemex, konfiguracja](https://github.com/Lemmy00/lemex/blob/2f0e12c10d0baf7404a83da3b8cb8f04b77822c9/docs/config.md): konfiguracja dostarczona z programem wskazuje zdalne EPFL RCP i wymaga klucza. [Kod lokalnego dostawcy](https://github.com/Lemmy00/lemex/blob/2f0e12c10d0baf7404a83da3b8cb8f04b77822c9/codex-rs/model-provider-info/src/lib.rs#L774) dopuszcza jednak własny lokalny serwer bez klucza/logowania. Potrzebny jawnie wybrany profil lokalny; sama zmiana nazwy backendu na Lemex nie zapewnia braku opłat.
- [Format żądania Lemex](https://github.com/Lemmy00/lemex/blob/2f0e12c10d0baf7404a83da3b8cb8f04b77822c9/codex-rs/codex-api/src/common.rs#L279): wymagane Responses API; zwykły serwer Chat Completions nie wystarczy. HTTP przekazuje pełne wejście, bez wymogu `previous_response_id`. WebSockety trzeba wyłączyć w tym profilu.
- [Dokumentacja Ollama](https://docs.ollama.com/api/openai-compatibility#responses-api) opisuje bezstanowe Responses API i wywoływanie funkcji. [Tryb lokalny](https://docs.ollama.com/faq#how-do-i-disable-ollamas-cloud-features) pozwala wyłączyć chmurę przez `OLLAMA_NO_CLOUD=1`. To zgodność protokołu na poziomie dokumentacji, nie wykonany test wszystkich narzędzi Lemex/LeanFlow.
- AutoformBot pozostaje alternatywą. Dziedziczy model i rozliczenia agenta, w którym działa; w tym przeglądzie nie potwierdzono jego kompletnego darmowego lokalnego wykonania. Nadal wymaga osobnej oceny wersji Lean ≥4.27, podczas gdy Atlas zachowuje przypięcie 4.26.

Odczytano lokalny sprzęt: 32 GB RAM, NVIDIA GeForce RTX 3060 Laptop GPU,
6144 MiB VRAM według `nvidia-smi`. Nie ma lokalnego serwera Ollama/llama.cpp,
Lean/Lake ani działającego WSL2. Wagi 8B BF16 nie zmieszczą się w całości
w 6 GB VRAM. Kwantyzacja i częściowe użycie RAM są kandydatem do próby;
nie zmierzono szybkości, zajętości pamięci ani skuteczności tłumaczenia.
Nie pobrano wag i nie uruchomiono żadnego modelu.

**Wniosek:** wariant bez opłat API jest technicznie możliwy, ale gotowość
całego procesu na tym komputerze pozostaje niepotwierdzona. Najpierw
izolowany pilot LeanFlow + Lemex + lokalny model; warunkiem wyboru są
rzeczywiste testy narzędzi i formalizacji, a nie wyłącznie dostępność endpointu.
Przed uznaniem trybu offline wyłączyć również zewnętrzne wyszukiwanie/MCP
i sprawdzić brak ruchu poza loopback. Lokalny adres serwera sam w sobie
nie dowodzi, że ten serwer nie przekazuje wywołań do chmury.

Kontynuacja przygotowania pilota: utworzono wyłącznie lokalny pakiet
czterech obiektów przez istniejące `lean_transcription.prepare`, sprawdzając
bieżące kanoniczne źródła względem indeksu. LST-01: `thm:de-morgan-logic`;
LST-02: `thm:negation-quantifiers`, `thm:same-quantifier-order`, `thm:swap-mixed`.
Pakiet zawiera źródła i kontekst obu rozdziałów: 85806 bajtów,
SHA-256 `0440ce23ca9ea3435b219b6d60982cf76459b77e821a63b02942ac52ab06a07c`.
Plik roboczy `atlas-free-formalizer-pilot-20261127.json` zapisano w katalogu
tymczasowym użytkownika, bez duplikowania rozdziałów w repozytorium.
`prepared_only`, `model_called=false`, koszt zewnętrzny 0, bez transferu,
wykonania i certyfikatu. To nie jest wynik tłumaczenia przez LLM.

Poniżej zachowano wcześniejszą ocenę z 26.11; kolejność kandydatów i zakres
płatnych integracji zastępuje powyższa aktualizacja.

Na polecenie użytkownika sprawdzono gotowe rozwiązania, aby dalszy rozwój
Atlasu wykorzystywał istniejące modele i narzędzia formalizacji. Obecny
translator Atlasu jest parserem i generatorem regułowym; nie trenujemy
własnego modelu językowego. Poniższa ocena opiera się na dokumentacji
autorów, a nie na wykonanym benchmarku tych narzędzi w naszej bibliotece.

| Rozwiązanie | Udokumentowany zakres | Dopasowanie i ograniczenia |
| --- | --- | --- |
| [AutoformBot, Meta](https://github.com/facebookresearch/autoform-bot) | Plugin dla Codex, Claude Code i Muse: artykuł, rozdział lub notatki → plan zależności → definicje i dowody Lean. Licencja MIT. | Pierwszy kandydat do oceny gotowego procesu. Aktualna dokumentacja wydania 0.7.0 wymaga Lean ≥4.27, a Atlas ma przypięte 4.26. Wymagany osobny projekt pilotażowy; nie aktualizujemy przypięcia Atlasu automatycznie. |
| [LeanFlow, EPFL](https://github.com/epfl-lara/LeanFlow) | LaTeX/PDF → szkic stwierdzeń Lean do przeglądu i późniejszego dowodzenia; osobne tryby dowodzenia i napraw. Apache-2.0. | Alternatywa do porównania. Wykorzystuje istniejący Codex, Claude Code lub Lemex. Dokumentacja wymaga Python ≥3.12; na Windows wskazuje WSL2. WSL2 nie jest zainstalowany w odczytanym lokalnym środowisku. |
| [Goedel-Formalizer-V2-8B](https://huggingface.co/Goedel-LM/Goedel-Formalizer-V2-8B) | Opublikowane wagi modelu przekształcającego nieformalne sformułowanie problemu w stwierdzenie Lean 4. Apache-2.0, 8B, BF16. | Możliwy lokalny generator bez treningu. Nie jest kompletnym procesem formalizacji rozdziału. Konieczne pomiary zasobów, zgodności z naszym Mathlib i jakości na polskim materiale. Karta nie określa minimalnego VRAM; nie deklarujemy, że model zmieści się na bieżącym komputerze. |

Dokumentacja nie dowodzi poprawnego tłumaczenia dowolnego polskiego
manuskryptu. Poprawna kompilacja Lean nie wystarcza do potwierdzenia, że
wygenerowana teza ma dokładnie te same założenia i znaczenie co źródło.
Korzystanie z gotowego procesu nie znosi potrzeby oceny tych warunków.

## Stan Atlasu w chwili przeglądu

- Przypięte Lean 4.26.0 i Mathlib
  `2df2f0150c275ad53cb3c90f7c98ec15a56a1a67`; kompilacja i audyt
  aksjomatów zarejestrowanych przykładów są wykonywane w CI.
- `lean_parser` i `lean_draft_generator` obsługują ograniczony język formuł:
  spójniki, kwantyfikatory, równości, porównania, proste działania i jawne
  typy `Prop`, `Nat`, `Int`, `Real`. Nierozpoznane fragmenty są odrzucane.
- Słownik pojęć i kontekst indeksu zapewniają powiązanie ze źródłem.
  Generator zwraca niezrecenzowany szkic; nie tłumaczy swobodnie całego
  polskiego rozdziału i nie uruchamia dowolnego kodu użytkownika.
- Bieżący RT-09c dotyczy zaufanego, stałego przykładu Mathlib offline oraz
  odrzucenia niekompletnego pakietu importów. To nie jest gotowy runner
  niezaufanych wyników modelu. Szczegóły i rzeczywiste wyniki w
  [dzienniku](ATLAS_DEVELOPMENT_PROGRESS.md).

## Kolejny pilot integracyjny

Po zakończeniu bieżącej stabilizacji, w odpowiedniej fazie planu, ocenić
gotowy proces AutoformBot i alternatywę LeanFlow, a następnie wybrać
adapter do Atlasu. Nie budować uniwersalnego translatora ani nie trenować
własnego modelu przed takim porównaniem. Reguły Atlasu zachowują funkcję
kontroli składni, pochodzenia, zakresu i ograniczeń.

1. Użyć odrębnego projektu Lean i przypiąć wersje narzędzia oraz Mathlib.
   Sprawdzić zgodność wersji, licencję i sposób wywoływania istniejącego
   modelu. Nie uruchamiać instalatorów ani agentów w kanonicznym repozytorium.
2. Przygotować wybrane obiekty LST-01 i LST-02 wraz z definicjami,
   założeniami i oryginalnymi etykietami, np. `thm:de-morgan-logic`,
   `thm:negation-quantifiers`, `thm:same-quantifier-order`,
   `thm:swap-mixed`. Dodać osobne przypadki z jawnymi typami i przypadki
   wymagające odmowy. Istniejące mapowania LST-02 mają nadal
   `needs_review`; nie są zatwierdzonym wzorcem semantycznym.
3. Rozdzielnie mierzyć zachowanie wszystkich założeń i znaczenia,
   poprawność składni, kompilację, dowód bez luk, koszty/czas i odmowy.
   Nie zaliczać szkicu ze `sorry` jako gotowego dowodu.
4. Atlas przekazuje wyłącznie wybrany fragment i niezbędny kontekst,
   zachowuje jego skróty i pokazuje wynik jako szkic do przeglądu.
   Generowanie, kompilacja i recenzja znaczenia mają osobne statusy.
5. Wykonanie zewnętrznego dostawcy lub pobranie dużych wag stanowi osobny
   krok wdrożenia. Ten przegląd niczego nie instaluje, nie pobiera wag,
   nie wysyła źródeł do modeli ani nie wykonuje płatnych wywołań.

Ten zapis ustala kierunek oceny gotowych narzędzi. Nie zamyka L1.5.6,
nie przeskakuje do L1.5.7/G2 i nie zastępuje niezależnego odbioru.
