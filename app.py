import logging
from config.base import create_table
from model import City, Country, Industry, NewMission, Priority, TargetType, Target

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


if __name__ == "__main__":
    create_table()
    logging.info("created")