from flask import Flask, jsonify, request, Blueprint
from project.api.utils import Interpreter

interpret_blueprint = Blueprint('interpret', __name__)


@interpret_blueprint.route('/interpret', methods=['POST'])
def interpret():
    data = request.get_json()
    if not data:
        return jsonify({
            'error': 'empty json'
        }), 400

    raw_text = data.get('raw_text')
    raw_text = raw_text.lower()

    interpreter = Interpreter(raw_text)

    response = interpreter.interpret_text()

    return jsonify(response), 201
