from flask import Blueprint, request, jsonify
from returns.result import Success

from repository.new_mission_repository import create_mission, get_mission_by_id, get_all_missions, update_mission, \
    delete_mission
from model import NewMission

new_mission_blueprint = Blueprint("new_mission", __name__)


@new_mission_blueprint.route('', methods=['POST'])
def create():
    data = request.json
    mission = NewMission(**data)
    result = create_mission(mission)
    if isinstance(result, Success):
        return jsonify({'id': result.value.id}), 201
    return jsonify({'error': result.error}), 400


@new_mission_blueprint.route('', methods=['GET'])
def get_all():
    result = get_all_missions()
    if isinstance(result, Success):
        missions = [{
            'id': mission.id,
            'target_id': mission.target_id,
            'country_id': mission.country_id,
            'city_id': mission.city_id,
            'industry_id': mission.industry_id,
            'type_id': mission.type_id,
            'priority_id': mission.priority_id
        } for mission in result.unwrap()]
        return jsonify(missions), 200
    return jsonify({'error': result.error}), 400


@new_mission_blueprint.route('/<int:mission_id>', methods=['GET'])
def get_by_id(mission_id):
    result = get_mission_by_id(mission_id)
    if isinstance(result, Success):
        mission = result.unwrap()
        mission_data = {
            'id': mission.id,
            'target_id': mission.target_id,
            'country_id': mission.country_id,
            'city_id': mission.city_id,
            'industry_id': mission.industry_id,
            'type_id': mission.type_id,
            'priority_id': mission.priority_id
        }
        return jsonify(mission_data), 200
    return jsonify({'error': result.error}), 404


@new_mission_blueprint.route('/<int:mission_id>', methods=['PUT'])
def update(mission_id):
    data = request.json
    result = update_mission(mission_id, data)
    if isinstance(result, Success):
        mission = result.value
        mission_data = {
            'id': mission.id,
            'target_id': mission.target_id,
            'country_id': mission.country_id,
            'city_id': mission.city_id,
            'industry_id': mission.industry_id,
            'type_id': mission.type_id,
            'priority_id': mission.priority_id
        }
        return jsonify(mission_data), 200
    return jsonify({'error': result.error}), 400


@new_mission_blueprint.route('/<int:mission_id>', methods=['DELETE'])
def delete(mission_id):
    result = delete_mission(mission_id)
    if isinstance(result, Success):
        return jsonify({'message': 'Mission deleted successfully'}), 200
    return jsonify({'error': result.error}), 404
