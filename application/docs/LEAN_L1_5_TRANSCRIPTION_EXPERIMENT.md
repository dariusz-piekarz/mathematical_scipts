# L1.5.1 — lokalny pakiet wejściowy transkrypcji

Rozpoczęto na polecenie użytkownika kontynuowania funkcjonalności po technicznym 3/3 L1.4.3, bez uznawania otwartej niezależnej recenzji za zaliczoną.

POST /api/lean/transcription/prepare: entity_id, expected_source_sha256, consent (jawne true). Tylko pełne indeksowane twierdzenie z jedną poprawną etykietą, maks. 32 KiB UTF-8. Jedna migawka odczytu SQLite, SHA fragmentu, rozdziału i powiązania, deterministyczny identyfikator żądania. Źródło to indeks, nie gwarancja aktualności dysku. Nie przyjmujemy kodu, adresów dostawców, kluczy, budżetów ani dowolnego LaTeX z klienta. Brak sieci, kosztów zewnętrznych, zapisu i uruchamiania Lean; licencja niezweryfikowana, transfer zabroniony. status=prepared, candidate_status=not_generated, certificate=false.

Akceptacja: dokładne źródło, powtarzalność, brak zapisu/uruchomienia, odrzucenie błędnych lub nieaktualnych SHA, niejednoznacznych etykiet, obiektów innych niż twierdzenie, przekroczenia limitu bajtów, braku zgody i nadmiarowych pól. Testy HTTP i pełne CI 2+1. Kolejne podetapy L1.5: UI przygotowania; dopiero po stabilizacji polityka licencji i kosztów oraz izolowany adapter dostawcy; później przyjęcie kandydata draft/needs_review bez rejestracji i uruchamiania, osobna ocena semantyki. Nie oznaczać pakietu jako wygenerowanego Lean.
