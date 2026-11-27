# ME-30 — audyt I całki Birkhoffa (2026-11-27)

- Stan wyjściowy: bfdbe929c571fe8fdeec89c16c24a48127baec13; CI 46064476858 zakończone sukcesem (testy i PDF), 46064476805 oraz 46064476809 również sukces.
- Rozpisano kryterium Cauchy'ego sieci sum bezwarunkowych w obu kierunkach, ograniczenie do podszeregów oraz regułę dzielenia na dwie rozłączne części.
- Uzupełniono oszacowanie błędu dla skończonej addytywności, uzasadnienie zbieżności obcięć w L1 i dominację w dowodzie skalarnym.
- Dodano przykład e_t w nieośrodkowej przestrzeni Hilberta, z dowodem całkowalności Birkhoffa i braku silnej mierzalności oraz zerowej miary wektorowej.
- Dodano regresję skończonych modeli sum ortogonalnych. Sprawdzono lokalnie unikalność etykiet i domknięcie środowisk źródłowych; nie jest to dowód poprawności kompilacji.
- Nie zmieniano istniejących etykiet ani liczby pozycji indeksu (nowy przykład nie należy do indeksowanych środowisk). Nowa kompilacja i testy wymagają odczytu wyników CI. Następny etap: niezależny audyt matematyczny i kontrola PDF.
