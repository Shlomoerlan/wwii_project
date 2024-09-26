#wwii_project created to get data and normalizing 

it makes easier to get the get info 

# Mission Management System

## Description

This project is a Python-based Mission Management System that utilizes Flask, SQLAlchemy, and PostgreSQL. It provides REST APIs to handle operations related to missions, such as creating, retrieving, updating, and deleting mission records from a database. The system is designed with a focus on efficiency and uses indexing to optimize query performance.

## Features

- Create, read, update, and delete (CRUD) operations for missions.
- Data models for `Mission`, `City`, `Country`, `Industry`, `Target`, and more.
- SQL queries with optimized performance using indexes.
- Repositories to handle interaction with the database using SQLAlchemy.

## File Structure

- **`app.py`**: The entry point of the application, responsible for setting up Flask and routing.
- **Controllers**:
  - `mission_controller.py`: Handles API requests for mission-related operations.
  - `new_mission_controller.py`: Manages the logic related to the creation of new missions.
- **Models**:
  - `City.py`, `Country.py`, `Industry.py`, `Mission.py`, `NewMission.py`, `Priority.py`, `Target.py`, `TargetType.py`: Define the data structure and mapping to the database.
- **Repositories**:
  - `mission_repository.py`: Provides database operations related to missions, such as querying and updating mission data.
  - `new_mission_repository.py`: Focuses on creating and managing new mission entries.
- **SQL Files**:
  - `create_tables_and_insertion.sql`: Contains SQL commands to create the necessary tables and insert sample data.
  - `queries.sql`: Includes SQL queries to retrieve data related to missions and targets, optimized for performance.
- **CSV Files**:
  - Query performance results before and after indexing:
    - `query_1_with_indexing.csv` / `query_1_without_indexing.csv`
    - `query_2_with_indexing.csv` / `query_2_without_indexing.csv`
- 
###  To run the project go to "app" and press the button 
````python
if __name__ == "__main__":
    create_table()
    app.register_blueprint(new_mission_blueprint, url_prefix="/api/targets")
    app.register_blueprint(mission_blueprint, url_prefix="/api/missions")
    app.run(debug=True)
````
```bash
pip install pytest flask toolz returns psycopg2-binary sqlalchemy
