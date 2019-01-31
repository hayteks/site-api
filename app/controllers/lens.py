from app import app
from flask import jsonify
from flask import request
from app.database.mydbconn import db_execute_scalar

@app.route('/lens/<cod_cliente>', methods=['GET'])
def lens_get(cod_cliente):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_LENTES %s;", (cod_cliente))
    return jsonify(results)


@app.route('/lens/<cod_lente>/opccod', methods=['GET'])
def lens_get_opcod(cod_lente):
    results = results = db_execute_scalar("EXEC SPT_WEBV3_LIST_GRADE_OPCCOD %s;", (cod_lente))
    return jsonify(results)


@app.route('/lens/<cod_lente>/details', methods=['GET'])
def lens_get_details(cod_lente):
    results = results = db_execute_scalar("EXEC SPT_WEBV3_LIST_DIAMETROS %s;", (cod_lente))
    return jsonify(results)


    