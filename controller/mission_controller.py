


@app.route('/api/mission', methods=['GET'])
def get_all_missions():
    missions = mission.query.all()
    return jsonify([mission.to_json() for mission in missions])