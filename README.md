# PokemonGoNotify

Dette er et lite script jeg har laget som baserer seg på www.pogonorge.com i Oslo som sender meg mail hvis en spesiell pokemon dukker opp.

Før tjenesten kan sende mail fra din gmail-konto så må du tillate den å sende mail. Det aktiverer du her:
https://www.google.com/settings/security/lesssecureapps

Nettside som gir deg Latitude og Longitude koordinater:
http://www.latlong.net/

For å kjøre scriptet så må du installere disse pakkene:
- requests
- pyOpenSSL
- ndg-httpsclient
- pyasn1

Du må endre configen med følgende attributter:

1. En streng med de pokemonene du vil bli varslet om
2. Lokasjonen din i Latitude og Longitude. Hvis du lar strengene være tomme så bruker scriptet din IP-addresse til å avgjøre hvor du befinner deg.
3. Hvor sterk pokemonen skal være før den sendes på mail. Tallet er summen av verdiene til attack, defense og stamina. 45 er en perfekt pokemon og 0 vil sende på alle forekomster. En Pokemon med ukjente verdier vil få default 0 som sum.
4. Hvor nærme en pokemon skal være i kilometer før det sendes en mail uansett hvor sterk den er.
5. Om scriptet skal sende mail på alle pokemoner som har perfekt IV, uansett om de befinner seg i listen eller ikke.
6. En gmail-konto som mailen skal sendes fra. Den legger til "@gmail.com" automagisk hvis du ikke har '@' i strengen.
7. Mottakers epost-adresse. Trenger ikke å være gmail, men kan også være samme som avsender.  Den legger til "@gmail.com" automagisk hvis du ikke har '@' i strengen.

Når du starter opp scriptet så spør den etter passordet til avsenderadressen. Den er nødvendig for å få tilgang til å kunne sende epost fra avsenderens adresse
