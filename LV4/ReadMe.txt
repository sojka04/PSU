ZAD 1.
U ovom zadatku koristi se linearni model regresije, što znači da model predviđa izlaznu vrijednost kao linearnu funkciju ulaznih varijabli. Ovaj model daje osnovnu aproksimaciju podataka.

ZAD 2.
U drugom zadatku koristi se polinomski model regresije, koji proširuje osnovni linearni model dodajući višestruke stupnjeve varijabli. To omogućuje bolju aproksimaciju složenih odnosa u podacima, što znači da polinomni model može bolje pratiti varijacije u podacima nego linearni model iz prvog zadatka.

ZAD 3.
Kada povećavamo stupanj polinoma (degree), model može bolje pratiti podatke, ali postoji rizik od prekomjerne prilagodbe (overfitting) ako se stupanj poveća previše. Idealno je koristiti optimalan stupanj koji minimizira pogreške na trening i test podacima. Previše visok stupanj može dovesti do modela koji je previše prilagođen specifičnostima skupa podataka i može izgubiti sposobnost generalizacije.

ZAD 4.

a) Dataset sadrži 6699 automobila.

b) Tipovi podataka u dataframeu uključuju:

float64 za numeričke varijable poput cijene i kilometraže.

int64 za varijable poput godine proizvodnje, broja sjedala i snage motora.

object za kategorijske varijable poput naziva automobila, tipa goriva i tipa mjenjača.

c) Automobil s najmanjom cijenom je Maruti 800 AC (1997) s cijenom od 10.31 INR, dok je automobil s najvećom cijenom BMW X7 xDrive 30d DPE (2020) s cijenom od 15.79 INR.

d) U 2012. godini proizvedeno je 575 automobila.

e) Automobil s najmanje kilometara je Maruti Eeco 5 STR With AC Plus HTR CNG, dok je automobil s najviše kilometara Toyota Fortuner 4x4 (2012).

f) Najčešći broj sjedala je 5, što se može vidjeti iz distribucije podataka.

g) Srednja kilometraža za benzinske automobile je oko 54,101 km, dok za dizelske automobile iznosi oko 88,040 km.

ZAD 5.
Kada gradimo model za predviđanje cijene automobila, trebamo:

Izbaciti nepotrebne varijable poput imena automobila pomoću funkcije df.drop().

Podijeliti podatke na trening i test skupove u omjeru 80%-20% pomoću train_test_split() iz sklearn.

Skalirati ulazne podatke korištenjem MinMaxScaler ili StandardScaler iz sklearn kako bismo osigurali da varijable s različitim skalama ne utječu negativno na model.

Izgraditi linearni regresijski model pomoću sklearn i evaluirati ga korištenjem funkcija kao što su mean_absolute_error, r2_score, i mean_squared_error.

Evaluirati model na trening i test podacima kako bismo usporedili njegove performanse.

ZAD 6.
Kada dodamo kategoričke varijable u model, koristimo funkciju pd.get_dummies() za one hot kodiranje. Ovo omogućuje modelu da bolje razumije kategorijske informacije. Dodavanje ovih varijabli može poboljšati performanse modela jer pružaju više informacija o specifičnostima automobila, što može rezultirati preciznijim predviđanjima cijena.