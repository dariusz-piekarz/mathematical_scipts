# Lean Formalization — iteracja zabezpieczenia wyników asynchronicznych

**Data:** 22.11.2026. **Gałąź:** `biblioteka-matematyczna-iteracja-6`.

## Wykonane
Naprawiono błąd interfejsu: kiedy użytkownik otworzył inny fragment LaTeX w czasie wykonywania `POST /api/lean/run`, starsza odpowiedź mogła zmienić status dowodu, log, widok i przycisk dotyczący nowego fragmentu. W `application/frontend/app.js` dodano `isCurrentLeanRun(epoch,item)`. Przed wyświetleniem odpowiedzi, błędu oraz w `finally` sprawdzamy zarówno epokę wyboru, jak i identyczność obiektu formalizacji.

Dodano `application/tests/test_lean_browser_async.py`: uruchamia wyjętą bezpośrednio z bieżącego `app.js` funkcję w Node `vm`, kontrolując rozwiązywanie asynchronicznych obietnic. Sprawdza przypadki: (a) stary sukces po zmianie fragmentu, (b) sukces bieżącego fragmentu, (c) stary błąd po zmianie, (d) błąd bieżącego fragmentu. Gdy Node nie ma w PATH, test zostaje jawnie pominięty; w GitHub Actions uruchomienie wymaga dostępnego Node.

## Zakres i ograniczenia
Nie zmieniono kanonicznego LaTeX ani plików Lean. Test modeluje logikę asynchroniczną interfejsu, nie zastępuje pełnego testu Playwright. Lokalnie sprawdzono analogiczny scenariusz w Node 22 (wszystkie przypadki zakończone powodzeniem); wyniki CI nowego commitu trzeba osobno potwierdzić. Rzeczywiste wykonanie `lake env lean` i semantyczna wierność tłumaczenia pozostają odrębnymi celami. Status `compiled` nie jest certyfikatem dowodu źródłowego.

## Następny krok
Dodać test E2E przeglądarki dla zmiany fragmentu w trakcie uruchomienia Lean, później wersjonowane raporty wykonania (`source SHA + Lean SHA + toolchain`). Zachować rozdzielenie statusu wierności treści od statusu kompilacji.
