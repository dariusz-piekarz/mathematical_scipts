# Audyt LXXVI (76) — rozdział 21: drugi przegląd i zamknięcie

**Data:** 2026-11-23. **Repozytorium:** dariusz-piekarz/mathematical_scipts.
**Istniejąca gałąź:** biblioteka-matematyczna-iteracja-6.
**Kanoniczny plik:** chapters/pl/measure_theory/21-twierdzenie-riesza-markowa-kakutaniego.tex.
**Zweryfikowany blob:** fd6eedf8e96f645283ba837061cc3e7c0e955aae.
**Wersja testów:** tools/tests/test_measure_theory_ch21.py, blob 64c4d64165410b588c0b795b325725dc63eafa2e.
**Commit objęty pełną kontrolą:** be18f56721885eb9c268c50ed81015eb0ffa6f6b.

## I. Drugi, niezależny przegląd merytoryczny

Po poprawkach audytu LXXIV i uzupełnieniu audytu LXXV powtórnie sprawdzono:
1. Lemat o metrycznej mierze zewnętrznej: odległość od domkniętego F jest 1-lipschitzowska, oddzielone pasy A_j o indeksach tej samej parzystości pozwalają oszacować miarę zewnętrzną reszty; nie jest używana nieuprawniona ciągłość z dołu przed stwierdzeniem mierzalności.
2. Zwarta reprezentacja: treść a(U) z dodatniego funkcjonału, podaddytywność na otwartych za pomocą jawnie zbudowanych funkcji theta_i, przedłużenie do metrycznej miary zewnętrznej, mierzalność borelowska, regularność i identyfikacja całki przez sumy poziomicowe. Sprawdzono obie nierówności w oszacowaniach dolnych i górnych; błąd całki dąży do zera wraz z krokiem podziału zakresu f.
3. Lokalizacja: konstrukcja wyczerpania U_n o zwartych domknięciach, poprawne przedłużenie chi_n h przez zero, zgodność miar na U_n za pomocą unikalności z rozdziału 20, sklejenie po rozłącznych warstwach i regularność wynikowej miary.
4. C_0 i skończona masa: gęstość C_c(X) w C_0(X), przybliżanie jednostki przez odcięcia oraz równość normy dodatniego funkcjonału i masy reprezentującej miary.
5. Wersja zespolona: funkcjonał M(g)=sup{|T(h)|: |h|≤g} na funkcjach nieujemnych, jego addytywność uzyskiwana przez rozkład h według g_i/(g_1+g_2) i dobranie faz; rozszerzenie do rzeczywistego dodatniego funkcjonału, przedłużenie do L¹(σ), zastosowanie dualności L¹–L∞, miara zespolona ν=wσ, wzór na wariację i odtworzenie normy za pomocą mierzalnej funkcji fazowej przybliżanej w L¹(|ν|) przez funkcje C_c.
6. Przykład skończonej miary atomowej: dodatnia odległość pomiędzy skończenie wieloma różnymi punktami daje rozłączne relatywnie zwarte otoczenia; funkcje odcinające i fazy conj(a_j)/|a_j| realizują normę sumy funkcjonałów ewaluacji.
7. Wniosek porządkowy, jednoznaczność z całek C_c i ograniczenie w problemie momentów.

Poprawki źródłowe: commit f64f6f6b13d2b5c3c1159cf8d6283a8d4ecb3f51 (ciągły podział jedności, przypadek pustego F, poprawna terminologia), commit bd98d18a92ccedb5aaab59fce4907b38ab522bfb (szczegółowy przykład atomowy). Druga kontrola nie wykazała nowej luki matematycznej wymagającej następnego commitu. W źródle pozostaje 21 różnych etykiet; zewnętrzne odsyłacze są potwierdzone również przez rzeczywisty build.

## II. Potwierdzenie rzeczywistego przebiegu GitHub Actions

**Run:** https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45280854102
**Run head:** be18f56721885eb9c268c50ed81015eb0ffa6f6b (zawiera najnowszy przykład i korektę jego testu).

Klasyczne statusy tego commitu:
- measure-theory/ch21-regressions: success;
- measure-theory/ch21-pdf: success.
Oba prowadzą do tego samego przebiegu.

Z logów trzech zakończonych sukcesem jobów:
- regresje, ID 138069314212: Ran 8 tests ... OK i Ran 4 tests ... OK; łącznie **12/12 PASS**;
- PDF, ID 138069313726: pełna książka **260 stron, 1 903 389 bajtów**; samodzielny rozdział 21 **7 stron, 285 325 bajtów**; import 8 zewnętrznych etykiet bez kolizji z 21 lokalnymi; końcowe odsyłacze rozwiązane;
- publikacja statusów, ID 138069906876: completed/success.

## III. Rzeczywisty artefakt i wizualizacja

Artefakt ID 14869528173, nazwa measure-theory-ch21-pdf-and-logs, rozmiar ZIP 2 744 749 bajtów, rzeczywiście pobrano i rozpakowano. Zawiera PDF książki, PDF samodzielnego rozdziału, dwa logi i podglądy PNG.

Oryginalny siedmiostronicowy PDF wyrenderowano w całości. Zweryfikowano montaż stron 1–7 i osobno stronę 7 w wysokiej rozdzielczości. Nowy przykład atomowy ma pełne obliczenia i kończy się przed kompletną sekcją 21.7. Ostatnia strona ma około 1365 znaków, nie jest osieroconym krótkim fragmentem, a tekst, numeracja, wzory i marginesy nie mają widocznych kolizji.

W końcowych, a nie pośrednich logach:
- pełna książka: 0 Overfull hbox, 14 nieblokujących Underfull hbox, 0 nierozwiązanych odsyłaczy i 0 multiply defined; 56 nieblokujących ostrzeżeń hyperref dotyczących zakładek PDF;
- samodzielny rozdział: 0 Overfull hbox, 0 Underfull hbox, 0 nierozwiązanych odsyłaczy i 0 multiply defined; 3 nieblokujące ostrzeżenia hyperref.

## IV. Werdykt

**ROZDZIAŁ 21: STABILNY / ZAMKNIĘTY** dla dokładnego bloba fd6eedf8e96f645283ba837061cc3e7c0e955aae, po iteracjach LXXIV–LXXVI, dwóch przeglądach merytorycznych, rzeczywistych 8+4 testach, obu poprawnych PDF-ach i oględzinach wszystkich siedmiu stron. Nie oznacza to formalnej certyfikacji wszystkich twierdzeń w Lean.

W ustalonej kolejności rozdziały 15–21 mają zamknięte audyty. **Następna jednostka: rozdział 22** — zbieżność miar i twierdzenia zwartościowe; przed dalszym rozdziałem 23 wymaga osobnej kontroli matematycznej i CI.
