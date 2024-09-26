

1.
SELECT air_force, COUNT(*) AS mission_count
FROM mission
WHERE EXTRACT(YEAR FROM mission_date) = 1943
  AND air_force IS NOT NULL
GROUP BY air_force
ORDER BY mission_count DESC
LIMIT 1;




CREATE INDEX idx_mission_date ON mission(EXTRACT(YEAR FROM mission_date));
DROP INDEX IF EXISTS idx_mission_date;


2.








CREATE INDEX idx_mission_date ON mission(mission_date);
CREATE INDEX idx_air_force ON mission(air_force);
CREATE INDEX idx_airborne_aircraft ON mission(airborne_aircraft);

DROP INDEX IF EXISTS idx_mission_date;
DROP INDEX IF EXISTS idx_air_force;
DROP INDEX IF EXISTS idx_airborne_aircraft;
