# Biblioteka matematyczna — test podglądu odsyłaczy, 20.11.2026

Rozszerzono `application/tests/browser_ci_e2e.py` o rzeczywisty podgląd jednoznacznego cytowanego fragmentu ze wspólnej bazy. Chromium otwiera rozdział zawierający odsyłacz, najeżdża na `.ref-link`, sprawdza `#referenceTip`, treść `.tip-code` i przycisk `#tipOpen`.

GitHub Actions [#44707891398](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/44707891398), commit `a9259c8675da574aac102950bf9c9ac22e28bfbf`: **success**. 85 testów Python, `OK (skipped=1)`; rzeczywisty Chromium: 355 rozdziałów, 16 dziedzin, podgląd `tw:korzenie` z `ALG-00`, 0 błędów JS, sukces osobnego testu draft/save/page-leave.

Ograniczenia: bez testu gwarantowanego dostarczenia beacon przy X-close i bez matematycznego audytu nierozwiązanych/konfliktowych etykiet. Test przy opuszczeniu strony dotyczy `pagehide`, nie gwarantuje usunięcia szkicu przy każdym sposobie zamknięcia przeglądarki. Kanoniczne źródła `chapters/pl` i gałąź `main` nietknięte.
