# Audyt CXXXVIII (138) — PDF i układ rozdziału 29
Data: 2026-11-24. Gałąź biblioteka-matematyczna-iteracja-6.
## Zweryfikowana wersja
Run 45371886126, commit 192d20d95f527141d75392ab87ee086d3182d8f2, blob źródła 303e077c31f2c4c3c7a144b81e2945a5bbdced4d. Wszystkie trzy zadania zakończyły się success. Artefakt 14908888320, sha256 a1c2f38ab8e5f1ad8ba4433a92ec93c125d593e0c7d9c964ead2e960a9c412de, pobrany i rozpakowany w środowisku roboczym.
- Pełny skrypt: 297 stron, osobny rozdział: 35 stron.
- Końcowe logi obu kompilacji: 0 ostrzeżeń o nierozwiązanych odsyłaczach, 0 komunikatów Overfull.
- Rzeczywisty przegląd wizualny wszystkich stron 1–35 izolowanego PDF na sześciu planszach; dodatkowo strony 8 i 25 wyrenderowane w większej rozdzielczości. Rysunki normalnych prostokąta oraz granicy półprzestrzennej nie mają widocznych kolizji opisów ani obcięć. Nie stwierdzono widocznych problemów układu stron.
- W logu izolowanego rozdziału wystąpiły dwa ostrzeżenia hyperref dotyczące math shift w tytule sekcji 29.8 (wiersz 2891). Zakładka PDF miała poprawny tekst, ale usunięto przyczynę ostrzeżenia.
## Drobna poprawka
Commit 4fcf062a1420842f0a33a9d0efe6ac05d197ff96, blob af8b4ddf9387e5023eab56de458bfc48ce130e62. Zastosowano texorpdfstring dla BV w tytule sekcji. Nie zmieniono treści matematycznej ani etykiet. Oczekuje na ponowną kompilację. Weryfikacja wizualna opisana powyżej dotyczy wyłącznie poprzedniego artefaktu, nie nowej wersji.
## Otwarte
Potwierdzić CI dla końcowej poprawki, porównać render nowej wersji i potwierdzić usunięcie ostrzeżeń zakładki. Do tego czasu rozdział otwarty, 28/31 ustabilizowanych.
