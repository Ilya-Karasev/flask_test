from flask import Blueprint, jsonify

two_bp = Blueprint('model_2', __name__)

@two_bp.route('/', methods=['GET'])
def get_model_two():
    return jsonify({'message': 'Model 2 endpoint'})
