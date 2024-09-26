from dataclasses import dataclass
from typing import Optional

@dataclass
class Mission:
    mission_id: int
    mission_date: str
    theater_of_operations: Optional[str] = None
    country: Optional[str] = None
    aircraft_series: Optional[str] = None
    mission_type: Optional[str] = None
    takeoff_base: Optional[str] = None
    target_country: Optional[str] = None
    target_latitude: Optional[float] = None
    bomb_damage_assessment: Optional[str] = None

    def __repr__(self):
        return (f"Mission(mission_id={self.mission_id}, mission_date={self.mission_date}, "
                f"theater_of_operations={self.theater_of_operations}, country={self.country}, "
                f"aircraft_series={self.aircraft_series}, mission_type={self.mission_type}, "
                f"takeoff_base={self.takeoff_base}, target_country={self.target_country}, "
                f"target_latitude={self.target_latitude}, bomb_damage_assessment={self.bomb_damage_assessment})")
