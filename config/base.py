from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Table, Index, inspect
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine('postgresql://postgres:1234@localhost/wwii_missions')

_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()


def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()


def create_table():
    tables_to_create = [table for name, table in Base.metadata.tables.items() if name != 'mission']
    Base.metadata.create_all(engine, tables=tables_to_create)


def drop_tables():
    tables_to_drop = [table for name, table in Base.metadata.tables.items() if name != 'mission']
    Base.metadata.drop_all(engine, tables=tables_to_drop)


@contextmanager
def session_scope():
    session = session_factory()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def create_index_on_column(table_name, column_name, index_name=None):
    index_name = index_name or f'idx_{table_name}_{column_name}'
    try:
        with session_factory() as session:
            engine = session.get_bind()
            metadata = MetaData()
            table = Table(table_name, metadata, autoload_with=engine)
            inspector = inspect(engine)
            indexes = inspector.get_indexes(table_name)
            index_names = [index['name'] for index in indexes]

            if index_name in index_names:
                print(f"Index '{index_name}' already exists on '{table_name}' table.")
                return
            index = Index(index_name, table.c[column_name])
            index.create(bind=engine)
            print(f"Index '{index_name}' created successfully on '{table_name}({column_name})'.")

    except SQLAlchemyError as e:
        print(f"An error occurred while creating the index: {e}")
