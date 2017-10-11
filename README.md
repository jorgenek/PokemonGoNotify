# PokemonGoNotify

Dette er et lite script jeg har laget som baserer seg på https://nomaps.me/livemap/oslo som sender meg mail hvis en spesiell pokemon dukker opp og samtidig poster til https://twitter.com/OsloPogo.

Før tjenesten kan sende mail fra din gmail-konto så må du tillate den å sende mail. Det aktiverer du her:
https://www.google.com/settings/security/lesssecureapps

Nettside som gir deg Latitude og Longitude koordinater:
http://www.latlong.net/

For å kjøre scriptet så må du installere disse pakkene:
- requests
- pyOpenSSL
- ndg-httpsclient
- pyasn1
- lxml

Du må endre configen med følgende attributter:

1. En streng med de pokemonene du vil bli varslet om utenom de med høy IV
2. Lokasjonen din i Latitude og Longitude. Hvis du lar strengene være tomme så bruker scriptet din IP-addresse til å avgjøre hvor du befinner deg.
3. En gmail-konto som mailen skal sendes fra. Den legger til "@gmail.com" automagisk hvis du ikke har '@' i strengen.
4. Mottakers epost-adresse. Trenger ikke å være gmail, men kan også være samme som avsender.  Den legger til "@gmail.com" automagisk hvis du ikke har '@' i strengen.
5. For å poste til twitter så må du ha opprettet en app på https://apps.twitter.com/ og legge med access_token og andre nødvendige nøkler.

Når du starter opp scriptet pokemonnotifyscript.py så spør den etter passordet til avsenderadressen. Den er nødvendig for å få tilgang til å kunne sende epost fra avsenderens adresse

Man kan også kjøre scriptet gyms.py som gir en liten oversikt over hvilke teams som kontrollerer flest gymer i Oslo og omegn.
