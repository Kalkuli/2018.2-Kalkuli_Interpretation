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
    price_regex = re.compile('Valor Total R\$ \d+,\d{2}')
    list_prices = price_regex.findall(raw_text)
    return jsonify({'list_prices': list_prices}), 201
