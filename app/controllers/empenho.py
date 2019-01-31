from app import app
from flask import jsonify
from flask import request
from flask import abort
from app.database.mydbconn import db_execute_scalar, db_execute
import json

@app.route('/empenho/grade/<cod_pedido>/<cod_produto>/<cod_condpag>', methods=['POST'])
def empenho_grade(cod_pedido, cod_produto, cod_condpag):
    if not request.json:
        abort(401)

    db_execute("EXEC SPT_WEBV3_SET_EMPENHO_BEGIN %s, %s, %s;", (cod_pedido, cod_produto, cod_condpag))

    statement = ''
    _pedidos = json.dumps(request.json['pedido'])
    pedidos = json.loads(_pedidos)
    for pedido in pedidos:
        statement += "EXEC SPT_WEBV3_SET_EMPENHO_OPCCODE '" + str(cod_pedido) + "', '" + str(pedido['OPCCOD']) + "', " + str(pedido['QTD']) + ";"
        
    db_execute(statement, '')

    results = db_execute_scalar("EXEC SPT_WEBV3_SET_EMPENHO_END %s, %s;", (cod_pedido, cod_produto))
    return jsonify(results)


@app.route('/empenho/parapar/<cod_pedido>/<cod_produto>', methods=['POST'])
def empenho_parapar(cod_pedido, cod_produto):
    results = db_execute_scalar("EXEC SPT_WEBV3_SET_EMPENHO_PARAPAR %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s;",
    (
        cod_pedido,
        request.json['parOshtk'],
        cod_produto,
        request.json['REsferico'],
        request.json['RCilindrico'],
        request.json['REixo'],
        request.json['LEsferico'],
        request.json['LCilindrico'],
        request.json['LEixo'],
        request.json['Oscliente'],
        request.json['nome'])
    )
    return jsonify(results)

@app.route('/empenho/parapar/<cod_pedido>/delete', methods=['POST'])
def empenho_parapar_delete(cod_pedido):
    results = db_execute("EXEC SPT_WEBV3_DEL_UM_PAR %s, %s, %s;",
    (
        cod_pedido,
        request.json['Oshtk'],
        request.json['Produto'])
    )
    return jsonify(results)


@app.route('/empenho/montagem/<cod_pedido>/<os_htk>', methods=['POST'])
def empenho_montagem(cod_pedido, os_htk):
    results = db_execute_scalar("EXEC SPT_WEBV3_SET_EMPENHO_PARAPAR_MONTAGEM %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s;",
    (
        cod_pedido,
        os_htk,
        request.json['UID'],
        request.json['RDNP'],
        request.json['RALTURA'],
        request.json['LDNP'],
        request.json['LALTURA'],
        request.json['Marca'],
        request.json['Cor'],
        request.json['Aro'],
        request.json['Modelo'],
        request.json['TipoAro'],
        request.json['Ponte'],
        request.json['polimento'],
        request.json['quebracanto'],
        request.json['Material'])
    )
    return jsonify(results)