import pytest
from sqlalchemy.orm import Session

from src.schemas.car import CarSchema, CarFilterSchema
from src.services.car import CarService
from src.models.car import Car

# Test Car creation
@pytest.fixture(name="test_create_initial_cars")
def test_car_initial_creation(session: Session):
    num_rows = 10
    car_service = CarService(session=session)
    car_service.create_initial_data(num_rows=num_rows)

    cars = session.query(Car).all()

    assert len(cars) == num_rows


# Test filter Cars
def test_get_filter_by_attributes(session, test_create_initial_cars):
    car_service = CarService(session=session)
    new_car = car_service.create_car(
        CarSchema(
            color="black",
            model="Mustang Custom",
            brand="Ford",
            year="1969",
            fuel="gasoline",
            cylinders="8",
            power=290.0,
            gearshift="manual",
            weight=1570,
            seats=5,
            abs=False
        )
    )

    cars = car_service.get_filter_by_attributes(CarFilterSchema(model=new_car.model))

    assert cars.count() == 1