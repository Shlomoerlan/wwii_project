CREATE:

 CREATE TABLE IF NOT EXISTS target (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        latitude NUMERIC,
        longitude NUMERIC
    );

 CREATE TABLE IF NOT EXISTS country (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country_name VARCHAR(255) UNIQUE
    );

  CREATE TABLE IF NOT EXISTS city (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_name VARCHAR(255),
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES country(id)
    );

   CREATE TABLE IF NOT EXISTS industry (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        industry_name VARCHAR(255) UNIQUE
    );

 CREATE TABLE IF NOT EXISTS target_type (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type_name VARCHAR(255) UNIQUE
    );

 CREATE TABLE IF NOT EXISTS priority (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        priority_level VARCHAR(50)
    );

CREATE TABLE IF NOT EXISTS mission (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        target_id INTEGER,
        country_id INTEGER,
        city_id INTEGER,
        industry_id INTEGER,
        type_id INTEGER,
        priority_id INTEGER,
        FOREIGN KEY (target_id) REFERENCES target(id),
        FOREIGN KEY (country_id) REFERENCES country(id),
        FOREIGN KEY (city_id) REFERENCES city(id),
        FOREIGN KEY (industry_id) REFERENCES industry(id),
        FOREIGN KEY (type_id) REFERENCES target_type(id),
        FOREIGN KEY (priority_id) REFERENCES priority(id)
    );

INSERT(FROM MISSION):

INSERT INTO Country (country_name)
SELECT DISTINCT target_country
FROM mission
WHERE target_country IS NOT NULL
ON CONFLICT (country_name) DO NOTHING;

INSERT INTO TargetTypes (type_name)
SELECT DISTINCT target_type
FROM mission
WHERE target_type IS NOT NULL
ON CONFLICT (type_name) DO NOTHING;


INSERT INTO Target (latitude, longitude)
SELECT DISTINCT
    nm.target_latitude::decimal,
    nm.target_longitude::decimal
FROM mission nm
WHERE nm.target_latitude IS NOT NULL
  AND nm.target_longitude IS NOT NULL
ON CONFLICT (latitude, longitude) DO NOTHING;


INSERT INTO new_mission (target_id, country_id, city_id, type_id)
SELECT DISTINCT
    t.id AS target_id,
    c.id AS country_id,
    ci.id AS city_id,
    tt.id AS type_id
FROM mission nm
JOIN target t ON nm.target_latitude = t.latitude AND nm.target_longitude = t.longitude
JOIN City ci ON nm.target_city = ci.city_name
JOIN Country c ON nm.target_country = c.country_name
LEFT JOIN target_type tt ON nm.target_type = tt.type_name
WHERE nm.target_id IS NOT NULL
ON CONFLICT DO NOTHING;


insert into new_mission (target_id, country_id, city_id, industry_id, type_id, priority_id)
select distinct
	t.id,
	co.id,
	ci.id,
	ind.id,
	ty.id,
	pr.id
from mission m
join target t on t.latitude = m.target_latitude and t.longitude = m.target_longitude
join country co on co.country_name = m.target_country
join city ci on ci.city_name = m.target_city
join industry ind on ind.industry_name = m.target_industry
join target_type ty on ty.type_name = m.target_type
join priority pr on pr.priority_level = m.target_priority