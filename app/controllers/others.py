from app import app
from flask import jsonify
from flask import request
from app.database.mydbconn import db_execute_scalar
import buscacep

@app.route('/faq', methods=['GET'])
def faq_get():
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_FAQ;", '')
    return jsonify(results)

@app.route('/downloads', methods=['GET'])
def downloads_get():
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_DOWNLOADS;", '')
    return jsonify(results)

@app.route('/sales/<cod_cliente>', methods=['GET'])
def sales_list(cod_cliente):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_REPRESENTANTES %s;", cod_cliente)
    return jsonify(results)

@app.route('/cep/<numero>', methods=['GET'])
def get_cep(numero):
    res = buscacep.busca_cep_correios_as_dict(numero)
    return jsonify(res)


    



    