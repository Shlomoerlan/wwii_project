import logging
from flask import Flask
from config.base import create_table
from controller.mission_controller import mission_blueprint
from controller.new_mission_controller import new_mission_blueprint
from model import City, Country, Industry, NewMission, Priority, TargetType, Target, Mission

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


if __name__ == "__main__":
    create_table()
    app.register_blueprint(new_mission_blueprint, url_prefix="/api/missions")
    app.register_blueprint(mission_blueprint, url_prefix="/api/missions")
    app.run(debug=True)