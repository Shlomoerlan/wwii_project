from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError
from typing import List, Dict
from model import NewMission
from config.base import session_factory

def create_mission(mission: NewMission) -> Result[NewMission, str]:
    with session_factory() as session:
        try:
            session.add(mission)
            session.commit()
            session.refresh(mission)
            return Success(mission)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def get_mission_by_id(mission_id: int) -> Result[NewMission, str]:
    with session_factory() as session:
        try:
            mission = session.query(NewMission).filter(NewMission.id == mission_id).one_or_none()
            if mission:
                return Success(mission)
            return Failure(f"Mission with ID {mission_id} not found.")
        except SQLAlchemyError as e:
            return Failure(str(e))

def get_all_missions() -> Result[List[NewMission], str]:
    with session_factory() as session:
        try:
            missions = session.query(NewMission).all()
            return Success(missions)
        except SQLAlchemyError as e:
            return Failure(str(e))

def update_mission(mission_id: int, update_data: Dict) -> Result[NewMission, str]:
    with session_factory() as session:
        try:
            mission = session.query(NewMission).filter(NewMission.id == mission_id).one_or_none()
            if not mission:
                return Failure(f"Mission with ID {mission_id} not found.")
            for key, value in update_data.items():
                setattr(mission, key, value)
            session.commit()
            session.refresh(mission)
            return Success(mission)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))

def delete_mission(mission_id: int) -> Result[bool, str]:
    with session_factory() as session:
        try:
            mission = session.query(NewMission).filter(NewMission.id == mission_id).one_or_none()
            if not mission:
                return Failure(f"Mission with ID {mission_id} not found.")
            session.delete(mission)
            session.commit()
            return Success(True)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))
