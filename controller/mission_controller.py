from flask import Blueprint, jsonify, request
from dictalchemy.utils import asdict
from repository.mission_repository import get_all_missions, get_mission_by_id

mission_blueprint = Blueprint('mission', __name__)

@mission_blueprint.route('/', methods=['GET'])
def get_missions():
    limit = request.args.get('limit', default=None, type=int)
    missions = get_all_missions(limit=limit)
    dict_missions = list(map(asdict, missions))
    return jsonify(dict_missions)

@mission_blueprint.route('/<int:mission_id>', methods=['GET'])
def get_mission(mission_id):
    mission = get_mission_by_id(mission_id)
    if mission:
        return jsonify(asdict(mission.unwrap()))
    return jsonify({'error': 'Mission not found'}), 404