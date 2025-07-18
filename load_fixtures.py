from dotenv import load_dotenv
from src.services.car import CarService
from src.data.database import Base, engine, session

load_dotenv()   

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

car_Service = CarService(session=session)
car_Service.create_initial_data(num_rows=100)
