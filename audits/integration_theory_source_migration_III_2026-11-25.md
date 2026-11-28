# Migracja źródłowa III — całka Lebesgue'a

Źródło: commit d70b383e4057611b4d0961a185f671178c6fef9c. Przeniesiono konstrukcję z TM-07, wraz z twierdzeniem o aproksymacji monotonicznej z TM-06, twierdzenia graniczne, liniowość i wzór warstwowy z TM-08 oraz dowód zgodności z całką Riemanna z TM-08. Dowody zupełności L1 zaadaptowano z TM-14 w przypadku p=1, z własnymi etykietami, aby nie oznaczać słabszej tezy etykietą ogólnego wyniku Lp. Zachowano część porównawczą HK/McShane/Denjoy, przykłady parametryczne oraz lemat o absolutnej ciągłości całki. Nie importowano powtórnie kryterium Lebesgue'a (już w IT-02).

Kontrola lokalna: 53 etykiet w IT-11, 46 wystąpień odsyłaczy, brak nierozwiązanych lokalnych odsyłaczy w sprawdzonym zakresie i brak kolizji etykiet z 01, 02, 04, 07, 08; zgodność par środowisk. Nie uruchomiono kompilacji/CI. Dalsza migracja: miary związane z całkowaniem, Radon, Haar; audyty i poszerzenie zakresu po migracji.
