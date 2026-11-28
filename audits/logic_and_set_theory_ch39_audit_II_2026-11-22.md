# Logika matematyczna i teoria mnogości — audyt II rozdziału 39

**Data:** 22 listopada 2026 r.  
**Gałąź:** biblioteka-matematyczna-iteracja-6.  
**Źródło:** chapters/pl/logic_and_set_theory/39-slaba-zwartosc-charakterystyki-i-logika-infinitarna.tex.  
**Blob:** 9d06016d71a4c42434b8f0a58c13f666160a4034 (bez zmian od audytu I).  
**Werdykt matematyczno-redakcyjny:** czysty; drugi czysty audyt (2/2) po potwierdzeniu bieżącego CI. Pierwszy audyt uzyskał [pełne zielone CI 45070762870](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070762870).

## 1. Niezależna analiza węzłów profili

Badano ograniczenia dziedzin w konstrukcji f_α:α→μ. Przy δ≤α ograniczenie do δ ma długość dokładnie δ, a każda mniejsza restrykcja należy do tego samego drzewa. Z silnej graniczności wynika μ^{|δ|}<κ dla 0<μ<κ, δ<κ. Warto sprawdzić osobno α=0 i μ=1: lewa strona jest wtedy równa 1, co nie zmienia nierówności przy nieprzeliczalnej κ.

Dla gałęzi b wybiera się a(δ)≥δ o f_{a(δ)}|δ=b|δ. Konstrukcja f nie gwarantuje, że a(δ) jest rosnąca; poprawny dowód nie zakłada tego. Zamiast tego, po wybraniu nieograniczonego zbioru D z wartością h(δ)=b(a(δ)) równą jednemu kolorowi, rekurencja wymusza δ_ξ większe od wszystkich wcześniejszych a(δ_η). Dopiero stąd wynika α_η=a(δ_η)<δ_ξ≤a(δ_ξ)=α_ξ. W drugim kroku dowodu dla η<ξ argument α_η jest już w dziedzinie f_{α_ξ}|δ_ξ, co ściśle uzasadnia c({α_η,α_ξ})=b(α_η)=i.

Ważne: wybór i wymaga regularności i μ<κ. Sam fakt, że μ jest skończone, nie byłby wystarczającym ogólnym uzasadnieniem dla całej tezy z dowolnym μ<κ. Tekst korzysta z właściwego ograniczenia.

## 2. Niezależna analiza leksykograficznych stożków

Ścieżka węzła t obejmuje dokładnie po jednym poprzedniku na poziomach mniejszych od ht(t) oraz t na poziomie ht(t). Dla dwóch nieporównywalnych węzłów istnieje najmniejszy poziom różnicy; wybrany porządek liniowy na tym poziomie rozstrzyga ich położenie. Przedłużenia zachowują pierwszą różnicę, więc porządek stożków jest niezmienniczy.

Kluczowe jest to, że do wykazania A∩T_δ≠∅ potrzeba *dwóch* wykorzystań regularności κ: suma zbiorów mniej niż κ poziomów poniżej δ ma moc <κ, a podział κ wielu indeksów H między <κ węzłów poziomu δ musi mieć włókno mocy κ. Stąd A spotyka każdy poziom. W sprzeczności dla s,t∈A nieporównywalnych nie jest potrzebne porównanie trzech kolejnych indeksów: dwa zbiory U_s,U_t mają moc κ i są nieograniczone, podczas gdy jednorodność kolorowania wymaga wszystkich elementów jednego wcześniejszych niż wszystkie elementy drugiego. Jest to niemożliwe w żadnym z kolorów. A jest zatem gałęzią.

## 3. Niezależna analiza zwartości infinitarnej logiki zdaniowej

Każda dopuszczona formuła zależy od zbioru zmiennych mocy <κ. W konstrukcji drzewa T_α wymaga się spełnienia tylko tych formuł φ_ξ, dla których ξ<α i nośnik zawiera się w α. To ograniczenie zapewnia jednocześnie niepustość poziomu (lokalne spełnianie mniej niż κ formuł) oraz zachowanie spełniania przy zmniejszaniu dziedziny częściowego wartościowania. W gałęzi b każde φ_ξ pojawia się po przekroczeniu zarówno indeksu ξ, jak i ograniczonego w regularnej κ nośnika formuły.

Przy odwrotnej implikacji zbiór węzłów T ma moc κ, więc można przydzielić im κ zmiennych. Poziomowa alternatywa P_α używa <κ zmiennych; zakaz wspólnego przyjęcia wartości 1 dla nieporównywalnych węzłów jest formułą skończoną. Lokalnie, dla podteorii mocy <κ, wystarczy wybrać węzeł ponad wszystkimi wzmiankowanymi poziomami (ich supremum jest <κ z regularności). Prawdziwe zmienne kodują wtedy jego poprzedników. Globalne wartościowanie wymusza obecność co najmniej jednego wybranego węzła na każdym poziomie i ich porównywalność. To dokładnie gałąź współkońcowa.

Wniosek końcowy jest świadomie ograniczony do infinitarnej **logiki zdaniowej**; pełnej zwartości logiki pierwszego rzędu L_{κ,κ} nie przedstawiono jako następstwa bez dowodu.

## 4. Ponowna kontrola matematyki i składu

Sprawdzono dowód, że relacja podziałowa wyklucza singularność: przy cf(κ)=μ<κ podział κ na μ małych przedziałów prowadzi do kolorowania, które nie może mieć jednorodnego zbioru mocy κ. W materiale nie występuje pomylenie regularności z silną granicznością.

Weryfikacja statyczna: **949 wierszy, 22 odrębne etykiety, 25 odsyłaczy, 4 definicje, 4 lematy, 6 twierdzeń, 2 wnioski, 4 uwagi, 1 przykład i 12 dowodów**. Wszystkie środowiska LaTeX są zamknięte i wszystkie etykiety mają prawidłowe cele.

Na podstawie pełnego CI **[45070358451 — SUCCESS](https://github.com/dariusz-piekarz/mathematical_scipts/actions/runs/45070358451)** pobrano prawdziwy plik PDF i log. Książka ma **337 stron A4**, a rozdział 39 obejmuje strony PDF **332–337**. Sześć stron wyrenderowano i zbadano na montażu 3×2. Nie stwierdzono obciętych wzorów ani kolizji, a kontrola logu nie wykazała błędów LaTeX.

Po zaktualizowaniu reguły terminologicznej ujednolicono nazwy we wszystkich 39 rozdziałach. Dodano także dwie niezależne metody testowe: trójkolorowe skończone profile oraz wszystkie poddrzewa pełnego drzewa binarnego o trzech poziomach. Aktualnie moduł testów rozdziału 39 zawiera **11 metod**; ich osobny przebieg CI musi zakończyć się pomyślnie.

## 5. Werdykt

Audyt II **matematycznie czysty**, bez modyfikowania źródła rozdziału 39. Po ukończonym zielonym CI nowego testu jest **drugim czystym audytem (2/2)**. Następnie wykonać jeden audyt III potwierdzający na identycznym blobie; dopiero wtedy rozdział uzyska status stabilny. Kontrole Python i LaTeX nie oznaczają formalnego dowodu w Lean.
