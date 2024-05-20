from flask import Blueprint, jsonify

one_bp = Blueprint('model_1', __name__)

@one_bp.route('/', methods=['GET'])
def get_model_one():
    return jsonify({'message': 'Model 1 endpoint'})
