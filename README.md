

![EasternWeb](logo.png "EasternWeb")




Framework for crypto and traditional market analysis
------------------------
Use the website (see: src/website) as a local API to gather market data.

Runtime Instructions (uses Python3):
----------------
1. `$python manage makemigrations website`
2. `$python manage migrate`
3. `$./start-server.sh`
4. `$./gatherer.sh`
5. Visit http://localhost:8000/admin/Signals

