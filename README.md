

![EasternWeb](logo.png "EasternWeb")




Framework for Crypto and Traditional Market Analysis
------
Use the project (see: src/website) as a local API to gather market data. Analysis tools in development. Data can be analyzed through
the browser or interactively through the shell by typing `$ python manage.py shell` in console.

Runtime Instructions (uses Python3):
----------------
1. `$python manage makemigrations website`
2. `$python manage migrate`
3. `$./start-server.sh`
4. `$./gatherer.sh`
5. Visit http://localhost:8000/admin/Signals

