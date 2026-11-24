# L1.5.1 — lokalny pakiet wejściowy transkrypcji

Rozpoczęto na polecenie użytkownika kontynuowania funkcjonalności po technicznym 3/3 L1.4.3, bez uznawania otwartej niezależnej recenzji za zaliczoną.

POST /api/lean/transcription/prepare: entity_id, expected_source_sha256, consent (jawne true). Tylko pełne indeksowane twierdzenie z jedną poprawną etykietą, maks. 32 KiB UTF-8. Jedna migawka odczytu SQLite, SHA fragmentu, rozdziału i powiązania, deterministyczny identyfikator żądania. Źródło to indeks, nie gwarancja aktualności dysku. Nie przyjmujemy kodu, adresów dostawców, kluczy, budżetów ani dowolnego LaTeX z klienta. Brak sieci, kosztów zewnętrznych, zapisu i uruchamiania Lean; licencja niezweryfikowana, transfer zabroniony. status=prepared, candidate_status=not_generated, certificate=false.

Akceptacja: dokładne źródło, powtarzalność, brak zapisu/uruchomienia, odrzucenie błędnych lub nieaktualnych SHA, niejednoznacznych etykiet, obiektów innych niż twierdzenie, przekroczenia limitu bajtów, braku zgody i nadmiarowych pól. Testy HTTP i pełne CI 2+1. Kolejne podetapy L1.5: UI przygotowania; dopiero po stabilizacji polityka licencji i kosztów oraz izolowany adapter dostawcy; później przyjęcie kandydata draft/needs_review bez rejestracji i uruchamiania, osobna ocena semantyki. Nie oznaczać pakietu jako wygenerowanego Lean.


## L1.5.2 — kontrakt integracji UI (przygotowanie odbioru, nie implementacja)

Przegląd na kandydacie b13ee5d92af4f4fd4c57761eb530d60ca944cfc6: `loadLeanFragment` zwiększa `state.leanEpoch` przed pobraniem, `renderLeanFragment` pokazuje źródło i zarejestrowany kod, a `loadLeanFragment` może być wywoływane z katalogu oraz Czytnika. Pakiet eksperymentalny nie może współdzielić stanu wykonania Lean ani zastąpić `leanCode`.

- Osobny panel pod źródłem: „Przygotuj transkrypcję (eksperyment lokalny)”, z niezaznaczonym domyślnie checkboxem zgody na lokalne przygotowanie. Wyraźnie: brak generacji, transferu i kosztu; licencja niezweryfikowana. Zgoda jest jednorazowa, związana z konkretnym wycinkiem. Nie interpretować jej jako zgody na przyszłą usługę zewnętrzną.
- Żądanie POST musi zawierać jedynie `entity_id`, `expected_source_sha256` i `consent: true`, pobrane z aktualnego wyniku fragmentu. Nie pobierać identyfikatora z innego bieżącego rozdziału ani z tekstu użytkownika. Wymagać exact_entity, pojedynczej etykiety oraz SHA. Typ twierdzenia potwierdzać z wiarygodnych metadanych obiektu albo poprzez walidację backendu; nie wnioskować z kształtu ID. Nie mapować dowodu ani zakresu wierszy na sąsiednie twierdzenie bez jawnego wyboru.
- Przy zmianie fragmentu (już na początku `loadLeanFragment`) wyzerować pakiet, zgodę i błąd; odrzucać stare odpowiedzi i błędy na podstawie epoch i tożsamości obiektu. Równoległe kliknięcia nie powinny mnożyć żądań. Nie opierać działania przycisku na gotowości runnera ani na istnieniu formalizacji. Nie wyświetlać sukcesu po samym wysłaniu POST.
- Po odpowiedzi sprawdzić wersję i status kontraktu, moduł, ID, etykietę, zakres, SHA, źródło i rozmiar, jawne flagi false, brak kodu i dostawcy oraz zerowy koszt. Rozbieżność lub nieobsługiwany kontrakt = jawny błąd i brak pakietu. Renderować tekstowo (textContent), bez interpretowania LaTeX jako HTML. Nie traktować przygotowanego pakietu jako draft Lean: candidate_status=not_generated. Identyfikator żądania nie jest tokenem autoryzacji.
- Wymagane testy Node: brak zgody, zaznaczenie zgody dla A i zmiana na B, spóźniony sukces i błąd A, podwójne kliknięcie, błędne flagi/SHA/identyfikator, odpowiedź 409, tekst zawierający HTML, wyzerowanie przy ponowieniu. Wymagane rzeczywiste Chromium + API na kanonicznym twierdzeniu LST-01: zgodność pakietu z wybranym źródłem, brak zmian kodu Lean, odróżnienie „przygotowano” od „wygenerowano”, brak POST do runnera, przejście do innego obiektu. Sprawdzić również brak gotowości runnera, brak istniejącej formalizacji i niepoprawny typ obiektu.

Implementację oraz nową walidację 2+1 rozpocząć dopiero po rozliczeniu bieżącego podetapu. Żadna z powyższych kontroli UI nie jest jeszcze wykonana. Nie jest to niezależny odbiór L1.5.1.


## Decyzja 24.11.2026 — silnik lokalny i opcjonalne adaptery zewnętrzne

Użytkownik zatwierdził własny silnik translacji wspomagany opcjonalnie lokalną AI, a następnie rozszerzył plan o możliwość podłączenia zewnętrznego API (np. Codex, Claude). Tryb lokalny pozostaje domyślny i samodzielny; brak automatycznego fallbacku do chmury. Szczegóły i kolejność: [plan autoformalizacji](LEAN_LOCAL_AUTOFORMALIZATION_PLAN.md). Bieżący kontrakt offline oraz walidacja L1.5.2 pozostają nienaruszone. W lokalnym przygotowaniu koszt zewnętrzny wynosi 0; opcjonalne wywołania zewnętrzne otrzymają osobny kontrakt, zgodę i limity. Nie pobierać modeli, nie przesyłać źródeł ani nie uruchamiać kandydatów automatycznie.
