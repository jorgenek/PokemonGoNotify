# PokemonGoNotify

Dette er et lite script jeg har laget som baserer seg på www.pogovestfold.com i Oslo som sender meg mail hvis en spesiell pokemon dukker opp.

Før tjenesten kan sende mail fra din gmail-konto så må du tillate den å sende mail:
https://www.google.com/settings/security/lesssecureapps

Scriptet spør etter:
1. Om du vil benytte deg av en default liste med sjeldne pokemons eller om du ønsker å skrive dem inn selv (separert med komma)
2. Hvor bra pokemonen skal være før den sendes på mail. Tallet er summen av verdiene til attack, defense og stamina. 45 er en perfekt pokemon og 0 vil sende på alle.
En som har ukjente verdier vil få default 0 som sum.
3. En gmail-konto som mailen skal sendes fra.
4. Passordet til den kontoen så tjenesten får lov til å sende mail. 
5. Mottakers epost-adresse. Trenger ikke å være gmail, men kan også være samme som avsender.

Ettersom jeg på jakt etter Chansey så vil den sendes på mail uansett IV verdier
