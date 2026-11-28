# RRC — iteracja 312

## Rozdział 18
Pełna kontrolna lektura 1243 wierszy blobu e21b6dfba78d200607d94eb8695241bc24ca25aa (10 sekcji). Nie wykryto nowych błędów matematycznych ani luk wymagających zmiany; źródła nie zmieniano. Jest to kontrola tego samego audytora, nie niezależna recenzja innej osoby. Run 45984997926 po 308 zakończony SUCCESS; 45985450719 oraz końcowy 45985977450 nadal queued w czasie sprawdzania, przy czym końcowy sprawdzono ponownie po edycji rozdziału 19. Odbiór wizualny 12 stron wersji po 307 udokumentowano w 311. Stabilizacja merytoryczna osiągnięta w ramach przeprowadzonych audytów, techniczny odbiór ostatniej wersji pozostaje otwarty. Aby nie powtarzać lektury bez zmian, rozpoczęto rozdział 19 równolegle z oczekiwaniem na CI.

## Rozdział 19
Pierwsza szczegółowa lektura sekcji 19.1–19.3; odczytano również początek sekcji 19.4–19.5, których jeszcze nie odebrano.

Commit źródła 421255f636920b7094c1ad0930fe6274b4be62b5, blob 933364760b80f5a9ea3e0d6d9cf6435f21c70636.
- Rozpisano energię logarytmu w wymiarze 2 i ustalono notację oraz rzeczywisty charakter funkcji.
- Uzasadniono Poincarégo przez odsyłacz do poprzedniego rozdziału.
- W lemacie o próbach gładkich uzasadniono zachowanie H_0^1 przez obcięcie, przez aproksymację, ograniczoność i słabą zbieżność. Zastąpiono dwupunktową aproksymację prostą konstrukcją w_n=chi+(1-chi)v_n, gwarantującą warunek dopuszczalności i zbieżność w H^1. Doprecyzowano argument maksimum w podaddytywności.
- W dolnym oszacowaniu pojemności kondensatora wykorzystano równoważne próby gładkie, eliminując nieuzasadnione twierdzenie o przekrojach Sobolewa. Uzasadniono przynależność profilu radialnego do H_0^1 i dokładnie obliczono energię.
- Naprawiono sprzeczność dotyczącą osiągalności: przy warunku na otwartym otoczeniu domkniętej kuli infimum nie jest osiągane; dowód przez większą kulę zawartą w otoczeniu dopuszczalności. Profil dla promienia r jest jedynie granicą ciągu dopuszczalnego.

Kontrola źródła: 923 wiersze (869 przed zmianami), 37 zachowanych unikatowych etykiet, 27 wystąpień odsyłaczy, brak niezgodności begin/end. Trzy nowe cele zewnętrzne potwierdzone jednoznacznie w rozdziałach 9,10,18; wcześniejszy chap:pde-embeddings sprawdzono osobno. Brak dedykowanej kompilacji rozdziału 19; pozostałe CI przy odczycie były queued. Następny etap: pojemność punktu dla W^{1,p}, usuwalność osobliwości i równość przestrzeni Dirichleta. Nie deklaruje się stabilizacji rozdziału 19.
