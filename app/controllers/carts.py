from app import app
from flask import jsonify
from flask import request
from flask import abort
from app.database.mydbconn import db_execute_scalar

@app.route('/carts/<cod_pedido>/total', methods=['GET'])
def carts_total(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_CARRINHO_TOTAL %s;", (cod_pedido))
    return jsonify(results)

@app.route('/carts/<cod_pedido>/parapar', methods=['GET'])
def carts_parapar_list(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_CARRINHO_PARAPAR %s;", (cod_pedido))
    return jsonify(results)


@app.route('/carts/<cod_pedido>/parapar/<cod_item>', methods=['GET'])
def carts_parapar_details(cod_pedido, cod_item):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_CARRINHO_PARAPAR_DETALHES %s, %s;", (cod_pedido, cod_item))
    return jsonify(results)

@app.route('/carts/<cod_pedido>/grade', methods=['GET'])
def carts_grade_list(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_CARRINHO_GRADE %s;", (cod_pedido))
    return jsonify(results)

@app.route('/carts/<cod_pedido>/grade/<cod_item>', methods=['GET'])
def carts_grade_details(cod_pedido, cod_item):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_CARRINHO_GRADE_DETALHE %s, %s;", (cod_pedido, cod_item))
    return jsonify(results)
