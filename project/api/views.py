from flask import Flask, jsonify, request, Blueprint
import re


interpret_blueprint = Blueprint('interpret', __name__)

@interpret_blueprint.route('/interpret', methods=['POST'])
def interpret():
    data = request.get_json()
    if not data:
        return jsonify({
            'erro': 'sem dado'
        }), 400

    raw_text = data.get('raw_text')
    raw_text = raw_text.lower()
    price_regex = re.compile('valor total r\$ \d+,\d{2}')
    list_prices = price_regex.findall(raw_text)

    date_regex = re.compile('\d{2}/\d{2}/\d{4}')
    list_date = date_regex.findall(raw_text)

    cnpj_regex = re.compile('\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}')
    list_cnpj = cnpj_regex.findall(raw_text)
    return jsonify({
        'list_prices': list_prices,
        'list_date': list_date,
        'list_cnpj': list_cnpj
        }), 201
