import os
from main.app import app

IS_LOCAL = True if os.getenv('LOCAL') is None else False 

app.run(debug = IS_LOCAL)


