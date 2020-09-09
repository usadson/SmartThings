# Smart Things
Groep: ICT1m2

# Frontend
De front-end is je eigen PC. De script werkt alleen met Windows ivm WMI.
## Installatie guide
1.  Download en installeer [Open hardware monitor](https://openhardwaremonitor.org/downloads/)
2.  Installeer [Python3](https://www.python.org/)
3.  Installeer WMI doormiddel van "pip install wmi" in de CMD te typen.
4.  Voer het volgende uit  `python Frontend/Temperatuur.py`
# Backend
De back-end is de Raspberry PI.
## Benodigdheden:
- Raspberry PI
- SenseHAT
- Geupdate Raspbian installatie
- apache2
- CGI module apache2
## Installatie guide:
1.  Navigeer naar /var/www/html/
2.  Kopieer backend/smartthings.py naar je huidige directory
3.  Maak smartthings.py uitvoerbaar doormiddel van `chmod +x`
4.  Maak een leeg bestand aan genaamd data.json
5.  Maak data.json publiek door `chmod 755` te gebruiken.
6.  Ga naar de map Backend en voer control.py uit
