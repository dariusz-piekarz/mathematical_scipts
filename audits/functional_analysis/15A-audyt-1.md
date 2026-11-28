# Analiza funkcjonalna — 15A — audyt 01

24 listopada 2026. Gałąź biblioteka-matematyczna-iteracja-6.
Punkt wyjścia: 7de0de82e109444dc23932ca44c8728e09ab4d30.
Raport 15/03 zamyka 15; bezpośrednio sprawdzono job audit-ch15 przebiegu
45283098577: completed/success, wszystkie 9 kroków success. Nie jest to CI 15A.
Raport 15A/01 nie istniał przy odczycie.

## Kontrola matematyczna
- Istnienie całki: wspólne rozdrobnienie, moduł ciągłości i ciąg dyadyczny wystarczają przy zupełności ciągowej, także bez metryzowalności.
- Liniowość i oszacowanie seminormowe: poprawne. Addytywność względem przedziału miała brakujące założenie istnienia całek na podprzedziałach. W przestrzeni niezupełnej całka na całym przedziale może istnieć dzięki znoszeniu się dwóch całek istniejących tylko w uzupełnieniu.
- Przemienność z ciągłym operatorem: granica sum przechodzi przez operator bez zupełności przestrzeni docelowej.
- Środek ciężkości: znormalizowane sumy są kombinacjami wypukłymi.
- Uzupełnienie: zanurzenie topologiczne zapewnia zbieżność w podprzestrzeni, gdy granica do niej należy.
- Całka niewłaściwa: ogony każdej seminormy kontrolują ciąg i dowolny rzeczywisty parametr.
- Newton–Leibniz: oszacowanie różnicy ilorazowej, orientacja dla h<0 i rozdzielanie punktów przez funkcjonały.
- Parametr: Hahn–Banach i jednostajna ciągłość pochodnej na zwartym prostokącie.
- Fubini: wspólne sumy podwójne i niezależna kontrola obu średnic.
- Silna całka operatorów: Banach–Steinhaus daje wspólne ograniczenie norm.

## Przykłady
Cztery środowiska przykładów: c00 (rozłączne nośniki i dodatnie współrzędne całki), C∞ (ciągłość różniczkowania i ewaluacji), Schwartz (kontrola seminorm), grupa mnożenia na zespolonym L² (zbieżność zmajoryzowana i norma różnicy 2). Dodano do pierwszego przykładu odbicie z przeciwnym znakiem na [1,2]: całka całej krzywej jest zerem, lecz ograniczenie do [0,1] nie ma całki w c00.

## Zmiany
Źródło: 6caa8199f4cabecdb2745e58e40a40a6806252b8, blob f42bf05883d30c43cc6037ed3e78476a5bf6318f.
Test: cea45adb526ec26e852061a67c1afba00ba02baf; dokładne całkowanie odcinkami liniowych funkcji z użyciem Fraction dla 32 współrzędnych. Test jest świadkiem skończenie wymiarowym, nie dowodem nieskończenie wymiarowym.
Sprawdzono parowanie środowisk: bez rozbieżności.
Nie wykonano pełnego sprawdzenia odsyłaczy między rozdziałami, kompilacji ani inspekcji PDF. Nie potwierdzono uruchomienia nowego testu ani CI 15A.

**Werdykt: 0/2, niestabilny.** Następna iteracja: niezależny audyt 15A, uruchomienie regresji, bramka CI z pełnym kontekstem odsyłaczy (także 15B i 17), PDF. Nie przechodzić do 15B.
