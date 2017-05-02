# PokemonGoNotify

Dette er et lite script jeg har laget som baserer seg på http://pogonorge.com i Oslo som sender meg mail hvis en spesiell pokemon dukker opp.

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
3. En gmail-konto som mailen skal sendes fra. Den legger til "@gmail.com" automagisk hvis du ikke har '@' i strengen.
4. Mottakers epost-adresse. Trenger ikke å være gmail, men kan også være samme som avsender.  Den legger til "@gmail.com" automagisk hvis du ikke har '@' i strengen.

Når du starter opp scriptet så spør den etter passordet til avsenderadressen. Den er nødvendig for å få tilgang til å kunne sende epost fra avsenderens adresse
