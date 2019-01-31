from app import *
from flask import abort
from flask import request
from flask import jsonify

from app.database.mydbconn import *
from app.database.mydbconn import db_execute_scalar

from app.controllers.index import *
from app.controllers.users import *
from app.controllers.lens import *
from app.controllers.others import *
from app.controllers.dashboard import *
from app.controllers.orders import *
from app.controllers.carts import *
from app.controllers.empenho import *


@app.before_request
def check_auth():
    if request.endpoint != 'user_validate':

        token = request.headers.get('token')
        iduser = request.headers.get('iduser')
        if request.environ['REQUEST_METHOD'] != 'OPTIONS':
            if token:
                results = db_execute_scalar("EXEC SPT_WEBV3_ATUALIZA_TOKEN %s, %s;", (token, iduser))
                if results[0]['RETORNO'] != 1:
                    abort(403)    
            else:
                abort(401)

# @app.errorhandler(Exception)
# def handle_exception(ex):
#     # app.logger.exception(ex)
#     abort('Internal server error by HTK', 500)
