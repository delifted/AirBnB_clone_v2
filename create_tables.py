from models.engine.db_storage import DBStorage
from models.base_model import Base
from models.state import State
from models.city import City

def create_tables():
    # Instantiate the DBStorage to initialize the database connection
    storage = DBStorage()

    # Create the tables
    storage._DBStorage__session().query(State).count()
    storage._DBStorage__session().query(City).count()
    Base.metadata.create_all(bind=storage._DBStorage__engine)

if __name__ == "__main__":
    create_tables()
