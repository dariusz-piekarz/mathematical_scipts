# RRC 16 — iteracja 291: naprawa diagnostyki PDF

Przebieg 45975563615, job 140426298004, zakończył się niepowodzeniem na kroku kontroli logu. Wcześniejsze kroki: struktura, odsyłacze, kompilacja zależności, przeniesienie 18 numerów i kompilacja rozdziału — sukces. PDF A4, 20 stron, 485352 bajty; artefakt 15186104816. Log końcowy: Overfull hbox (14.56825pt too wide) in paragraph at lines 986--996. Nie stwierdzono innego krytycznego komunikatu w końcowym kroku diagnostycznym.

Przyczynę zlokalizowano w dowodzie lem:pde16-newton-holder: długie oszacowania w akapicie matematyki śródtekstowej. Dwa wyrażenia przeniesiono do trybu eksponowanego. Nie zmieniono treści matematycznej, tekstu ani etykiet: porównanie po usunięciu delimiterów matematyki i białych znaków identyczne; wszystkie 109 wystąpień label/ref/eqref identyczne. Nowe źródło 2970995cf79c7a0e9fe27fcb42a979497d8b6e4d, 1904 wiersze, commit 431ea808c02b610e5fcc2e57df5daa12e5c476ca. Nie wyciszano diagnostyki ani nie modyfikowano workflow.

Nowy przebieg 45976114789, status queued przy odczycie.

Odbiór techniczny nadal otwarty. PDF z nieudanego przebiegu nie jest wersją końcową. Po sukcesie nowej kompilacji należy rzeczywiście obejrzeć wszystkie strony i wykonać audyt kontrolny.
