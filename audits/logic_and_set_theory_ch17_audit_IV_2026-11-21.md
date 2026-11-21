# Logika matematyczna i teoria mnogości — rozdział 17, audyt IV

**Data:** 21 listopada 2026 r.  
**Rozdział:** 17 — *Arytmetyka formalna i kodowanie składni*.  
**Podstawa:** `logika_rozdzial_17_audyt_III.tex`.  
**Wynik:** **czysty audyt stabilizacyjny**, bez dalszych zmian w źródle.

## Kontrola niezależna

1. **Q oraz PA:** sprawdzono spójność języka, numerałów, schematu indukcji z parametrami, wszystkich przypadków aksjomatów w kontrmodelu Q i argumentu przez poprawność rachunku dowodowego. Zwrócono uwagę na to, że Q8 definiuje `<` i nie narzuca zwykłych własności ostrego porządku w modelu niestandardowym.
2. **Skończone odcinki i Σ₁-zupełność:** skontrolowano jawne stosowanie Q1–Q3, Q5, Q8 przy ustalonych numerałach, podstawienia w formułach ograniczonych, przypadek n=0, skończone alternatywy/koniunkcje i wybór standardowych świadków w zdaniach Σ₁. Nie wprowadzono ukrytej indukcji w Q.
3. **Funkcje rekurencyjne:** sprawdzono dopuszczenie arności 0, funkcję poprzednika, zamkniętość operacji p.r., poprawność formuły na ograniczoną minimalizację i uzasadnienie pierwotnej rekurencyjności kolejnych liczb pierwszych.
4. **Kodowanie i dowody:** sprawdzono poprawność kodu `aba=2700`, odkodowywanie liczb, niezależność uzasadnienia funkcji kodowania w lemacie 6.3 od późniejszego lematu 6.5, sprawdzanie poprawności składni oraz obecność skończonych certyfikatów dla aksjomatów teorii efektywnie aksjomatyzowalnej.
5. **LaTeX i skład:** 34 unikatowe etykiety, 28 odsyłaczy, 5 lematów i 5 dowodów, zbilansowane środowiska, 0 przepełnień, 10 stron PDF, bez nakładania się napisów. Trzy cele w przygotowanym rozdziale 18 zostały rozstrzygnięte w PDF przez wspólną kompilację 01–18 przed wyodrębnieniem samego rozdziału 17.

## Testy

**10/10 PASS** na ostatecznym pliku, w tym pełne testy modelu Q na skończonej próbce, zgodności arności zero, kodów pierwszych i minimalizacji. Testy numeryczne stanowią weryfikację falsyfikacyjną, a nie dowód ogólny.

## Decyzja

**Wersja stabilna lokalnie.** Nie stwierdzono kolejnych błędów matematycznych, luk dowodowych, problemów językowych lub błędów składu. Można integrować rozdział 17 na istniejącej gałęzi `biblioteka-matematyczna-iteracja-6`, zaktualizować katalog i workflow, następnie uruchomić GitHub CI. Formalne zamknięcie dopiero po CI PASS.