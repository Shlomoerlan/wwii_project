

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

SELECT country, bomb_damage_assessment ,AVG(attacking_aircraft) AS average_damage
FROM mission
WHERE bombing_aircraft > 5
GROUP BY country, bomb_damage_assessment;


"AUSTRALIA"		                                                                                                        7.3888888888888889
"GREAT BRITAIN"		                                                                                                    26.5680426624530911
"SOUTH AFRICA"		                                                                                                    6.3333333333333333
"USA"	        "1 DIRECT HIT ON BATTLESHIP, 2 NEAR MISSES. TRANSPORT SUNK."	                                        6.0000000000000000
"USA"	        "1 TRANSPORT SEEN TO CAPSIZE FROM BOMBING"	                                                            9.0000000000000000
"USA"	        "3 LARGE FIRES"	                                                                                        6.0000000000000000
"USA"	        "4 BOMBS MISSED ENEMY CRUISER, 3 BOMBS STRUCK TRANSPORT NEAR SHORE - DIRECT HITS, TRANSPORT BURNING"	8.0000000000000000
"USA"	        "4 SHIPS IN GULF TARGETED.  RESULTS UNCERTAINDUE TO CLOUDS"	                                            9.0000000000000000
"USA"	        "ATTACKED TRANSPORTS AND DESTROYER, RESULTS UNKNOWN"	                                                6.0000000000000000
"USA"	        "BDA NOT PERFORMED DUE TO ENEMY INTERCEPTORS"	                                                        6.0000000000000000
"USA"	        "BDA NOT PERFORMED DUE TO ENEMY SEARCHLIGHTS AND AA FIRE"	                                            6.0000000000000000
"USA"	        "DOCKS WERE HIT.  LARGE FIRE BURNING BEFORE AND AFTER ATTACK."	                                        7.0000000000000000
"USA"	        "EXCELLENT"	                                                                                            8.0000000000000000
"USA"	        "GOOD"	                                                                                                8.0000000000000000
"USA"	        "HITS ON RUNWAY AND PARKING AREA."	                                                                    9.0000000000000000
"USA"	        "NO HITS"	                                                                                            6.0000000000000000
"USA"	        "NOT STATED, LANDED AT MINDANEO"	                                                                    9.0000000000000000
"USA"		                                                                                                            18.4035664234282124
		                                                                                                                16.5182405910875087



CREATE INDEX idx_mission_date ON mission(mission_date);
CREATE INDEX idx_air_force ON mission(air_force);
CREATE INDEX idx_airborne_aircraft ON mission(airborne_aircraft);

DROP INDEX IF EXISTS idx_mission_date;
DROP INDEX IF EXISTS idx_air_force;
DROP INDEX IF EXISTS idx_airborne_aircraft;

2.
select bomb_damage_assessment, count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country, bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1

"EXCELLENT" 7


