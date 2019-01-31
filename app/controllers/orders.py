from app import app
from flask import jsonify
from flask import request
from flask import abort
from app.database.mydbconn import db_execute_scalar, db_execute


@app.route('/orders/numped/<cod_cliente>', methods=['GET'])
def orders_numped(cod_cliente):
    results = db_execute_scalar("EXEC SPT_WEBV3_GET_NUMPED %s;", (cod_cliente))
    return jsonify(results)

@app.route('/orders/history/<cod_cliente>', methods=['POST'])
def history_get(cod_cliente):
    if not request.json:
        abort(401)
    if request.json['cod_master'] == '0':
        request.json['cod_master'] = ''
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_HISTORICO %s, %s, %s, %s, %s, %s, %s;", (cod_cliente, request.json['id_ini'], request.json['id_qtd'], request.json['status'], request.json['data_ini'], request.json['data_fim'], request.json['cod_master']))
    return jsonify(results)

@app.route('/orders/financial/<cod_cliente>', methods=['POST'])
def financial_get(cod_cliente):
    if not request.json:
        abort(401)
    if request.json['cod_master'] == '0':
        request.json['cod_master'] = ''
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_FINANCEIRO %s, %s, %s, %s, %s, %s, %s, %s, %s;", (cod_cliente, request.json['id_ini'], request.json['id_qtd'], request.json['status'], request.json['data_ini'], request.json['data_fim'], request.json['campo'], request.json['order'], request.json['cod_master']))
    return jsonify(results)

@app.route('/orders/financial/details/<titulo>', methods=['GET'])
def financial_details_get(titulo):
    results = db_execute_scalar("EXEC spt_WEBSITE_FINANCEIRO_DRIL_DROW %s;", (titulo))
    return jsonify(results)



@app.route('/orders/details/<cod_pedido>/grade', methods=['GET'])
def history_details_grade(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_HISTORICO_DETALHES_GRADE %s;", (cod_pedido))
    return jsonify(results)

@app.route('/orders/details/<cod_pedido>/grade/<cod_produto>', methods=['GET'])
def history_details_grade_grade(cod_pedido, cod_produto):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_HISTORICO_DETALHES_GRADE_GRADE %s, %s;", (cod_pedido, cod_produto))
    return jsonify(results)

@app.route('/orders/details/<cod_pedido>/pap', methods=['GET'])
def history_details_pap(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_HISTORICO_DETALHES_PARAPAR %s;", (cod_pedido))
    return jsonify(results)

@app.route('/orders/details/<cod_pedido>/rastreio', methods=['GET'])
def history_details_rastreio(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_HISTORICO_RASTREIO %s;", (cod_pedido))
    return jsonify(results)

@app.route('/orders/details/<cod_pedido>/boleto', methods=['GET'])
def history_details_boleto(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_HISTORICO_BOLETOS %s;", (cod_pedido))
    return jsonify(results)

@app.route('/orders/details/<cod_pedido>/danfes', methods=['GET'])
def history_details_danfe(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_HISTORICO_DANFES %s;", (cod_pedido))
    return jsonify(results)


@app.route('/orders/condpag', methods=['GET'])
def orders_condpag():
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_CONDPAG;", '')
    return jsonify(results)

@app.route('/orders/condpag/<cod_pedido>', methods=['POST'])
def orders_condpag_set(cod_pedido):
    if not request.json:
        abort(401)
    db_execute("EXEC SPT_WEBV3_SET_CONDPAG %s, %s;", (cod_pedido, request.json['cod_condpag']))
    return jsonify({ 'success': True })

@app.route('/orders/<cod_pedido>/cancel', methods=['GET'])
def orders_cancel(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_DEL_PEDIDO %s;", (cod_pedido))
    return jsonify(results)

@app.route('/orders/<cod_pedido>/frete', methods=['GET'])
def orders_frete(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_FRETE %s;", (cod_pedido))
    return jsonify(results)

@app.route('/orders/<cod_pedido>/transportadoras', methods=['GET'])
def orders_transportadoras(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_TRANSPORTADORA %s;", (cod_pedido))
    return jsonify(results)


@app.route('/orders/<cod_pedido>/transportadoras', methods=['POST'])
def orders_set_transportadoras(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_SET_TRANSPORTADORA %s, %s, %s;", 
    (cod_pedido, request.json['CODTRANSP'], request.json['VALFRETE']))
    return jsonify(results)

@app.route('/orders/<cod_pedido>/formapgto', methods=['GET'])
def orders_forma_pgto(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_FORM_PAGAMENTO %s;", (cod_pedido))
    return jsonify(results)

@app.route('/orders/<cod_pedido>/close', methods=['POST'])
def orders_set_close(cod_pedido):
    results = db_execute_scalar("EXEC SPT_WEBV3_SET_GRAVA_PEDIDO %s, %s, %s, 'WV3';", (cod_pedido, request.json['NUMOS'], request.json['EMAIL']))
    return jsonify(results)

@app.route('/orders/suggest/<cod_pedido>/<cod_frete>', methods=['GET'])
def orders_get_suggest(cod_pedido, cod_frete):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_SUGERE_LENTES %s, %s;", (cod_pedido, cod_frete))
    return jsonify(results)

@app.route('/orders/suggest/<cod_pedido>/<cod_frete>', methods=['POST'])
def orders_set_suggest(cod_pedido, cod_frete):
    results = db_execute_scalar("EXEC SPT_WEBV3_SET_SUGERE_LENTES %s, %s, %s, %s;", (cod_pedido, cod_frete, request.json['COD_PRODUTO'], request.json['QUANTIDADE']))
    return jsonify(results)