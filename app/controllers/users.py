from app import app
from flask import jsonify
from flask import request
from flask import abort
from app.database.mydbconn import db_execute_scalar
import base64
import string
import random
from Crypto.Cipher import DES3
import hashlib

@app.route('/user/<cod_cliente>', methods=['GET'])
def user_get(cod_cliente):
    results = db_execute_scalar("EXEC SPT_WEBV3_GET_USUARIO %s;", cod_cliente)
    return jsonify(results)

@app.route('/user/validate', methods=['POST'])
def user_validate():
    results = db_execute_scalar("EXEC SPT_WEBV3_VALIDA_USUARIO %s, %s;", 
        (request.json['email'], encrypt_pass(request.json['password'])))
    return jsonify(results)

@app.route('/user/companies/<id_user>', methods=['GET'])
def user_companies(id_user):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_EMPRESAS %s;", id_user)
    return jsonify(results)

@app.route('/user/password/<id_user>', methods=['POST'])
def user_password(id_user):
    if not request.json:
        abort(401)
    results = db_execute_scalar("EXEC SPT_WEBV3_SET_SENHA %s, %s;", (encrypt_pass(request.json['password']), id_user))
    return jsonify(results)

def encrypt_pass(password):
    key = 'x2'
    key_byte = key.encode('utf-8')
    m = hashlib.md5()
    m.update(key_byte)
    pad_len = 8 - len(password) % 8
    padding = chr(pad_len) * pad_len
    password += padding

    cryptor = DES3.new(m.digest(), DES3.MODE_ECB)
    data = cryptor.encrypt(password)

    return base64.b64encode(data).decode('utf-8')

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@app.route('/users/<cod_cliente>', methods=['GET'])
def users_list(cod_cliente):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_USUARIOS %s;", cod_cliente)
    return jsonify(results)

@app.route('/users/<cod_cliente>', methods=['POST'])
def users_create(cod_cliente):
    new_key = id_generator()
    crpt_key = encrypt_pass(new_key)
    results = db_execute_scalar("EXEC SPT_WEBV3_CREATE_USUARIO %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s;",
    (
        cod_cliente,
        request.json['user']['EMAIL'],
        request.json['user']['NOME'],
        crpt_key,
        request.json['user']['SETOR'],
        request.json['user']['_inclPedido'],
        request.json['user']['_visuCobranca'],
        request.json['user']['_inclNovoEndereco'],
        request.json['user']['_recEmailPedido'],
        request.json['user']['_recebEmailDanf'],
        request.json['user']['_recEmailembarque'],
        request.json['user']['_recebEmailBoleto'],
        request.json['user']['_recEmailatraso'],
        request.json['user']['_recEmailtresdias'],
        request.json['user']['_recEmailnegativar'],
        '',
        '')
    )
    return jsonify(results)

@app.route('/users/<cod_cliente>', methods=['PUT'])
def users_set(cod_cliente):
    results = db_execute_scalar("EXEC SPT_WEBV3_SET_USUARIO %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s;",
    (
        cod_cliente,
        request.json['user']['EMAIL'],
        request.json['user']['NOME'],
        request.json['user']['SETOR'],
        request.json['user']['_inclPedido'],
        request.json['user']['_visuCobranca'],
        request.json['user']['_inclNovoEndereco'],
        request.json['user']['_recEmailPedido'],
        request.json['user']['_recebEmailDanf'],
        request.json['user']['_recEmailembarque'],
        request.json['user']['_recebEmailBoleto'],
        request.json['user']['_recEmailatraso'],
        request.json['user']['_recEmailtresdias'],
        request.json['user']['_recEmailnegativar'],
        '',
        '')
    )
    return jsonify(results)

@app.route('/users/<cod_cliente>', methods=['DELETE'])
def users_del(cod_cliente):
    results = db_execute_scalar("EXEC SPT_WEBV3_DEL_USUARIO %s;", cod_cliente)
    return jsonify(results)



@app.route('/enderecos/<cod_cliente>', methods=['GET'])
def enderecos_list(cod_cliente):
    results = db_execute_scalar("EXEC SPT_WEBV3_LIST_ENDERECO %s;", cod_cliente)
    return jsonify(results)

@app.route('/enderecos/<cod_cliente>', methods=['POST'])
def enderecos_create(cod_cliente):
    results = db_execute_scalar("EXEC SPT_WEBV3_CREATE_ENDERECO %s, %s, %s, %s, %s, %s, %s;", (cod_cliente, 
        request.json['ENDERECO'], 
        request.json['COMPLEMENTO'], 
        request.json['BAIRRO'], 
        request.json['MUNICIPIO'], 
        request.json['CEP'], 
        request.json['UF']))
    return jsonify(results)

@app.route('/enderecos/<cod_cliente>/<cod_endereco>', methods=['PUT'])
def enderecos_set(cod_cliente, cod_endereco):
    results = db_execute_scalar("EXEC SPT_WEBV3_SET_ENDERECO %s, %s, %s, %s, %s, %s, %s, %s;", (cod_cliente, cod_endereco, 
        request.json['ENDERECO'], 
        request.json['COMPLEMENTO'], 
        request.json['BAIRRO'], 
        request.json['MUNICIPIO'], 
        request.json['CEP'], 
        request.json['UF']))
    return jsonify(results)

@app.route('/enderecos/<cod_cliente>/<cod_endereco>', methods=['DELETE'])
def enderecos_del(cod_cliente, cod_endereco):
    results = db_execute_scalar("EXEC SPT_WEBV3_DEL_ENDERECO %s, %s;", (cod_cliente, cod_endereco))
    return jsonify(results)

@app.route('/enderecos/<cod_cliente>/default', methods=['POST'])
def enderecos_default(cod_cliente):
    results = db_execute_scalar("EXEC SPT_WEBV3_SET_ENDERECO_PRINCIPAL %s, %s, %s", (cod_cliente, 
        request.json['COD_ENDERECO']))
    return jsonify(results)