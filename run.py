from app import app

#importando rotas
from app.controllers import *

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=88, debug=True)
