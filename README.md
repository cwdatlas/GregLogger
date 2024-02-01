---
About
---
GregLogger is an app that stores data from my GT new horizons
server. A virtual computer manipulates data from this application.
Using this app I can also see the logs while not in game. 
---
Usage
---
This app is used through two places, the viewer being the web portal and the api.
The endpoints for the api are as follows: /repo/get_all /repo/post, /repo/delete/int:log_id.
log_id must be gotten from the csv file as this method is built for when a database is used.
rather than a csv file. I use postman currently to interact with the api. Remember that http://127.0.0.1:5000
 should be your server addresss.

You can use the previously stated link to access the web portal where you can see the logs displayed.

---
How to run
---
you must have git and python installed to run this program
- Create a folder to clone the project into.
- Use 'git repo clone 'https://github.com/cwdatlas/CountyDatabase' in your command line
- Navigate to the directory with main.py (you should already be there), then type either python/python3/py main.py
- The command you use depends on your system. 'py main.py' works for me.