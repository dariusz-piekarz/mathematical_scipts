# AM II 16 — Twierdzenie Taylora — audyt

Data: 27.11.2026. Gałąź: biblioteka-matematyczna-iteracja-6.

## Historia zmian

- 5972644 — utworzenie rozdziału: reszty Peana, całkowa, Lagrange'a, zapis wielowskaźnikowy.
- ae84c5f — włączenie do książki.
- b746dc1 — przypadek wymiaru zerowego, przykład punktowej różniczkowalności, geometria przybliżenia, rysunek TikZ, algebra Banacha.
- afe107c — uzupełnienie indukcji punktowej, różniczkowania wielomianu i przesunięcia płaszczyzny stycznej.
- 27cf8c85 — szczegółowe całkowanie przez części, oszacowania reszt, indukcja Rolle'a, obliczenia przykładów.

## Kontrole po ostatniej zmianie

Blob źródłowy: 51beb721600ba6119a38f8213abca5cb33fa2c27 (535 wierszy).

1. Audyt stabilizacyjny: ponownie przeczytano cały rozdział; sprawdzono dowody, oszacowania, przykłady, matematykę rysunku i odsyłacze. Brak nowych usterek.
2. Audyt kontrolny: ponowna lektura całości na identycznym blobie. Zweryfikowano również hipotezy kanonicznych izometrii, symetrii punktowych pochodnych, wielomianów jednorodnych i przekrojów prostoliniowych w AM II 15. Sprawdzono indukcję reszty Peana, jednoznaczność, całkowanie przez części, oszacowania Höldera, zastosowania Rolle'a, zapis wielowskaźnikowy i przykłady. Nie stwierdzono nowych usterek merytorycznych.

Kontrola statyczna: 14 etykiet bez duplikatów w rozdziałach 14–16, 19/19 różnych odsyłaczy wewnętrznych z istniejącymi celami, jeden atlasref z istniejącym celem FA-15::thm:taylor15. Stos środowisk LaTeX poprawny. Rozdział włączony do książki AM II.

**Stabilizacja merytoryczna 2/2.** Nie modyfikowano źródła podczas obu czystych kontroli.

## Odbiór techniczny

Przebiegi dla 27cf8c85: AM II 45996287180, aplikacja 45996287174, terminologia 45996287163 — wszystkie queued w chwili kontroli. Nie wykonano dodatkowego uruchomienia CI. Nie potwierdzono jeszcze kompilacji aktualnego PDF, wizualnej kontroli rysunku ani lokalnej walidacji globalnych listingów. Odbiór techniczny pozostaje otwarty.

## Następny etap

Odbiór aktualnego PDF rozdziału 16 przed rozpoczęciem dalszej części AM II; w międzyczasie audyt AM I 40 (całka Riemanna–Stieltjesa).

## Odbiór techniczny i wizualny — kontrola końcowa 27.11.2026

AM II 45996287180 i terminologia 45996287163 dla 27cf8c85: success; aplikacja 45996287174: failure. Następny wspólny snapshot c5898591c0866f9e27a3535711e6917246771a72: AM II 46022724954, AM I 46022724890 i 46022717401, terminologia 46022717326, aplikacja 46022717478 — success. W bieżącej gałęzi blob rozdziału 16 (51beb721600ba6119a38f8213abca5cb33fa2c27) i pliku książki (6c405744d012452423425e07a5656122a5c7dc4e) identyczne z testowanym snapshotem. Job validate: instalacja LaTeX, kompilacja książki i publikacja artefaktu zakończone sukcesem.

Pobrano artefakt 15212195097 (ZIP 1209272 bajty), rozpakowano mathematical_analysis_ii.pdf (1228484 bajty, 142 strony fizyczne). Rozdział 16 zajmuje strony fizyczne 130–135 (drukowane 126–131). Wyrenderowano i obejrzano wszystkie sześć stron w skali 1,4, w tym rysunek 16.1 z dwiema powierzchniami i przekrojem. Nie zauważono obcięć, kolizji ani błędów składu. Kontrola ekstrakcji rozdziału: 0 ciągów ?? i 0 bloków tekstowych poza stroną; w całym PDF brak stron bez tekstu oraz brak linków GOTO poza zakresem stron. Nie wykonano ponownego odbioru wizualnego pozostałych rozdziałów ani lokalnej walidacji globalnych listingów. Kontrola dotyczy rozdziału 16 i wskazanego artefaktu, nie całej bieżącej gałęzi.

**Rozdział 16: stabilizacja merytoryczna 2/2 i odbiór kompilacji oraz składu zaliczone.** Można rozpocząć kolejny rozdział AM II zgodnie z planem.
