from app import app
from flask import jsonify
from flask import request
from flask import abort
from app.database.mydbconn import db_execute_scalar

@app.route('/tickets/<cod_cliente>', methods=['GET'])
def tickets_total(cod_cliente):
    results = db_execute_scalar("EXEC SPT_WEBV3_GET_TOTAL_CUPOM_DESC %s;", cod_cliente)
    return jsonify(results)

@app.route('/payments/<cod_cliente>/month', methods=['GET'])
def payments_month(cod_cliente):
    results = db_execute_scalar("EXEC SPT_WEBV3_GET_TOTAL_PAG_ABERTO_MES %s;", cod_cliente)
    return jsonify(results[0])

@app.route('/payments/<cod_cliente>/total', methods=['GET'])
def payments_total(cod_cliente):
    results = db_execute_scalar("EXEC SPT_WEBV3_GET_TOTAL_PAG_ABERTO %s;", cod_cliente)
    return jsonify(results[0])