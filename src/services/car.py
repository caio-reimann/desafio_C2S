from sqlalchemy.orm import Session
from src.schemas.car import CarFilterSchema, CarSchema
from src.models.car import Car
from tests.factories.car import CarFactory


class CarService:

    def __init__(self, session: Session):
        self.session: Session = session

    def create_initial_data(self, num_rows: int):
        for i in range(num_rows):
            car: Car = CarFactory.create_car()
            self.session.add(car)
            self.session.commit()

    def create_car(self, car: CarSchema) -> Car:
        new_car = Car(**car.model_dump())
        self.session.add(new_car)
        self.session.commit()

        return new_car


    def get_filter_by_attributes(self, filters: CarFilterSchema) -> list[Car]:
        filters_dict = filters.model_dump(exclude_unset=True)
        sql_filters = (getattr(Car, key) == filters_dict[key] for key in filters_dict)
        return self.session.query(Car).filter(*sql_filters)

    