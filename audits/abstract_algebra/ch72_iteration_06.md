# AA-72 — audyt VI, niezależna kontrola zamykająca

Stan odczytu b6f205965c0afa792cb1405c14df7d8e1fdecf49. AA-72: blob 74ce108e02500804172271157af3792ce98fa83b; AA-69: 73550fe9088795bb4735414200fcc0ffde4120e0; AA-70: 18f76eb8ecb04ecbaf316065b6e52c2c4d2b0d53; regresje: 182ed4998ef59dce8c422b072a4652f7b7b7564f.

## Kontrola semantyczna
Ponownie odczytano AA-72 i odpowiednie twierdzenia AA-69/70. Lemat aa:lem:weyl-rho daje rho(h_i)=1 i rho w P, a zatem lambda+rho jest ściśle dominująca. Lemat aa:lem:weyl-regular-orbits daje trywialność stabilizatora; znak orbity jest wyznaczony jednoznacznie przez wyznacznik iloczynu odbić. Tożsamości A_rho=e^rho C oraz A_rho ch L=A_{lambda+rho} zachodzą w tym samym pierścieniu i przy tych samych hipotezach. Mnożenie przez e^{-rho} jest działaniem jednostki pierścienia, a następnie zastosowanie tożsamości do B nie wymaga mnożenia dwóch nieskończonych szeregów. Argument P ma właściwy znak. Sprawdzono bazę rekurencji, przypadki spoza Q_+, tablice z zerową współrzędną, terminację orbity, parzystość i oba krańce A1 oraz anulowanie w A2. Nie stwierdzono nowych usterek.

## Niezależny rachunek dokładny
Wykonano dodatkową kontrolę typu A2 w JS (bez importów), z niezależnym modelem rozgałęzienia Gelfanda–Tsetlina dla najwyższej wagi GL3 (a+b,b,0). Wynik: 45 modeli a,b>=0, a+b<=8, 8265 porównań krotności, 45 porównań sumy krotności ze wzorem wymiarowym Weyla, 5055 ujemnych niezerowych składników alternantu; PASS. To dodatkowy rachunek kontrolny, nie nowy obowiązkowy krok CI i nie formalizacja Lean. Kod umożliwiający powtórzenie:

```js
const perms=[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]];
const sign=p=>p.reduce((n,x,i)=>n+p.slice(i+1).filter(y=>y<x).length,0)%2?-1n:1n;
const P=v=>v[0]+v[1]+v[2]!==0||v[0]<0||v[2]>0?0n:BigInt(1+Math.min(v[0],-v[2]));
let models=0,weights=0,dimensions=0,negativeTerms=0;
for(let a=0;a<=8;a++)for(let b=0;b<=8-a;b++){
 const L=[a+b,b,0],rho=[2,1,0],shift=L.map((x,i)=>x+rho[i]),D=a+2*b;
 const gt=new Map();
 for(let u=b;u<=a+b;u++)for(let v=0;v<=b;v++)for(let t=v;t<=u;t++){
  const k=[t,u+v-t,D-u-v].join(",");gt.set(k,(gt.get(k)||0n)+1n);
 }
 let sum=0n;
 for(let x=-2;x<=D+2;x++)for(let y=-2;y<=D+2;y++){
  const mu=[x,y,D-x-y];let m=0n;
  for(const p of perms){const c=sign(p)*P(p.map((j,i)=>shift[j]-mu[i]-rho[i]));if(c<0n)negativeTerms++;m+=c}
  if(m!==(gt.get(mu.join(","))||0n))throw Error("multiplicity mismatch");
  sum+=m;weights++;
 }
 if(sum!==BigInt((a+1)*(b+1)*(a+b+2)/2))throw Error("dimension mismatch");
 models++;dimensions++;
}
console.log({models,weights,dimensions,negativeTerms,status:"PASS"});
```

## CI i PDF
Potwierdzono rzeczywiste CI 45504497437 (head e9041876b045e1ee2f3be45339ded434699f9ebf, 151 kroków success) oraz 45504587648 (head 46bd1949f54c099906070eb838ca9740e8a26e9c, success), w obu zaliczone regresje AA-72, kompilacja i weryfikacja PDF oraz odsyłaczy. Porównanie commitów od e904187 do b6f2059 (19 commitów) wykazało brak zmian źródeł algebry, preambuły, testów i jej workflow. Run 45566123175 (head 52e3cd2, zmiana raportu V) w toku, 7 kroków success, jeden aktywny, 142 oczekujące; nie deklaruje się jego zaliczenia. Oględziny wszystkich stron AA-72 i logu zostały udokumentowane w audycie V dla identycznego źródła; nie powtarzano inspekcji niezmienionego PDF. Nie uruchamiano Lean.

## Decyzja
AA-72 STABILNY w zatwierdzonym zakresie: po korekcie technicznej IV dwa czyste audyty V/VI, dwa zielone przebiegi CI niezmienionego materiału i udokumentowana kontrola wszystkich stron rozdziału. AA-01–72 mają zakończoną stabilizację rozdziałową. Nie otwierać AA-73. Cały tom pozostaje otwarty do końcowego audytu przekrojowego (integralność, zależności, hipotezy, dowody, regresje i PDF całej książki).
