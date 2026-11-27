# RRC 16 — iteracja 290: dedykowana walidacja techniczna

Źródło rozdziału: 03474f39ddc0242e8692db1f8bd3d128a782b17d (1900 wierszy), bez zmian. Trzecia lektura 64/64 zakończona bez korekt w iteracji 289.

Dodano .github/workflows/partial-differential-equations-ch16.yml, commit 9032bdaaa07458f102736ee2bc3a7cfddadcdd05, blob 1bd5231c1095910033e77b9f888db623b1568b43, na podstawie sprawdzonego workflow RRC 15.

Pipeline:
- kontrola unikatowości etykiet, wszystkich odsyłaczy i stosu środowisk, zgodności kolejności rozdziałów z manifestem, numeru rozdziału 16 i synchronizacji bloku listingów;
- kompilacja rozdziałów zależnych 03,07,08,09,10,15,17 z rzeczywistymi licznikami rozdziałów;
- przeniesienie 18 zewnętrznych numerów z aux (nie fikcyjne numery);
- kompilacja izolowanego RRC 16 z kanoniczną preambułą i licznikiem chapter=15;
- pdfinfo, tekst PDF, render każdej strony w PNG, kontrola krytycznych komunikatów LaTeX (niezdefiniowane makra, odsyłacze, overfull hbox, brakujące znaki);
- artefakt pde-ch16-audit zawierający PDF, log, tekst i obrazy stron.

Brak środowisk figure/tikzpicture/axis w źródle rozdziału 16, dlatego nie dodano osobnego testu rysunków tego rozdziału. Workflow dziedziczy metodę weryfikacji RRC 15; izolowany PDF sprawdza numery odsyłaczy, nie docelowe hiperłącza do nieobecnych w nim rozdziałów.

Uruchomienie rzeczywiście zarejestrowane przez GitHub: run 45975563615, head_sha 9032bdaaa07458f102736ee2bc3a7cfddadcdd05, status queued przy odczycie. Nie potwierdzono jeszcze kompilacji, logu ani kontroli wizualnej. Globalne CI nie jest zastępowane dedykowanym workflow.

Następna iteracja 291: odczytać wynik run 45975563615; przy sukcesie pobrać artefakt i rzeczywiście obejrzeć strony, przy niepowodzeniu zdiagnozować log i naprawić przyczynę.
